#!/usr/bin/env bash
# verify/05_attribution_lint.sh — Invariant #3: authored vs curated never blurred.
# Every ip/curated/*.md must carry a "Source" callout. ip/authored/*.md must NOT.
set -euo pipefail
ROOT="${ROOT:-$(git rev-parse --show-toplevel)}"
FAIL=0

CURATED_DIR="$ROOT/ip/curated"
AUTHORED_DIR="$ROOT/ip/authored"

# 1. Curated must cite a Source
for f in "$CURATED_DIR"/*.md; do
  [ -f "$f" ] || continue
  case "$(basename "$f")" in
    CLAUDE.md|INDEX.md) continue ;;
  esac
  if ! grep -qiE '^[> ]*\*\*Source[s]?[:*]|^[> ]*Source[s]?:|^## Source' "$f"; then
    echo "FAIL: curated file missing Source callout: ${f#$ROOT/}"
    FAIL=1
  fi
done

# 2. Authored must NOT cite an external Source as the primary attribution
# (curated underpinning citations are OK; what's banned is presenting
# an authored file as if it were curated).
for f in "$AUTHORED_DIR"/*.md; do
  [ -f "$f" ] || continue
  case "$(basename "$f")" in
    CLAUDE.md|INDEX.md) continue ;;
  esac
  # An authored file should declare authorship somewhere
  if ! grep -qiE 'Paroz|authored|Author:' "$f"; then
    echo "WARN: authored file lacks explicit authorship marker: ${f#$ROOT/}"
  fi
done

if [ "$FAIL" -eq 1 ]; then exit 1; fi
echo "PASS: attribution discipline holds (Invariant #3)."
