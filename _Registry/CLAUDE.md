# Registry — Routing

Inventories. Each file answers "what exists?" for one class of capability.
Registries are read at session start; they are not narrative documents.

| File | Inventory |
|---|---|
| `Skills.md` | Every skill available in this project, grouped: core document, business framework, professional, Notion, Practice OS |
| `Cadences.md` | Recurring rituals — daily, sprint, weekly, monthly, quarterly, annual, and trigger-based |
| `MCPs.md` | Connected MCP services, their capabilities, and when to reach for each |

## Skills registry

Practice OS skills live in `.claude/skills/<name>/SKILL.md` and are the only
ones this repo ships. The rest of `Skills.md` catalogs skills available in the
wider environment. Adding a Practice OS skill means: write the SKILL.md with
YAML frontmatter, register it here, and add it to the root `## Skills` block —
check 03 in `scripts/CLAUDE.md` verifies the two agree.

Atomic subagents live in `.claude/agents/<name>.md`. Three exist:
`dq-validator`, `schema-reviewer`, `compliance-checker`. Each has one job and
an explicit boundary; do not widen their scope.

## Cadences registry

Two tiers. Team-level rituals (standup, sprint, 1-on-1, PI planning) and
Practice OS rituals (sanitization audit, weekly synthesis, governance gate,
attribution lint, IP coverage, diagram refresh). A new trigger-based workflow
in `Workflows/` needs a row in the trigger table.

## MCP registry

Notion is the live reference — fetch by page ID rather than trusting a
snapshot. GitHub MCP scope is restricted to this repository. Gmail produces
drafts only, never sends. Diagram MCP output follows the palette and layout
rules in `methodology/diagram-generation.md`.

## Keeping registries honest

Each file carries a `*Last updated*` stamp at the bottom. Update it in the same
commit that changes the inventory, and log the change per `_Logs/CLAUDE.md`.
