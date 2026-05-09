# Diagram Generation

> Conventions for diagrams in this practice. Three flavors: Mermaid (preferred for in-repo), ASCII (preferred for plain-text routing files), Excalidraw (local review artifacts only — gitignored).

## Mermaid (in-repo, version-controlled)

Use the diagram MCP (`mcp__a28417ff-…`) for `generate_mermaid_diagram` and `draw_svg_image` calls. Embed Mermaid in `_Diagrams/*.md` files (rendered live by GitHub).

| Diagram type | Mermaid block |
|---|---|
| Architecture | `flowchart TD` or `flowchart LR` |
| Sequence (handoffs, negotiation) | `sequenceDiagram` |
| State (lifecycle phases) | `stateDiagram-v2` |
| Gantt (roadmap) | `gantt` |
| Mindmap (decompositions) | `mindmap` |
| ER (data model) | `erDiagram` |

## ASCII (plain-text in markdown)

Default for routing/flow diagrams in CLAUDE.md and IP files where Mermaid would be overkill. ASCII renders everywhere.

```
+--------+     +--------+     +--------+
| Bronze | --> | Silver | --> |  Gold  |
+--------+     +--------+     +--------+
```

Conventions:
- Boxes via `+--+` corners.
- Arrows `-->` for direction.
- Vertical `|` for hierarchy.
- Avoid Unicode box-drawing for grep-friendliness.

## Excalidraw (local only)

Excalidraw files are local review artifacts. Gitignored (`*.excalidraw`). The generator script produces them on demand; they don't live in the repo.

If a diagram needs whiteboard-style sketch aesthetic, draw in Excalidraw locally, export as PNG, and check in only the PNG to `_Diagrams/`.

## Style constraints (enforced via convention)

| Constraint | Rule |
|---|---|
| Palette | Pastel: `#AEC6CF` (blue) · `#B7E4C7` (green) · `#FDFD96` (yellow) · `#C3B1E1` (purple) · `#D3D3D3` (gray). No bright red, orange, neon. |
| Layout | Strictly left-to-right or top-to-bottom. No zig-zag flows. |
| Text | No ordinals (1, 2, 3) to indicate sequence — use arrows. All labels grammatically correct. |
| Spacing | Box height min 62px for two-line text. Vertical gap between stacked boxes ≥14px. |
| Overlap guard | Any element below a detail card starts after `card_y + card_height + gap`. |
| Style (Excalidraw only) | Whiteboard sketch aesthetic. roughness=1. Virgil font. White canvas. |

## v1.2.0 diagram inventory

13 Mermaid diagrams under `_Diagrams/`:

| File | Subject |
|---|---|
| `_Diagrams/no-lac-architecture.md` | No LAC Bronze→Platinum medallion architecture |
| `_Diagrams/ai-ready-platinum-5-principles.md` | AI-Ready Platinum 5 Principles + 6-question rubric |
| `_Diagrams/dabs-contract-flow.md` | DABs Data-Contract Golden Path: contract YAML → DLT/UC/permissions/views |
| `_Diagrams/practice-os-3-layers.md` | The three-layer mental model (Context / Queries / Discipline) |
| `_Diagrams/ip-catalog-attribution.md` | Authored vs Curated vs EMBA buckets |
| `_Diagrams/10q-discovery-flow.md` | 10Q discovery session decision flow |
| `_Diagrams/platform-mandate-coalition.md` | Sequence: engineers → adjacent → manager → decision-maker |
| `_Diagrams/strategy-cascade.md` | Roger Martin Cascade |
| `_Diagrams/case-answer-shapes.md` | 4 prompt types → framework combos |
| `_Diagrams/medallion-layers-table.md` | Property table per Medallion layer |
| `_Diagrams/ai-consumption-contract-shape.md` | What an AI Consumption Contract looks like in practice |
| `_Diagrams/sanitization-flow.md` | Sanitization pass workflow |
| `_Diagrams/governance-audit-flow.md` | Governance audit gate decision flow |

## Cross-references

- `_Diagrams/` — the rendered diagrams.
- `practice-context/voice-and-style.md` — output style discipline these diagrams support.
