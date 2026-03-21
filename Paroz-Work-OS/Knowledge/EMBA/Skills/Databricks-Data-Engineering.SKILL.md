---
name: databricks-data-engineering-reference
description: "Comprehensive Databricks data engineering reference guide for lakehouse architecture, Unity Catalog governance, Delta Live Tables, medallion architecture (Bronze/Silver/Gold/Platinum), ABAC/RBAC access control, Power BI integration, and performance optimization. Use this skill when asked about: Databricks best practices, Delta Lake optimization, Unity Catalog setup, data pipeline design, CDC patterns, streaming architectures, data governance frameworks, TCO comparisons with BigQuery/GCP, migration planning, medallion architecture design, Power BI DirectQuery integration, ABAC column masking, row-level security, Data Mesh principles, data product management, QuestBank implementation patterns, regulatory compliance (OFSI/PIPEDA), or any Databricks certification preparation."
---

# Databricks Data Engineering Reference Guide

## 1. Overview

### 1.1 Project Context
This skill provides comprehensive guidance for Databricks implementations, with a focus on enterprise-grade data platforms in regulated financial services environments. The reference implementation (QuestBank) demonstrates patterns for:
- 137 users across 32 departments and 6 legal entities
- Hybrid BigQuery/Databricks architecture
- Unity Catalog centralized governance
- Power BI integration with DirectQuery

### 1.2 When to Use This Skill
**Trigger phrases and use cases:**
- "How do I implement medallion architecture?"
- "What's the best practice for Unity Catalog setup?"
- "How do I optimize Delta Lake tables?"
- "Compare Databricks vs BigQuery for [use case]"
- "How do I set up ABAC column masking?"
- "Design a CDC pipeline with DLT"
- "Power BI integration with Databricks"
- "Data governance for regulated industries"
- "Migration from on-premise to Databricks"
- "Databricks certification preparation"

### 1.3 Core Principles
1. **Simplicity First**: Prefer out-of-box Databricks features over custom solutions
2. **Consumer-Centric Bias**: Design trade-offs benefit data consumers over producers
3. **Read-Left / Write-Right**: Data flows one direction through medallion layers
4. **Centralized Governance**: Unity Catalog as single source of truth
5. **Data Products as Units**: Access control at data product level, not raw tables

---

## 2. Architecture Patterns

### 2.1 Medallion Architecture (Extended)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    MEDALLION ARCHITECTURE LAYERS                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   BRONZE          SILVER           GOLD           PLATINUM              │
│   (Landing)       (Cleansed)       (Business)     (BI Consumption)      │
│                                                                         │
│   ┌─────────┐    ┌─────────┐      ┌─────────┐    ┌─────────┐           │
│   │ Raw     │    │ Cleaned │      │ Business│    │ 1:1 BI  │           │
│   │ Ingested│ ─> │ Typed   │ ─>   │ Logic   │ ─> │ Semantic│           │
│   │ Data    │    │ Dedupe  │      │ Aggreg  │    │ Models  │           │
│   └─────────┘    └─────────┘      └─────────┘    └─────────┘           │
│                                                                         │
│   Source-aligned  Domain-aligned   Star Schema    Dept Datamarts        │
│   Append-only     SCD handling     Enterprise     Power BI ready        │
│                                    KPIs                                 │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Layer Definitions:**

| Layer | Purpose | Data Model | Refresh Pattern | Ownership |
|-------|---------|------------|-----------------|-----------|
| **Bronze** | Raw ingestion, audit trail | Source-aligned | Append-only | Platform team |
| **Silver** | Cleansed, typed, deduplicated | Domain-aligned | Incremental | Domain teams |
| **Gold** | Business aggregates, KPIs | Star schema | Full/Incremental | Enterprise |
| **Platinum** | BI semantic layer | Department datamarts | Incremental | Functional teams |

### 2.2 Platinum Layer Details

The Platinum layer is a community-proposed extension optimized for BI consumption:

**When to use Platinum:**
- Departmental datamarts need clear ownership boundaries
- 1:1 mapping to Power BI semantic models simplifies governance
- Cross-domain data access required without compromising security
- AI/ML-ready feature stores beyond standard reporting
- Regulatory compliance requires isolated consumption layers

**When to avoid Platinum:**
- Current Gold layer meets business needs
- Straightforward reporting without cross-domain complexity
- Early in data maturity journey
- Cost optimization is the priority

**Schema Structure Example:**
```sql
-- Production catalog with departmental Platinum schemas
prod_analytics.platinum_finance.revenue_monthly
prod_analytics.platinum_finance.customer_lifetime_value
prod_analytics.platinum_marketing.campaign_performance
prod_analytics.platinum_risk.regulatory_capital_reports
prod_analytics.platinum_operations.supply_chain_metrics
```

### 2.3 Unity Catalog Hierarchy

```sql
-- Recommended structure
CREATE CATALOG dev_lakehouse;
CREATE CATALOG prod_lakehouse;

-- Bronze/Silver: Source system-aligned
CREATE SCHEMA prod_lakehouse.bronze_salesforce;
CREATE SCHEMA prod_lakehouse.silver_customer;

-- Platinum: Department-aligned for BI consumption
CREATE SCHEMA prod_lakehouse.platinum_finance;
CREATE SCHEMA prod_lakehouse.platinum_marketing;
CREATE SCHEMA prod_lakehouse.platinum_risk;

-- Gold: Minimal enterprise KPIs only
CREATE SCHEMA prod_lakehouse.gold_enterprise;

-- Compliance-sensitive data in isolated catalogs
CREATE CATALOG hr_prod MANAGED LOCATION 's3://company-hr-prod/';
CREATE SCHEMA hr_prod.platinum_workforce;
```

---

## 3. Data Ingestion Patterns

### 3.1 COPY INTO (Batch)

Best for: One-time or scheduled batch loads from cloud storage

```sql
COPY INTO bronze_schema.orders
FROM 's3://bucket/orders/'
FILEFORMAT = PARQUET
COPY_OPTIONS ('mergeSchema' = 'true')
```

**Key options:**
- `mergeSchema`: Auto-evolve schema
- `force`: Reload previously loaded files
- `format_options`: Specify parsing details

### 3.2 Auto Loader (Continuous)

Best for: Incremental file ingestion with exactly-once guarantees

```python
# Python with DLT
@dlt.table(name="customer_bronze",
           comment="Customer data from cloud storage")
def customer_bronze():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("cloudFiles.inferColumnTypes", "true")
        .load(f"{source}/customers")
    )
```

```sql
-- SQL with DLT
CREATE STREAMING LIVE TABLE customer_bronze
COMMENT "Customer data incrementally ingested"
AS SELECT *
FROM cloud_files("${source}/customers", "json", 
                 map("cloudFiles.inferColumnTypes", "true"));
```

**Auto Loader vs COPY INTO:**

| Feature | Auto Loader | COPY INTO |
|---------|------------|-----------|
| Incremental | Yes (automatic) | Manual tracking |
| Streaming | Yes | No |
| Checkpointing | Automatic | N/A |
| Scalability | Millions of files | Thousands of files |
| Schema evolution | Automatic | Manual |

### 3.3 Streaming from Kafka

```python
# Direct ingestion to Bronze
@dlt.table
def bronze_events():
    return (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", kafka_bootstrap)
        .option("subscribe", "events_topic")
        .option("startingOffsets", "earliest")
        .load()
        .select(
            from_protobuf("value", 
                         options={"schema.registry.subject": "events-value"})
            .alias("event")
        )
        .select("event.*")
    )
```

---

## 4. Delta Live Tables (DLT)

### 4.1 Core Concepts

**DLT is a declarative ETL framework that:**
- Automatically manages dependencies between tables
- Handles checkpoint management for streaming
- Provides built-in data quality controls (Expectations)
- Supports both batch and streaming workloads

### 4.2 Table Types

| Type | Definition | Behavior |
|------|------------|----------|
| **Live Table** | `dlt.table` with `dlt.read()` | Fully recomputed each run |
| **Streaming Live Table** | `dlt.table` with `dlt.read_stream()` | Incremental, stateful |
| **Materialized View** | Uses `dlt.read()` | Recomputed periodically |

### 4.3 DLT Pipeline Example

```python
import dlt
from pyspark.sql.functions import *

# Bronze: Raw ingestion
@dlt.table(
    name="bronze_orders",
    comment="Raw orders from source",
    table_properties={"quality": "bronze"}
)
def bronze_orders():
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("/mnt/data/orders/")
    )

# Silver: Cleaned and typed
@dlt.table(
    name="silver_orders",
    comment="Cleansed orders with type validation"
)
@dlt.expect_or_drop("valid_amount", "amount > 0")
@dlt.expect("valid_customer", "customer_id IS NOT NULL")
def silver_orders():
    return (
        dlt.read_stream("bronze_orders")
        .select(
            col("order_id").cast("string"),
            col("customer_id").cast("string"),
            col("amount").cast("decimal(10,2)"),
            to_timestamp("order_date").alias("order_date")
        )
    )

# Gold: Business aggregates
@dlt.table(name="gold_daily_revenue")
def gold_daily_revenue():
    return (
        dlt.read("silver_orders")
        .groupBy(date_trunc("day", "order_date").alias("date"))
        .agg(
            sum("amount").alias("total_revenue"),
            count("*").alias("order_count")
        )
    )
```

### 4.4 Data Quality Expectations

```python
# Drop invalid records
@dlt.expect_or_drop("valid_ssn", "LENGTH(ssn) = 11")

# Fail pipeline on violations
@dlt.expect_or_fail("critical_field", "id IS NOT NULL")

# Log but keep records (default)
@dlt.expect("soft_validation", "email LIKE '%@%'")

# Multiple expectations
@dlt.expect_all({
    "valid_date": "order_date <= current_date()",
    "positive_amount": "amount > 0",
    "known_customer": "customer_id IS NOT NULL"
})
```

### 4.5 CDC with APPLY CHANGES INTO

```sql
-- Create target table for CDC
CREATE OR REFRESH STREAMING LIVE TABLE customers;

-- Apply CDC changes
APPLY CHANGES INTO LIVE.customers
FROM STREAM(LIVE.customers_cdc)
KEYS (customer_id)
APPLY AS DELETE WHEN operation = 'DELETE'
SEQUENCE BY timestamp
COLUMNS * EXCEPT (operation, timestamp);
```

**Python equivalent:**
```python
dlt.create_streaming_table("customers")

dlt.apply_changes(
    target="customers",
    source="customers_cdc",
    keys=["customer_id"],
    sequence_by="timestamp",
    apply_as_deletes=expr("operation = 'DELETE'"),
    except_column_list=["operation", "timestamp"]
)
```

---

## 5. Unity Catalog Governance

### 5.1 Access Control Model

**The Three Pillars of Access Control:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                     ACCESS CONTROL MODEL                            │
├─────────────────┬─────────────────────┬─────────────────────────────┤
│   1. WHO        │   2. WHAT           │   3. ASSIGNMENT             │
│   User/Group    │   Asset-specific    │   Role → User               │
│                 │   Role              │                             │
├─────────────────┼─────────────────────┼─────────────────────────────┤
│ EntraID groups  │ IAM/Databricks      │ Grants actual access        │
│ mapped to org   │ roles defining      │ to specific Data Products   │
│ chart and real  │ capabilities for    │ by linking WHO to WHAT      │
│ users           │ job functions       │                             │
└─────────────────┴─────────────────────┴─────────────────────────────┘
```

### 5.2 RBAC Implementation

```sql
-- Schema-level access grant
GRANT USAGE ON SCHEMA questbank_prod.platinum_finance 
TO `Lakehouse_Finance`;

GRANT SELECT ON SCHEMA questbank_prod.platinum_finance 
TO `Lakehouse_Finance`;

-- Verify grants
SHOW GRANTS ON SCHEMA questbank_prod.platinum_finance;

-- Group-based ownership (mandatory for production)
ALTER TABLE platinum_finance.revenue_summary 
OWNER TO `finance-data-team`;
```

### 5.3 ABAC: Column Masking

```sql
-- Create masking function
CREATE FUNCTION questbank_prod.platinum.mask_ssn(ssn STRING)
RETURN CASE
  WHEN is_account_group_member('Lakehouse_Compliance') 
    OR is_account_group_member('Lakehouse_Fraud')
    OR is_account_group_member('Lakehouse_InternalAudit')
  THEN ssn
  ELSE CONCAT('***-**-', RIGHT(ssn, 4))
END;

-- Apply mask to column
ALTER TABLE platinum_finance.customers
ALTER COLUMN ssn SET MASK questbank_prod.platinum.mask_ssn;
```

### 5.4 ABAC: Row Filtering

```sql
-- Create row filter function
CREATE FUNCTION filter_by_region(region STRING)
RETURNS BOOLEAN
RETURN is_account_group_member(CONCAT('region-', region));

-- Apply row filter
ALTER TABLE prod_lakehouse.platinum_finance.customer_data
SET ROW FILTER filter_by_region ON (region);
```

**Key ABAC constraints:**
- RLS applies first, then column masking
- Each column can have only one mask
- Delta Sharing cannot share tables with masks—use dynamic views instead

### 5.5 Unity Catalog Axioms

1. **Metastore-level privileges**: UC permissions refer to account-level identities
2. **Privilege inheritance**: Inherited downward from catalog → schema → table
3. **Ownership matters**: Only owners or metastore admins can grant privileges
4. **USE for boundaries**: USE CATALOG/SCHEMA required to interact with objects
5. **Simplified derived objects**: View owners need SELECT + USE permissions
6. **No data leakage**: Misconfigured clusters cannot access UC data

---

## 6. Performance Optimization

### 6.1 Top 5 Databricks Performance Tips

1. **Use Appropriately-Sized Clusters**
   - Larger clusters aren't more expensive for the same workload—they complete faster
   - Match cluster size to data volume
   - Use auto-scaling for variable workloads

2. **Enable Photon for SQL Workloads**
   - 2-10x faster for analytical queries
   - Native vectorized engine
   - Automatic for SQL Warehouses

3. **Implement Liquid Clustering** (replaces Z-ORDER)
   ```sql
   ALTER TABLE my_table 
   CLUSTER BY (date_column, id_column);
   ```

4. **Enable Predictive Optimizations**
   - Auto-runs OPTIMIZE, VACUUM, ANALYZE
   - 2.2x query performance boost
   - 50% storage cost savings

5. **Clean Out Legacy Configurations**
   - Remove old Spark configurations
   - Let Databricks defaults apply
   - Use intelligent workload management

### 6.2 Delta Lake Optimization

**OPTIMIZE Command:**
```sql
-- Compact small files
OPTIMIZE delta.`/path/to/table`;

-- With Z-ORDER (pre-Liquid Clustering)
OPTIMIZE delta.`/path/to/table` 
ZORDER BY (date_column, id_column);
```

**VACUUM Command:**
```sql
-- Remove files older than retention period
VACUUM delta.`/path/to/table` RETAIN 168 HOURS;

-- Dry run first
VACUUM delta.`/path/to/table` DRY RUN;
```

**ANALYZE Command:**
```sql
-- Compute table statistics
ANALYZE TABLE my_table COMPUTE STATISTICS;

-- Specific columns
ANALYZE TABLE my_table COMPUTE STATISTICS 
FOR COLUMNS col1, col2;
```

### 6.3 Query Performance Patterns

```sql
-- Leverage partition pruning
SELECT * FROM orders 
WHERE order_date >= '2024-01-01';  -- Assumes partitioned by date

-- Use Delta caching
SET spark.databricks.io.cache.enabled = true;

-- Broadcast small dimension tables
SELECT /*+ BROADCAST(dim_product) */ *
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.id;
```

---

## 7. Power BI Integration

### 7.1 Connection Patterns

| Pattern | Description | Best For |
|---------|-------------|----------|
| **DirectQuery** | Real-time queries to SQL Warehouse | Live data, governance |
| **Import** | Data copied to Power BI | Performance, offline |
| **Publish to Service** | Databricks → Power BI Service | Quick deployment |
| **Power BI Tasks** | Orchestrated refresh | CI/CD integration |

### 7.2 DirectQuery Best Practices

**Recommended Configuration:**
- Enable Serverless SQL Warehouse
- Use Liquid Clustering on common filter columns
- Enable AAD passthrough for identity flow
- Materialize aggregations in Databricks first

```sql
-- Optimize for Power BI queries
CREATE TABLE platinum_finance.monthly_revenue
CLUSTER BY (fiscal_month, region)
AS
SELECT 
    date_trunc('month', order_date) as fiscal_month,
    region,
    SUM(amount) as revenue,
    COUNT(*) as order_count
FROM gold_orders
GROUP BY 1, 2;
```

### 7.3 AAD Passthrough Flow

```
┌──────────────┐    OAuth/SSO     ┌──────────────────────────────────┐
│              │   ─────────────► │                                  │
│  POWER BI    │                  │     DATABRICKS SQL WAREHOUSE     │
│  SERVICE     │  ◄───────────── │     (Serverless)                 │
│              │    Query Results │                                  │
└──────────────┘                  └──────────────┬───────────────────┘
      │                                          │
      │ User Identity                            │ Queries
      │ (AAD Token)                              │
      ▼                                          ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         UNITY CATALOG                               │
│                     ACCESS CONTROL LAYER                            │
│                                                                     │
│  1. RBAC Check: Is user in group? → GRANT/DENY schema access       │
│  2. ABAC Check: What columns can they see? → Apply column masks    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8. TCO & Platform Comparison

### 8.1 Databricks vs BigQuery TCO

**Billing Model Differences:**

| Aspect | BigQuery | Databricks |
|--------|----------|------------|
| Compute | Bytes scanned (on-demand) or Slots | DBU (Databricks Units) |
| Storage | Bundled with BQ / GCS separate | GCS Standard/Nearline |
| Scaling | Auto (slots) or reserved | SQL Serverless auto-scale |
| Optimization | Query optimization | Predictive I/O, Photon |

**Typical TCO Results:**
- 25-50% cost reduction with Databricks (AT&T case study: 300% 5-year ROI)
- 2-10x faster query performance
- 30% data rationalization during migration

### 8.2 Migration Considerations

**Migration Checklist:**
- [ ] Assess current workloads and costs
- [ ] Map capabilities to Databricks features
- [ ] Plan phased migration approach
- [ ] Implement governance early (Unity Catalog)
- [ ] Validate performance improvements
- [ ] Train team on new platform

**AT&T Migration Stats:**
- 1,500 servers migrated
- 50,000+ production CPUs
- 12,500 data sources
- 300 schemas
- 2.5 years total migration
- 15 FTE internal resources

---

## 9. Data Governance Framework

### 9.1 Dual-Layer Governance Model

```
┌═══════════════════════════════════════════════════════════════════════┐
│                         COLLIBRA (Source of Truth)                    │
│                                                                       │
│   BUSINESS GOVERNANCE                                                 │
│   ┌─────────────────────┐  ┌─────────────────────┐  ┌───────────────┐ │
│   │ Business Glossary   │  │ Data Classification │  │ Access        │ │
│   │ "What is Customer?" │  │ "Is this PII?"      │  │ Workflows     │ │
│   └─────────────────────┘  └─────────────────────┘  └───────────────┘ │
│                                                                       │
└═══════════════════════════════════════════════════════════════════════┘
                                   │
                                   │ Collibra Edge / API (Policy Sync)
                                   ▼
┌═══════════════════════════════════════════════════════════════════════┐
│                     UNITY CATALOG (Enforcement Engine)                │
│                                                                       │
│   TECHNICAL GOVERNANCE                                                │
│   ┌─────────────────────┐  ┌─────────────────────┐  ┌───────────────┐ │
│   │ RBAC Grants         │  │ ABAC Column Masks   │  │ Audit Logs    │ │
│   │ GRANT TO group      │  │ mask_ssn()          │  │ system.access │ │
│   └─────────────────────┘  └─────────────────────┘  └───────────────┘ │
│                                                                       │
└═══════════════════════════════════════════════════════════════════════┘
```

### 9.2 Data Classification (CDMC-Aligned)

| Classification | Description | Access Controls |
|----------------|-------------|-----------------|
| **Public** | Non-sensitive business data | Standard RBAC |
| **Internal** | Business-sensitive data | RBAC + Audit logging |
| **Confidential** | PII, financial data | RBAC + Masking + Audit |
| **Restricted** | Regulatory, highly sensitive | RBAC + Masking + Approval + Enhanced audit |

### 9.3 Access Request Workflow

```
┌─────────────┐    ┌───────────────┐    ┌─────────────┐    ┌──────────────┐
│             │    │               │    │             │    │              │
│    User     │    │   Collibra    │    │  Entra ID   │    │ Unity Catalog│
│   Request   │ ─► │   Workflow    │ ─► │   Group     │ ─► │ Access       │
│             │    │   Approval    │    │   Updated   │    │ Granted      │
│             │    │               │    │   (SCIM)    │    │              │
└─────────────┘    └───────────────┘    └─────────────┘    └──────────────┘

Audit Trail:
  - Request ID, Justification .............. Collibra
  - Approver, Approval Date ................ Collibra  
  - Group membership change ................ Entra ID
  - First query after access ............... Unity Catalog
```

---

## 10. Data Mesh Alignment

### 10.1 Decentralized Production, Centralized Governance

| Aspect | Decentralized (Domain Teams) | Centralized (Platform Team) |
|--------|------------------------------|----------------------------|
| Data ingestion | ✓ | |
| Data processing | ✓ | |
| Data Product definition | ✓ | |
| Publishing to Exchange | ✓ | |
| Access approval | ✓ (Data Stewards) | |
| Discovery & Exchange | | ✓ |
| Security controls | | ✓ |
| Tooling & tenants | | ✓ |
| Audit & compliance | | ✓ |

### 10.2 Data Product Definition

A **Data Product** is:
- A governed, discoverable, and consumable dataset
- Published for organizational use
- Owned by a domain team
- The unit of access control

**Data Products are NOT:**
- Raw source tables
- Intermediate processing tables
- Ad-hoc query results

### 10.3 Secure Data Tenant Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SECURE DATA TENANT                                   │
│         (GCP Project or Databricks Workspace)                           │
├─────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐  │
│  │  Data Access    │  │  Processing     │  │  Output                 │  │
│  │  (Read)         │  │  Tools          │  │  (Write)                │  │
│  ├─────────────────┤  ├─────────────────┤  ├─────────────────────────┤  │
│  │ Data Products   │  │ BigQuery/DBX    │  │ BI Workspace            │  │
│  │ via Exchange    │  │ Dataproc/DLT    │  │ ML Models               │  │
│  │                 │  │ Vertex AI/MLFlow│  │ Published Data Products │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────────────┘  │
├─────────────────────────────────────────────────────────────────────────┤
│  SECURITY CONTROLS: VPC-SC │ Audit Logging │ DLP │ IaC Deployment      │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 11. Quick Reference Tables

### 11.1 DLT Decorator Reference

| Decorator | Purpose | Example |
|-----------|---------|---------|
| `@dlt.table` | Define a DLT table | `@dlt.table(name="my_table")` |
| `@dlt.view` | Define a DLT view | `@dlt.view(name="my_view")` |
| `@dlt.expect` | Soft data quality check | `@dlt.expect("valid", "col > 0")` |
| `@dlt.expect_or_drop` | Drop invalid records | `@dlt.expect_or_drop("valid", "col > 0")` |
| `@dlt.expect_or_fail` | Fail pipeline on violations | `@dlt.expect_or_fail("critical", "id IS NOT NULL")` |
| `@dlt.expect_all` | Multiple expectations | `@dlt.expect_all({"e1": "...", "e2": "..."})` |

### 11.2 Unity Catalog Privilege Reference

| Privilege | Applies To | Description |
|-----------|------------|-------------|
| `USE` | Catalog, Schema | Required to interact with objects |
| `SELECT` | Table, View | Read data |
| `MODIFY` | Table | Insert, update, delete |
| `CREATE` | Schema | Create tables/views |
| `USAGE` | Catalog, Schema | Browse metadata |
| `ALL PRIVILEGES` | Any | Full permissions |

### 11.3 Delta Lake Commands

| Command | Purpose | Syntax |
|---------|---------|--------|
| `OPTIMIZE` | Compact files | `OPTIMIZE table_name` |
| `VACUUM` | Remove old files | `VACUUM table_name RETAIN 168 HOURS` |
| `ANALYZE` | Compute statistics | `ANALYZE TABLE table_name COMPUTE STATISTICS` |
| `DESCRIBE HISTORY` | View table history | `DESCRIBE HISTORY table_name` |
| `RESTORE` | Time travel | `RESTORE TABLE table_name TO VERSION AS OF 5` |

### 11.4 Common Spark Configurations

| Configuration | Value | Purpose |
|---------------|-------|---------|
| `spark.databricks.io.cache.enabled` | `true` | Enable Delta caching |
| `spark.sql.shuffle.partitions` | `auto` | Let Databricks optimize |
| `spark.databricks.delta.optimizeWrite.enabled` | `true` | Optimize writes |
| `spark.databricks.delta.autoCompact.enabled` | `true` | Auto-compact files |

---

## 12. Symbols & Abbreviations Glossary

| Term | Definition |
|------|------------|
| **ABAC** | Attribute-Based Access Control; access determined by user/data attributes |
| **ACID** | Atomicity, Consistency, Isolation, Durability; transaction properties |
| **AAD** | Azure Active Directory; Microsoft identity service |
| **CDC** | Change Data Capture; tracking data changes |
| **CDMC** | Cloud Data Management Capabilities; data classification framework |
| **DBU** | Databricks Unit; compute billing unit |
| **DLT** | Delta Live Tables; declarative ETL framework |
| **OFSI** | Office of the Superintendent of Financial Institutions |
| **PIPEDA** | Personal Information Protection and Electronic Documents Act |
| **RBAC** | Role-Based Access Control; access by group membership |
| **RLS** | Row-Level Security; filter rows by policy |
| **SCD** | Slowly Changing Dimension; dimension handling patterns |
| **SCIM** | System for Cross-domain Identity Management |
| **SPA** | Strategic Priority Alignment; quarterly planning |
| **TCO** | Total Cost of Ownership |
| **UC** | Unity Catalog; Databricks governance layer |
| **VPC-SC** | VPC Service Controls; GCP security perimeter |

---

## 13. Implementation Checklists

### 13.1 New Data Product Checklist

- [ ] Define business purpose and consumers
- [ ] Design schema following medallion patterns
- [ ] Implement in Bronze → Silver → Gold/Platinum
- [ ] Add data quality expectations
- [ ] Configure Unity Catalog permissions
- [ ] Document in Collibra
- [ ] Publish to Data Exchange
- [ ] Monitor with system tables

### 13.2 Migration Checklist

- [ ] Inventory current data assets and costs
- [ ] Map to Databricks equivalents
- [ ] Plan phased migration waves
- [ ] Set up Unity Catalog governance
- [ ] Migrate and validate data
- [ ] Test query performance
- [ ] Train users on new platform
- [ ] Decommission legacy systems

### 13.3 Governance Checklist

- [ ] Design Unity Catalog hierarchy
- [ ] Configure SCIM sync from identity provider
- [ ] Implement RBAC at schema level
- [ ] Define masking functions for PII
- [ ] Enable audit logging
- [ ] Configure Collibra integration
- [ ] Document access request process
- [ ] Set up compliance reporting

---

## 14. Common Pitfalls to Avoid

1. **Over-engineering medallion layers**: Not every use case needs Platinum
2. **Individual ownership in production**: Always use group-based ownership
3. **Skipping data classification**: Classification drives security controls
4. **Power BI Import with PII**: Use DirectQuery for governed data
5. **Manual checkpoint management**: Let DLT handle it automatically
6. **Legacy Spark configurations**: Remove old configs, trust defaults
7. **Per-column permissions**: Use ABAC policies instead
8. **Ignoring audit logs**: system.access tables are your compliance trail
9. **Dual governance**: One source of truth (Collibra → Unity Catalog)
10. **Shadow data sharing**: All sharing through governed channels

---

## 15. Success Metrics

### 15.1 Performance Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Query execution time | 2-10x improvement | Benchmark queries |
| Pipeline reliability | >99% success rate | DLT event logs |
| Data freshness | Per SLA | Pipeline latency |
| Cost per query | Decreasing trend | DBU consumption |

### 15.2 Governance Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Time to data access | < 2 days | Workflow tracking |
| Audit coverage | 100% | system.access completeness |
| Self-serve adoption | 50% via Exchange | Workflow analytics |
| Compliance findings | Zero | Regulatory review |

### 15.3 Productivity Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Development time | 50-80% reduction with DLT | Sprint velocity |
| Time to production | 3x faster | Deployment frequency |
| Maintenance overhead | 60% reduction | Support tickets |

---

---

## Build vs. Buy Decision Framework for Data Platforms

### Evaluation Criteria Matrix

Use this weighted scoring matrix to compare building a custom data platform capability versus buying a vendor solution. Adjust weights to reflect your organization's strategic priorities.

| Criterion | Weight | Build | Buy | Score Build | Score Buy |
|-----------|--------|-------|-----|-------------|-----------|
| **Time-to-Value** | 20% | 12-18 months typical; requires hiring, architecture, development, and testing cycles | 3-6 months typical; vendor onboarding, configuration, and integration | | |
| **Customization** | 15% | Full control over architecture, data model, UX, and workflow; can optimize for exact requirements | Limited to vendor configuration options and APIs; customization may require professional services | | |
| **Total Cost (3-year)** | 20% | Dev team salaries + infrastructure + testing + ongoing maintenance + opportunity cost of delayed delivery | License fees + implementation consulting + training + annual maintenance + customization surcharges | | |
| **Vendor Lock-in** | 10% | None — full ownership of code, data formats, and deployment | Medium-High — proprietary formats, migration costs, contract dependencies | | |
| **Maintenance Burden** | 15% | Internal team responsible for upgrades, patches, security, scaling, and on-call | Vendor-managed updates, SLA-backed uptime, security patches included | | |
| **Regulatory Fit** | 10% | Custom compliance controls tailored to specific regulatory requirements (OFSI, PIPEDA, SOC2) | Check vendor certifications; may need additional controls for gaps | | |
| **Integration Complexity** | 10% | Custom APIs and connectors built to exact specifications; full control over data flow | Pre-built connectors for common systems; may lack support for niche or legacy systems | | |

**How to score:** Rate each option 1-5 (1 = poor, 5 = excellent) in the Score columns. Multiply each score by the weight. Sum weighted scores to compare.

### TCO Calculation Template

#### Build TCO (3-Year)

```
Development Costs:
  Dev FTEs (N) × avg salary × months to build     = $_______
  Infrastructure (dev/test/prod environments)       = $_______
  Testing & QA cycles                               = $_______
  Opportunity cost (revenue delayed by build time)  = $_______
                                          Subtotal  = $_______

Ongoing Annual Costs (× 3 years):
  Maintenance FTEs × avg salary                     = $_______
  Infrastructure (compute + storage + networking)    = $_______
  On-call / incident response                       = $_______
  Upgrades and feature enhancements                 = $_______
                                          Subtotal  = $_______

                              TOTAL BUILD TCO (3yr) = $_______
```

#### Buy TCO (3-Year)

```
Implementation Costs:
  License / subscription (initial)                  = $_______
  Implementation consulting                         = $_______
  Training (initial rollout)                        = $_______
  Customization / configuration                     = $_______
                                          Subtotal  = $_______

Ongoing Annual Costs (× 3 years):
  Annual license / subscription                     = $_______
  Annual maintenance and support fees               = $_______
  Ongoing training (new hires, updates)             = $_______
  Internal admin / integration maintenance          = $_______
                                          Subtotal  = $_______

                                TOTAL BUY TCO (3yr) = $_______
```

### Decision Heuristics

| Heuristic | Guidance | Example |
|-----------|----------|---------|
| **Build when core differentiator** | If the capability is a source of competitive advantage, build it to maintain control and uniqueness | Proprietary risk scoring engine, custom trading algorithm, unique data enrichment pipeline |
| **Buy when commodity capability** | If the capability is widely available and not a differentiator, buy to save time and focus resources | Standard ETL tooling, BI dashboards, identity management, log aggregation |
| **Partner when complementary** | If the capability extends your platform but requires specialized expertise you lack, partner with a vendor who integrates into your stack | Cloud-native security monitoring, specialized ML model serving, niche regulatory reporting |

### Decision Flowchart

```
Is this capability a core competitive differentiator?
  │
  ├── YES → Do you have the engineering talent to build and maintain it?
  │           ├── YES → BUILD (invest in proprietary advantage)
  │           └── NO  → PARTNER (find a vendor who integrates into your architecture)
  │
  └── NO  → Does a mature vendor solution exist that meets >80% of requirements?
              ├── YES → BUY (redirect engineering effort to differentiating work)
              └── NO  → BUILD (but plan to replace with vendor solution when market matures)
```

### Databricks-Specific Considerations

When evaluating build vs. buy for data platform components in a Databricks ecosystem:

| Component | Recommendation | Rationale |
|-----------|---------------|-----------|
| **Core data lakehouse** | Buy (Databricks) | Commodity infrastructure; focus engineering on data products |
| **ETL / pipeline orchestration** | Buy (DLT + Workflows) | Out-of-box DLT handles 80%+ of pipeline patterns |
| **Data governance catalog** | Buy (Unity Catalog + Collibra) | Governance tooling is not a differentiator |
| **Custom ML models** | Build | Proprietary models are competitive advantage |
| **BI dashboards** | Buy (Power BI / Databricks SQL) | Standard visualization is commodity |
| **Domain-specific data products** | Build | Business logic and domain expertise are differentiators |
| **Monitoring & alerting** | Partner (Datadog / vendor) | Specialized capability, not core business |
| **Data quality rules** | Build on DLT Expectations | Custom rules on commodity framework |

---

*This skill is based on materials including: Big Book of Data Engineering (2nd & 3rd Ed), Big Book of Data Warehousing and BI, Databricks Certified Data Engineer Associate Study Guide, QuestBank implementation documentation, and enterprise governance frameworks.*
