# Forkable Subprojects — Routing

Two self-contained subprojects, carried here to be copied out. Neither is live
practice content, and neither is loaded as practice context.

| Subproject | What it is | Start at |
|---|---|---|
| `dabs-data-product-template/` | Databricks Asset Bundle driven by one `data-contract.yml` | `dabs-data-product-template/README.md` |
| `career-command-center/` | Personal job-search operating system for Claude Code | `career-command-center/README.md` |

## Read this before treating a nested CLAUDE.md as instructions

Both subprojects ship their own `CLAUDE.md`. Those files are **payload**: they
configure the agent inside a fork, not inside Noosphere.
`career-command-center/CLAUDE.md` opens by casting the reader as a career coach — that instruction applies to
someone who has copied the folder out, never to work on this repository.

When editing a subproject, you are a maintainer of a template. Keep
placeholders as placeholders. Do not fill them in with real content.

## DABs Data-Contract Golden Path

The flagship. One `data-contract.yml` declares a data product; the bundle
wires it into Bronze ingestion, Silver DLT expectations, Gold transformations,
Platinum AI-ready views, Unity Catalog access control, and CI/CD gates.

- Source of truth: `dabs-data-product-template/data-contract.yml`, validated
  against `dabs-data-product-template/data-contract.schema.json`.
- Python lives in `dabs-data-product-template/src/contract/` (loader plus
  checks) and `dabs-data-product-template/src/pipelines/` (one module per
  medallion layer).
- Gate it with `dabs-data-product-template/scripts/validate_bundle.sh` and the
  unit tests under `dabs-data-product-template/tests/`. Check 04 in
  `scripts/CLAUDE.md` runs both.
- The authored write-up is `ip/authored/dabs-data-contract-golden-path.md`;
  the four walkthroughs are in `dabs-data-product-template/docs/`.

Bootstrap a fork with the `dabs-template-init` skill.

## Career Command Center

A folder a job seeker opens in Claude Code. `profile.yml` holds the user's
profile and drives every response; six slash commands live in
`career-command-center/.claude/skills/`. It carries its own routing table,
invariants, and session-start protocol, independent of this repo's.

**Ten files in it hold personal data and none of them is tracked.** Each ships
as a `.example` template that is tracked;
`career-command-center/bootstrap.sh` copies each to its live filename at
session start, and `career-command-center/.gitignore` keeps the live copy out
of git. Editing this subproject means editing the `.example` files.

The risk is not only the user's own data. `target-companies.md` and
`interview-retro.md` ask for recruiter and interviewer names — other people's
personal data, gathered by someone with no standing to publish it. Before
v1.4.0 all ten were tracked, guarded only by a comment reading "do not commit
this file." A comment is not a control.

## Not to be confused with

`Templates/` (capitalized) holds single-document formats — decision memo,
status update, RCA, user story. See `Templates/CLAUDE.md`.
