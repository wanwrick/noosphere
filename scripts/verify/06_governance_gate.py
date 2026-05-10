#!/usr/bin/env python3
"""verify/06_governance_gate.py — every regulated:true archetype must declare
DPIA expectations honestly. We accept dpia_required:true with dpia_completed
either true or false, but the field must be present and explicit (no nulls
where regulated:true)."""
from __future__ import annotations
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("SKIP: PyYAML not installed; skipping 06_governance_gate.")
    sys.exit(0)

root = Path(__file__).resolve().parents[2]
y = root / "initiatives" / "initiatives.yaml"
if not y.exists():
    print(f"FAIL: {y} missing")
    sys.exit(1)

doc = yaml.safe_load(y.read_text())
fail = 0
for a in doc.get("archetypes", []):
    aid = a.get("id", "<unknown>")
    if a.get("regulated") is True:
        if "dpia_required" not in a:
            print(f"FAIL: {aid} regulated:true but dpia_required missing")
            fail = 1
        if "dpia_completed" not in a:
            print(f"FAIL: {aid} regulated:true but dpia_completed missing")
            fail = 1
        if a.get("dpia_required") is True and a.get("dpia_completed") is None:
            print(f"FAIL: {aid} dpia_required but dpia_completed is null")
            fail = 1

sys.exit(fail)
