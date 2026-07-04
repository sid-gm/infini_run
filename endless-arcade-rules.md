# Endless Arcade — Genre Ruleset

> Formerly "Infinite Runner." Generalized to cover any **endless, continuously-moving
> arcade game** — the auto-runner, the recognition-finder, *and* the navigation-survivor are
> three archetypes of one skeleton.

## What an endless arcade game *is*

- The world never rests for free: it is either in **continuous motion** of its own — or held
  under a **relentless standing pressure** (a pursuer, a rising tide, a closing arena) that
  punishes any hesitation — so the player can never stop and think at no cost, and challenges
  arrive in an endless stream at a known, readable pace. (See Rule 1.)
- The player owns only a **tiny action set** (usually one core action) and expresses skill
  through **one legible axis**:
  - **Timing** — *when* to act (the runner: jump at the right instant), or
  - **Recognition / targeting** — *what / where* to act on (the finder: spot the target in
    a moving field and tap it), or
  - **Navigation / planning** — *where to route yourself over time* through a space you
    yourself fill (the survivor: thread a safe path as your own trail steadily closes the
    room in).
- Difficulty **escalates endlessly**. There is no win state — only how far / long / much
  you push.
- A run ends on an **unambiguous failure** — contact with a hazard, *or* a clock running
  out. The failure is always "my fault."
- **Goal:** survive and accumulate. **Score = one climbing number** you try to beat next
  run.

**Three archetypes, one skeleton:**
- **Timing-runner** (Canabalt, Geometry Dash, Flappy Bird): the avatar auto-moves; the
  skill is *when* to jump.
- **Recognition-finder** (the "Where's Waldo" shooter): the field auto-scrolls; the skill
  is *spotting and tapping* the target before the timer empties.
- **Navigation-survivor** (Snake, Tron light-cycles): the avatar auto-moves and leaves a
  lasting trail behind it; the skill is *planning a path* through a field you progressively
  fill, steering so that you never cross the space you have already taken.

**Two sources of difficulty.** In the runner and the finder, difficulty is **generated** —
the world spawns each challenge and throws it at the player, whose job is to react. In the
survivor, difficulty is **accumulated** — the player's own progress is what fills and
tightens the space, so the challenge grows out of past success rather than being handed in
from outside. Both escalate endlessly, and both keep failure squarely "my fault." Several
rules below (5, 9, 13) read differently depending on which source a game draws from, and
each one names it.

Everything below holds for all three. Where they diverge, the rule names the axis.

---

## Control & feel

**1. Constant motion, or a standing pressure the player cannot switch off.**
The world moves on its own — the avatar runs forward, the crowd scrolls past, or the avatar
glides ahead one step at a time trailing its body behind it — and never pauses for the
player to think. The player's job is to *respond* to that motion, and for the survivor to
*plan out ahead of* it, but never to start or stop it: the avatar cannot be halted, only
redirected.

**The motion may also be player-paced — provided hesitation is never free.** Some games let
the player meter their own advance (hop when ready, pick the next corridor, feather the
throttle) rather than auto-scrolling every frame. This still satisfies the rule *only if a
relentless standing pressure punishes standing still* — a force that keeps closing in whether
or not the player acts:
- **A pursuer that eats the dawdler** — Crossy Road's eagle swoops if you idle; Pac-Man's
  ghosts hunt you through a maze you move through at your own step.
- **An encroaching field** — a rising tide or lava line (Tomb of the Mask), a wall of glitch
  chewing up the level behind you (Pac-Man 256), an arena that steadily shrinks.
- **A throttle you can ease but not kill** — a racer where you may slow but the road never
  stops feeding hazards and falling behind is its own failure.
The test is simple: *can the player stop and think for free?* If standing still is a safe,
cost-free option, the rule is broken — that is a turn-based puzzle (2048, a golf game), not an
endless arcade game. The world must always be spending something the player cannot get back —
distance, safe ground, time, a margin ahead of the chaser — so that even a self-paced advance
is a race the player is always already losing a little. (Master: Constant motion / relentless
pressure; input economy.)

**2. One skill axis — count the axes, not the buttons.**
One *model* is the spine, not necessarily one button. The original test was "one core verb,
at most one secondary," but the truer measure is the **axis**: every input the player can make
must serve the *same* legible skill and feed the *same* mental model — never open a second
system to learn.
- A single verb is the purest form — *jump* for the runner, *tap-to-strike* for the finder,
  *steer* (redirect your heading) for the survivor — and most great games of the genre keep
  to it.
- But **a small, bounded set of inputs is fine when they are all the same axis.** Temple
  Run's turn-left, turn-right, jump, slide and lean are five inputs that are one idea —
  *reactive spatial dodging*; the player never switches mental models between them. Tetris's
  move, rotate and drop are one idea — *fitting the falling piece*. These do not violate the
  rule; they are one axis expressed through a few legible controls.
- For the survivor, note that a reversal straight back into your own trail is not a genuine
  choice but an instant self-kill, so it is simply forbidden as an input rather than offered
  as a move.

**What the rule still forbids is mixing axes.** The moment a second input demands a
*different* kind of skill — steering *and* shooting (navigation plus targeting, the Doodle
Jump / Into the Dead blur), timing a jump *and* solving a match — the player must hold two
models at once and can no longer build the single clean instinct the genre runs on. A bounded
handful of inputs on one axis: allowed. Two axes bolted together: not. Keep the *axis* count
at one; the *button* count can be a small, legible few. (Master: Depth without complexity;
one axis, however many legible inputs it needs.)

**3. Instant, guaranteed reaction to every input.**
Act → the world responds *this frame*, with a satisfying pop. Tap the avatar and it jumps;
tap the target and it dies. No input is ever swallowed. For a grid-stepped survivor the new
heading naturally takes effect on the next step rather than mid-cell, but the input must
still be *registered and committed the instant it is pressed* — buffered, never dropped — so
the turn the player asked for is always the turn they get. (Master: 1:1 responsiveness.)

**4. One legible skill axis, with a deterministic model the player can trust.**
The whole game rests on a single learnable model:
- **Timing axis:** the jump arc is always the same height, distance, duration — the player
  internalizes it and trusts it absolutely.
- **Recognition axis:** the scroll speed, target appearance, and spawn rules are fixed and
  readable — the player learns "this is what the target looks like, this is how fast the
  field moves, this is how long I have."
- **Navigation axis:** the grid, the step rate, and the rules of the trail are fixed and
  known — the player learns "this is exactly how far I move with each step, this is how my
  body lengthens when I feed, and this is how much open room I have left to work with." The
  model is spatial rather than reactive: instead of trusting a jump arc or a scroll speed,
  the player trusts that the *space itself* behaves identically every run, so any trap they
  end up in was one the layout let them foresee and route around.
Any variation (hold = higher jump; rare target type) must be **explicit and legible**.
Everything must be frame-rate-independent so the model is identical on every device.
(Master: Legible, consistent, deterministic model.)

> Note: each archetype deliberately trades the others' axes away for its own — the finder
> gives up timing for recognition, the survivor gives up reaction for planning. Each is a
> legitimate, complete game in its own right. But a single game should commit to **one**
> primary axis and not blur them together, or the player can never build a clean mental
> model.

---

## Fairness & generation *(the make-or-break of this genre)*

**5. Every challenge solvable on sight.**
Because the stream is endless/generated, the player cannot memorize it. So generation must
*guarantee*:
- **Runner:** every obstacle is clearable with the known action set and fixed arc; no
  impossible spawns (e.g. two gaps closer than one arc allows); spacing always respects the
  worst-case reaction window at the current speed.
- **Finder:** the target is always actually *present and findable* — never fully occluded,
  never flung off-screen, never rendered unresolvably small. Hazards may clutter and
  relocate it, never make it impossible.
- **Survivor:** the generator's only obligation is that the *objective* — the food, the
  pickup — is always reachable at the moment it appears; it is never spawned inside a wall
  or walled off where no legal path could ever lead. The hazard, by contrast, is the
  player's own accumulated trail, so an unwinnable position is permitted **only when the
  player has built it themselves**, one freely-chosen turn at a time. This is the survivor's
  form of "solvable on sight": not that every board can be read and cleared at a glance, but
  that every dead end is one the player steered into of their own accord and could have
  avoided. The world never hands you a death — you can only route yourself into one.
This preserves "my fault" failure **without memorization**. (Master: Determinism + "my
fault" failures.)

**6. Readable at speed — telegraph the threat.**
Hazards and targets are high-contrast against the background and appear far enough ahead /
clearly enough to react in time. As speed or density rises, readability must be *protected*
— lead distance grows for the runner; the target keeps a minimum size and contrast floor
for the finder. The survivor gets this half for free: the only thing that can kill you is
your own trail, and it is already drawn across the screen in full — high-contrast, unmoving,
nothing hidden. The difficulty there is never *seeing* the threat but *planning around* it,
so the survivor's readability duty shifts to keeping the trail visually distinct from both
the background and the objective, so the player can always tell at a glance which cells are
walls of their own making. If readability collapses, Rule 5 breaks. (Master: Legible
physics.)

**7. Unambiguous failure.**
On any run-ending event the player instantly understands *what* ended the run — the hazard
the runner hit, the clock the finder let expire, or the stretch of their own trail the
survivor steered into. No mystery deaths, no "where did it go." The cause is always visible,
and reads as the player's own mistake. The survivor is the purest case of all: with nothing
on the board capable of killing you but your own body, every death is self-evidently
self-inflicted. (Master: Determinism + "my fault" failures.)

---

## Loop, difficulty & motivation

**8. Near-frictionless restart — a stat card is allowed, a menu is not.**
Failure → back into a fresh run almost instantly. A **single-tap end-of-run card** showing
the score and personal-best is not only allowed but often *desirable* — the
"you got 11, best is 12" sting is part of the addictive, frustrating-fun loop. What's
forbidden is a **navigable menu** the player must work through (settings, level-select,
multiple buttons). Rule of thumb: from "I want to retry" to "I'm playing again" in **one
tap, under a second**. (Master: Frictionless "one more try.")

**9. Escalating difficulty — the flow channel.**
Difficulty rises **smoothly and continuously**, never in jarring steps, never plateauing.
The increments may be tied to success rather than to a clock — each cleared obstacle or
collected target nudges the dial — provided they stay small enough that the curve *feels*
like one unbroken climb rather than a staircase:
- **Runner:** speed up, density up, gaps tighten.
- **Finder:** crowd denser, targets smaller, scroll faster, hazards more frequent — applied
  in small per-success increments, not level jumps.
- **Survivor:** here the ramp is **self-generated and unavoidable** — every objective the
  player collects lengthens their trail, which permanently eats into the safe space and
  tightens every decision that follows. The designer need not turn a knob; the player's own
  success *is* the difficulty knob, and it only ever turns one way. Optional reinforcers (a
  faster step rate as the score climbs, a smaller arena) can sharpen the curve, but growth
  alone already guarantees the field closes in forever. The danger to watch for is the
  opposite of a spike — a long flat *plateau* at the start, when a short trail in a wide
  space poses no real threat; if that dead stretch drags on, tighten the starting space or
  raise the step rate so the climb begins promptly (see also Rule 13).
The ramp must respect Rules 5–6 at every point: harder, but always fair and readable.
(Master: Risk vs. reward; flow.)

**10. Optional risk/reward lines — encouraged, not required.**
This rule describes an *enrichment*, not a membership test. A game may layer in optional
challenges worth more but demanding tighter execution, so bold players push the edge while
cautious players still progress:
- **Runner:** coins on a harder route (Geometry Dash).
- **Finder:** a rare "golden target" worth bonus time but tinier and faster; or a risky
  deliberate hazard-tap that clears the field for a time gain if you survive the chaos.
- **Survivor:** a high-value objective set somewhere awkward — deep inside your own coils,
  jammed against a corner, or rigged to vanish on a short timer — so that claiming it demands
  a riskier, more committed route than an ordinary pickup. The bold player threads into the
  tight spot for the bonus; the cautious player lets it expire and keeps to open ground.

**But a game with no risk/reward line at all is still a complete, first-class endless arcade
game.** Flappy Bird, Canabalt and Super Hexagon offer the player no optional side-bet
whatsoever — there is only the one line, *survive* — and they are exemplars of the genre, not
deficient versions of it. When the core loop is pure enough, the *only* risk/reward decision
is "how long do I dare keep going," and that is sufficient. Treat this rule as a dial to reach
for when a game feels one-note, never as a box every game must tick. (Master: Risk vs. reward
— a way to add depth, not a requirement for entry.)

**11. Score = one climbing number; personal-best is the goal.**
No ending. Score is a **single monotonic metric** — distance, targets found, time survived,
trail length or objectives collected, or combo. Show it live during play and the best score
persistently. The meta-goal is beating your last run; self-competition is the engine.
(Master: Score / personal-best.)

> The failure timer (finder) and the distance counter (runner) are the same idea from two
> sides: a continuously-moving pressure the player races against. The survivor's shrinking
> pool of safe space is a third face of the same idea — pressure that mounts not from a clock
> or a speedometer but from how much room you have already spent.

---

## Onboarding, depth & arc

**12. Legible goal in one screenshot.**
A new player understands it instantly, zero text:
- **Runner:** I move right, things hit me, I jump, I go far.
- **Finder:** there's a crowd, that's the target (iconic stripes), I tap it before the clock
  empties.
- **Survivor:** there I am, there's the dot; I steer toward it and grow longer, and the
  lengthening tail I have to keep clear of is my own.
(Master: Instantly legible goal.)

**13. The first moments *are* the tutorial.**
The opening is a guaranteed-survivable on-ramp:
- The first challenge is trivial and unmissable (the first jump is a gimme; the first target
  is big, near-center, in a tiny crowd).
- **But the pressure is honest from the first second** — the clock genuinely ticks, the
  hazard genuinely kills. The on-ramp is survivable because the *challenge* is easy, not
  because the stakes are padded; the player must feel what loses the game immediately. This
  rules out any *invincible warm-up*: the avatar must never begin in a state where failure is
  physically *impossible*.
- **What "capable of dying" requires is that *some* live hazard can kill from the first
  input — not that every hazard is already armed.** The line that matters is whether the
  player could lose in the opening seconds if they were careless, not which specific threat
  does it. So:
  - If the *only* thing that can kill the avatar is its own trail, it must start long enough
    to fold into itself — a wall-less survivor that begins too short to self-collide is a lie,
    because the one rule that can kill the player is quietly switched off.
  - But a survivor on a **walled board may legitimately start short and grow into
    self-lethality**, because a real failure condition — the boundary — is live from frame
    one. Classic Snake is honest the instant a wall can end the run, even before the tail is
    long enough to matter. The grace period here is not a padded invincibility; it is a brief,
    finite stretch in which one hazard (the wall) is already lethal while a second (the tail)
    is still arming itself in plain view.
  The test is unchanged in spirit: *can the player physically lose right now?* If yes, by any
  means, the opening is honest. If no — if every failure condition is switched off — it is a
  lie, no matter how the avatar is dressed up.
- Each new idea (each hazard) is introduced **alone** before being combined with others.
(Master: Teach through play, not tutorials — honest stakes from frame one, by at least one
live hazard.)

**14. Depth from combination, not from rules — measured at the skill loop.**
One axis, endless situations. Depth comes from *combinations* — obstacle chains and rhythm
for the runner; crowd density, target camouflage, and hazard interactions for the finder;
for the survivor, the ever-shifting maze of your own trail, where a single rule ("don't
cross your own path") yields boundless planning depth as the board fills and the safe routes
narrow — not from adding rules. Keep the rule count near zero; let the situations get rich.

**The "near-zero rule count" is measured at the *moment-to-moment skill loop*, not at the
whole app.** What must stay minimal is the set of rules the player reasons with *while
dodging, spotting or planning* — the live model under their thumb. Meta-progression that sits
*outside* that loop does not count against it:
- **Cosmetic unlocks** — Crossy Road's hundred characters, Subway Surfers' skins — change
  nothing about how the run plays.
- **Between-run upgrades and currency** — coins banked toward a shop, Alto's goal list,
  permanent stat boosts — are resolved on the stat card, not mid-dodge.
- **Power-ups, *if* they stay legible** — Jetpack Joyride's gadgets, Subway Surfers'
  jetpack/magnet/hoverboard. A power-up is fine when it temporarily *simplifies* the loop (a
  magnet that auto-collects, a board that grants one free crash) or reskins the same axis —
  and only becomes a violation when it forces the player to learn and juggle a genuinely *new*
  in-run system mid-run.
The guard, then, is leakage: meta-systems are unconstrained *as long as they do not rewrite
the skill model the player is holding while the world is moving*. A shop is free. A second
control scheme the player must master to survive the next ten seconds is not. Keep the *live*
rule count near zero; let the *situations* — and the cosmetic, economic scaffolding around the
run — get as rich as they like. (Master: Depth without complexity; unbounded depth of
execution, measured at the loop, not the launcher.)

**15. Arc inside the run, and across runs.**
Each run has a micro-arc — easy on-ramp (learn) → rising challenge (apply) → personal
frontier (where failure is likely). For the survivor this arc *is* the filling of the space:
open and forgiving at the start, tense and crowded by the middle, a near-solid field of your
own trail at the frontier. Across runs, a macro-arc — the player's skill ceiling climbs as
they internalize the patterns (the arc and its rhythms; the target's look and the field's
flow; the survivor's instinct for always leaving themselves an exit). (Master: Clear arc.)

---

## Quick archetype cheat-sheet

| Rule dimension        | Timing-runner            | Recognition-finder                       | Navigation-survivor                       |
|-----------------------|--------------------------|------------------------------------------|-------------------------------------------|
| Motion (R1)           | Avatar auto-runs         | Field auto-scrolls                       | Avatar auto-moves, leaving a trail        |
| Core verb (R2)        | Jump (timing)            | Tap-to-strike (recognition)              | Steer (navigation / planning)             |
| Skill model (R4)      | Fixed jump arc           | Fixed scroll speed + target look         | Fixed grid, step rate, and trail rules    |
| Challenge (R5)        | Clear the obstacle       | Spot the target                          | Plan a safe path; don't trap yourself     |
| Failure (R7)          | Collision                | Clock hits zero                          | Collision with your own trail             |
| Score (R11)           | Distance                 | Targets found                            | Trail length / objectives collected       |
| Difficulty knobs (R9) | Speed, density, gaps     | Crowd size, target size, scroll, hazards | Trail length (self-made), space size, step rate, bonus risk |
