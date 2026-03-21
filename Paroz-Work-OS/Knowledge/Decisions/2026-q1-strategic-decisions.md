# Q1 2026 Strategic Decisions Log

> Ratified decisions from Q1 2026 strategic sessions with Adam Neus and leadership. These decisions shape execution across all 5 Q1 initiatives.

**Sources:** Adam Neus meetings (Dec 5, Dec 29 2025; Jan 21 2026), team syncs (Feb-Mar 2026)
**Notion Source IDs:** `2d87b88e-336f-80bf-a79f-fcee1d0b3bd3`, `2ef7b88e-336f-804a-9c03-fe2fc2fc8fa6`, `2c07b88e-336f-805d-ba19-ca732fb1a7d5`
**Logged:** 2026-03-11

---

## Decision 1: Banking Data Goes to Databricks (Not BigQuery)

**Date:** Dec 2025 (formalized Jan 2026)
**Decision Maker:** Adam Neus (Managing Director)
**Status:** Ratified and executing

### Context
QFG operates two data platforms: Databricks (Azure) for banking and BigQuery (GCP) for brokerage. The question was whether QuestBank (banking) data should flow into BigQuery alongside brokerage data or stay in Databricks.

### Options Considered
1. **All data to BigQuery** (GCP consolidation)
2. **All data to Databricks** (Azure consolidation)
3. **Banking to Databricks, brokerage stays in BigQuery** (hybrid)

### Decision
Option 3: Banking data to Databricks; brokerage data stays in BigQuery.

### Rationale
- OSFI and PIPEDA regulatory requirements demand stronger governance controls
- Unity Catalog provides finer-grained access control than BigQuery IAM alone
- Databricks compute handles compliance workloads (AML, FinCrime)
- Separation of banking and brokerage data reduces blast radius
- GCP serverless private endpoint not yet available (7-min cluster spin-up for 30-sec queries)

### Consequences
- Two platform governance models (Unity Catalog + BigQuery IAM) unified via Entra ID
- Cross-platform catalog sync needed (Collibra evaluated)
- DataWizards team needs expertise in both platforms
- Higher operational complexity offset by stronger regulatory posture

---

## Decision 2: Databricks Dashboards Over Power BI

**Date:** Jan 2026
**Decision Maker:** Adam Neus, with input from Paroz and architecture team
**Status:** Ratified; executing for new use cases

### Context
Power BI Premium costs $2,500/user. 80% of PBI reports are tables exported to Excel. The question was whether to continue investing in Power BI or shift to Databricks native dashboards.

### Options Considered
1. **Continue Power BI** (status quo, familiar to business)
2. **Databricks AI/BI Dashboards** (native, cost-effective, better access control)
3. **Hybrid: PBI for existing, Databricks for new** (transition path)

### Decision
Option 3 (transitioning toward Option 2): All new dashboards on Databricks. Existing Power BI reports maintained but not expanded.

### Rationale
- Significant cost reduction ($2,500/user vs. Databricks compute costs)
- Databricks dashboards inherit Unity Catalog access controls (no separate PBI security layer)
- AI/BI Genie provides natural language querying on top of dashboards
- Reduces tool sprawl and simplifies the governance model

### Consequences
- Business users need training on Databricks dashboard UI
- Some Power BI features (advanced DAX, paginated reports) not available natively
- Metric views and semantic layer become critical for dashboard quality
- Engineering workshop (Mar 26) and BA workshop (post-Apr 6) planned to support transition

---

## Decision 3: Simplified PII Access Model

**Date:** Mar 5, 2026
**Decision Maker:** Architecture team (Paroz, Dan, governance council)
**Status:** Ratified; implemented in access group design

### Context
Original access model had four PII access levels: Full, Partial, Superuser, and None. This created complexity in group management and ambiguity in what "partial" and "superuser" meant.

### Options Considered
1. **Keep 4 levels** (status quo)
2. **Simplify to 2 levels:** Full PII access or No PII access (with column masking)
3. **Simplify to 3 levels:** Full, Masked, None

### Decision
Option 2: Binary PII access (Full or Masked). Removed Superuser and Partial roles.

### Rationale
- "Partial" was ambiguous (which columns? which rows?)
- "Superuser" created accountability gaps (too broad, no audit precision)
- Binary model is easier to implement, audit, and explain
- ABAC column masking handles the nuance (mask specific fields, not entire access levels)
- Reduces Entra ID group proliferation

### Consequences
- Simpler group management in Entra ID
- Some users who had "partial" access need reclassification
- Column masking policies must be granular enough to replace the old "partial" concept
- Governance feature ~80% complete with this simplified model

---

## Decision 4: Consumer-First Approach

**Date:** Jan 21, 2026
**Decision Maker:** Adam Neus
**Status:** Ratified; shapes Q1-Q2 roadmap priorities

### Context
In building the data mesh, the question was whether to focus on producer-side tooling (publishing workflows, quality certification, metadata management) or consumer-side experience (discovery, access, self-serve).

### Options Considered
1. **Producer-first:** Build publishing infrastructure, then attract consumers
2. **Consumer-first:** Build discovery and access, let consumer demand pull producers
3. **Balanced:** Build both simultaneously

### Decision
Option 2: Consumer-first. Build self-serve access and discovery before producer automation.

### Rationale
- Consumers are currently underserved (especially brokerage side)
- Producer automation is complex and long-lead
- Consumer adoption creates network effects that incentivize producers
- Demonstrating consumer value builds organizational buy-in
- Self-serve environments are the quickest win with highest visibility

### Consequences
- Q1-Q2 2026 focuses on catalog, access workflows, self-serve environments
- Producer tooling deferred to Q2-Q3 2026
- DataWizards publishes initial data products to seed the exchange
- Risk: without producer tooling, data product quality may be inconsistent early on

---

## Decision 5: Brainless First Philosophy

**Date:** Dec 29, 2025 (articulated in SPA)
**Decision Maker:** Adam Neus
**Status:** Ratified; embedded in design principles

### Context
The data access management framework could be built with full sophistication from day one (ABAC + RBAC + dynamic policies + AI-assisted access) or could start simple and evolve.

### Options Considered
1. **Full sophistication** (all access patterns implemented simultaneously)
2. **Brainless first** (simplest viable model, add complexity as adoption grows)

### Decision
Option 2: Start with the simplest access model that works. Add sophistication only when scale or compliance demands it.

### Rationale
- Complex systems fail in complex ways; simple systems scale
- Adoption matters more than features in the first 6 months
- Team can iterate faster with a simple foundation
- Regulatory minimums can be met with basic controls
- Premature optimization of governance kills momentum

### Consequences
- Phase 1 access controls are Power BI-level (coarse-grained)
- Phase 2 adds ABAC/RBAC as adoption grows
- Design must be modular so sophistication layers can be added without rewrites
- Risk of governance gaps in early phases (mitigated by manual steward oversight)

---

## Decision 6: Data Engineering Team Owns Data Strategy

**Date:** Feb-Mar 2026 (emerging from multiple meetings)
**Decision Maker:** Adam Neus
**Status:** Active; organizational implications being worked through

### Context
Data strategy decisions (architecture, tool selection, governance model) were previously distributed across multiple teams. The question was who owns the strategy going forward.

### Options Considered
1. **Distributed ownership** (each team makes its own data decisions)
2. **Central governance body** (a committee or council)
3. **Data engineering team** (DataWizards) owns strategy, with governance oversight

### Decision
Option 3: Data engineering team (DataWizards, led by Paroz) owns data strategy execution. Adam provides strategic direction. Governance council provides oversight.

### Rationale
- Engineering team has the deepest technical context
- Single ownership avoids decision paralysis across committees
- Aligns accountability with execution capability
- Adam provides strategic direction (the "what"); engineering determines the "how"

### Consequences
- DataWizards becomes the de facto data strategy team (not just a build team)
- Team needs product management skills, not just engineering
- Cross-functional coordination becomes Paroz responsibility
- Risk of overloading a small team (~5 engineers) with strategy + execution
- Likely team restructuring: evolution toward 5 product managers with capability mapping

---

## Summary: Decision Dependency Map

```
Decision 6 (DE owns strategy)
    |
    +-- Decision 1 (Banking to Databricks)
    |       |
    |       +-- Decision 2 (Databricks dashboards over PBI)
    |
    +-- Decision 4 (Consumer-first)
    |       |
    |       +-- Decision 5 (Brainless first)
    |
    +-- Decision 3 (Simplified PII)
            |
            +-- Feeds into: Access Management Framework
```

---

*Cross-references: [q1-strategy.md](../Work/q1-strategy.md) for initiative context, [access-management.md](../Work/access-management.md) for framework details, [data-mesh-vision.md](../Work/data-mesh-vision.md) for architectural philosophy*

*Logged 2026-03-11. Decisions are stable unless explicitly revisited by Adam or leadership.*
