#!/usr/bin/env python3
"""Ragdoll Lab server: static files + /interpret (natural language -> action spec via claude CLI)."""
import json
import subprocess
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8741
MODEL = "claude-haiku-4-5-20251001"

PROMPT = """You translate a natural-language command about a 3D physics sandbox into ONE JSON action spec. Output ONLY the JSON object — no prose, no code fences.

Scene inventory — the current environment, its named targets, and movable props:
__INVENTORY__

Output schema (omit fields that don't apply):
{
  "action": "throw" | "drop",
  "object": {"id": "<existing prop id>"} OR {"shape": "box" | "sphere", "size": <meters: cube edge or sphere diameter>, "mass": <kg>},
  "count": <objects per run, default 1>,
  "target": "<one of the target names in the inventory: e.g. head|torso|pelvis in 'ragdoll', or ramp|box in 'ramp'>",
  "speed": <m/s, throw only; convert units (1 mph = 0.447 m/s)>,
  "height": <drop height in meters, drop only, default 3.5>,
  "jitterDeg": <random aim/position spread per run in degrees, default 3>,
  "reseed": <true ONLY if the command asks for random/varied/different directions or positions; makes each batch draw fresh randomness instead of repeating>,
  "origin": [<x>,<y>,<z>] OR {"azimuth": <deg around target>, "dist": <m>, "height": <m>} <where the thrown object starts; omit to use the fixed default start>,
  "runs": <how many times the scenario is simulated, default 1>,
  "sweep": {"param": "speed" | "height" | "count", "from": <start value in SI>, "to": <end value in SI>, "steps": <number of runs>},
  "duration": <simulated seconds per run, default 6>,
  "note": "<one short sentence stating your interpretation>"
}

Rules:
- SWEEP whenever the command says "sweep", "ramp", "step ... up/down", or gives an incremental RANGE across runs ("from 1 to 100 mph", "1 mph, 2 mph, … 100 mph", "increasing speed"). Emit a "sweep" object: {"param":"speed"|"height"|"count","from":<SI start>,"to":<SI end>,"steps":<run count>}. Do NOT also output top-level "runs" or the swept field. "across/over N runs" → steps=N. Convert from/to to SI. Set jitterDeg=0 and a short duration like 2 so every run is a clean, comparable snapshot. NEVER write the swept field as an array like "speed":[0.45,44.7] — always use the "sweep" object. A plain "50 times at 30 mph" is NOT a sweep — that repeats one identical throw → runs=50. Sweep example: "throw boxes at the head, sweep speed from 1 to 100 mph across 50 runs" -> {"action":"throw","object":{"shape":"box","size":0.3,"mass":5},"target":"head","sweep":{"param":"speed","from":0.45,"to":44.7,"steps":50},"jitterDeg":0,"duration":2,"note":"ramp box speed 1->100 mph at the head across 50 runs"}.
- TARGET must be one of the target names in the inventory for the current environment. In the "ramp" environment: DROP a ball onto target "ramp" (the concave scoop launches it into the tower); target "box" is the tower to topple. Do not "throw" at the ramp — the scenario is a ball falling onto it.
- START POSITION is FIXED by default — the object spawns from the same spot every run. Only set "reseed":true (which randomizes the spawn direction per run) when the command explicitly asks for random/varied/different/"from a random direction" starts. Set "origin" only when the command specifies where to throw from ("from behind", "from 5 m away", "from above"). Do NOT randomize the start otherwise.
- "the box" / "the ball" refers to an existing prop when one plausibly matches; use its id. Otherwise define the object inline with realistic size and mass for what was named (a tire ~ 9 kg 0.65 m, a brick ~ 2.5 kg 0.2 m, etc. — approximate any object with a box or sphere).
- "100 times" means runs=100 (the whole scenario repeats from the same starting scene). "drop 10 balls" means count=10 within each run.
- If the command asks for "random", "different", "varied", or "each from a different direction" (aim or position) but names no repeat count, set reseed=true and bump runs to at least 24 so the variation is actually visible as a distribution. An explicit count ("100 times") still sets runs.
- Convert every quantity to SI units. Be literal about masses the user states.

Command: __COMMAND__"""


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/interpret":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length))
            prompt = (
                PROMPT
                .replace("__INVENTORY__", json.dumps(payload.get("inventory", {}), indent=1))
                .replace("__COMMAND__", payload.get("command", ""))
            )
            proc = subprocess.run(
                ["claude", "-p", prompt, "--model", MODEL],
                capture_output=True, text=True, timeout=120,
            )
            if proc.returncode != 0:
                raise RuntimeError(f"claude CLI failed: {proc.stderr.strip()[:300]}")
            out = proc.stdout.strip()
            start, end = out.find("{"), out.rfind("}")
            if start == -1 or end <= start:
                raise ValueError(f"no JSON in interpreter output: {out[:300]}")
            spec = json.loads(out[start:end + 1])
            body = json.dumps({"spec": spec}).encode()
        except Exception as exc:
            body = json.dumps({"error": str(exc)}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        if "/interpret" in (args[0] if args else ""):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    print(f"Ragdoll Lab running at http://localhost:{PORT}")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
