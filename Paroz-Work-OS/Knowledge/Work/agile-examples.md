# Agile Ticket Examples - DataWizards Approved

> Real examples from DataWizards sprint sessions showing correct ticket format. Use as gold standard when generating output.

These are real examples from DataWizards sprint sessions, showing correct ticket format.
Use these as the gold standard when generating output.

---

## Example 1 - Flat Independent Task (most common)

This is what Paroz asked for after Claude initially over-engineered an Equifax pipeline ticket.

```markdown
### 🔌 **Equifax Pipeline - Silver Layer Integration (CRSA)**

**Context:**
Shreya Shukla's CRSA team needs a Silver layer pipeline that combines Equifax credit data
from CTC and QuestBank into a unified view for credit risk modelling. This is an
OCDC-related pipeline - not a treasury pipeline.

**Work to be done:**
- Ingest Equifax file from SFTP/GCS landing zone into Bronze using existing file ingestion pattern
- Apply 5 DLT baseline quality expectations (not-null keys, unique key, valid date range, record count vs. trailer, schema conformance)
- Join CTC historical Equifax data with QuestBank Equifax data in Silver layer
- Route failed records to quarantine using `force_batch_sync` pattern (consult Yelena / Gabriel for pattern reference)
- Unit tests with >80% coverage for join logic and quality gate routing

**Acceptance Criteria:**
1. Silver table accessible at `silver_uat.questbank_lms.equifax_credit_combined`
2. CTC + QuestBank records correctly merged with no duplication
3. All 5 DLT quality expectations applied; quarantine routing confirmed functional
4. Shreya Shukla validates output matches expected credit risk model input format
5. Unit tests passing with >80% coverage

**Assigned To:** Ljupco Grmaskoski (reviewer), Gabriel Cortes (builder)
**Priority:** High
**Estimated Effort:** 3 days
**Dependencies:** Airflow DAG and secrets management (Ljupco owns live process); Shreya Shukla to confirm field list
```

---

## Example 2 - Spike Ticket (no subtasks)

From the Salesforce UAT quality investigation session.

```markdown
### 🔍 **Salesforce UAT Data Quality - Client & Loan Objects - Spike**

**Context:**
QuestBank delineation testing is blocked by data quality issues in Salesforce UAT.
Client__c and Loan__c have GUID mismatches and missing mandatory fields that prevent
test runs from completing. This spike identifies root causes for fix tickets next sprint.

**Investigation Scope:**
- Client__c: Map which client records have missing `External_Client_Id__c`; determine
  if source is LMS or Enablement; check if issue is in Bronze ingestion or Silver transform
- Loan__c: Identify GUID mismatches between Salesforce `Loan_Id__c` and LMS `arrangement_id`;
  trace back through Silver to Bronze to source Pub/Sub topic
- For each issue, classify as BLOCKING (prevents test run) vs NON-BLOCKING (data quality only)
- Reference SF mapping doc for valid picklist values: [Google Sheets link from Federico]
- Check `silver_uat.questbank_lms` and `silver_uat.questbank_sf` for data evidence

**Expected Output:**
- Written findings per object with root cause + recommended fix approach
- Issue priority list: BLOCKING items at top
- Fix tickets drafted and ready for next sprint estimation

**Time Box:** 2 days
**Assigned To:** Ljupco Grmaskoski
**Priority:** High
**Dependencies:** UAT environment access, Salesforce mapping Google Sheet, Federico Pegazzano
  available for Broker_Condition__c context
```

---

## Example 3 - Story + Tasks (pipeline implementation)

From the Finance Platinum layer migration work.

```markdown
## 🏗️ **ECBBAL Balance Refresh - Silver to Finance Platinum Migration**

**As a** Data Engineer
**I want to** migrate the ECBBAL stored procedure logic from SQL Server to Databricks
**So that** the Finance team has a reliable, automated balance refresh on the Databricks platform
and all downstream Finance reports consume from the authoritative Platinum layer

### 📊 **Data Flow:**
**Source:** `Silver.QuestBank_Temenos_LMS.AA_ARRANGEMENT_ACTIVITY`
**Target:** `platinum_uat.finance.ecbbal_arrangement_balance`
**Transformation:** Balance aggregation with window functions; deduplication; NULL handling
**Frequency:** Daily refresh
**Latency SLA:** < 10 minutes

### 🎯 **Acceptance Criteria:**
1. Balance aggregation logic produces identical results to SQL Server stored procedure
2. Delta table created with correct partitioning and Z-ORDER on arrangement_id
3. Incremental refresh handles late-arriving data correctly
4. Unit tests written with >80% coverage for aggregation logic
5. Performance meets SLA (< 10 minutes for daily refresh)
6. Clement Kwong validates output against legacy system
7. Documentation complete with data lineage notes

### ⚙️ **Tasks:**

---

### 🔍 **Analyze SQL Server Stored Procedure Logic**

**Input:**
- `Finance_ECBBAL_SP_v.2.0.sql` source file
- Current SQL Server execution plan and performance metrics
- Business requirements from Finance team

**Outcome:**
- Documented logic breakdown with Databricks translation notes
- Identified SQL Server-specific syntax requiring conversion (CROSS APPLY, PIVOT, temp tables)
- List of dependent Silver tables and their Unity Catalog equivalents

**Notes:**
- Key patterns to translate: CROSS APPLY → LATERAL VIEW, ISNULL → COALESCE,
  GETDATE() → CURRENT_DATE(), sds.* → Silver.QuestBank_Temenos_LMS.*
- Document MERGE vs INSERT/UPDATE patterns
- Flag any business rules embedded in SQL that are not obvious

**Assigned To:** Mariano Barrionuevo
**Priority:** High
**Estimated Effort:** 2 days
**Dependencies:** None - this is the critical path blocker for all other tasks

---

### 🛠️ **Implement Aggregation Logic in PySpark/Spark SQL**

**Input:**
- Analysis document from previous task
- Silver layer table: `silver_uat.questbank_temenos.AA_ARRANGEMENT_ACTIVITY`
- Target schema definition

**Outcome:**
- PySpark notebook/module with balance aggregation logic
- Unit tests with >80% coverage using chispa + pytest
- Test scenarios:
  - Happy path: valid arrangements with positive balance
  - Empty input: zero arrangements - returns empty DataFrame
  - NULL balances: COALESCE handling preserves rows
  - Duplicate arrangements: dedup logic removes extras
  - Late-arriving records: incremental logic handles correctly
- Performance benchmark results

**Notes:**
- Replace CROSS APPLY with explode() or LATERAL VIEW
- Use window functions for running balance calculation
- Test with sample data from UAT environment
- Mock Silver tables for unit tests using pytest fixtures - do NOT connect to live UAT
- Edge cases: NULL arrangement_id (should fail), negative balance (should be valid)

**Assigned To:** Mariano Barrionuevo + Gabriel Cortes
**Priority:** High
**Estimated Effort:** 3 days
**Dependencies:** Analysis task complete

---

### ✅ **Validate Against Legacy and Document**

**Input:**
- Completed aggregation logic from previous task
- Access to legacy SQL Server output for same period

**Outcome:**
- Row-count and checksum reconciliation report vs SQL Server output
- Any discrepancies documented with root cause
- Technical runbook in Notion with: how to re-run, how to troubleshoot, table lineage
- Sign-off from Clement Kwong

**Notes:**
- Validate on at least 30 days of historical data
- Checksum comparison: sum of balances by product type is a useful quick check
- Flag any known differences between legacy and new (e.g., intentional business rule changes)

**Assigned To:** Mariano Barrionuevo
**Priority:** High
**Estimated Effort:** 2 days
**Dependencies:** Implementation task complete; Clement Kwong availability for validation

---
```

---

## Example 4 - Maintenance Story with Multiple Tasks

One acceptable exception to lean-first: grouping related maintenance items in one sprint view.

```markdown
## ⚙️ **LMS Silver Pipeline - Hardening & Reliability Sprint**

**As a** Data Engineer
**I want to** harden the LMS Silver layer pipelines against common failure modes
**So that** the team spends less time firefighting and can focus on new feature delivery

### 🎯 **Acceptance Criteria:**
1. All 7 LMS Pub/Sub topics confirmed receiving and processing correctly
2. Dead-letter queue routing configured for malformed messages
3. Pipeline alerts firing in Datadog for record count drops > 20%
4. Retry logic handles transient GCP Pub/Sub failures without manual intervention
5. Unit tests updated to cover new error handling paths

### ⚙️ **Tasks:**

---

### 🚨 **Add Dead-Letter Queue Routing for Malformed LMS Messages**

**Input:**
- Current LMS Bronze DLT pipeline code in GitLab
- List of Pub/Sub topics: [topic list]
- `expect_or_drop` quarantine pattern from Gabriel Goulart / Yelena Hakhumyan

**Outcome:**
- Dead-letter routing configured for all 7 LMS Pub/Sub topics
- Malformed messages land in quarantine table, not silently dropped
- Unit tests with >80% coverage for routing logic
- Test scenarios: valid message, malformed JSON, missing required field, oversized payload

**Notes:**
- Use `force_batch_sync` API pattern from Work Stream D - consult Gabriel/Yelena
- Quarantine table: `silver_uat.questbank_lms.quarantine_lms_ingest`
- Test edge cases: NULL message body, duplicate message_id

**Assigned To:** Ljupco Grmaskoski
**Priority:** High
**Estimated Effort:** 2 days
**Dependencies:** Access to all 7 LMS Pub/Sub topic configs

---

### 📊 **Configure Datadog Alerts for LMS Record Count Monitoring**

**Input:**
- Existing Datadog integration (DataOps owns setup)
- LMS table baseline record counts from profiling
- Alert threshold guidance: >20% drop triggers alert

**Outcome:**
- Datadog monitors created for each LMS Silver table
- Alert fires to DataWizards Google Chat channel on threshold breach
- Runbook linked in Datadog alert description

**Notes:**
- Work with Francisco Diez (DataOps) for Datadog access and monitor creation
- Use daily record count as baseline metric, not real-time
- Include day-of-week seasonality - weekend counts are lower; don't false-alert

**Assigned To:** Gabriel Cortes
**Priority:** Medium
**Estimated Effort:** 1 day
**Dependencies:** Francisco Diez (DataOps) must grant Datadog monitor creation access

---
```

---

## Example 5 - Cross-Platform Message (Google Chat)

When Paroz needs a clean Google Chat message (no markdown table, no headers that break).

```
@DataWizards - Sprint update 🧙

Two big changes to know about for this sprint:

**Regulatory extracts take priority.** Capacity has been reallocated. CMHC, DUCA, Investor Reporting, and RESL are the primary deliverables. Pipeline hardening is parked until next sprint.

Ownership this sprint:
• @Artur - Temenos Silver pipelines + BigQuery Iceberg unblock (pending OAuth2 from Francisco)
• @Ljupco - LMS pipeline hardening + Equifax pipeline review
• @Gabriel - LMS DLT quarantine pattern + CMHC data validation
• @Hayk - LOS/Enablement pipeline packaging
• @Federico - LOS code reviews + DUCA extract support
• @Mariano - Enablement + Alterna reporting
• @Yelena - LOS DLT pipelines + naming standards

Let me know in standup if anything is blocked. 🙏
```
