# Databricks Data Engineering Quick Reference

## Medallion Architecture

| Layer | Purpose | Pattern | Ownership |
|-------|---------|---------|-----------|
| **Bronze** | Raw ingestion | Append-only, source-aligned | Platform |
| **Silver** | Cleansed, typed | Incremental, domain-aligned | Domain |
| **Gold** | Business KPIs | Star schema | Enterprise |
| **Platinum** | BI semantic | 1:1 Power BI mapping | Functional |

## Three Pillars of Access Control

```
WHO (Entra ID Groups) + WHAT (Roles) + ASSIGNMENT (Grants) = ACCESS
```

## Key Commands

### Data Ingestion
```sql
-- Auto Loader (Streaming)
CREATE STREAMING LIVE TABLE bronze_table AS
SELECT * FROM cloud_files("path", "json");

-- COPY INTO (Batch)
COPY INTO bronze_table FROM 's3://bucket/'
FILEFORMAT = PARQUET;
```

### Delta Lake Operations
```sql
OPTIMIZE table_name;                    -- Compact files
VACUUM table_name RETAIN 168 HOURS;     -- Remove old files
ANALYZE TABLE table_name COMPUTE STATS; -- Update statistics
RESTORE TABLE t TO VERSION AS OF 5;     -- Time travel
```

### DLT Data Quality
```python
@dlt.expect("valid", "col > 0")         # Log violations
@dlt.expect_or_drop("valid", "col > 0") # Drop invalid
@dlt.expect_or_fail("pk", "id NOT NULL") # Fail pipeline
```

### Unity Catalog ABAC
```sql
-- Column masking
CREATE FUNCTION mask_ssn(ssn STRING)
RETURN CASE WHEN is_account_group_member('Compliance') 
            THEN ssn ELSE '***-**-' || RIGHT(ssn,4) END;

ALTER TABLE t ALTER COLUMN ssn SET MASK mask_ssn;

-- Row filtering
CREATE FUNCTION filter_region(region STRING)
RETURN is_account_group_member(CONCAT('region-', region));
```

## Performance Optimization Checklist

- [ ] Enable Photon for SQL workloads
- [ ] Use Liquid Clustering (replaces Z-ORDER)
- [ ] Enable Predictive Optimizations
- [ ] Size clusters appropriately (don't assume bigger = more expensive)
- [ ] Remove legacy Spark configurations
- [ ] Use Delta caching: `spark.databricks.io.cache.enabled = true`

## Power BI Integration

| Pattern | Best For | Governance |
|---------|----------|------------|
| **DirectQuery** (Recommended) | Live data, governed | AAD passthrough |
| Import | Small, static data | Snapshot only |
| Delta Sharing | External sharing | Materialized aggregates |

## QuestBank Reference Numbers

- **137 users** | 110 Data Lake | 134 Power BI | 24 PBI-only
- **13 Entra ID groups** → 7 Platinum schemas
- **85% PII** in data estate requiring masking
- **2-4 days** access request target (from 2-4 weeks)

## Data Classification (CDMC)

| Level | Access Controls |
|-------|-----------------|
| Public | Standard RBAC |
| Internal | RBAC + Audit |
| Confidential | RBAC + Masking + Audit |
| Restricted | RBAC + Masking + Approval + Enhanced Audit |

## Governance Flow

```
Collibra (Source of Truth) → API/Edge → Unity Catalog (Enforcement)
                                ↓
                        system.access (Audit)
```

## Common Spark Configurations

| Setting | Value | Purpose |
|---------|-------|---------|
| `spark.databricks.delta.optimizeWrite.enabled` | `true` | Optimize writes |
| `spark.databricks.delta.autoCompact.enabled` | `true` | Auto-compact |
| `spark.sql.shuffle.partitions` | `auto` | Let Databricks optimize |

## Glossary

| Term | Meaning |
|------|---------|
| ABAC | Attribute-Based Access Control |
| DLT | Delta Live Tables |
| UC | Unity Catalog |
| CDC | Change Data Capture |
| DBU | Databricks Unit (billing) |
| SCIM | System for Cross-domain Identity Management |

---
*Reference: Databricks Data Engineering Skill v1.0*
