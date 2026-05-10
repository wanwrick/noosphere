---
name: weekly-practice-synthesis
description: Run the Friday Weekly Practice Synthesis ritual. Reflects on the week's engagements, IP applied, corrections logged, system fixes proposed, and surfaces insight candidates. Use every Friday end-of-day, or whenever the user wants a structured retrospective on the practice itself.
---

# weekly-practice-synthesis

You are running the **Weekly Practice Synthesis** ritual — the practice's
Friday retro. Output is one page, BLUF, and ends with a punch list.

## Source files
- `_Registry/Cadences.md` (Practice OS Rituals section — synthesis format).
- `_Logs/feedback.md` (this week's corrections).
- `_Logs/evolution.md` (this week's system fixes).
- `_Logs/sanitization-audit.md` (this week's audit findings).
- `initiatives/initiatives.yaml` (this week's archetype phase changes).
- `insights/` (existing POVs — once Phase 11 lands).

## When to invoke
- Friday end-of-day, weekly cadence.
- User says "weekly synthesis", "Friday retro", "practice check-in".
- After a high-density week of engagements where lessons risk being lost.

## Required inputs
1. Date range (default: last 7 days).
2. Whether this week touched live engagements vs IP authoring vs both.

## Steps
1. Pull commits in the date range and group by directory:
   `ip/authored`, `ip/curated`, `initiatives`, `data-products`,
   `governance`, `methodology`, `_Logs`.
2. Read `_Logs/feedback.md` entries dated in the range.
3. Read `_Logs/evolution.md` entries dated in the range.
4. Read `initiatives/initiatives.yaml` diff (phase + scorecard changes).
5. Read `_Logs/sanitization-audit.md` entries.
6. Identify insight candidates: any 3+ corrections in the same theme, any
   POV the user articulated in chat or commits.
7. Identify open governance items: archetypes blocked by `dpia_required:
   true` and `dpia_completed: false`.

## Output shape
```
# Weekly Practice Synthesis — <Mon DD> to <Fri DD>

**BLUF:** <One sentence on the week's signal: what shifted, what's stuck.>

## Engagements touched
<archetype IDs + one-line phase delta each>

## IP applied this week
- Authored: <list, with link>
- Curated: <list, with link + cited author>

## Corrections logged → system fixes
| Correction | Frequency | System fix proposed |
|---|---|---|
<rows from feedback.md>

## Insight candidates (POVs to develop)
1. <candidate, one line — link to draft if any>
2. <…>

## Open governance items
- <archetype ID>: <DPIA / classification / masking gap>

## Punch list (next week, max 5)
- [ ] <action, owner, due trigger>
- [ ] <…>
```

## Verification
- BLUF: first sentence stands alone.
- Punch list: every item has an owner and a trigger or date.
- Sanitization: no employer / stakeholder names.
- Banned style absent.
- If 3+ corrections in same theme → autoresearch loop trigger noted
  (see `Workflows/self-improvement.md`).

## Handoff
- Save synthesis to `_Logs/synthesis-<YYYY-MM-DD>.md`.
- Append insight candidates to `insights/_backlog.md` (once Phase 11
  lands; until then keep at end of synthesis file).
- If a system-level fix surfaced: open the change as part of next
  commit and log to `_Logs/evolution.md`.
