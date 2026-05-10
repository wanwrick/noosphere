# Repository Conventions

Operational discipline for editing this repo. Pairs with `CONTRIBUTING.md` (which is the public-facing version of the same rules).

## File naming

- `kebab-case.md` for content files (frameworks, IP pages, playbooks, workflows).
- `SCREAMING_CASE.md` for top-level system files (`CLAUDE.md`, `README.md`, `LICENSE`, `CONTRIBUTING.md`).
- `_underscore-prefix` for system folders (`_Logs/`, `_Registry/`, `_Diagrams/`).
- Decision logs: `Knowledge/Decisions/<YYYY-MM-DD>-<topic>.md` (date prefix mandatory).

## Placeholder convention

All personalizable content uses bracket syntax:

| Placeholder | Use for |
|---|---|
| `[Your Name]` | Person name in fork-target files |
| `[Practice Name]` | Practice / firm / employer name |
| `[Producer Team]` | Team codename |
| `[Stack]` | Technology stack |
| `[Date]` | Date stamp |
| `[ARCHETYPE-X]` | Anonymized initiative reference |
| `your-notion-page-id-here` | Notion page IDs |
| `your-notion-database-id-here` | Notion database IDs |

Never use `TBD`, `<placeholder>`, `XXX`, or other ad-hoc syntax. The v1.1.2 patch existed solely to fix one such deviation.

## Where content goes

| Adding... | Goes in... | Then update... |
|---|---|---|
| Authored IP page | `ip/authored/<file>.md` (sanitize first) | `ip/INDEX.md` + `_Logs/evolution.md` |
| Curated IP page | `ip/curated/<file>.md` (Source callout required) | `ip/INDEX.md` + cross-refs |
| EMBA framework | `Knowledge/EMBA/<subdir>/<file>.md` | `Knowledge/EMBA/CLAUDE.md` |
| Strategy toolkit | `Knowledge/Strategy/<file>.md` | `Knowledge/Strategy/CLAUDE.md` |
| Evergreen MBA framework | `Knowledge/Frameworks/<domain>.md` | None (existing routing covers it) |
| Workflow / playbook | `Workflows/<file>.md` (Verification Loop required) | `_Registry/Cadences.md` if trigger-based |
| Template | `Templates/<file>.md` (Pre-Delivery Verification required) | `README.md` directory tree |
| Decision | `Knowledge/Decisions/<date>-<topic>.md` | None |
| Initiative archetype | `initiatives/archetypes/ARCHETYPE-<letter>-<scope>.md` | `initiatives/initiatives.yaml` |
| Skill | `.claude/skills/<name>/SKILL.md` | `_Registry/Skills.md` |
| Correction / preference | `_Logs/feedback.md` | None |

## Mandatory sections per file class

| Class | Mandatory section |
|---|---|
| `Templates/<file>.md` | Pre-Delivery Verification |
| `Workflows/<file>.md` | Verification Loop |
| `ip/curated/<file>.md` | Source callout in first 10 lines |
| `Knowledge/Decisions/<file>.md` | Standard decision-memo headings |
| `.claude/skills/<name>/SKILL.md` | YAML frontmatter (name, description, when-to-use, version, inputs, outputs, verification) |

## Version discipline

Any change to repo structure (new file class, new routing rule, edited workflow) requires:

1. **Bump version** in `_Logs/evolution.md`:
   - **Major** (`x.0.0`): structural overhaul (rare).
   - **Minor** (`1.x.0`): new file class or routing rule.
   - **Patch** (`1.1.x`): edits to existing files only.
2. **Add a changelog entry** with: date · version · author · changed-files table · design decisions · gap that triggered the update.
3. **Update `README.md`** if directory tree or "What's New" changed.
4. **Update `CLAUDE.md` routing** if a new file requires a new route.

## Cross-reference hygiene

Renaming or moving a file requires updating:

- `CLAUDE.md` (root + nested routing).
- `README.md` (directory tree).
- `_Registry/Cadences.md` if trigger-based.
- Any sibling file that links to the moved one.

`grep -r "old-filename" .` is your friend.

## What does NOT belong in this repo

- Real customer / employer / team / stakeholder names (sanitization invariant).
- JIRA codes, dollar figures, dated meeting attributions.
- Personal Notion page IDs (placeholder convention).
- `.excalidraw` files (gitignored — local review artifacts only).
- Any file with raw Notion-source content that hasn't been sanitized.
- `.claude/cache/`, `.claude/sessions/` (gitignored).
