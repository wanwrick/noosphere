# Story Templates Reference - DataWizards

> Quick-copy templates for each ticket type. Always check Section 1 Decision Gate in Knowledge/Work/agile-ticket-system.md first.

Quick-copy templates for each ticket type. Always check Section 1 Decision Gate first.

---

## Template A - Flat Independent Task

```markdown
### [Emoji] **Task Title**

**Context:**
[1–2 sentences: why this task exists, what problem it solves.]

**Work to be done:**
- [Specific action 1]
- [Specific action 2]
- [Specific action 3]
- [If code: Unit tests with >80% coverage for core logic]

**Acceptance Criteria:**
1. [Measurable pass/fail criterion]
2. [Measurable pass/fail criterion]
3. [Unit tests written and passing (for code tasks)]

**Assigned To:** [Name]
**Priority:** High | Medium | Low
**Estimated Effort:** [X days]
**Dependencies:** [None | List blockers]
```

---

## Template B - Spike

```markdown
### 🔍 **[Investigation Topic] - Spike**

**Context:**
[Why we're doing this investigation. What decision or unblock it enables.]

**Investigation Scope:**
- [Specific question or area 1]
- [Specific question or area 2]
- [Specific question or area 3]
- [Data objects, fields, or systems to examine]

**Expected Output:**
- [Documented findings in Notion/Confluence]
- [Specific recommendation or decision ready for next sprint]
- [Any blockers or risks identified]

**Time Box:** [X days]
**Assigned To:** [Name]
**Priority:** High | Medium | Low
**Dependencies:** [None | List]
```

---

## Template C - Story + Tasks (Pipeline Implementation)

```markdown
## [Emoji] **Story Title**

**As a** [specific role]
**I want to** [action/capability]
**So that** [business value]

### 📊 **Data Flow:**
**Source:** `[System].[Schema].[Table]`
**Target:** `[Catalog].[Schema].[Table]`
**Transformation:** [Brief description]
**Frequency:** [Real-time | Daily | Hourly | Monthly]
**Latency SLA:** [< X minutes]

### 🎯 **Acceptance Criteria:**
1. [Core functional requirement - measurable]
2. [Data quality validation with threshold]
3. [Performance SLA]
4. [Unit tests >80% coverage for core logic]
5. [Integration test passes in UAT]
6. [Validation sign-off from domain owner]
7. [Documentation complete]

### ⚙️ **Tasks:**

---

### [Emoji] **Task: Analyze Source Data & Map to Target**

**Input:**
- Source system documentation or sample extract
- Target schema definition
- Business requirements from [domain owner name]

**Outcome:**
- Data profiling report (row counts, null rates, cardinality for key fields)
- Source-to-target mapping document
- Edge case inventory
- Schema DDL for target Delta table

**Notes:**
- Profile at least 7 days of data - identify seasonality
- Flag any data quality issues found during profiling
- Note columns requiring special handling (arrays, nested structs, NULLable keys)

**Assigned To:** [Name]
**Priority:** High
**Estimated Effort:** 2 days
**Dependencies:** None - this is the critical path first task

---

### [Emoji] **Task: Implement Transformation Logic**

**Input:**
- Analysis document from previous task
- Silver source tables: `silver_uat.[domain].[table]`
- Target schema DDL

**Outcome:**
- PySpark / Spark SQL transformation code
- Unit tests with >80% coverage using pytest + chispa
- Test scenarios:
  - Happy path: valid records transform correctly
  - Empty input: returns empty output
  - NULL key columns: dropped or handled per business rule
  - Duplicate records: dedup logic removes extras
  - Late-arriving records: incremental logic handles correctly
- Performance benchmark: confirm meets SLA

**Notes:**
- Apply 5 DLT baseline quality expectations (not-null, unique key, valid range, record count, schema conformance)
- Use `expect_or_fail` for critical fields; `expect_or_drop` + quarantine for recoverable violations
- Mock Silver tables for unit tests - do NOT connect to live UAT in unit tests
- Test edge cases: NULL primary key (fail), NULL nullable field (coalesce), negative balance (valid if business allows)

**Assigned To:** [Name]
**Priority:** High
**Estimated Effort:** 3 days
**Dependencies:** Analysis task complete

---

### [Emoji] **Task: Integration Test & Validate Against Legacy**

**Input:**
- Completed pipeline code
- UAT environment access
- Legacy system output for comparison period

**Outcome:**
- Row-count and checksum reconciliation report vs legacy
- E2E test results in UAT environment
- Any discrepancies documented with root cause
- Sign-off from [domain owner: Clement Kwong / Rachel dela Fuente / Chhavi Kashyap]

**Notes:**
- Compare at minimum: total row count, sum of key numeric columns, sample spot-check of 20+ records
- Test failure recovery: manually kill pipeline mid-run and confirm restart picks up correctly
- Confirm Datadog alert fires on record count drop > 20%

**Assigned To:** [Name]
**Priority:** High
**Estimated Effort:** 2 days
**Dependencies:** Implementation task complete; domain owner available for sign-off

---
```

---

## Template D - Story + Tasks (SQL Migration)

Use for Finance Platinum / Silver-to-Platinum SQL migration work.

```markdown
## 📊 **[Report Name] - SQL Migration to Databricks Platinum Layer**

**As a** Data Engineer
**I want to** migrate [report name] logic from SQL Server to Databricks
**So that** the [Finance / Risk / Operations] team has an automated, maintainable report
on the Databricks platform with no dependency on legacy SQL Server

### 📊 **Data Flow:**
**Source:** `silver_uat.questbank_temenos.[table]`
**Target:** `platinum_uat.[domain].[report_table]`
**Transformation:** [Aggregation / Join / Filter logic description]
**Frequency:** [Daily | Monthly]
**Latency SLA:** [< X minutes]

### 🎯 **Acceptance Criteria:**
1. Output matches SQL Server report for same reporting period
2. Row count reconciled: Databricks == SQL Server ± 0 rows
3. Key metric totals match within 0.01% tolerance
4. Unit tests with >80% coverage for aggregation logic
5. Performance meets SLA: [< X minutes]
6. [Stakeholder name] validates and signs off
7. Documentation complete with SQL translation notes

### ⚙️ **Tasks:**

---

### 🔍 **Task: Analyze SQL Server Stored Procedure / Query**

**Input:**
- Original `.sql` file from Finance_Delivery package
- SQL Server execution plan
- Business requirements from Finance team

**Outcome:**
- Logic breakdown document with Databricks translation notes
- Identified SQL Server-specific syntax requiring conversion:
  - CROSS APPLY → LATERAL VIEW
  - ISNULL() → COALESCE()
  - GETDATE() → CURRENT_DATE()
  - sds.* → silver_uat.questbank_temenos.*
  - PIVOT → window functions + conditional aggregation
- Dependency table list with Unity Catalog equivalents

**Notes:**
- Flag any logic that is ambiguous or undocumented - get clarification before implementing
- Document temp table patterns - replace with CTEs
- Note any MERGE statements - translate to Delta MERGE INTO

**Assigned To:** [Name]
**Priority:** High
**Estimated Effort:** 1–2 days
**Dependencies:** None - blocks all other tasks

---

### 🛠️ **Task: Implement in Spark SQL / PySpark**

**Input:**
- Analysis document from previous task
- Silver layer tables: `silver_uat.questbank_temenos.[tables]`
- Target schema DDL

**Outcome:**
- Spark SQL or PySpark implementation
- Unit tests with >80% coverage using pytest + chispa
- Test scenarios:
  - Happy path: standard reporting period output
  - Empty period: no data for date range - returns empty or zero
  - NULL handling: all ISNULL/COALESCE replacements verified
  - Aggregation accuracy: sum/count matches hand-calculated sample
  - Edge date: month boundary, fiscal year start
- Performance benchmark

**Notes:**
- Replace ALL SQL Server syntax using patterns from Section 8.2 of SKILL.md
- Use CTEs instead of temp tables
- Test with a 30-day window of UAT data before comparing to legacy

**Assigned To:** [Name]
**Priority:** High
**Estimated Effort:** 3 days
**Dependencies:** Analysis task complete

---

### ✅ **Task: Reconcile vs Legacy and Get Sign-off**

**Input:**
- Completed Databricks query / pipeline
- Legacy SQL Server output CSV for same period
- [Stakeholder] availability

**Outcome:**
- Reconciliation report: row count, key metric totals, discrepancy log
- All discrepancies investigated - intentional differences documented
- Sign-off from [Finance stakeholder]
- Technical notes added to Notion runbook

**Notes:**
- If discrepancy found: first check NULL handling, then check date range logic, then aggregation grouping
- "Intentional" differences are those where legacy logic was wrong - document explicitly

**Assigned To:** [Name]
**Priority:** High
**Estimated Effort:** 1–2 days
**Dependencies:** Implementation task complete

---
```

---

## Template E - Multi-Story Epic Breakdown

Only produce when Paroz explicitly asks for an epic breakdown.

```markdown
# [Epic Name] - Story Breakdown

## 👥 Team Allocation
**Team 1 ([Name] + [Name]):** [Story titles]
**Team 2 ([Name] + [Name]):** [Story titles]

---

## [Story 1 - full Template C or D format]

---

## [Story 2 - full Template C or D format]

---

## [Story 3 - full Template C or D format]

---

## 🎯 Critical Path:

[Story / Task] ← MUST GO FIRST (blocks all others)
    ↓
[Story A] ← Depends on above
[Story B] ← Depends on above
[Story X] ← Can run in parallel (no dependencies)
[Story Y] ← Can run in parallel (no dependencies)
    ↓
[Integration & UAT] ← Final gate

## 📅 Sprint Planning:
- **Sprint 1:** [Foundation stories + independent parallel stories]
- **Sprint 2:** [Dependent stories]
- **Sprint 3:** [Final stories + integration testing]
- **Sprint 4:** [UAT, documentation, buffer if needed]

**Total Estimated Effort:** X weeks (Y business days)
```
