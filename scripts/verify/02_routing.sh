#!/usr/bin/env bash
# verify/02_routing.sh — every backtick path referenced in CLAUDE.md routing
# table must exist (file or directory).
set -euo pipefail
ROOT="${ROOT:-$(git rev-parse --show-toplevel)}"
FILE="$ROOT/CLAUDE.md"
FAIL=0

# Extract paths from the routing table (lines that look like ` `path/...` `)
PATHS=$(grep -oE '`[A-Za-z_][A-Za-z0-9_./-]*`' "$FILE" \
  | tr -d '`' \
  | grep -E '\.(md|sh|py|yaml|yml|json)$|/$' \
  | sort -u || true)

# Also include directory references that end with / in the routing table
DIRS=$(awk '/^\| / && /`[A-Za-z_][A-Za-z0-9_/-]*\/`/' "$FILE" \
  | grep -oE '`[A-Za-z_][A-Za-z0-9_/-]*/`' \
  | tr -d '`' | sort -u || true)

CHECK="$PATHS
$DIRS"

while read -r p; do
  [ -z "$p" ] && continue
  if [ ! -e "$ROOT/$p" ]; then
    echo "FAIL: routing target missing: $p"
    FAIL=1
  fi
done <<< "$CHECK"

if [ "$FAIL" -eq 1 ]; then
  exit 1
fi
echo "PASS: all routing-table targets exist (or are explicitly deferred)."
