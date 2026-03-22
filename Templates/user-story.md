# User Story: Template

> Agile story format with acceptance criteria, technical notes, and subtask breakdown. Optimized for Jira import.

---

## Story

**Title:** [Concise action-oriented title]

**As a** [persona: data analyst / business user / compliance officer / data engineer],
**I want to** [specific action or capability],
**So that** [measurable business value or outcome].

**Story Points:** [1 / 2 / 3 / 5 / 8 / 13]
**Priority:** [P0-Critical / P1-High / P2-Medium / P3-Low]
**Sprint:** [Sprint number]
**Epic:** [Parent epic name]

---

## Acceptance Criteria

```gherkin
GIVEN [precondition / context]
WHEN [action taken]
THEN [expected observable result]

GIVEN [precondition / context]
WHEN [action taken]
THEN [expected observable result]

GIVEN [edge case / error condition]
WHEN [action taken]
THEN [graceful handling / error message]
```

**Example:**
```gherkin
GIVEN a Bronze table with raw transaction data
WHEN the Silver pipeline runs the daily refresh
THEN all records pass data quality expectations (nulls < 1%, schema match 100%)

GIVEN a source system sends records with a new unexpected column
WHEN the Bronze ingestion job processes the batch
THEN the new column is captured in a _metadata field and an alert fires to #data-quality
```

---

## Technical Notes

**Approach:**
- [Implementation guidance]
- [Architecture considerations]

**Dependencies:**
- [Upstream: what must be ready first]
- [Downstream: what this unblocks]

**Data Considerations:**
- Source table(s): [schema.table]
- Target table(s): [schema.table]
- Volume estimate: [rows/day]
- SLA: [freshness requirement]

---

## Subtasks

| # | Subtask | Type | Est. | Owner |
|---|---------|------|------|-------|
| 1 | [Implementation task] | Dev | [hours] | |
| 2 | [Unit tests] | Test | [hours] | |
| 3 | [Integration test] | Test | [hours] | |
| 4 | [Documentation update] | Docs | [hours] | |
| 5 | [Code review] | Review | [hours] | |
| 6 | [Deploy to staging] | DevOps | [hours] | |

---

## Definition of Done

- [ ] Code complete and peer reviewed
- [ ] Unit tests passing (>80% coverage)
- [ ] Integration tests passing
- [ ] Data quality expectations defined (Silver+ layers)
- [ ] Documentation updated
- [ ] Deployed to staging and validated
- [ ] Product owner approval

---

## Pre-Delivery Verification

Before moving to sprint, confirm:

- [ ] **Persona:** The "As a" role is a real person on your team or stakeholder list, not a generic user.
- [ ] **Value:** The "So that" statement is measurable. If you cannot tell when the value is delivered, rewrite it.
- [ ] **Acceptance criteria:** Each criterion can be tested in isolation without running the others. If two criteria share a GIVEN, split them.
- [ ] **Edge case:** At least one criterion covers a failure or error condition.
- [ ] **Subtasks:** Every subtask has an owner. No orphaned tasks.
- [ ] **Dependencies:** Upstream dependencies are confirmed ready, not just assumed ready.
- [ ] **Estimate:** Story points reflect the full subtask list. If subtasks were added late, re-estimate.

If any check fails, fix it before committing to the sprint.
