# Consulting - SKILL Reference
## Professional Resource Collection + Consulting Frameworks

---

## Overview

This SKILL combines formal consulting methodologies with Paroz's professional data platform architecture documentation. Not tied to a single EMBA course but draws from Business Strategy, Critical Thinking, Operations Management, and MIS.

---

## Core Consulting Frameworks

### MECE (Mutually Exclusive, Collectively Exhaustive)

The foundation of structured consulting analysis. Every decomposition must be:
- **Mutually Exclusive:** No overlap between categories (each item belongs in exactly one bucket)
- **Collectively Exhaustive:** All possibilities covered (nothing falls through the cracks)

**Application pattern:**
1. Define the problem statement precisely
2. Decompose into MECE buckets (3-5 categories)
3. Validate: Can every relevant fact be placed in exactly one bucket?
4. Prioritize: Which buckets have the highest impact?

**Common MECE structures:**
| Structure | Example |
|-----------|---------|
| **Revenue = Price x Volume** | Diagnose revenue decline |
| **Internal vs. External** | Root cause analysis |
| **Customer segments** | Market opportunity sizing |
| **Value chain stages** | Cost reduction analysis |
| **Geography / Product / Channel** | Growth strategy |

### Issue Trees

Hierarchical decomposition of a problem into sub-problems:

```
Core Question: Why is profitability declining?
|
+-- Revenue declining?
|   +-- Price decrease?
|   +-- Volume decrease?
|       +-- Market shrinking?
|       +-- Losing market share?
|           +-- Product issues?
|           +-- Distribution issues?
|           +-- Competitive pressure?
|
+-- Costs increasing?
    +-- Fixed costs up?
    |   +-- Rent / facilities?
    |   +-- Headcount?
    +-- Variable costs up?
        +-- COGS?
        +-- Distribution?
```

**Rules:**
1. Start with the core question (hypothesis or open-ended)
2. Each level must be MECE
3. Go 3-4 levels deep maximum
4. Leaves become testable hypotheses
5. Prioritize branches by impact and data availability

### Hypothesis-Driven Problem Solving

**The McKinsey approach:** Start with a hypothesis, then prove/disprove.

| Step | Action | Deliverable |
|------|--------|------------|
| 1. **Frame** | Define problem, scope, success criteria | Problem statement + issue tree |
| 2. **Hypothesize** | Formulate initial answer based on pattern recognition | "Day 1 answer" |
| 3. **Design** | Plan analyses to prove/disprove hypothesis | Workplan with analyses mapped to hypotheses |
| 4. **Analyze** | Run analyses, gather evidence | Data-backed findings |
| 5. **Synthesize** | Combine findings into narrative | "So what?" for each finding |
| 6. **Recommend** | Present actionable recommendations | Pyramid-structured recommendation |

**Key principle:** "Answer first, then support." Never present analysis chronologically. Lead with the recommendation, then show the evidence.

### Pyramid Principle (Barbara Minto)

Communication structure for consulting deliverables:

```
           Recommendation
          /       |           Argument 1  Arg 2   Arg 3
    /   |   Data  Data  Data
```

**Rules:**
1. Start with the answer/recommendation (BLUF)
2. Group supporting arguments logically (3-5 max)
3. Each argument supported by evidence
4. Arguments at same level must be MECE
5. Each level answers "why?" or "how?" from the level above

### 80/20 Rule (Pareto Principle)

- 80% of the value comes from 20% of the analysis
- Focus on the vital few, not the trivial many
- In consulting: identify the 2-3 analyses that will confirm or kill the hypothesis
- Avoid "boiling the ocean" (analyzing everything)

---

## Engagement Lifecycle

### Consulting Project Phases

| Phase | Duration | Key Activities | Deliverable |
|-------|----------|---------------|-------------|
| **Scoping** | Week 1 | Problem definition, stakeholder mapping, data inventory | Scope document + workplan |
| **Diagnostic** | Weeks 2-3 | Data collection, interviews, analysis | Hypothesis validation |
| **Design** | Weeks 3-4 | Solution development, option evaluation | Options with recommendation |
| **Delivery** | Week 5-6 | Presentation, implementation roadmap | Final deck + action plan |

### Stakeholder Management in Consulting

| Stakeholder Type | Engagement Approach |
|-----------------|-------------------|
| **Sponsor** (decision maker) | Weekly updates, manage expectations, align on scope |
| **Champion** (internal advocate) | Regular check-ins, co-create solutions, build ownership |
| **Subject Matter Expert** | Structured interviews, validate findings, peer review |
| **Resistor** | Understand concerns, involve early, address objections with data |

---

## Data Platform Architecture (Questrade-Specific)

### Migration Strategy (5 Phases)

1. **Phase 1A:** Move long-running/problematic reports to Databricks Gold.Legacy Schema
2. **Phase 1B:** Keep well-running reports in EDW, begin parallel Databricks setup
3. **Phase 2:** Move upstream, start removing EDW dependency
4. **Phase 3:** Refactor into true semantic layer (Gold.Medallion Schema)
5. **Phase 4:** EDW decommission, fully migrated to Databricks
6. **Phase 5:** Gold.Legacy decommission, fully on Gold.Medallion

### Domain Architecture

| Domain Type | Description | Owner |
|------------|-------------|-------|
| **Business Capability Domain** | Produced by SW Engineering Squads (microservice architecture) | Engineering |
| **Data Domain** | Enterprise data model combining sources across journeys (e.g., Account, Customer) | Data Engineering |
| **Department Domain** | Datamarts/data products built for specific department needs | Data Engineering + Business |

### PaaS Governance Challenge
Service name-based access provisioning is not scalable for cross-domain data exploration. AD Group-based access provides a better governance model. (Cross-ref: access-management.md for current approach.)

---

## Consulting Economics and Career

### Firm Tiers

| Tier | Firms | Characteristics |
|------|-------|----------------|
| **MBB** | McKinsey, BCG, Bain | Strategy focus, highest prestige, $200K+ starting |
| **Big 4** | Deloitte, PwC, EY, KPMG | Broad services, larger teams, industry depth |
| **Boutique** | Specialized firms | Deep domain expertise, smaller teams, flexible |
| **Internal** | Corporate strategy teams | Organizational knowledge, career stability, lower comp |

### Consulting Pricing Models

| Model | How It Works | Best For |
|-------|-------------|----------|
| **Time & Materials** | Hourly/daily rates x time spent | Uncertain scope, exploratory work |
| **Fixed Fee** | Set price for defined deliverable | Well-scoped projects |
| **Retainer** | Monthly fee for ongoing advisory | Long-term relationships |
| **Value-Based** | Fee tied to outcomes achieved | High-confidence, measurable impact |

---

## Cross-Domain Connections

| Related SKILL | Connection Point |
|---------------|-----------------|
| **Critical Thinking** | IDEALS method, hypothesis testing, logical structure |
| **Business Strategy** | Porter's Five Forces, VRIN, competitive positioning |
| **Operations Management** | Process analysis, bottleneck identification |
| **Presentations** | Pyramid Principle, executive communication |
| **Databricks** | Data platform architecture, Medallion schema |
| **DataWizards** | Domain-driven design, team structure |
| **MIS** | Digital transformation strategy, IT/IS alignment |

---

## When to Use This SKILL

| Real-World Task | Relevant Section |
|----------------|-----------------|
| Structure a complex problem | MECE + Issue Trees |
| Approach an ambiguous analysis | Hypothesis-Driven Problem Solving |
| Write a consulting-style recommendation | Pyramid Principle |
| Plan a data platform migration | 5-Phase Migration Strategy |
| Design data domain architecture | Domain Architecture definitions |
| Prioritize what to analyze | 80/20 Rule |
| Manage a consulting engagement | Engagement Lifecycle |
| Communicate findings to executives | Pyramid Principle + Presentations SKILL |

---

*Cross-references: [Critical-Thinking.SKILL.md](./Critical-Thinking.SKILL.md) for IDEALS method, [Business-Strategy.SKILL.md](./Business-Strategy.SKILL.md) for competitive analysis, [Effective-Management-Presentations.SKILL.md](./Effective-Management-Presentations.SKILL.md) for communication structure*
