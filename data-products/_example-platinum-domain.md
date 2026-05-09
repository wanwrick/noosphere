# Example — Platinum Domain Data Product

> Generic example data product entry. Forks should replace with their actual data-product registry entries.

## Identity

| Field | Value |
|---|---|
| ID | DP-001 |
| Name | example_platinum_domain |
| Description | Example data product showing the Platinum-tier shape: wide BI-friendly Gold table + question-oriented agent-friendly scoped views + UC Functions for governed business logic. |
| Owner team | producer-platform |
| Steward | data-product-steward-role |
| Classification | internal |
| Version | 1.0.0 |

## Grain

One row per `<entity>` per `<period>`.

## Schema (top of mind)

See the full schema in `templates/dabs-data-product-template/data-contract.yml`. Headline columns:

- `account_id` (STRING, internal) — stable identifier.
- `event_timestamp` (TIMESTAMP, internal) — UTC.
- `account_email` (STRING, confidential, **PII**, masked via `mask_completely`).
- `amount` (DECIMAL, internal) — transaction amount.
- `currency_code` (STRING, public) — ISO-4217.

## Freshness

P95 ingestion-to-availability lag: 90 minutes.

## BI consumption

- DirectQuery from BI tool to `<catalog>.example_platinum_domain.example_data_product_gold`.
- Cleared groups see unmasked PII; default groups see masked.
- Auto-refreshed dashboards on hourly cadence.

## AI consumption

Per the AI Consumption Contract (auto-generated):

- **Answerable questions** — three questions about account activity, currency mix, and per-account totals.
- **Scoped views** — `vw_account_activity_for_agents` (5 columns; PII excluded by construction).
- **UC Functions** — `classify_amount_band` (deterministic mapping).
- **Used by** — agentic-analytics pilot (ARCHETYPE-D).

## Compliance

- Classification: internal (overall) · confidential (PII column).
- DPIA: completed (link in `governance/compliance-register.yaml`).
- Audit logging: wired on Confidential-class column reads.
- Erasure window: per PIPEDA-style → 30 days from request.

## SLIs

| Metric | Target | Last 30 days |
|---|---|---|
| Freshness p95 | ≤ 90 min | 78 min |
| Quality breach count | ≤ 1 | 0 |
| Schema-drift alerts | 0 expected | 0 |

## Cross-references

- `data-products.yaml` row `DP-001`.
- `templates/dabs-data-product-template/data-contract.yml` — the source of truth.
- `templates/dabs-data-product-template/docs/from-contract-to-ai-consumption.md` — how this contract becomes a runtime interface.
- `ip/authored/ai-ready-platinum-layer.md` — the design principle this exemplifies.
