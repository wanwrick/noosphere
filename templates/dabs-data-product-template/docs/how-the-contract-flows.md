# How the Contract Flows

> One picture. From `data-contract.yml` to deployed pipeline + AI Consumption Contract.

```
                         data-contract.yml
                                |
                +---------------+---------------+
                |               |               |
                v               v               v
         +----------+    +----------+    +-------------+
         | metadata |    |  schema  |    | ai_consump  |
         +----------+    +----------+    +-------------+
              |                |                 |
              |                |                 |
              v                v                 v
   resources/permissions.yml   resources/schema.yml + UC tags        Platinum scoped views
   (UC ABAC grants from        (column tags + masking from           + UC Functions registered
    metadata.classification)    schema.columns[].pii)                  from ai_consumption.*)
              |                |                 |
              v                v                 v
        +-----------+   +-----------+    +------------------+
        | Bronze    |   | Silver    |    | Platinum         |
        +-----------+   +-----------+    +------------------+
              ^                |                 ^
              |                |                 |
              | bronze.        | quality_        | scripts/generate_ai_contract.py
              | ingestion_     | expectations[]  | -> docs/ai-consumption-contract.md
              | strategy       | -> DLT          |
              | (snapshot/     | @expect_or_*    |
              |  incremental/  |
              |  cdc)          |
```

## Where each contract field lands

| Contract field | Where it shows up |
|---|---|
| `metadata.id` | Table-name prefix in every Medallion layer (e.g., `<id>_bronze`) |
| `metadata.owner_team` | UC tags · alert recipients · grant principals |
| `metadata.classification` | UC schema-level grants in `resources/permissions.yml` |
| `metadata.version.current` | Tagged in deployment + tracked in evolution.md downstream |
| `grain.description` | UC table comment + AI Consumption Contract doc |
| `bronze.source_type` | Drives Spark format (json/jdbc/kafka/...) |
| `bronze.ingestion_strategy` | Dispatches to `src/shared/ingestion_strategies.py` |
| `bronze.incremental_column` | Watermark column for incremental strategy |
| `bronze.schema_evolution` | Auto Loader `schemaEvolutionMode` |
| `schema.columns[]` | Bronze explicit schema DDL + UC column tags + masking |
| `schema.columns[].pii` | UC tag `pii=true|false` |
| `schema.columns[].masking_function` | UC `ALTER COLUMN ... SET MASK` |
| `freshness.sla_minutes` | Silver freshness expectation + alert threshold |
| `quality_expectations[]` | DLT decorators in `src/pipelines/silver.py` |
| `completeness.*` | Silver post-load assertions + monitoring |
| `ai_consumption.scoped_views[]` | Platinum DLT views in `src/pipelines/platinum.py` |
| `ai_consumption.uc_functions[]` | UC Functions registered (placeholder bodies) |
| `ai_consumption.*` | AI Consumption Contract markdown via `scripts/generate_ai_contract.py` |
| `consumed_by.*` | Documentation only — surfaces in AI Consumption Contract |
| `slis.*` | Monitoring + alerting thresholds |

## Dependency order at deploy time

1. UC schema exists (per `resources/schema.yml`).
2. UC permissions applied (per `resources/permissions.yml`).
3. DLT pipeline defined (per `resources/pipeline.yml`).
4. Pipeline runs: Bronze → Silver → Gold → Platinum.
5. Post-pipeline: UC tags + masking applied via `src/shared/unity_catalog_helpers.py`.
6. Post-pipeline: AI Consumption Contract regenerated.

## Why this design holds up under change

- **Contract is source of truth.** Every implementation file is a function of the contract; rebuilding from scratch is a `bundle deploy`.
- **No hidden state.** Schemas, expectations, masking functions all derive from the contract YAML.
- **No leaky abstractions.** Custom code is allowed only at Gold; everywhere else the patterns are reusable.
- **Forks inherit.** A new data product is a new `data-contract.yml` and a copy of the bundle scaffold; no per-product Python.
