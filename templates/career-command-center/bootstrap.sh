#!/usr/bin/env bash
# bootstrap.sh — create the Career Command Center's working files.
#
# Every file this creates holds personal data once a session populates it, so
# none of them is tracked by git. Each ships as a `.example` template that is
# tracked; this script copies each to its live filename, once, without ever
# overwriting work you have already done.
#
# Run automatically by the SessionStart hook. Safe to run by hand any time:
#   bash bootstrap.sh

set -euo pipefail

cd "$(dirname "$0")"

CREATED=0
for example in \
  profile.example.yml \
  GOALS.example.md \
  _Logs/session-log.example.md \
  job-search/applications-tracker.example.md \
  job-search/target-companies.example.md \
  interview-prep/star-stories.example.md \
  interview-prep/interview-retro.example.md \
  career-strategy/compensation-strategy.example.md \
  career-strategy/positioning-narrative.example.md \
  career-strategy/90-day-plan.example.md
do
  # profile.example.yml -> profile.yml ; foo.example.md -> foo.md
  live="${example/.example/}"

  [[ -f "$example" ]] || continue
  if [[ ! -f "$live" ]]; then
    mkdir -p "$(dirname "$live")"
    cp "$example" "$live"
    CREATED=$((CREATED + 1))
  fi
done

if [[ $CREATED -gt 0 ]]; then
  echo "Career Command Center: created $CREATED working file(s) from templates."
  echo "These are gitignored — they will hold your personal data and must not be committed."
fi
