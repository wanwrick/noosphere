#!/usr/bin/env python3
"""verify/07_ip_coverage.py — Invariant #1: every active archetype names
≥1 IP file in ip_applied (authored or curated) AND every named IP file
exists on disk."""
from __future__ import annotations
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("SKIP: PyYAML not installed; skipping 07_ip_coverage.")
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
    ip = a.get("ip_applied", {}) or {}
    authored = ip.get("authored") or []
    curated = ip.get("curated") or []
    total = len(authored) + len(curated)
    if total < 1:
        print(f"FAIL: {aid} has no ip_applied entries (Invariant #1).")
        fail = 1
        continue
    for slug in authored:
        path = root / "ip" / "authored" / f"{slug}.md"
        if not path.exists():
            print(f"FAIL: {aid} cites authored:{slug} but {path.relative_to(root)} missing")
            fail = 1
    for slug in curated:
        path = root / "ip" / "curated" / f"{slug}.md"
        if not path.exists():
            print(f"FAIL: {aid} cites curated:{slug} but {path.relative_to(root)} missing")
            fail = 1

if fail == 0:
    print("PASS: every archetype has ≥1 IP applied and every IP slug resolves.")
sys.exit(fail)
