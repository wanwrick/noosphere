# Extending the Template

> Common extensions and where they belong. Keep the contract authoritative; add code in the few places where custom logic is allowed.

## Adding a new ingestion strategy

If your source needs a strategy beyond `snapshot` / `incremental` / `cdc`:

1. Add a class in `src/shared/ingestion_strategies.py`:

   ```python
   class StreamingFromKafkaStrategy:
       name = "streaming-kafka"
       def read(self, spark, contract, source_path):
           ...
   ```

2. Register it in `_REGISTRY`.
3. Update `data-contract.schema.json` to allow the new value in `bronze.ingestion_strategy`.
4. Add a fixture under `tests/fixtures/` exercising the new value.
5. Update `docs/how-the-contract-flows.md`.

## Adding a new quality-violation mode

The current modes are `fail` · `drop` · `drop_to_quarantine` · `warn`. To add (e.g.) `route_to_dlq`:

1. Add to `_VALID_VIOLATIONS` in `src/contract/quality_check.py`.
2. Update `to_dlt_decorator_name()` to map it.
3. Update the JSON Schema's `quality_expectations[].on_violation` enum.
4. Document the semantics in this file.

## Adding a new column classification

Default tiers: `public` · `internal` · `confidential` · `restricted`. To add a new tier (e.g., `regulatory-archived`):

1. Update the `classification` enum in `data-contract.schema.json` (both `metadata.classification` and `schema.columns[].classification`).
2. Update the grant logic in `src/shared/unity_catalog_helpers.py:emit_grant_statements()`.
3. Add a corresponding compliance rule in the parent repo's `compliance-checker` skill.

## Custom Gold transformations

This is the *only* place domain-specific logic belongs. In `src/pipelines/gold.py`:

```python
@dlt.table(name=table_name, comment="Gold — cross-source joins.")
def gold_table():
    silver_df = dlt.read(silver_table)
    other_silver_df = dlt.read(other_silver_table)
    return silver_df.join(other_silver_df, "key").withColumn("derived", ...)
```

Per the No LAC principle: Bronze and Silver remain pattern-driven; opinion lives at Gold.

## Custom UC Functions

When `data-contract.yml` declares UC Functions, `unity_catalog_helpers.py` emits CREATE FUNCTION skeletons. Fill in the bodies in a separate file (`src/governance/uc_functions.sql` is a common convention). Deploy via the bundle.

## Per-environment overrides

`databricks.yml` already declares `dev` / `staging` / `prod` targets with per-target variables. Override anything by:

```yaml
targets:
  prod:
    variables:
      catalog: prod
      schedule_cron: "0 0 * * * ?"
      autoscale_max: 16
```

## Multi-source data products

If a single data product ingests from multiple sources:

1. Bronze becomes a Bronze-per-source pattern (`<id>_bronze_source_a`, `<id>_bronze_source_b`).
2. Each source has its own row in `bronze` (extend the schema to a list).
3. Silver still emits one cleaned table per source.
4. Gold is where the cross-source join happens — that's the No LAC stance.

Update the schema to support `bronze: list[BronzeSource]` if you go this route.

## Multi-region deployment

Add region-specific targets to `databricks.yml`:

```yaml
targets:
  prod-eu:
    workspace:
      host: ${DATABRICKS_HOST_PROD_EU}
    variables:
      catalog: prod_eu
  prod-na:
    workspace:
      host: ${DATABRICKS_HOST_PROD_NA}
    variables:
      catalog: prod_na
```

The contract stays single; the bundle deploys per region.

## Anti-patterns to avoid

- **Pushing custom code into Silver.** Don't. Silver is pattern-only by design.
- **Skipping the contract for "small" products.** A product without a contract is a product without an audit story.
- **Hand-editing the AI Consumption Contract markdown.** It is regenerated from the YAML; edits are lost on next regeneration.
- **Bypassing `validate_bundle.sh`.** The 6 checks exist because each one represents a class of production incident.
