# IP Catalog Index

One-page roll-up of all IP in this practice. Authored vs Curated never blurred. Source attribution mandatory in `curated/`.

## Authored (6)

| File | Headline |
|---|---|
| `authored/no-lac-principle.md` | *No Lack of Analytical Capability.* Bronze through Platinum architecture; custom code only at Gold; humility as posture. |
| `authored/ai-ready-platinum-layer.md` | UC metadata as runtime semantic layer for AI agents. 5 Principles + 6-question rubric. *1× publish → 1× govern → 5+ consume.* |
| `authored/10q-framework.md` (+ `10q-toolkit/`) | New data source onboarding stress-test across 10 dimensions. Toolkit: intake form · elicitation guide · tracker schema · Miro blueprint. |
| `authored/enterprise-claude-md.md` | Production-ready CLAUDE.md pattern for regulated-industry data engineering teams. |
| `authored/platform-mandate-playbook.md` | Risa Mish Congress Model + Shai Dubey Negotiation Map + Kotter overlay for platform-team formalization. Stakeholder-name-free. |
| `authored/dabs-data-contract-golden-path.md` | Doc page describing the working forkable subproject at `templates/dabs-data-product-template/`. |

## Curated (12 named authors)

| File | Author | Source type |
|---|---|---|
| `curated/data-thinking-4-pillars.md` | Yassine Mahboub | LinkedIn post |
| `curated/defending-ai-spend-12q.md` | Raj Grover | LinkedIn post |
| `curated/dashboard-factory-escape-9q.md` | Sebastian Hewing | LinkedIn post |
| `curated/context-wall-meta-knowledge-graph.md` | Firat Tekiner | Medium article series |
| `curated/data-product-architecture-5-pillars.md` | Piotr Czarnas | LinkedIn post |
| `curated/data-contracts-producer-consumer.md` | Tom Baeyens | LinkedIn post |
| `curated/bain-3-layer-agentic.md` | Bain & Company | Insights article (Apr 2026) |
| `curated/metadata-driven-ingestion-framework.md` | Yasar Kocyigit | Open-source GitHub repo |
| `curated/dabs-custom-templates.md` | Mengyu Shi | LinkedIn post |
| `curated/dabs-cicd-asset-bundles.md` | Mengyu Shi | LinkedIn post |
| `curated/dataplex-six-data-product-principles.md` | Google Cloud | Documentation |
| `curated/cdo-top-10-deliverables.md` | Synthesized — origin unclear | (Disclaimer in file) |

## EMBA grounding

Cornell-Queen's EMBA frameworks live in `Knowledge/EMBA/`. Cross-cutting strategy toolkits live in `Knowledge/Strategy/`. Evergreen MBA frameworks live in `Knowledge/Frameworks/`.

## Attribution policy

Every file in `curated/` must start with a Source callout naming the author + URL. Lint enforces. See `methodology/attribution-policy.md`.

## How to add an authored file

1. Sanitize first (run `Workflows/sanitization-pass.md`).
2. Add file under `authored/`.
3. Add row to this index.
4. Bump version in `_Logs/evolution.md` (minor bump if structural; patch otherwise).

## How to add a curated file

1. Confirm the source is publicly published (open-source repo, public LinkedIn / Medium post, public documentation).
2. Add file under `curated/` starting with a Source callout (author + URL + date).
3. Add row to this index.
4. Cite the file from any authored IP that draws on it.
