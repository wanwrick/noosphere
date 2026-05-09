#!/usr/bin/env bash
# verify/03_skill_invocation.sh — every skill named in CLAUDE.md must exist
# at .claude/skills/<name>/SKILL.md, and every subagent at .claude/agents/<name>.md.
set -euo pipefail
ROOT="${ROOT:-$(git rev-parse --show-toplevel)}"
CLAUDEMD="$ROOT/CLAUDE.md"
FAIL=0

# Extract backtick-quoted skill names from the "Skills (v1.2.0)" + atomic block.
SKILLS=$(awk '/^## Skills/{flag=1;next} /^## /{flag=0} flag' "$CLAUDEMD" \
  | grep -oE '`[a-z][a-z0-9-]+`' | tr -d '`' | sort -u)

# Atomic subagents listed under same section.
SUBAGENTS="dq-validator schema-reviewer compliance-checker"

for s in $SKILLS; do
  # Skip the subagents (they live in agents/, not skills/)
  case " $SUBAGENTS " in *" $s "*) continue ;; esac
  if [ ! -f "$ROOT/.claude/skills/$s/SKILL.md" ]; then
    echo "FAIL: skill missing: .claude/skills/$s/SKILL.md"
    FAIL=1
  fi
done

for a in $SUBAGENTS; do
  if [ ! -f "$ROOT/.claude/agents/$a.md" ]; then
    echo "FAIL: subagent missing: .claude/agents/$a.md"
    FAIL=1
  fi
done

if [ "$FAIL" -eq 1 ]; then exit 1; fi
echo "PASS: all skills + subagents declared in CLAUDE.md exist."
