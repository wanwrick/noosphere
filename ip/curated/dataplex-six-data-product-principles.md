# Dataplex — Six Data Product Principles

> **Source:** Google Cloud — Dataplex Data Products documentation. Public reference principles for data product design on Google Cloud.

## The six principles

| # | Principle | What it means |
|---|---|---|
| 1 | **Use case-driven design** | Data products are curated collections solving specific business problems, not random data dumps |
| 2 | **Clear ownership** | Explicit accountability for each data product |
| 3 | **Rich context** | Essential for agent-based consumption and discoverability |
| 4 | **Contractual guarantees** | Trust guarantees on refresh cadence, data quality, SLAs |
| 5 | **Governed access** | Approval workflows with clear auditability |
| 6 | **Easy discovery** | Available in catalog universal search |

## Why these matter beyond Dataplex

Even if you're on Databricks / Snowflake / Fabric / dbt-core, the six principles generalize. They are the **table-stakes** properties of a data product on **any** modern lakehouse / warehouse stack:

- Use case-driven (vs database-driven).
- Clear ownership (vs shared confusion).
- Rich context (vs sparse description).
- Contractual guarantees (vs assumptions).
- Governed access (vs IT ticket queue).
- Easy discovery (vs tribal knowledge).

## When to use this in this practice

- **Cross-cloud / multi-platform conversations** — when explaining data products to a team that uses GCP / Dataplex, this is their vocabulary.
- **Data mesh on GCP** — direct mapping to Dataplex Data Products + Catalog Federation.
- **Cross-reference for the 5-Pillars** (Czarnas) — Czarnas is engineering-pillars; Dataplex is product-design-principles. They overlap but address different audiences.

## Mapping to this practice

| Dataplex principle | This practice's component |
|---|---|
| 1 — Use case-driven | Dashboard Factory Escape 9-Q (Q1 + Q2) |
| 2 — Clear ownership | `data-contract.yml` `metadata.owner_team` + `metadata.steward` |
| 3 — Rich context | AI-Ready Platinum 6-question metadata rubric |
| 4 — Contractual guarantees | `data-contract.yml` `freshness` + `quality_expectations[]` |
| 5 — Governed access | UC ABAC grants in `resources/permissions.yml` |
| 6 — Easy discovery | UC catalog + (per `bain-3-layer-agentic.md`) MCP Catalog for agent discovery |

## Cross-references

- `data-product-architecture-5-pillars.md` (Czarnas) — engineering pillars; complements these design principles.
- `data-contracts-producer-consumer.md` (Baeyens) — operationalizes Principle 4.
- `context-wall-meta-knowledge-graph.md` (Tekiner) — operationalizes Principle 3 at agent scale.
