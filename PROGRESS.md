# Ragdoll Lab — Progress & Architecture

_Last updated: 2026-07-07_

## Vision

A 3D physics sandbox where users describe scenarios in natural language ("throw the box
at the human 100 times at 50 mph") and an LLM compiles them into simulations that run by
themselves. The end goal is letting users build **chaotic environments** conversationally:
populate a scene, script events, run them many times, and study the distribution of
outcomes — not just a single playthrough.

This is *not* RL (nothing learns a policy). The pattern is:

```
natural language ──LLM──▶ declarative action spec (JSON)
action spec ──deterministic engine──▶ N seeded headless runs
runs ──▶ metrics distribution + click-to-replay any run in 3D
```

The LLM never touches the physics loop. It only translates intent into config. Everything
downstream is deterministic, reproducible code.

## What works today

- **3D scene (WebGL)** — three.js renderer, orbit/zoom camera, shadows, ground plane.
- **Humanoid mannequin ragdoll** — 11 rigid bodies (head, torso, pelvis, upper/lower
  arms and legs) joined by cone-twist constraints with rough anatomical limits
  (neck, spine, shoulders, elbows, hips, knees). Built from primitives in cannon-es.
- **Frozen-until-impact standing** — the mannequin starts as static bodies in a standing
  pose (no balancing needed). Any impact above ~1.2 m/s on any part flips the whole body
  to dynamic, so it stands until something knocks it over, then ragdolls realistically.
- **Manual interaction** — buttons to drop boxes/crates, click the mannequin to shove it
  (impulse at the clicked point), reset to standing.
- **LLM command box** — free-text commands are sent to `/interpret` along with a JSON
  **scene inventory** (every prop's id/shape/size/mass/position + mannequin state). The
  LLM sees structured state, not pixels. It returns a strict action spec, shown in the UI
  before running.
- **Seeded batch simulation** — the engine snapshots the live scene, then re-runs the
  scenario N times headless at fixed 60 Hz timesteps (100 × 6 s runs ≈ seconds of wall
  clock). Each run draws all randomness (aim jitter, spin, spawn positions) from a
  mulberry32 RNG seeded with the run number → run #37 is always exactly run #37.
- **Results panel** — per-batch summary (hit rate, topple rate, median time-to-topple,
  mean peak impact) plus a per-run table. Clicking a run restores the snapshot and
  replays that exact seed live in 3D (fixed-step, so the replay matches the headless run).
- **Object fallback** — commands naming objects that don't exist ("throw a brick") get
  an inline primitive definition (shape/size/mass estimated by the LLM) spawned at a
  seeded random position each run.
- **Parameter sweep** — a batch can step ONE parameter across its runs instead of
  repeating one setting. "sweep the box speed from 1 to 100 mph over 50 runs" →
  `sweep:{param:"speed", from:0.45, to:44.7, steps:50}` → run 0 at 1 mph … run 49 at
  100 mph (linear). A sweep pins one seed across all runs so the swept value is the only
  variable (a transfer curve), where a plain batch varies the seed to get a distribution
  at one setting. Runs are addressed by **index** here (seeds can repeat). The results
  table shows the swept value per row; "Play all" + the `s/run` box replay the ramp.
  Supported params: `speed`, `height`, `count`.

Verified end-to-end: "throw the box at the human 100 times at 50 mph" → `{action: throw,
object: box_1, target: torso, speed: 22.35, runs: 100}` → 100 simulated runs → replay.

## Files

| File | Role |
|---|---|
| `index.html` | The entire app: scene, physics, ragdoll, snapshot/restore, batch runner, results UI, command box. No build step; three.js + cannon-es load from unpkg via importmap. |
| `server.py` | Serves static files on **port 8741** and handles `POST /interpret`: builds a prompt (schema + scene inventory + command), shells out to the logged-in `claude` CLI (Haiku model), parses the JSON spec out of the reply. No API key handling — reuses Claude Code auth. |

**Run it:** `python3 server.py` in this folder → http://localhost:8741. (A plain static
server also works, but the AI command box needs `server.py`.)

## Action spec schema (the LLM's output contract)

```json
{
  "action": "throw" | "drop",
  "object": {"id": "box_1"} OR {"shape": "box"|"sphere", "size": 0.45, "mass": 30},
  "count": 1,          // objects per run ("drop 10 balls" → 10)
  "target": "torso" | "head" | "pelvis",
  "speed": 22.35,      // m/s, throw only (LLM converts units)
  "height": 3.5,       // m, drop only
  "jitterDeg": 3,      // per-run random aim/position spread
  "origin": [3.5,1.4,0],  // optional throw start: [x,y,z] or {azimuth,dist,height}
  "runs": 100,         // how many times the scenario repeats
  "sweep": {           // optional: step ONE param across runs instead of repeating
    "param": "speed",  // "speed" | "height" | "count"
    "from": 0.45,      // SI start value (run 0)
    "to": 44.7,        // SI end value (last run)
    "steps": 50        // number of runs; replaces `runs` when present
  },
  "duration": 6,       // simulated seconds per run
  "note": "human-readable interpretation"
}
```

When `sweep` is present it defines the run count (`steps`) and overrides the swept field
per run; omit top-level `runs` and the swept field. Sweeps hold the seed constant so the
swept value is the only thing that changes between runs. The engine also accepts a
**shorthand** the interpreter tends to emit — a `[from, to]` array on a sweepable field
(e.g. `"speed": [0.45, 44.7]` with `"runs": 50`) is read as that same sweep. Non-numeric
values for `speed`/`height` fall back to their defaults rather than propagating NaN.

**Throw start is deterministic.** An inline thrown object spawns from a fixed point every
run (default: 3.5 m from the target along +x, 1.4 m up). It is randomized per run **only**
when `reseed:true` (the command asked for varied directions). Set `origin` to pin an exact
start — `[x,y,z]` for absolute coords, or `{azimuth,dist,height}` polar around the target.

Key invariant: **object identity is pinned in the spec**. All 100 runs of a batch use the
identical object (same dims, same mass) — otherwise you're comparing different experiments.

## Design decisions worth remembering

- **Visual mesh ≠ collision shape.** Renderer can show anything; physics collides
  primitives. This is what will let pretty assets slot in later without touching results.
- **Replay = re-simulation.** Nothing stores trajectories; same snapshot + same seed +
  fixed timestep reproduces the run. Cheap and exact (on the same machine/browser).
- **Batches reuse the live world** (snapshot/restore) rather than isolated copies. Simple,
  but it's why the UI locks during a batch. Web Workers would remove that limit.
- **Metrics are event-driven**: collide listeners on ragdoll parts record first-hit time
  and peak impact velocity; topple = head dropping below 0.8 m.

## Known limitations

- Two verbs (`throw`, `drop`), one object type per command, single-event scenarios.
- Primitive shapes only (box/sphere). cannon-es Trimesh collision is genuinely weak
  (trimesh-vs-box doesn't work), so arbitrary meshes need convex hulls — or Rapier.
- Batch runs are single-threaded on the main thread (fine at current scale).
- Determinism is same-machine/same-browser, not cross-platform bit-exact.
- One hardcoded actor (the mannequin); scene starts from one fixed layout.

## Roadmap → "chaotic environments via LLM"

Rough order of attack; each step builds on the previous without rework:

1. **Event scripts.** Replace the single action with an `events: [{t, action, ...}]`
   array in the spec (the engine's `applyAction` becomes a scheduler). Unlocks
   "drop a crate, then 2 seconds later throw three balls at his head".
2. **Scene construction verbs.** `spawn`/`place`/`stack` actions so the LLM can *build*
   the environment ("put a wall of 20 boxes behind him", "scatter 30 balls around") —
   this is the core of user-created chaos. Scene setup commands mutate the live scene;
   batch commands snapshot it.
3. **More object vocabulary.** Cylinders + compound bodies (tire, ladder, table as
   welded primitives), LLM-estimated dimensions. Then an asset cache folder for pretty
   GLB visuals (Poly Pizza retrieval or image→3D generation) mapped onto the same
   primitive colliders.
4. **Multiple actors.** Parameterize the ragdoll builder (position, scale, count) →
   "a crowd of 5 mannequins". Metrics become per-actor.
5. **LLM-defined metrics.** Let the spec declare what to measure ("count how many boxes
   end up touching him") compiled to a small expression the recorder evaluates.
6. **Engine swap to Rapier** (WASM) when scale demands it: faster, deterministic by
   design, real trimesh/convex-decomposition support. The spec layer carries over
   unchanged; only the engine adapter is rewritten.
7. **Parallel batches in Web Workers** — needed once runs × duration gets big; also
   frees the UI during batches.
8. **Conversation, not commands.** Multi-turn: the LLM keeps scene context, can answer
   "why did he fall in only 60% of runs?" from the metrics, and propose variations.

## Quick test commands

- `throw the box at the human 100 times at 50 mph` (needs a dropped box first, else it spawns one)
- `drop 10 0.1kg balls on the mannequin, run it 50 times`
- `throw a 2.5 kg brick at his head 30 times at 20 m/s`
