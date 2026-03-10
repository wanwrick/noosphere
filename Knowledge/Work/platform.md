# Databricks -- Technical Reference

> **Template note:** This is a sample platform reference (Databricks). Replace entirely with your own platform context and technical patterns.

> Comprehensive reference for the [Platform Name] data platform: Medallion Architecture, Unity Catalog, Delta Live Tables, security, Power BI integration, and optimization.

---

## 1. Medallion Architecture (Extended)

### Bronze Layer -- Raw Ingestion
**Purpose:** Land raw data exactly as received. Full fidelity, immutable audit trail.

**Patterns:**
```sql
-- COPY INTO for batch files
COPY INTO bronze.banking.transactions
FROM 's3://raw-data/transactions/'
FILEFORMAT = PARQUET
FORMAT_OPTIONS ('mergeSchema' = 'true')
COPY_OPTIONS ('mergeSchema' = 'true');

-- Auto Loader for streaming files
spark.readStream.format("cloudFiles")
  .option("cloudFiles.format", "json")
  .option("cloudFiles.schemaLocation", checkpoint_path)
  .load(raw_path)
  .writeStream.format("delta")
  .option("checkpointLocation", checkpoint_path)
  .trigger(availableNow=True)
  .toTable("bronze.banking.transactions")
```

**Best Practices:**
- Append-only (never update/delete in bronze)
- Include ingestion metadata: `_ingestion_timestamp`, `_source_file`, `_batch_id`
- Schema evolution enabled (`mergeSchema = true`)
- Partition by ingestion date for efficient pruning

### Silver Layer -- Cleansed & Conformed
**Purpose:** Deduplicated, validated, standardized data with business keys.

**Patterns:**
```sql
-- Delta Live Tables declarative pipeline
CREATE OR REFRESH STREAMING LIVE TABLE silver_transactions
COMMENT "Cleansed transactions with deduplication"
TBLPROPERTIES ("quality" = "silver")
AS SELECT
  transaction_id,
  account_id,
  amount,
  currency,
  transaction_date,
  CASE WHEN amount >= 0 THEN 'credit' ELSE 'debit' END AS transaction_type
FROM STREAM(LIVE.bronze_transactions)
WHERE transaction_id IS NOT NULL;
```

**Quality Rules (DLT Expectations):**
```python
@dlt.expect_or_drop("valid_transaction_id", "transaction_id IS NOT NULL")
@dlt.expect_or_fail("valid_amount", "amount IS NOT NULL AND amount != 0")
@dlt.expect("valid_currency", "currency IN ('CAD', 'USD', 'EUR')")
```

### Gold Layer -- Business-Ready
**Purpose:** Dimensional models, star schemas, KPI calculations. Optimized for analytics.

**Design:**
- Fact tables: measurable events (transactions, trades, logins)
- Dimension tables: descriptive context (customers, accounts, products, dates)
- Pre-calculated aggregations for common queries
- Slowly Changing Dimensions (SCD Type 2 for history)

### Platinum Layer -- Curated & Governed
**Purpose:** Pre-built, certified datasets for specific consumers. Self-serve analytics.

- Certified metrics with documented business definitions
- Pre-joined datasets for Power BI
- ML feature stores
- Governed access via Unity Catalog

---

## 2. Unity Catalog

### Hierarchy
```
Metastore (Organization-level)
  └── Catalog (Environment: prod, dev, staging)
        └── Schema (Domain: banking, trading, customers)
              └── Table / View / Function
```

### Setup Examples
```sql
-- Create catalog
CREATE CATALOG IF NOT EXISTS prod;
USE CATALOG prod;

-- Create schema
CREATE SCHEMA IF NOT EXISTS banking
COMMENT 'Core banking data domain'
MANAGED LOCATION '[your-storage-uri]/banking';

-- Grant access
GRANT USAGE ON CATALOG prod TO `data-engineers`;
GRANT USAGE ON SCHEMA prod.banking TO `data-engineers`;
GRANT SELECT ON SCHEMA prod.banking TO `data-analysts`;
```

### Data Lineage
Unity Catalog automatically tracks:
- Table-to-table lineage (which tables feed which)
- Column-level lineage (which columns derive from which)
- Job-level lineage (which notebooks/pipelines transform data)

---

## 3. Security -- ABAC & RBAC

### ABAC (Attribute-Based Access Control) -- Column Masking
```sql
-- Create masking function
CREATE FUNCTION mask_sin(sin STRING)
RETURNS STRING
RETURN CASE
  WHEN IS_MEMBER('compliance-team') THEN sin
  ELSE CONCAT('***-***-', RIGHT(sin, 3))
END;

-- Apply to column
ALTER TABLE customers
ALTER COLUMN social_insurance_number
SET MASK mask_sin;
```

### RBAC -- Row-Level Security
```sql
-- Create row filter function
CREATE FUNCTION region_filter(region STRING)
RETURNS BOOLEAN
RETURN (
  IS_MEMBER('national-team') OR
  region = CURRENT_USER_ATTRIBUTE('region')
);

-- Apply to table
ALTER TABLE transactions
SET ROW FILTER region_filter ON (region);
```

### Access Control Patterns
| Role | Catalog | Schema | Table | Column |
|------|---------|--------|-------|--------|
| Data Engineer | USAGE | ALL PRIVILEGES | ALL PRIVILEGES | Full access |
| Data Analyst | USAGE | USAGE | SELECT | Masked PII |
| Business User | USAGE | USAGE | SELECT (Gold/Platinum only) | Masked PII |
| Compliance | USAGE | USAGE | SELECT | Full access (unmasked) |

---

## 4. Delta Live Tables (DLT)

### Pipeline Types
- **Batch:** Process all available data, then stop (`triggered`)
- **Streaming:** Continuous processing (`continuous`)
- **Triggered Streaming:** Process available data incrementally (`availableNow=True`)

### Python DLT Example
```python
import dlt

@dlt.table(
    comment="Silver-layer cleansed customer records",
    table_properties={"quality": "silver"}
)
@dlt.expect_or_drop("valid_customer_id", "customer_id IS NOT NULL")
@dlt.expect("valid_email", "email RLIKE '^[^@]+@[^@]+$'")
def silver_customers():
    return (
        dlt.read_stream("bronze_customers")
        .dropDuplicates(["customer_id"])
        .withColumn("load_timestamp", F.current_timestamp())
    )
```

### CDC with APPLY CHANGES INTO
```python
dlt.create_streaming_table("silver_accounts")

dlt.apply_changes(
    target="silver_accounts",
    source="bronze_accounts_cdc",
    keys=["account_id"],
    sequence_by="event_timestamp",
    apply_as_deletes=F.expr("operation = 'DELETE'"),
    except_column_list=["operation", "_rescued_data"]
)
```

---

## 5. Power BI Integration

### DirectQuery Configuration
- Connect Power BI to Databricks SQL Warehouse
- Use AAD passthrough for user-level security
- ABAC column masking applies automatically
- Optimize with Databricks SQL caching and result caching

### Performance Optimization
| Technique | Impact | When to Use |
|-----------|--------|-------------|
| Databricks SQL Warehouse | High | All DirectQuery workloads |
| Result caching | High | Repeated queries |
| Liquid Clustering | Medium | Replace partitioning for flexible access |
| Z-ORDER | Medium | Frequently filtered columns |
| Photon engine | High | CPU-intensive queries |
| Materialized views | High | Complex aggregations |
| Import mode fallback | High | When DirectQuery latency unacceptable |

### Power BI Best Practices for Databricks
- Use Gold/Platinum layer tables (pre-aggregated, star schema)
- Minimize the number of columns pulled into Power BI model
- Use measures over calculated columns
- Set query timeout appropriately
- Implement row-level security via RBAC on Databricks side

---

## 6. Performance & Optimization

### Liquid Clustering (Replaces Partitioning + Z-ORDER)
```sql
CREATE TABLE gold.banking.daily_transactions
CLUSTER BY (transaction_date, account_type);

-- Optimize periodically
OPTIMIZE gold.banking.daily_transactions;
```

**Advantages over partitioning:**
- No need to choose partition columns upfront
- Works with high-cardinality columns
- Incrementally reorganizes data
- Can change clustering keys without rewriting

### Photon Engine
- Vectorized query engine written in C++
- 2-10x faster for analytics queries
- Enabled at cluster/warehouse level
- Best for scan-heavy, aggregation-heavy workloads

### Query Optimization Checklist
1. Use appropriate file statistics (column min/max)
2. Enable Photon for analytical workloads
3. Use Liquid Clustering on frequently queried columns
4. Leverage result caching for repeated queries
5. Right-size SQL Warehouses (auto-scaling)
6. Optimize table layout with OPTIMIZE command
7. Use materialized views for expensive aggregations
8. Monitor query profiles for bottlenecks

---

## 7. Data Mesh Alignment

### Principles Applied to [Platform Name]
1. **Domain Ownership:** Each business domain owns its data (banking, trading, customers)
2. **Data as Product:** Gold/Platinum layers treated as products with SLAs
3. **Self-Serve Infrastructure:** Templated pipelines, automated provisioning
4. **Federated Governance:** Unity Catalog + domain-level stewards + central standards

### Data Product Qualities
- Discoverable (catalog with search and descriptions)
- Addressable (consistent naming conventions)
- Trustworthy (quality scores, freshness SLAs)
- Self-describing (schema documentation, lineage)
- Interoperable (standardized formats, shared dimensions)
- Secure (ABAC/RBAC, audit logging)

---

## 8. Regulatory Compliance

### [Financial Regulator] Requirements
- Accurate financial reporting data
- Audit trail from source to report
- Data lineage and governance documentation
- Timely delivery of regulatory submissions

### [Privacy Regulation] Compliance
- PII identification and classification
- Column masking for sensitive fields (SIN, DOB, address)
- Consent tracking and data retention policies
- Right to access and deletion mechanisms
- Breach notification procedures

### Compliance Architecture
```
Source Data → Bronze (full audit) → Silver (PII tagged) → Gold (masked by default)
                                                              │
                                                              ├── Analysts: Masked PII
                                                              └── Compliance: Full access via ABAC
```

---

## TCO Comparison: Databricks vs. BigQuery

| Dimension | Databricks (Azure) | BigQuery (GCP) |
|-----------|-------------------|----------------|
| Compute Model | Cluster-based, SQL Warehouse | Serverless, slot-based |
| Pricing | DBU-based + cloud infra | On-demand or flat-rate |
| Governance | Unity Catalog (unified) | Data Catalog + IAM |
| ML Integration | MLflow native | Vertex AI integration |
| Streaming | Structured Streaming | Pub/Sub + Dataflow |
| Best For | Complex ETL, ML, multi-cloud | Ad-hoc analytics, simplicity |
| [Company Name] Fit | ✅ Primary platform | Reference only |
