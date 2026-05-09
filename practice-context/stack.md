# Stack

Default technology stack assumed by this practice. Forks should replace specifics with their own.

## Compute + Lakehouse

- **Databricks** on **GCP** (or Azure / AWS). Unity Catalog as governance control plane.
- **BigQuery** for federated analytical reads + cross-cloud sharing.
- **Delta Lake** as the storage format on cloud object storage.

## Pipeline

- **DLT (Delta Live Tables)** for declarative pipelines with built-in expectations.
- **DABs (Databricks Asset Bundles)** for environment-aware deployment (dev / staging / prod) and CI/CD.
- **Lakeflow Connect** for query-based incremental ingestion when CDC is unavailable.
- **Auto Loader** for cloud-file ingestion with schema evolution.
- **Structured Streaming** for Kafka / Pub/Sub / Event Hubs.

## Modeling layers (No LAC convention)

| Layer | Purpose | Code freedom |
|---|---|---|
| Bronze | Raw, schema-explicit, all-source landing | Reusable framework only |
| Silver I | Clean + standardize within source | Parameterized only |
| Silver II | Denormalize within source | Parameterized only |
| Silver III | SCD Type 2 historicals | Parameterized only |
| Gold | First cross-source join + business logic | Custom code lives HERE only |
| Platinum | Semantic + AI-ready scoped views + UC functions | Custom code only for AI consumption logic |

See `ip/authored/no-lac-principle.md` for the architecture rationale.

## BI + AI consumption

- **Power BI** with DirectQuery to UC SQL Warehouses.
- **AI/BI Genie** for natural-language analytical agents.
- **MCP (Model Context Protocol) servers** for governed tool access — Managed MCP Servers, MCP Catalog, DBSQL MCP server.
- **Agent Bricks** for production multi-agent orchestration.
- **Vector Search + UC Functions** as agent context primitives.

## Governance + security

- **Unity Catalog ABAC** with column-level masking + row-level security.
- **EntraID groups** → UC grants (or equivalent IdP).
- **Classification:** Public / Internal / Confidential / Restricted (CDMC-aligned).
- **Audit logs** via UC + System Tables.

## Infra-as-code

- **Terraform** for cloud substrate (VPC, networking, KMS, IAM, GCS).
- **Terraform UC modules** authored by the producer team for catalogs / schemas / grants.
- **DABs** for Databricks-side resources (jobs, pipelines, workspace assets).
- **GitHub Actions** for CI/CD (lint + test + bundle validate + bundle deploy).

## Stack signals (for `claude-md-bootstrap` skill)

When bootstrapping a new project's CLAUDE.md, the skill detects these signals to choose the right Enterprise CLAUDE.md skeleton:

| Signal | Skeleton |
|---|---|
| `databricks.yml` present | Databricks/DLT/UC variant |
| `dbt_project.yml` present | dbt + warehouse variant |
| `pyproject.toml` + `dlt-init` present | Python lakehouse pipeline variant |
| `dataform.json` present | Dataform variant |

## Forks: replace this file

Forks should replace specifics (Databricks → Snowflake, GCP → AWS, etc.) but keep the layer-and-purpose structure. The No LAC principle is stack-agnostic; only the implementation details change.
