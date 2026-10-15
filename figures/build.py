"""Build every figure and mockup and copy them into ../img with their published names.

    pip install playwright pillow && playwright install chromium
    python3 build.py
"""
import shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
NAMES = dict(line.split() for line in """01-1-thesis fig-1-1-thesis
01-2-before-after fig-1-2-before-after
01-3-ecosystem fig-1-3-ecosystem
02-1-stack fig-2-1-stack
02-2-modes fig-2-2-modes
03-1-components fig-3-1-components
03-2-parties fig-3-2-parties
03-3-two-checks fig-3-3-two-checks
04-1-vault-anatomy fig-4-1-vault-anatomy
04-2-lifecycle fig-4-2-lifecycles
05-1-mandate fig-5-1-mandate
05-2-custody fig-5-2-custody-boundary
05-3-gates fig-5-3-policy-gates
06-1-agent-loop fig-6-1-loop
06-2-signals fig-6-2-signals
06-3-routing fig-6-3-routing
07-1-onboarding fig-7-1-onboarding
07-2-copilot fig-7-2-copilot
07-3-autopilot fig-7-3-autopilot
07-4-stop fig-7-4-stop
08-1-risks fig-8-1-failure-modes
08-2-screen-map fig-9-1-screens
09-1-roadmap fig-10-1-roadmap
10-1-book mock-1-book
10-2-vaults mock-2-vaults
10-3-vault-detail mock-3-vault-detail
10-4-mandate mock-4-mandate
10-5-proposal mock-5-proposal
10-6-record mock-6-record
10-7-onboarding mock-7-onboarding""".splitlines())

(HERE / "src").mkdir(exist_ok=True)
(HERE / "out").mkdir(exist_ok=True)
import os
for theme in ["dark", "light"]:
    for script in ["figs_a.py", "figs_b.py", "figs_c.py", "mock.py"]:
        subprocess.run([sys.executable, script], cwd=HERE, check=True, env={**os.environ, "PM_THEME": theme})
subprocess.run([sys.executable, "render.py"], cwd=HERE, check=True)
for src, dst in NAMES.items():
    for sfx in ["", "-light"]:
        shutil.copy(HERE / "out" / f"{src}{sfx}.png", HERE.parent / "img" / f"{dst}{sfx}.png")
print(f"copied {2 * len(NAMES)} images to ../img (dark and light)")
