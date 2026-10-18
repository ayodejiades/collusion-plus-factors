"""Entry point for rops-run grid: runs harness/run_one.py with the market's dependencies.

Kaggle images already have pydantic, jinja2 and numpy. On a laptop without them, re-run under
`uv run --with ...` so nothing is installed globally.
"""
import importlib.util
import os
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).resolve().parent
NEEDED = ("pydantic", "jinja2", "numpy", "tqdm")
target = str(HERE / "run_one.py")

if all(importlib.util.find_spec(m) for m in NEEDED):
    os.execv(sys.executable, [sys.executable, target])
uv = shutil.which("uv")
if not uv:
    sys.exit("missing Python packages %s and no uv to provide them" % ", ".join(NEEDED))
args = [uv, "run", "-q"] + [x for m in NEEDED for x in ("--with", m)] + ["python", target]
os.execv(uv, args)
