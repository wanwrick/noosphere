# Managerial Accounting — SKILL Reference
## Cornell EMBA (NBAB 5020 / MBQC 812) | Dr. Danny Szpiro | Summer 2025

---

## Course Architecture

**5-topic structure** covering the full managerial accounting toolkit:

| Topic | Title | Core Concept |
|-------|-------|-------------|
| 1 | Introduction to Management Accounting | Cost fundamentals, allocation, job-order costing |
| 2 | Cost Management | Departmental costing, ABC/ABM, target costing |
| 3 | Cost Behavior | CVP analysis, operating leverage, quality costs |
| 4 | Planning & Analysis | Standard costing, variance analysis, flexible budgeting |
| 5 | Relevant Costs for Decision-Making | Make/buy, keep/drop, capital budgeting, EVA |

**Textbook:** Hilton & Platt, *Managerial Accounting* (selected chapters 2–17)

**Cases:** Flamerock Tire (ABC), Ithaca Airlines (CVP/DOL), Kirkland Instrumentation (transfer pricing), Martinson Imaging (capital budgeting), Moore Golf Balls (product mix)

**Grading:** Team Assignments + Final Deliverable (Kirkland Instrumentation transfer pricing case)

---

## The Big Picture: Three Pillars

Management accounting serves three interconnected functions:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  MEASUREMENT │ ──→ │   DECISION   │ ──→ │   CONTROL    │
│              │     │   MAKING     │     │              │
│ What does it │     │ Can/should   │     │ Did we meet  │
│ cost?        │     │ we do this?  │     │ our targets? │
└──────────────┘     └──────────────┘     └──────────────┘
```

**Financial vs Managerial Accounting:**

| Financial Accounting | Managerial Accounting |
|---------------------|----------------------|
| Entire entity (consolidated) | Pieces of the entity (disaggregated) |
| External focus | Internal focus |
| Designed to meet GAAP | Contingent design |
| Stewardship (historical) | Planning & decision-making (future) |
| **RULES** | **TOOLS** |

---

## Topic 1: Cost Fundamentals & Job-Order Costing

### Core Cost Taxonomy

Every cost can be classified on two independent dimensions:

| | Direct | Indirect |
|---|---|---|
| **Variable** | DM, DL (piece-rate) | Variable OH |
| **Fixed** | Dedicated equipment | Rent, insurance, salary |

**Key Definitions:**
- **Cost object**: The item being costed (product, service, project, department, customer)
- **Direct costs**: Costs obviously traceable to a single cost object
- **Indirect costs (overhead)**: Costs incurred for multiple cost objects — require allocation
- **Relevant range**: Volume range over which cost behavior assumptions hold

### Cost Categories
- **Total Cost** = Direct Material + Direct Labor + Overhead
- **Prime Cost** = DM + DL
- **Conversion Cost** = DL + OH
- **Product cost** (inventoriable) vs. **Period cost** (expensed immediately)
- **Opportunity costs**: Value of next-best alternative forgone
- **Sunk costs**: Already incurred, irrelevant for future decisions
- **Differential (incremental) costs**: Costs that change between alternatives

### Overhead Allocation Process (7 Steps)
1. Identify the cost object
2. Identify direct costs for the cost object
3. Identify indirect costs associated with the cost object
4. Select allocation base for each indirect cost pool
5. Compute the overhead rate (POHR)
6. Apply the overhead rate to the cost object
7. Determine full cost = direct costs + allocated overhead

**Predetermined Overhead Rate (POHR):**

$$POHR = \frac{\text{Estimated Total Manufacturing OH}}{\text{Estimated Total Units in Allocation Base}}$$

**Total OH estimation:** Y = a + bX
- Y = estimated total manufacturing OH
- a = estimated total fixed manufacturing OH
- b = estimated variable OH per unit of allocation base
- X = estimated total amount of allocation base

---

## Topic 2: Cost Management — Refining the Costing Process

### Two Refinement Steps
1. **Increase direct cost tracing** — reclassify costs from indirect to direct where possible
2. **Separate indirect cost pools** — use multiple cost pools with unique POHRs instead of one plantwide rate

### Departmental Costing
Service department costs must be allocated to production departments before being attached to products:

- **Direct Method**: Allocate service dept costs directly to production depts (ignores inter-service interactions)
- **Step-Down Method**: Allocate in preset order, recognizing work done among departments (more accurate)

### Joint Costing
When a single process produces multiple products (joint products + byproducts):
- Joint costs can be allocated based on: sales value, physical units, NRV
- Key decision: allocate to byproducts or not? (Three approaches shown in course)

### Activity-Based Costing (ABC)

ABC replaces arbitrary volume-based allocation with cause-and-effect activity drivers.

**Process:**
1. Identify activities that consume overhead resources
2. Assign overhead costs to activity cost pools
3. Identify cost drivers for each activity
4. Calculate activity rates = Activity Cost Pool / Cost Driver Quantity
5. Apply activity rates to products based on actual driver consumption

**Why ABC matters:** Traditional plantwide allocation often cross-subsidizes products. High-volume products subsidize low-volume, complex products — hiding true profitability.

### Flamerock Tire Case — ABC Revelation

| Product | Traditional ROS | ABC ROS |
|---------|----------------|---------|
| Snow | 13.3% | **21.6%** |
| Summer | 13.3% | **22.7%** |
| 4-Season | 14.8% | **(44.0%)** |
| High Performance | 18.2% | **(200.1%)** |

**Key insight:** Under traditional costing, all products appeared profitable. ABC revealed that 4S and HP were massively unprofitable — complexity costs (production runs, setups, parts administration) were being subsidized by high-volume Snow and Summer tires.

### Activity-Based Management (ABM)
Using ABC information for decision-making:
- Eliminate or reprice unprofitable products
- Reduce complexity and batch costs
- Focus on value-adding activities
- Redesign processes to reduce cost driver consumption

### Target Costing
Working backward from market price:
**Target Cost = Target Selling Price − Target Profit**

---

## Topic 3: Cost Behavior — CVP Analysis & Quality Costs

### Cost Behavior
- **Fixed costs**: Total constant within relevant range; per-unit cost decreases as volume increases
- **Variable costs**: Total varies proportionally with volume; per-unit cost remains constant
- **Mixed costs**: Contain both fixed and variable components (Y = a + bX)

### Cost-Volume-Profit (CVP) Analysis

**The Contribution Margin Model:**

```
Revenue − Variable Costs = Contribution Margin
Contribution Margin − Fixed Costs = Profit
```

**Key Formulas:**

$$\text{Break-Even (units)} = \frac{\text{Fixed Costs}}{\text{CM per unit}}$$

$$\text{Break-Even (dollars)} = \frac{\text{Fixed Costs}}{\text{CM\%}}$$

$$\text{Units for Target Profit} = \frac{\text{Fixed Costs + Target Profit}}{\text{CM per unit}}$$

$$\text{CM\%} = \frac{\text{Unit Price} - \text{Unit Variable Cost}}{\text{Unit Price}}$$

### Degree of Operating Leverage (DOL)

$$DOL = \frac{\text{Total Contribution Margin}}{\text{EBIT}}$$

**Interpretation:** A DOL of 4 means a 20% increase in sales produces an 80% increase in EBIT (and vice versa for decreases).

| | High Operating Leverage | Low Operating Leverage |
|---|---|---|
| Cost structure | High fixed, low variable | Low fixed, high variable |
| Risk profile | High risk, high reward | Low risk, low reward |
| Break-even | Higher | Lower |
| Profit sensitivity | Amplified swings | Moderate swings |

### Ithaca Airlines Case
Demonstrates DOL in practice — Scheduled Carrier (committed flights = high fixed costs = high DOL) vs. Charter Airline (fly only when chartered = lower fixed costs = lower DOL). Same total profit at full capacity, but vastly different risk profiles.

### Costs of Quality — Four Categories

| | Control Costs | Failure Costs |
|---|---|---|
| **Before delivery** | **Prevention**: quality engineering, training, audits, design reviews | **Internal Failure**: scrap, rework, downtime, re-inspection |
| **After delivery** | **Appraisal**: inspections, testing, supplier verification | **External Failure**: returns, warranties, lost sales, liability |

**Two Views:**
- **Traditional (AQL)**: Acceptable Quality Level — there's an optimal defect rate balancing control and failure costs (diminishing returns)
- **Total Quality Control (TQC)**: Zero defects IS achievable — increased prevention reduces all other costs; overall quality costs decrease. Target: total quality costs ≤ 2.5% of sales

**ABC + TQC Integration:** Use ABC to identify control activities to enhance and failure activities to eliminate.

---

## Topic 4: Planning & Analysis — Standard Costing & Flexible Budgeting

### Standard Costing
Predetermined costs for standard products/services — enables planning, performance evaluation, and management by exception.

**Setting standards for direct inputs:**
- Standard direct labor hours (SH) and rate (SR)
- Standard direct material quantity (SQ) and price (SP)
- Involve cross-functional stakeholders: designers, production, purchasing, HR, accounting

**Levels:** Ideal (theoretical maximum) → Practical (attainable with effort) → Short-term stretch

### Stretch Goals Framework (Szpiro/Kerr)

| | Lower Evaluation Risk | Higher Evaluation Risk |
|---|---|---|
| **Stretch Goals** | **Breakthroughs** ✓ (encourages calculated risk, innovation) | **Budget Game** (elaborate gaming, slack creation) |
| **Low Goals** | **Play it Safe** (minimal progress) | **Lose-Lose** (no innovation + punitive) |

**Kerr's Two Rules for Stretch Goals:**
1. **Do not punish failure**
2. Give people tools and help; make stretch supplemental to base targets; share the wealth from achieved stretch goals

### Variance Analysis — Direct Costs

**Core Decomposition:**

$$\text{Total Variance} = (\text{AP} \times \text{AQ}) - (\text{SP} \times \text{SQ})$$

**Price Variance** = AQ × (AP − SP)
- Materials: Materials Price Variance (MPV) → purchasing responsibility
- Labor: Labor Rate Variance (LRV) → labor market / mix changes

**Quantity (Efficiency) Variance** = SP × (AQ − SQ)
- Materials: Materials Quantity Variance (MQV) → production responsibility
- Labor: Labor Efficiency Variance (LEV) → production manager decisions

**Important:** Unfavorable ≠ "bad" and Favorable ≠ "good" — requires careful analysis of root causes.

### Flexible Budgeting

Static budgets present one activity level. Flexible budgets adjust for actual volume, separating volume effects from operational performance:

```
Static Budget → Sales Volume Variance → Flexible Budget → Flexible Budget Variance → Actual Results
```

**Full Variance Decomposition Tree:**

```
Static Budget Variance
├── Sales Volume Variance
│   ├── Market Size Variance
│   └── Market Share Variance
└── Flexible Budget Variance
    ├── Selling Price Variance
    ├── Direct Costs
    │   ├── Price Variance
    │   └── Quantity Variance
    ├── Variable Overhead
    │   ├── Spending Variance
    │   └── Efficiency Variance
    └── Fixed Overhead
        ├── Spending Variance
        └── Volume Variance
```

---

## Topic 5: Relevant Costs & Capital Budgeting

### Relevant Cost Framework
**Relevant costs**: Future costs that **differ** across alternatives. Both conditions must be true.

**Irrelevant costs:** Sunk costs (past) or future costs that don't differ across alternatives.

### Relevant Cost Decision Model
1. Recognize and define the problem
2. Identify feasible alternatives
3. Identify relevant costs for each alternative
4. Gather data on alternatives using similar periodic basis
5. Compare costs of alternatives
6. Assess qualitative factors (customer relations, supplier dependability, strategic capability, workforce)
7. Select alternative with greatest benefit

### Decision Types

**Make vs. Buy:**
- Compare incremental cost of making vs. purchase price
- Exclude allocated common fixed costs (they don't change)
- Consider: quality control, supply reliability, capacity utilization, strategic capability

**Keep vs. Drop (Product Line):**
- Drop if: product's CM < direct fixed costs saved by dropping
- Never allocate common fixed costs — they continue regardless
- Consider substitution effects between product lines

**Special Order:**
- Accept if: price > incremental cost AND sufficient excess capacity
- Never include allocated fixed costs in the analysis

**Product Mix (Constrained Resources):**
- Maximize CM per unit of the scarce resource (not CM per product unit)
- Rank products by CM per constraint unit; fill demand in rank order

### Capital Budgeting

**The Organization as a "Treasure Chest":**
- Organization = collection of projects funded by capital (debt + equity)
- Management responsibility: operate projects to create returns exceeding cost of capital
- NPV > 0 → treasure chest grows → shareholder value created

| Metric | Decision Rule |
|--------|--------------|
| NPV | Accept if NPV > 0 |
| IRR | Accept if IRR > discount rate |
| Payback | Accept if payback < threshold |
| Profitability Index | PV of future cash flows / Initial Investment |
| Accounting Rate of Return | Average Annual NIAT / Initial Investment |

**Key Application Principles:**
- Focus on relevant, after-tax cash flows
- Risk-adjust discount rates by project (don't use single WACC for all projects)
- Beware the **status quo fallacy**: competitors won't stand still if you don't invest
- Include initial investment, operating cash flows, and terminal cash flows

### Economic Value Added (EVA)

$$EVA = NOPAT - (\text{Capital Employed} \times WACC)$$

- Adjusts Net Income to NOPAT (removes GAAP distortions)
- Includes charge for equity capital (unlike traditional accounting)
- Positive EVA = value creation; Negative EVA = value destruction
- NPV of a project = PV of all future EVAs from that project

### Capital Budgeting Control Phases

| Timing | Control Type | Focus | Key Question |
|--------|-------------|-------|-------------|
| Past | Compliance Controls | Rules, boundaries, error avoidance | Did we spend what we budgeted? |
| Present | Operational Controls | Efficiency & effectiveness | Have we met targeted benefits? |
| Future | Strategic Controls | Learning, re-evaluation | What will improve future decisions? |

### Transfer Pricing (Final Deliverable — Kirkland Instrumentation)

**Context:** KII's Dollard Division (Indianapolis) manufactures MFI instruments. Roxboro Division (LA) wants to source MFI internally instead of importing from Taiwan.

**Key Transfer Pricing Principles:**
- **Minimum transfer price (seller):** Incremental cost + opportunity cost of lost external sales
- **Maximum transfer price (buyer):** Lower of external purchase price or value derived from internal use
- **Corporate perspective:** Transfer creates value if seller's incremental cost < buyer's savings

**Qualitative factors:** Supply reliability, corporate integration benefits, strategic capability, relationship building, capacity utilization

---

## Paroz's Applied Context

### Final Deliverable: Kirkland Instrumentation Transfer Pricing
Applied relevant cost analysis, transfer pricing principles, and qualitative assessment to determine:
- Corporate profitability impact of internal sourcing
- Minimum/maximum transfer price bounds
- Non-financial strategic factors (supply chain security, corporate integration, division autonomy)

### DataWizards Team — Flexible Budgeting Application
Applied flexible budgeting concepts to DataWizards team operations at Questrade, using variance analysis to understand performance deviations from plan and separate volume effects (scope changes) from operational efficiency (delivery performance).

### ABC Thinking in Data Platform Evaluation
Applied ABC logic to the Databricks vs GCP platform evaluation — identifying true cost drivers (data volume, pipeline complexity, governance overhead, team productivity) rather than using simplistic per-license or per-compute cost comparisons.

---

## When to Use This Skill

| Situation | Relevant Frameworks |
|-----------|--------------------|
| Product costing & profitability | Cost taxonomy, POHR, ABC, departmental costing |
| Make vs. buy decisions | Relevant costs, incremental analysis |
| Product line decisions | Keep/drop analysis, CM analysis |
| Pricing decisions | CVP, target costing, contribution margin |
| Risk assessment | Operating leverage, DOL, CVP sensitivity |
| Budgeting & planning | Standard costing, flexible budgeting, variance analysis |
| Performance evaluation | Variance analysis, EVA, flexible budget variance |
| Investment decisions | NPV, IRR, payback, risk-adjusted rates |
| Quality management | Four quality cost categories, TQC vs AQL |
| Transfer pricing / divisional | Min/max transfer price, corporate vs division perspective |
| Case interviews (MBB) | CVP, relevant costs, ABC, capital budgeting, EVA |
| Team goal-setting | Stretch goals framework, Kerr's rules |

---

## Key References

- Hilton, R.W. & Platt, D.E. *Managerial Accounting: Creating Value in a Dynamic Business Environment*. McGraw-Hill. (Chapters 2–17)
- Szpiro, D. Course materials, NBAB 5020, Cornell Johnson EMBA, Summer 2025.
- Case studies: Flamerock Tire, Ithaca Airlines, Kirkland Instrumentation, Martinson Imaging, Moore Golf Balls

---
*Created: February 5, 2026*
*Course: NBAB 5020 / MBQC 812 — Management Accounting (Dr. Danny Szpiro, Cornell, Summer 2025)*
