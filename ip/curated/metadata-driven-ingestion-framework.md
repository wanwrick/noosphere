# Metadata-Driven Lakehouse Ingestion Framework

> **Source:** Yasar Kocyigit. Open-source GitHub project. LinkedIn post + repo. [Post](https://www.linkedin.com/posts/yasarkocyigit_databricks-lakehouse-dataengineering-activity-7432386473104080897-S-nA).

## Core insight

An **open-source, metadata-driven ingestion framework for the Databricks Lakehouse**. YAML-based contracts define tables, data quality rules, and ingestion strategy across Bronze → Silver → Gold, with environment-based deployments via Databricks Asset Bundles.

## Capabilities

| Layer | Capability | Detail |
|---|---|---|
| Metadata | YAML-based contracts | Single source of truth for tables, DQ rules, ingestion strategy |
| Bronze | Strategy-aware ingestion | Snapshot · Incremental · CDC chosen per table via metadata |
| Silver | Quality + quarantine | DQ rules from YAML; failed records quarantined (not dropped) |
| Gold | Dimensional modeling | Fact + dimension tables with SCD paths |
| Deployment | Environment-based | dev / staging / prod via Databricks Asset Bundles |
| Observability | Monitoring + runbooks | Operational dashboards and incident-response patterns |

## The framework — before vs after

| Dimension | ❌ Ad-hoc pipeline code | ✅ Metadata-driven |
|---|---|---|
| Config | Logic scattered across notebooks | YAML contracts as single source of truth |
| Ingestion | One-size-fits-all or custom per table | Strategy-aware per contract |
| DQ rules | Bolted-on afterthought | Defined in metadata, enforced at Silver with quarantine |
| Deployment | Manual env management | Asset Bundles auto-deploy across dev/stg/prod |
| Onboarding | Write new pipeline per source | Add a YAML file, framework does the rest |

## Why it matters

Kocyigit's framework is **direct architectural inspiration** for the DABs Data-Contract Golden Path subproject in this practice. The pattern:

- YAML metadata as authoritative.
- Bronze ingestion strategy chosen from metadata.
- Silver DLT expectations generated from metadata.
- DABs for environment-aware deployment.

## When to use this in this practice

- As a reference implementation when explaining the DABs Golden Path to a new engineer.
- As an open-source pattern to point teams to who want a stand-alone (non-Noosphere) implementation.
- As architectural justification for "why YAML and not bespoke Python."

## Cross-references

- `data-contracts-producer-consumer.md` (Baeyens) — the contract layer above.
- `data-product-architecture-5-pillars.md` (Czarnas) — Pillar 4 (Standard Templates) is what this implements.
- `dabs-custom-templates.md` (Shi) — pairs with this for project-bootstrap.
- `dabs-cicd-asset-bundles.md` (Shi) — pairs with this for deployment.
- `../authored/dabs-data-contract-golden-path.md` — this practice's own implementation, contract-first.
