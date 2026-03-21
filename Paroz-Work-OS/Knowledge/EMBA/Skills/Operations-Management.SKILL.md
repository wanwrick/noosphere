# Operations Management — SKILL Reference
## Cornell EMBA (NCCB 5080 / MBQC 941) | Professor Yao Cui | Spring/Summer 2025

---

## Course Architecture

**7-session, 6-module structure** covering the design, operation, and improvement of transformation processes:

| Session | Module | Title | Core Concept |
|---------|--------|-------|-------------|
| 1 | 1 | Process Analysis I | Process view, flow diagrams, bottleneck analysis, capacity, Kristen's Cookie |
| 2 | 1-2 | Process Analysis II & Capacity Planning I | Little's Law, inventory buildup analysis, National Cranberry |
| 3 | 2-3 | Capacity Planning II & Waiting Time I | Linear programming (product mix), VUT equation, variability |
| 4 | 3 | Waiting Time Management II | Manzana Insurance case, service operations, priority rules |
| 5 | 4 | Inventory Management I | Newsvendor model, demand uncertainty, optimal service level |
| 6 | 4-6 | Inventory Management II & Supply Chain | EOQ/ROP, Beer Game, bullwhip effect, supply chain coordination |
| 7 | 5 | Lean Operations | Toyota Production System, 7 wastes, JIT, continuous improvement |

**Course Textbook (optional):** *Matching Supply with Demand*, 5th ed., Cachon & Terwiesch

**Central Framework:** Operations Management is the management (design, operation, and improvement) of transformation processes that create value for society.

```
Inputs → Transformation Process → Outputs
(Raw materials,    (Resources:         (Goods,
 Customers)         Labor & Capital)    Services)
```

**Grading:** Group Assignments (40%) + Participation (15%) + Beer Game (5%) + Final Exam (40%)

---

## The Strategic Role of Operations

### Order Winners (Competitive Dimensions)

| Order Winner | Required Capability |
|-------------|-------------------|
| **Price** | Low cost process |
| **Quality** | High quality process |
| **Time** | Fast process |
| **Flexibility** | Flexible process |

### Strategic Framework for Operations

```
Business Strategy ←→ Compatible? ←→ Desired Capabilities
                                          ↓
                    Processes ← Operations Structure → Resources
```

**Key Insight:** Operations structures must be compatible with corporate strategy. A company's operations function is either a competitive weapon or a corporate millstone — it is seldom neutral.

---

## Module 1: Process Analysis

### Process Flow Diagrams

| Element | Symbol | Meaning |
|---------|--------|---------|
| Activity/Task | □ (box) | Adds value to flow unit |
| Buffer/WIP | △ (triangle) | Waiting; does NOT add value |
| Arrow | → | Direction of flow |
| Flow Unit | — | What is being transformed (customer, product, order) |

### Key Process Measures

| Measure | Definition |
|---------|-----------|
| **Flow Time** | Time required to go through the whole process |
| **Capacity** | Maximum possible output rate |
| **Throughput Rate** | Actual output rate |
| **Bottleneck** | Resource(s) that determine the capacity of the whole process — the "slowest" resource |
| **Utilization** | Throughput Rate / Capacity |

### Bottleneck Analysis (2 Steps)

1. **Draw process flow diagram** — Define flow unit, activities, sequence, resources, buffers
2. **Identify bottleneck** — Determine capacity of each activity; bottleneck = lowest capacity step

### Little's Law

```
Inventory = Throughput Rate × Flow Time
    I     =       R        ×      T
```

| Variant | Formula | Application |
|---------|---------|------------|
| Find Inventory | I = R × T | Insurance company: claims in system |
| Find Throughput | R = I / T | Hospital: patient admissions |
| Find Flow Time | T = I / R | Days of inventory |

### Inventory Metrics

```
Days of Inventory = Inventory / COGS (daily)
Inventory Turns = COGS / Inventory
```

**Cross-functional effects:**
- **Inventory** → Balance sheet (working capital)
- **Throughput Rate** → Income statement (revenue generation)
- **Flow Time** → Responsiveness (lead time)

### Inventory Buildup Analysis

Used when demand temporarily exceeds capacity:
- When **Demand > Capacity**: inventory builds at rate (Demand − Capacity)
- When **Demand < Capacity** with buffer: inventory depletes at rate (Capacity − Demand)
- Throughput = min(Demand, Capacity) when no buffer; = Capacity when buffer exists

### Key Case: Kristen's Cookie Company (HBS)

Core lessons: Process flow mapping, bottleneck identification, capacity planning, batch vs single-piece flow, resource utilization, cycle time analysis.

### Key Case: National Cranberry Cooperative

Core lessons: Inventory buildup diagram, seasonal capacity constraints, overtime vs investment decisions.

---

## Module 2: Capacity Planning (Linear Programming)

### LP for Product Mix Optimization

```
Maximize:  Z = Σ(profit per unit × quantity)    (Objective)
Subject to: Resource constraints (hours, materials)
            Demand constraints (min/max quantities)
            Non-negativity (xᵢ ≥ 0)
```

### Excel Solver Application

1. Set up decision variables (quantities to produce)
2. Define objective function (maximize contribution)
3. Add resource constraints
4. Solver → Simplex LP → Solve

### Shadow Price

The value of one additional unit of a constrained resource. Tells you how much the objective would improve if you had one more hour, one more unit, etc.

### Key Insight: Overhead Allocation Trap

Profitability based on arbitrary allocation of fixed overhead to products can be very misleading. Making decisions based on accounting statements without understanding operational details can lead to wrong decisions.

### Key Cases

- **Petro Refinery:** LP product mix optimization
- **ABC Pharmaceutical:** Product mix with misleading margin analysis
- **Mihocko, Inc.:** LP with emission constraints tightening over time

---

## Module 3: Waiting Time Management

### The VUT Equation

```
Average Wait Time = V × U × T

Where:
V = Variability factor = (CVa² + CVp²) / 2
U = Utilization factor = u^(√(2(m+1))−1) / (1−u)
T = Service time = p

CVa = σa / μa (coefficient of variation of interarrival times)
CVp = σp / μp (coefficient of variation of service times)
u = utilization = p / (m × a)
m = number of servers
a = mean interarrival time
p = mean processing time
```

**For single server (m=1), simplified:**
```
Tq = [(CVa² + CVp²) / 2] × [u / (1−u)] × p
```

### Key VUT Insights

1. **Variability causes congestion** — Backups happen even when average capacity exceeds average demand
2. **Utilization amplifies variability** — As u → 1, wait times explode exponentially
3. **Three levers to reduce waiting:** Reduce variability (V), reduce utilization (U), or reduce service time (T)

### Caveats

- VUT yields **long-term, steady-state** average wait time
- Only applies when **u < 1** (if u ≥ 1, system is unstable — use inventory buildup analysis)
- Assumes **infinite buffer** (for small buffers, use simulation)
- Exact when m=1 and arrivals are Poisson (CVa = 1)

### Worked VUT Example

**Problem:** A single-server workstation processes units with mean processing time p = 4 hours. Interarrival CV = 1.2, processing CV = 0.8, utilization = 88%.

```
Step 1: Variability factor
  V = (CVa² + CVp²) / 2 = (1.44 + 0.64) / 2 = 1.04

Step 2: Utilization factor (single server, m=1)
  U = u / (1−u) = 0.88 / 0.12 = 7.33

Step 3: Wait time
  Tq = V × U × T = 1.04 × 7.33 × 4 = 30.5 hours

Step 4: Apply Little's Law for total flow time
  Flow time = Tq + p = 30.5 + 4 = 34.5 hours
  Throughput rate = 1/a (where a = p/u = 4/0.88 = 4.545 hrs)
  R = 1/4.545 = 0.22 units/hour
  WIP (inventory) = R × Flow time = 0.22 × 34.5 ≈ 7.6 units
```

**Improvement scenario (reduce utilization to 80%):**
```
  U_new = 0.80 / 0.20 = 4.0
  Tq_new = 1.04 × 4.0 × 4 = 16.6 hours (46% reduction!)
  Flow time_new = 16.6 + 4 = 20.6 hours
```

**Key insight:** Dropping utilization by just 8 percentage points (88% to 80%) cuts wait time nearly in half. This illustrates the nonlinear explosion of wait times as utilization approaches 100%.

### Exponential Distribution

When interarrival times are exponentially distributed: Mean = Stdev → CV = 1 → "Poisson" arrival pattern.

### Key Cases

- **Southern Tier Regional Airport:** Waiting time analysis in service operations
- **Manzana Insurance (Fruitvale Branch):** Service operations, priority rules, turnaround time management

---

## Module 4: Inventory Management

### The Newsvendor Model (Single-Period)

For perishable or single-season products where you order once before knowing demand:

```
Optimal Service Level: SL* = Cu / (Cu + Co)

Where:
Cu = underage cost (cost of stocking too few — lost margin)
Co = overage cost (cost of stocking too many — excess cost)
```

Then find order quantity Q* such that P(Demand ≤ Q*) = SL*

### Three Principles of Forecasting

1. **Forecasts are usually wrong** — include a measure of forecast error (std dev)
2. **Aggregate forecasts are more accurate** than individual forecasts
3. **Longer horizons → less accurate** forecasts

### EOQ Model (Multi-Period)

```
EOQ = Q* = √(2DS / H)

Where:
D = Demand rate (units/year)
S = Setup/ordering cost per order ($)
H = Annual holding cost per unit ($/unit/year)
    Often H = i × C (percentage of unit cost)
```

### EOQ Total Cost

```
TC = (Q/2)×H + (D/Q)×S + C×D
     [holding] [ordering] [purchase]
```

### EOQ Key Properties

- **Robustness:** Total cost curve is flat near optimum — moderate errors in parameters don't cause large cost increases
- If demand doubles, EOQ increases by only ~41%
- If Q not revised when demand doubles, cost increase is only ~6%

### Reorder Point (ROP)

```
ROP = d × L + Safety Stock

Where:
d = average daily demand
L = lead time (days)
Safety Stock = z × σd × √L
z = z-score for desired service level
```

### Why Hold Inventory?

1. Meet predictable demand variability (seasonal)
2. Safety stock for uncertainty
3. Reduce inter-dependence of operations (decoupling)
4. Economies of scale (cycle stock)
5. Pipeline inventory (in-transit)
6. Speculative (hedge price fluctuations)

### Annual Holding Cost: 20-35% of inventory value

---

## Module 5: Lean Operations (Toyota Production System)

### TPS Goal, Assumptions, Principles

**Goal:** Eliminate Waste (Muda)

**Assumptions:**
1. Plan ≠ Need (in real-time)
2. Problems will happen

**Principles:**
1. **Just-In-Time (JIT)** — Produce what is needed, when needed, in the amount needed
2. **Make problems visible, act immediately** when they occur

### Seven Types of Waste (Muda)

| # | Waste | Description |
|---|-------|-------------|
| 1 | **Overproduction** | Producing what/when/how much is unnecessary |
| 2 | **Inventory** | More than minimum required |
| 3 | **Waiting** | Workers or products idle |
| 4 | **Overprocessing** | Steps that don't add value |
| 5 | **Motion** | More than minimum required movement |
| 6 | **Handling/Transport** | More than minimum material movement |
| 7 | **Defect Correction** | Rework, scrap, inspection |

### Three-Step Lean Cycle

1. **Identify Waste** — Categorize using 7 types
2. **Understand Root Cause** — Ask "Why?" 5 times (5 Whys), bottleneck analysis, VUT logic
3. **Remove Waste Sustainably** — Specify pathways/connections/activities, bottom-up problem solving, make problems visible, repeat

### The OM Triangle

Three interchangeable buffers against uncertainty:
```
        Inventory
       /         \
  Capacity --- Information
```

You can substitute one for another: more information (better forecasting) reduces need for inventory; more capacity reduces need for inventory.

---

## Module 6: Supply Chain Management

### Beer Game

Simulation game demonstrating supply chain dynamics:
- 4 roles: Factory → Distributor → Wholesaler → Retailer → Customer
- Orders flow upstream, product flows downstream
- Demonstrates the **Bullwhip Effect**: small demand changes at retail amplify dramatically upstream

### Bullwhip Effect Causes

1. **Demand signal processing** — Each level forecasts from orders, not actual demand
2. **Order batching** — Economies of scale cause lumpy orders
3. **Price fluctuations** — Forward buying during promotions
4. **Rationing/shortage gaming** — Over-ordering during shortages

### Mitigation Strategies

- Share demand information across supply chain
- Reduce lead times
- Reduce order batching (smaller, more frequent orders)
- Stabilize pricing (EDLP vs promotional pricing)
- Allocate based on past sales, not current orders

---

## Session-by-Session Knowledge Map

| Session | Topics | Key Frameworks | Excel Models | Key Cases |
|---------|--------|---------------|-------------|-----------|
| 1 | Process Analysis | Flow diagrams, bottleneck, capacity | Kristen's_Cookie_Gantt_Chart.xlsm | Kristen's Cookie (HBS) |
| 2 | Little's Law, Inventory Buildup | I=R×T, buildup diagrams | Petro_Refinery.xlsx | National Cranberry Cooperative |
| 3 | LP Product Mix, VUT Equation | LP (Solver), VUT, CVa/CVp | ABC_Pharmaceutical.xlsx, Mihocko_Data.xlsx, VUT_Calculator.xlsx | Mihocko Inc., Southern Tier Airport |
| 4 | Service Operations, Priority | Waiting time analysis, service design | Manzana_Data.xlsx | Manzana Insurance (Fruitvale) |
| 5 | Newsvendor Model | SL* = Cu/(Cu+Co), forecast principles | Newsvendor_Calculator.xlsm | Newsvendor problems |
| 6 | EOQ, ROP, Beer Game | EOQ formula, bullwhip effect | EOQ_ROP_Calculator.xlsx, Beer_Game_Groups.xlsx | Beer Game simulation |
| 7 | Lean Operations / TPS | 7 wastes, JIT, 5 Whys, 3-step lean cycle | Session_7_Littlefield.pdf | Toyota Production System |

---

## Excel Models & Templates

| File | Location | Purpose |
|------|----------|---------|
| Kristen's_Cookie_Gantt_Chart.xlsm | Session 1/ | Process flow timing and Gantt chart |
| Petro_Refinery.xlsx | Session 2/ | LP refinery product mix model |
| ABC_Pharmaceutical.xlsx | Session 3/ | LP pharmaceutical product mix |
| Mihocko_Data.xlsx | Session 3/ | LP with emission constraints |
| VUT_Calculator.xlsx | Session 3/ | Waiting time VUT calculations |
| Manzana_Data.xlsx | Session 4/ | Insurance service operations data |
| Newsvendor_Calculator.xlsm | Session 5/ | Newsvendor model calculator |
| EOQ_ROP_Calculator.xlsx | Session 6/ | EOQ and reorder point calculations |
| Beer_Game_Groups.xlsx | Session 6/ | Beer game supply chain simulation data |

---

## Cross-Domain Connections

| Related SKILL | Connection Point |
|--------------|-----------------|
| **Business Decision Models** | LP optimization (BDM Session 6) = Capacity Planning (OM Session 3); simulation concepts for inventory modeling |
| **Managerial Accounting** | Cost concepts (variable/fixed, overhead allocation) directly used in capacity planning and EOQ |
| **Business Strategy** | Operations strategy must be compatible with corporate strategy; competitive dimensions (P,Q,T,F) |
| **Managerial Finance** | Capital budgeting for capacity investments; NPV of process improvement projects |
| **Financial Accounting** | Inventory on balance sheet; COGS calculations; days of inventory ratio |
| **Marketing** | Demand forecasting feeds newsvendor/EOQ; service quality (waiting times) affects customer satisfaction |

---

## Paroz's Deliverables

| Deliverable | File | Content |
|------------|------|---------|
| Assignment 1 | Session 1/Assignment_1.docx | Process analysis problems |
| Assignment 2 (Manzana) | Manzana Case/ folder | Group case: Manzana Insurance waiting time analysis |
| Final Exam | (taken in class) | Comprehensive OM exam |

---

## When to Use This SKILL

| Real-World Task | Relevant Module | Key Concepts |
|----------------|----------------|-------------|
| Map and optimize a business process | M1 | Process flow diagrams, bottleneck analysis |
| Calculate throughput or inventory metrics | M1 | Little's Law (I=R×T), days of inventory |
| Optimize product mix with constraints | M2 | Linear programming, Solver, shadow prices |
| Reduce customer wait times | M3 | VUT equation, variability reduction, utilization management |
| Decide how much inventory to order (one-time) | M4 | Newsvendor model, critical ratio |
| Set up a replenishment policy | M4 | EOQ, ROP, safety stock |
| Implement lean/continuous improvement | M5 | 7 wastes, 5 Whys, JIT, TPS principles |
| Diagnose supply chain problems | M6 | Bullwhip effect, information sharing, demand visibility |
| Evaluate capacity expansion investment | M1-M2 | Bottleneck analysis + NPV of additional capacity |
| Forecast demand for planning | M4 | Three forecasting principles + newsvendor logic |
