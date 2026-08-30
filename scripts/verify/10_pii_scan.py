#!/usr/bin/env python3
"""verify/10_pii_scan.py — wraps the PII gate.

Runs in --files-only mode. verify_all.sh output is surfaced in CI on a public
repository, so a finding must never echo the matched text: that would republish
the exact personal data the gate exists to suppress.
"""

import os
import subprocess
import sys

root = os.environ.get("ROOT") or subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True, check=True,
).stdout.strip()

result = subprocess.run(
    [sys.executable, os.path.join(root, "scripts", "lint_pii.py"), "--files-only"],
    cwd=root,
)

if result.returncode != 0:
    print("FAIL: PII scan found personal data. See Workflows/pii-audit-pass.md.")
    sys.exit(result.returncode)

print("PASS")
