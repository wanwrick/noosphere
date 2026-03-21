# DataWizards Agile Ticket System

> Complete ticket creation system for the DataWizards team. Decision gates, ticket types, technical patterns, team roster, formatting rules, and quality checklist. Source: agile-story-creator skill.

## ⚠️ LEAN FIRST - THE CARDINAL RULE

**Before writing anything, ask: what is the simplest ticket that captures the work?**

The default output is a **flat independent task** - no parent story, no subtasks, just a clean task.
Escalate to a story only when business context genuinely requires it.
Escalate to an epic breakdown only when explicitly requested.

History shows Claude defaults to over-engineering. Fight that instinct.

---

## SECTION 1 - DECISION GATE: What Ticket Type?

Run through this in order before writing a single line.

```
Is this time-boxed investigation/research with no predefined output?
    YES → SPIKE (Section 3). One ticket per engineer. No subtasks.
    NO  ↓

Is there a single, well-scoped deliverable with no meaningful sub-components?
    YES → FLAT INDEPENDENT TASK (Section 2). No parent, no subtasks.
    NO  ↓

Are there 3+ related tasks that share a business outcome AND benefit from grouping?
    YES → STORY + TASKS (Section 4). One story, tasks underneath. NOT sub-stories.
    NO  ↓

Is this a full feature/epic with multiple teams, multiple stories, explicit sprint planning?
    YES → MULTI-STORY EPIC BREAKDOWN (Section 5). Only when explicitly requested.
```

### When NOT to add subtasks

Do NOT create subtasks when:
- The work is already specific enough ("Update X table to add Y column")
- A single engineer can carry it start to finish without handoffs
- Breaking it down just adds Jira overhead
- Paroz used phrases like "just a task", "flat", "keep it simple", "don't over-engineer it"

### The one acceptable exception

A **maintenance/hardening story** with multiple tasks (not sub-stories) is acceptable
when grouping related maintenance items makes sense for a single sprint view.
Use this sparingly.

---

## SECTION 2 - FLAT INDEPENDENT TASK

The most common output. No parent story. No subtasks. Clean and direct.

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

### Example - Flat Task (no subtasks)

```markdown
### 🔌 **Configure Databricks External Table for CRSA BigQuery Dataset**

**Context:**
Shreya Shukla's CRSA team needs read access to historical CTC mortgage data in
`qt-mortgages-prod-3r.ctc_intellify_crsa_pdt_sec` via an external table in Unity Catalog
so analysts can join it against QuestBank data without leaving Databricks.

**Work to be done:**
- Create Unity Catalog external table pointing to BigQuery source using Iceberg federation
- Validate OAuth2 credentials from Francisco Diez (DataOps) are applied to `bq-iceberg-table-pipeline` service account
- Run query smoke test against CRSA dataset from a Databricks notebook
- Unit tests with >80% coverage for connection and table registration logic

**Acceptance Criteria:**
1. External table accessible from `silver_uat.questbank_lms` namespace without error
2. CRSA analysts can run SELECT queries against historical CTC data from Databricks
3. OAuth2 service account auth confirmed by DataOps - no hardcoded credentials
4. Unit tests written and passing

**Assigned To:** Artur Gyulambaryan
**Priority:** High
**Estimated Effort:** 2 days
**Dependencies:** Francisco Diez (DataOps) must provide OAuth2 credentials for `bq-iceberg-table-pipeline` service account
```

---

## SECTION 3 - SPIKE TICKET

Time-boxed investigation. One comprehensive ticket per engineer. **Zero subtasks.**
The whole point is that the outcome is unknown - that's why it's a spike.

```markdown
### 🔍 **[Investigation Topic] - Spike**

**Context:**
[Why we're doing this investigation. What decision it will inform.]

**Investigation Scope:**
- [Specific question or area to investigate 1]
- [Specific question or area to investigate 2]
- [Specific question or area to investigate 3]
- [Data objects, fields, or systems to examine]

**Expected Output:**
- [Documented findings in Notion/Confluence]
- [Specific recommendation or decision ready for next sprint]
- [Any edge cases or blockers identified]

**Time Box:** [X days]
**Assigned To:** [Name]
**Priority:** High | Medium | Low
**Dependencies:** [None | List blockers]
```

### Example - Spike (comprehensive, no subtasks)

```markdown
### 🔍 **Salesforce UAT Data Quality - Appraiser & Broker Objects - Spike**

**Context:**
QuestBank delineation testing is blocked by data quality issues in Salesforce UAT.
Specific GUID mismatches and missing mandatory fields were identified in Appraiser__c,
Broker__c, and Broker_Condition__c. This spike maps root causes so we can write fix tickets.

**Investigation Scope:**
- Appraiser__c: Confirm which appraiser records are missing `Appraiser_License__c` and `Appraiser_Company__c`; determine if source is LMS or LOS
- Broker__c: Identify GUID mismatches between Salesforce `Id` and `External_Broker_Id__c`; trace back to Enablement source table
- Broker_Condition__c: Investigate duplicate records (Federico flagged this); determine if root cause is pipeline logic or source duplication
- Document which issues are BLOCKING (prevent test run) vs NON-BLOCKING (data quality only)
- Reference SF mapping doc for valid picklist values: [Google Sheets link]

**Expected Output:**
- Written findings doc per object with root cause + recommended fix
- Priority-ranked issue list: BLOCKED items first
- Ready-to-execute fix tickets for next sprint

**Time Box:** 2 days
**Assigned To:** Artur Gyulambaryan
**Priority:** High
**Dependencies:** UAT environment access, Salesforce mapping Google Sheet
```

---

## SECTION 4 - STORY + TASKS

Use when a business outcome requires grouping. Story is the "why", tasks are the "what".
Tasks are NOT sub-stories - they are flat work items under one story.

```markdown
## [Emoji] **Story Title**

**As a** [specific role - Data Engineer, Business Analyst, Risk Analyst]
**I want to** [action/capability]
**So that** [business value - answer "why does this matter?"]

### 📊 **Data Flow:** *(include for pipeline stories)*
**Source:** `[System].[Schema].[Table]`
**Target:** `[Catalog].[Schema].[Table]`
**Transformation:** [Brief description]
**Frequency:** [Real-time | Daily | Hourly | Monthly]
**Latency SLA:** [< X minutes]

### 🎯 **Acceptance Criteria:**
1. [Measurable pass/fail - focus on WHAT, not HOW]
2. [Data quality validation with threshold]
3. [Performance SLA if applicable]
4. [Unit tests >80% coverage for core logic]
5. [Integration test in SIT/UAT passes]
6. [Documentation complete]

### ⚙️ **Tasks:**

---

### [Emoji] **Task Title**

**Input:**
- [Specific artifact or data needed to start]
- [Access or prerequisite required]

**Outcome:**
- [Concrete deliverable]
- [Unit tests with >80% coverage - for code tasks]
- [Test scenarios: list 3–5 specific cases]

**Notes:**
- [Implementation guidance]
- Test edge cases: null values, empty datasets, boundary conditions
- Mock external dependencies: [list what to mock]
- [Technical considerations]

**Assigned To:** [Name]
**Priority:** High | Medium | Low
**Estimated Effort:** [X days]
**Dependencies:** [None | Previous task | External blocker]

---
```

---

## SECTION 5 - MULTI-STORY EPIC BREAKDOWN

Only use when explicitly requested by Paroz. Always include all four components.

```markdown
# [Epic Name] - Story Breakdown

## 👥 Team Allocation
**Team 1 ([Name] + [Name]):** [Story titles]
**Team 2 ([Name] + [Name]):** [Story titles]

---
[Stories in full Section 4 format]

---

## 🎯 Critical Path:

[Foundation Story] ← MUST GO FIRST
    ↓
[Dependent Story A] ← Depends on foundation
[Dependent Story B] ← Depends on foundation
[Parallel Story X]  ← Can run in parallel (no dependencies)
    ↓
[Integration/UAT]   ← Final gate

## 📅 Sprint Planning:
- **Sprint 1:** [Stories]
- **Sprint 2:** [Stories]
- **Sprint 3:** [Stories + integration testing]

**Total Estimated Effort:** X weeks (Y business days)
```

---

## SECTION 6 - FORMATTING RULES (NON-NEGOTIABLE)

### Title Rules
- ❌ NEVER: `STORY-001`, `SUBTASK-001.1`, any numbering prefix
- ✅ ALWAYS: Clean titles ready for direct Jira paste
- ✅ ALWAYS: Emoji at the **START** of every title

### Emoji Reference

| Emoji | Use For |
|-------|---------|
| 🔌 | Integration / connectivity |
| 📋 | Planning / documentation |
| 🔍 | Discovery / investigation / spike |
| 🚀 | Deployment / release |
| 🔐 | Security / authentication |
| 📊 | Analytics / reporting / data flow |
| 🏗️ | Architecture / infrastructure |
| ⚙️ | Configuration / setup |
| 🧪 | Testing / validation |
| 📦 | Packaging / bundling |
| 💧 | Data pipeline / flow |
| 🔗 | Connection / linking (subtask) |
| 📝 | Documentation (subtask) |
| 🔧 | Configuration (subtask) |
| ⚡ | Performance (subtask) |
| 🛡️ | Security / quality (subtask) |
| 🚨 | Error handling (subtask) |
| 🎯 | Implementation (subtask) |
| 🛠️ | Development (subtask) |
| ✅ | Validation / testing (subtask) |

### Mandatory Fields on Every Ticket
Every ticket - task, spike, or subtask - must end with:
```
**Assigned To:** [Name]
**Priority:** High | Medium | Low
**Estimated Effort:** [X days]
**Dependencies:** [None | specific blocker]
```

---

## SECTION 7 - UNIT TESTING STANDARDS (MANDATORY)

Unit tests are **deliverables, not afterthoughts**. Every subtask or task that produces code must include them.

### In Outcome section, always write:
```
- Unit tests with >80% coverage for core logic
- Test scenarios:
  - Happy path: [describe]
  - Null/empty input: [describe]
  - Duplicate records: [describe]
  - Invalid data type: [describe]
  - Boundary condition: [describe]
```

### In Notes section, always write:
```
- Test edge cases: null values, empty datasets, boundary conditions
- Mock external dependencies: [Pub/Sub | BigQuery | Databricks tables | Salesforce API]
- Framework: pytest + chispa for PySpark; dbt test for SQL
```

### Framework Reference

| Use Case | Framework |
|----------|-----------|
| Python / PySpark transformation | pytest + chispa + unittest.mock |
| SQL / DBT model | dbt test + dbt-expectations |
| Integration / E2E | testcontainers |
| GCP service mocking | moto |
| HTTP / API mocking | responses |
| Coverage reporting | coverage.py |

### Coverage Targets

| Component | Minimum | Critical Paths |
|-----------|---------|----------------|
| Core transformation logic | >80% | 100% |
| Business rules | >80% | 100% |
| Error handling | >70% | 100% for critical errors |
| Utility functions | >70% | N/A |

---

## SECTION 8 - DATAWIZARDS TECHNICAL PATTERNS

### 8.1 DLT Data Quality - 5 Baseline Expectations

Every new DLT pipeline must include these five expectations. Apply to all new pipelines.

| # | Expectation | Rule Type | When to Use |
|---|-------------|-----------|-------------|
| 1 | Not-null on mandatory fields | `expect_or_fail` | Critical key fields - fail the batch |
| 2 | Unique key constraint | `expect_or_fail` | Primary keys - fail the batch |
| 3 | Valid range checks | `expect_or_drop` + quarantine | Numeric/date ranges - drop and route |
| 4 | Record count vs. trailer | `expect_or_fail` | File-based ingestion - fail if mismatch |
| 5 | Schema conformance | `expect_or_fail` | Column presence/types - fail the batch |

**Rule assignment logic:**
- `expect_or_fail` → Critical data integrity violations; batch should not proceed
- `expect_or_drop` + quarantine routing → Recoverable violations; bad rows quarantined, pipeline continues
- Quarantine pattern uses `force_batch_sync` API from Work Stream D; Gabriel Goulart and Yelena Hakhumyan are pattern owners

### 8.2 SQL Migration Patterns (SQL Server → Databricks SQL)

| SQL Server | Databricks SQL | Notes |
|------------|---------------|-------|
| `CROSS APPLY` | `LATERAL VIEW` or `explode()` | Use `explode_outer()` to preserve NULLs |
| `GETDATE()` | `CURRENT_DATE()` or `CURRENT_TIMESTAMP()` | |
| `ISNULL(x, y)` | `COALESCE(x, y)` | |
| `sds.*` | `Silver.QuestBank_Temenos_LMS.*` | Full catalog path required |
| `PIVOT` | Window functions + conditional aggregation | |
| Temp tables | CTEs or Delta temp views | |
| `MERGE` | `MERGE INTO` on Delta table | |
| `TOP N` | `LIMIT N` | |

### 8.3 Array Explosion Pattern

For the 19 array columns across LOS (6), LMS (5), and Enablement (8):

**Preferred approach:**
```sql
-- Use inline_outer() as table-valued function - cleanest SQL syntax
SELECT parent.*, exploded.*
FROM silver_uat.questbank_los.mortgage_finance_and_accounting_loan parent
LATERAL VIEW OUTER inline(from_json(parent.borrowers, schema_of_json(...))) exploded
```

**Key rules:**
- Use `_outer` variants (`inline_outer`, `explode_outer`) - preserves rows with NULL/empty arrays
- Use `schema_of_json()` for auto-discovery - do NOT hardcode schemas before profiling
- **Schema discovery is critical path** - must complete before parallel explosion work starts
- Gabriel Cortes and Mariano own LOS/Enablement explosion; Ljupco and Federico own LMS

### 8.4 Unity Catalog Schema References

**silver_uat schemas:**
- `silver_uat.questbank_enablement`
- `silver_uat.questbank_lms`
- `silver_uat.questbank_los`
- `silver_uat.questbank_sf`
- `silver_uat.questbank_temenos`
- `silver_uat.data_profiling`

**platinum_uat schemas:**
- `platinum_uat.capital_markets`
- `platinum_uat.collections`
- `platinum_uat.compliance`
- `platinum_uat.finance`
- `platinum_uat.fraud`
- `platinum_uat.internal_audit`
- `platinum_uat.legal_compliance`
- `platinum_uat.marketing`
- `platinum_uat.operations`
- `platinum_uat.product`
- `platinum_uat.risk`
- `platinum_uat.shared_services`
- `platinum_uat.technology`
- `platinum_uat.treasury`

**Out-of-scope for classification:** `Silver.QuestBank_Temenos_Money`
**In-scope for classification:** `Silver.QuestBank_Temenos_LMS`

### 8.5 Source-to-Target Pipeline Patterns

| Source | Bronze | Silver |
|--------|--------|--------|
| Temenos ODS/SDS | `bronze.questbank_temenos` | `silver_uat.questbank_temenos` |
| LOS Pub/Sub | `bronze.questbank_los` | `silver_uat.questbank_los` |
| LMS Pub/Sub | `bronze.questbank_lms` | `silver_uat.questbank_lms` |
| Salesforce | `bronze.questbank_sf` | `silver_uat.questbank_sf` |
| Enablement | `bronze.questbank_enablement` | `silver_uat.questbank_enablement` |

**GCS bucket paths:**
```
gs://questbank/los/raw/
gs://questbank/lms/raw/
gs://questbank/temenos/raw/
```

---

## SECTION 9 - TEAM REFERENCE

### Engineers and Default Domain Ownership

| Engineer | Primary Domain | Secondary |
|----------|---------------|-----------|
| Artur Gyulambaryan | Temenos Silver pipelines, BigQuery/Iceberg integration | Code reviews |
| Ljupco Grmaskoski | LMS, Temenos dedup logic, Airflow DAGs, secrets management | Reviewer for Equifax pipeline |
| Gabriel Cortes | LMS DLT pipelines, quarantine patterns, LOS array explosion | DLT pattern owner |
| Hayk Danielyan | LOS/Enablement pipeline packaging, array explosion | |
| Federico Pegazzano | LOS pipelines, code review | LMS support |
| Mariano Barrionuevo | Enablement pipelines, Alterna reporting, array explosion | Finance Platinum queries |
| Yelena Hakhumyan | LOS DLT pipelines, naming standards, Salesforce LOS fields | DLT quarantine pattern co-owner |

### Cross-Team Contacts

| Name | Team | Role |
|------|------|------|
| Francisco Diez | DataOps | OAuth2 / infrastructure / CI/CD |
| Shreya Shukla | CRSA | Credit risk - Equifax/OCDC pipeline consumer |
| Clement Kwong | LMS domain | Validation partner, LMS domain owner |
| Rachel dela Fuente | LOS domain | LOS domain expertise |
| Chhavi Kashyap | Data Products | Regulatory reports product owner |
| Margaret Chum | BI | GIC dashboards lead |
| Pedro Alves | External | BigQuery Iceberg integration partner |

### Sprint Prioritization Rule

**Regulatory extracts and Model Office UAT come first.**
Capacity reallocated regardless of domain expertise.
Pipeline hardening parked to later sprints unless explicitly re-prioritized.

---

## SECTION 10 - CROSS-PLATFORM OUTPUT RULES

### When to offer a clean copy-paste version

Always offer a clean copy-paste version when:
- Paroz is sending to **Google Chat** - markdown tables and headers break
- Paroz is sending to **Slack** - bold renders, but multi-line code blocks and ASCII art often break
- Paroz is sending to **Gmail** - no markdown rendering at all; use plain prose

### Audience-calibrated communication

| Audience | Format Rules |
|----------|-------------|
| Senior stakeholders (Mark Huang, Anna, Daniel Dininio, Ana Carrocci) | No markdown tables. No specific dates. Business-value framing. No feature numbers. |
| Engineering team (DataWizards) | Full technical breakdown. Tables fine. Code blocks fine. |
| Product leads (Chhavi Kashyap, business owners) | Business-value summaries. Minimal technical jargon. |
| Cross-team engineers (DataOps, Data Platform) | Technical, collaborative tone. Acknowledge dependencies. |

---

## SECTION 11 - RESPONSE BEHAVIOUR REFERENCE

| Paroz Says | Claude Does |
|------------|-------------|
| "Create a task for [X]" | Section 2 - Flat independent task |
| "Flat task", "keep it simple", "no subtasks" | Section 2 - flat task only |
| "Spike for [X]" | Section 3 - Spike, no subtasks |
| "Two spikes, one per engineer" | Two Section 3 tickets, each comprehensive |
| "Create a story for [X]" | Section 4 - Story + tasks |
| "Just one story with some tasks" | Section 4 - one story, tasks not sub-stories |
| "Break down [epic]" | Section 5 - Full epic breakdown |
| "Stories for [feature]" | Section 5 if multiple teams implied; Section 4 otherwise |
| "Add subtasks to [story]" | 3–6 Section 4 tasks with Input/Outcome/Notes |

### Correction history to internalize

These are patterns where Claude historically got it wrong. Never repeat these:
- ❌ Creating a story when a flat task was asked for
- ❌ Adding subtasks when "flat" or "just a task" was used
- ❌ Treating a spike like an implementation story with subtasks
- ❌ Over-decomposing: splitting a 2-day task into 4 subtasks across 2 stories
- ❌ Adding STORY-001 / SUBTASK-001.1 prefixes
- ❌ Making the first subtask "analyze requirements" when the requirements are already clear
- ❌ Assigning to the wrong engineer (check domain ownership in Section 9)

---

## SECTION 12 - QUALITY CHECKLIST

Before outputting any ticket, verify:

**Every ticket:**
- [ ] No prefix numbers anywhere (STORY-XXX, SUBTASK-XXX, etc.)
- [ ] Emoji at START of title
- [ ] Assigned To + Priority + Estimated Effort + Dependencies at end
- [ ] Lean - no unnecessary decomposition

**Code tasks/subtasks additionally:**
- [ ] Unit tests >80% in Outcome
- [ ] 3–5 specific test scenarios listed
- [ ] Testing framework specified (pytest/chispa/dbt test)
- [ ] Edge cases in Notes

**Story (Section 4) additionally:**
- [ ] As a / I want / So that format
- [ ] 5–7 measurable acceptance criteria
- [ ] Data Flow block if it's a pipeline story

**Multi-story epic (Section 5) additionally:**
- [ ] Team allocation at top
- [ ] Critical path diagram at end
- [ ] Sprint recommendations at end
- [ ] Dependencies mapped

---

## Reference Files

- `../../Templates/user-story.md` - Full templates by story type
- `agile-examples.md` - Real approved examples from DataWizards sprints
- `testing-patterns.md` - Test scenario templates and framework examples
