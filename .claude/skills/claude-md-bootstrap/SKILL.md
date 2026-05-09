---
name: claude-md-bootstrap
description: Generate a CLAUDE.md routing brain for a fork of Noosphere or for a new repo that follows the Noosphere routing pattern. Use when the user is forking the practice OS, starting a new client engagement repo, or migrating a legacy repo onto Noosphere conventions.
---

# claude-md-bootstrap

You are bootstrapping the **CLAUDE.md routing brain** — the ~480-token entry
file that turns a repo into a Noosphere-style operating system. Stay terse.
The output should be the file content, not commentary.

## When to invoke
- User says "fork Noosphere", "set up CLAUDE.md", "bootstrap the practice OS".
- A new repo lacks a CLAUDE.md or has a stale one written before the
  three-layer mental model.

## Required inputs (ask if missing)
1. **Practice / repo name** (e.g. "Noosphere", "Acme Data Practice").
2. **Author byline** (one line, optional credentials).
3. **Three-layer scope** — which directories own which layer?
   - Shared Context: identity, voice, IP catalog, MBA grounding.
   - Shared Queries: initiatives, data products, playbooks, talent.
   - Shared Discipline: governance, workflows, skills, logs.
4. **Routing table rows** — for each top-level directory with a CLAUDE.md,
   one row pointing to it.
5. **Invariants** — start with Sanitization (#0), IP-applied coverage (#1),
   governance gate (#2), source citation (#3), banned style (#4).
6. **Skill list** — names only, comma-separated.
7. **IP catalog** — authored vs curated, never blurred.

## Output shape
```
# <Repo name> — Practice Operating System

You are the AI work partner of <byline>. You **route** questions; nested
CLAUDE.md files own the detail. Default to BLUF, ≤25 words per sentence,
framework named explicitly. Cite sources: never blur authored vs curated IP.

## Three-Layer Mental Model
1. **Shared Context** — <one line>
2. **Shared Queries** — <one line>
3. **Shared Discipline** — <one line>

## Routing Table
| Question is about… | Read first |
|---|---|
<rows>

## Invariants
0. Sanitization is sacred. <one line on banned-token lint>
1. <…>

## Skills (vX.Y.Z)
<comma-separated names>

## IP Catalog (Honest Attribution)
**Authored** — <list>
**Curated** — <list with named authors>

## Session Protocol Summary
1. Load GOALS.md, _Logs/feedback.md, _Registry/Cadences.md.
2. Plan before execute.
3. Three-pass verification (framework, BLUF, action).
4. Close the loop: log corrections.
5. Self-improvement check.

## Version
vX.Y.Z. Changelog: _Logs/evolution.md.
```

## Verification (run before delivering)
- File ≤ 600 tokens (≈ 480 target).
- Every routing-table row points to a path that exists or is committed in
  the same change.
- No banned style words (leverage, utilize, synergies, deep dive,
  circle back).
- Sanitization: no employer / team / stakeholder / JIRA / vendor name.
- Invariant #1 satisfied: at least one IP file referenced in the catalog.

## Reference files
- `methodology/how-we-work.md` (Session Protocol long form)
- `ip/authored/enterprise-claude-md.md` (the authored pattern)
- Existing `CLAUDE.md` of this repo (canonical example)
