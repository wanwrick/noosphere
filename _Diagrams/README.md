# Diagrams

> 13 Mermaid diagrams + 3 PNG snapshots. GitHub renders Mermaid blocks natively. PNG files are v1.1 archive renders.

## Mermaid (v1.2.0)

Source files use `flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `mindmap`, and `erDiagram` per the conventions in `methodology/diagram-generation.md`.

| File | Subject | Mermaid type |
|------|---------|--------------|
| `no-lac-architecture.md` | Bronze → Silver → Gold → Platinum medallion stack | flowchart LR |
| `ai-ready-platinum-5-principles.md` | 5 Principles + 6-question metadata rubric | flowchart + mindmap |
| `dabs-contract-flow.md` | One YAML → ingestion · DLT · UC · views · CI | flowchart LR |
| `practice-os-3-layers.md` | Three-layer mental model | flowchart TB |
| `ip-catalog-attribution.md` | Authored · Curated · EMBA buckets | flowchart LR |
| `10q-discovery-flow.md` | 10-question intake decision flow | flowchart TB |
| `platform-mandate-coalition.md` | Coalition sequence — engineers to decision-maker | sequenceDiagram |
| `strategy-cascade.md` | Roger Martin Cascade | flowchart TB |
| `case-answer-shapes.md` | 4 prompt types → framework combos | flowchart LR |
| `medallion-layers-table.md` | Property table per medallion layer | flowchart TB |
| `ai-consumption-contract-shape.md` | AI Consumption Contract entity shape | erDiagram |
| `sanitization-flow.md` | Invariant #0 pre-commit gate flow | flowchart LR |
| `governance-audit-flow.md` | Invariant #2 7-check audit state diagram | stateDiagram-v2 |

## PNG archive (v1.1)

| File | Subject |
|------|---------|
| `diagram1_file_tree.png` | v1.1 file tree (superseded by README directory tree) |
| `diagram2_architecture.png` | v1.1 architecture (superseded by `no-lac-architecture.md`) |
| `diagram3_decision_tree.png` | v1.1 decision tree (superseded by `case-answer-shapes.md`) |

## Style

Pastel palette · L-to-R or T-to-B layout · no zig-zag · grammatically-correct labels · `methodology/diagram-generation.md` for the full ruleset.

## How to add a new diagram

1. Write Mermaid source in a new `<topic>.md` file here.
2. Add a row to the table above.
3. Add a row to the inventory in `methodology/diagram-generation.md`.
4. Run `bash scripts/lint_sanitization.sh` — must pass.
5. Commit. GitHub renders the Mermaid block in the rendered markdown view.
