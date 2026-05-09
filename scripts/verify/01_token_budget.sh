#!/usr/bin/env bash
# verify/01_token_budget.sh — CLAUDE.md must be ≤600 tokens (≈480 target).
# Token estimate: words × 1.3 (rough English-to-tokens ratio).
set -euo pipefail
ROOT="${ROOT:-$(git rev-parse --show-toplevel)}"
FILE="$ROOT/CLAUDE.md"
WORDS=$(wc -w < "$FILE")
EST_TOKENS=$(awk -v w="$WORDS" 'BEGIN { printf "%d", w*1.3 }')
LIMIT=600
echo "CLAUDE.md: $WORDS words ≈ $EST_TOKENS tokens (limit $LIMIT)"
if [ "$EST_TOKENS" -gt "$LIMIT" ]; then
  echo "FAIL: CLAUDE.md exceeds token budget."
  exit 1
fi
echo "PASS"
