#!/usr/bin/env bash
# verify/09_diagram_coverage.sh — every diagram declared in
# methodology/diagram-generation.md must exist in _Diagrams/.
set -euo pipefail
ROOT="${ROOT:-$(git rev-parse --show-toplevel)}"
INV="$ROOT/methodology/diagram-generation.md"
FAIL=0

DIAGRAMS=$(grep -oE '_Diagrams/[a-z0-9-]+\.md' "$INV" | sort -u)
for d in $DIAGRAMS; do
  if [ ! -f "$ROOT/$d" ]; then
    echo "FAIL: declared diagram missing: $d"
    FAIL=1
  fi
done

if [ "$FAIL" -eq 1 ]; then exit 1; fi
echo "PASS: every diagram declared in the inventory exists."
