# Data Mesh Vision and Architecture

> Strategic vision for QFG data mesh: decentralized ownership with centralized exchange, consumer-first philosophy, hybrid platform strategy, and quality governance economics.

**Source:** Adam Neus strategic sessions (Jan 21, Dec 29, Dec 5 2025-2026)
**Notion Source IDs:** `2ef7b88e-336f-804a-9c03-fe2fc2fc8fa6`, `2d87b88e-336f-80bf-a79f-fcee1d0b3bd3`
**Snapshotted:** 2026-03-11

---

## Core Architecture: Decentralized Ownership, Centralized Exchange

The data mesh at QFG is NOT a pure Zhamak-style mesh. It is a pragmatic hybrid:

| Aspect | Approach |
|--------|----------|
| **Data Production** | Decentralized: domain teams own their data products (RACI-style) |
| **Data Consumption** | Centralized exchange: single discovery, access, and governance layer |
| **Governance** | Federated: central policies, domain-level stewardship |
| **Platform** | Centralized: DataWizards provides shared infrastructure (Databricks + GCP) |

### RACI for Data Mesh

| Activity | Domain Team | DataWizards (Platform) | Data Governance |
|----------|------------|----------------------|----------------|
| Define data product | **R/A** | C | C |
| Build pipeline | C | **R/A** | I |
| Set quality SLAs | **R** | C | **A** |
| Classify data | **R** | I | **A** |
| Approve access | **R** | I | C |
| Monitor quality | C | **R** | **A** |
| Operate infrastructure | I | **R/A** | I |

---

## Consumer-First Strategy

**Principle:** Prioritize the subscriber (consumer) experience before building producer-side automation.

### Rationale
- Consumers are currently underserved, especially brokerage-side users
- Producer automation is complex (metadata management, quality certification, publishing workflows)
- Demonstrating consumer value creates pull demand for producers to publish
- Network effects: more consumers create incentive for more publishers

### Consumer Priorities (Q1-Q2 2026)
1. **Self-serve data environments** as the first deliverable
2. **Searchable data catalog** with AI-assisted discovery
3. **Simplified access request** workflow (target: < 2 days from request to access)
4. **Power BI integration** as the primary consumption tool (while evaluating Databricks dashboards)

### Producer Priorities (Q2-Q3 2026)
1. Metadata-driven publishing workflows
2. Automated quality certification
3. Data contract enforcement
4. Lineage tracking and impact analysis

---

## Hybrid Platform Architecture

QFG operates two major data platforms. The mesh must span both:

| Platform | Primary Use | Data Types | Consumer Tools |
|----------|------------|------------|---------------|
| **Databricks (Azure)** | Banking (QuestBank), regulatory, ML | Core banking, AML, credit card, loans | SQL Warehouse, Dashboards, Notebooks |
| **BigQuery (GCP)** | Brokerage, marketing, product analytics | Trading, CRM, Braze, website events | BigQuery, Looker, Data Studio |

### Governance Unification
- **Unity Catalog** is the primary governance control plane (Databricks side)
- **BigQuery IAM** for GCP-side access (mapped to same Entra ID groups)
- **Collibra** evaluated for cross-platform catalog sync
- **Entra ID** as the single identity source across both platforms

### Key Decision: Banking Data to Databricks
All QuestBank banking data goes to Databricks, not BigQuery. Rationale:
- Regulatory compliance requirements (OSFI, PIPEDA) need stronger governance
- Unity Catalog provides finer-grained access control
- Databricks compute can handle the compliance workloads
- Keeps sensitive banking data separate from brokerage analytics

---

## Quality Governance Economics

### The Lemons Problem (Information Asymmetry)

Core concern from Adam: without quality signals, consumers cannot distinguish good data from bad data. This creates a market failure:

1. **Low-quality data products** are cheap to produce (no investment in documentation, testing, SLAs)
2. **Consumers cannot tell** which products are high-quality before consuming them
3. **High-quality producers** get no reward for extra investment
4. **Result:** Quality deteriorates across the board (Akerlof market for lemons)

### Solution: Three-Tier Quality Certification

| Tier | Label | Requirements | Signal to Consumer |
|------|-------|-------------|-------------------|
| 1 | **Standards-Based** | Meets minimum metadata, naming, and documentation standards | Published and cataloged |
| 2 | **Automated Controls** | Passes automated data quality checks (completeness, freshness, schema validation) | Quality verified |
| 3 | **White-Glove** | Steward-certified, SLA-backed, with documented lineage and business context | Production-grade |

### Incentive Design
- Certification tier visible in the data catalog (transparency creates accountability)
- Higher-tier products get priority placement in search results
- Quality metrics rolled up to domain team OKRs
- Algorithmic monitoring flags degradation (no reliance on manual steward vigilance)

---

## Principal-Agent Challenges

### Data Steward Incentive Misalignment
- **The problem:** Data stewards (domain experts) are asked to do governance work orthogonal to their primary job
- **Classic principal-agent:** The organization (principal) wants rigorous governance; the steward (agent) wants to minimize additional work
- **Manifestation:** Delayed approvals, rubber-stamped access reviews, incomplete metadata

### Mitigation Strategies
1. **Algorithmic monitoring:** Automated checks reduce reliance on manual steward effort
2. **Embedded governance:** Build governance into the publishing pipeline (not a separate process)
3. **Incentive alignment:** Tie data product quality to team performance metrics
4. **Reduce friction:** AI-assisted metadata generation means stewards validate rather than create

---

## Critical Success Factors

### 1. Minimum Viable Liquidity
- The data exchange must have enough useful products to attract consumers
- Target: 20+ data products published with Tier 1+ certification before broad launch
- Cold-start strategy: DataWizards publishes core banking products first, then onboard domain teams

### 2. Network Effects
- Consumer adoption drives producer motivation (pull, not push)
- Usage analytics shared with publishers ("your data product was queried 450 times this month")
- Community of practice: regular data product showcases and feedback loops

### 3. Product Validation
- Treat each data product like a product launch: define the consumer, validate the need, measure adoption
- Apply the 10Q onboarding framework (from questbank-playbooks.md) to every new data product

---

## Organizational Vision

### Team Structure Evolution
- Current: centralized DataWizards team builds everything
- Future: 5 product managers with capability mapping across domains
- Each PM owns a domain data product portfolio
- DataWizards evolves from build team to platform team

### Approach by Business Unit
| Business Unit | Approach | Rationale |
|--------------|----------|-----------|
| **Bank (QuestBank)** | Structured, compliance-driven | Regulatory requirements demand formal governance |
| **Brokerage** | Client-driven, flexible | Brokerage users need speed; technology follows client need |

### Key Organizational Principle
**Client-driven technology:** Avoid mandating tools or processes. Let client (consumer) needs drive platform evolution. Different business units may need different approaches, and that is acceptable.

---

## Roadmap Alignment

| Phase | Timeline | Focus |
|-------|----------|-------|
| **Foundation** | Q1 2026 | ABAC/RBAC implementation, access groups, self-serve environments, core banking products published |
| **Consumer Launch** | Q2 2026 | Data catalog live, self-serve access workflows, consumer onboarding |
| **Producer Enablement** | Q2-Q3 2026 | Publishing workflows, quality certification, data contracts enforcement |
| **Scale** | Q3-Q4 2026 | Domain team onboarding, cross-platform governance, external marketplace evaluation |

### Unified Roadmap Need
Adam emphasized that all 5 Q1 initiatives must feed into a single unified roadmap. Currently, initiatives are tracked separately. The roadmap must show:
- Dependencies between initiatives
- Shared resource constraints (~23 FTE total)
- Regulatory deadlines that are non-negotiable (OSFI, FinCrime)
- Consumer-facing milestones vs. infrastructure milestones

---

*Cross-references: [q1-strategy.md](./q1-strategy.md) for initiative details, [access-management.md](./access-management.md) for access framework, [questbank-playbooks.md](./questbank-playbooks.md) for 10Q and data contracts*

*Snapshotted from Notion 2026-03-11. For live updates, fetch Notion page IDs above.*
