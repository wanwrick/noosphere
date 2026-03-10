# Operations Management -- Knowledge Base

> Covers process analysis, capacity planning, queueing theory, inventory management, and lean systems.

---

## 1. Process Analysis

### Key Definitions
- **Flow Rate (Throughput):** Units processed per time period
- **Flow Time:** Total time a unit spends in the system
- **Inventory (WIP):** Number of units in the system at any point

### Little's Law
```
Inventory = Flow Rate × Flow Time
    I     =    R     ×    T
```
The most fundamental operations equation. Always holds in steady state. Useful for diagnosing bottlenecks and estimating any one variable from the other two.

**Example:** If your data pipeline processes 100 records/min (R) and records spend 5 minutes in the system (T), then average WIP = 500 records.

### Bottleneck Analysis
- **Bottleneck:** The resource with the lowest capacity (highest utilization)
- **Process Capacity:** Determined by the bottleneck
- **To increase throughput:** Improve the bottleneck (everything else is waste)
- **Capacity = 1 / Processing Time** per resource

### Process Flow Diagrams
```
[Input] → [Activity 1] → [Activity 2] → [Activity 3] → [Output]
              ↓                              ↑
          [Buffer]                      [Rework Loop]
```

Map every step. Identify value-added vs. non-value-added. Time each step. Find the bottleneck.

---

## 2. Capacity Planning

### Utilization
```
Utilization = Flow Rate / Capacity
```
- Target: 70-85% for most systems
- Above 85%: Queue times increase exponentially
- At 100%: Infinite queues (in theory)

### Capacity Strategies
- **Lead Strategy:** Build capacity before demand (risk: idle capacity)
- **Lag Strategy:** Build capacity after demand materializes (risk: lost sales)
- **Match Strategy:** Incrementally add capacity as demand grows

### Implied Utilization
```
Implied Utilization = Demand / Capacity
```
If > 100%, the resource is a bottleneck. Prioritize investment here.

---

## 3. Queueing Theory

### VUT Equation
Predicts average waiting time in a queue:
```
Wait Time ≈ (V × U × T)

Where:
V = Variability factor = (CVa² + CVs²) / 2
U = Utilization factor = ρ / (1 - ρ)    [ρ = utilization]
T = Average service time
```

**Key insight:** Wait time is driven by three levers:
1. **Variability (V):** Reduce variation in arrivals and service times
2. **Utilization (U):** Don't run at 100%; leave buffer capacity
3. **Service Time (T):** Speed up the process

**The utilization curve:** Wait time increases exponentially as utilization approaches 100%. The jump from 80% to 90% is much worse than 70% to 80%.

### Reducing Wait Times
| Lever | Actions |
|-------|---------|
| Reduce Variability | Standardize processes, appointments, batch sizes |
| Reduce Utilization | Add capacity, cross-train, flexible resources |
| Reduce Service Time | Automation, eliminate waste, parallel processing |
| Pool Resources | Combine separate queues into one (pooling effect) |

---

## 4. Inventory Management

### Types of Inventory
- **Raw Materials:** Inputs waiting to be processed
- **Work-in-Process (WIP):** Partially completed units
- **Finished Goods:** Completed, awaiting sale/delivery
- **Safety Stock:** Buffer against demand/supply variability

### Economic Order Quantity (EOQ)
```
EOQ = √(2DS / H)

Where:
D = Annual demand
S = Fixed cost per order
H = Holding cost per unit per year
```

Trade-off: Ordering frequently (high S costs) vs. holding large inventory (high H costs).

### Reorder Point
```
ROP = (Average Daily Demand × Lead Time) + Safety Stock
Safety Stock = z × σ_demand × √(Lead Time)
```
Where z = service level factor (e.g., z=1.65 for 95% service level).

### Newsvendor Model (Single-Period Inventory)
For perishable or one-time decisions:
```
Critical Ratio = Cu / (Cu + Co)

Cu = Cost of underestimating (underage cost)
Co = Cost of overestimating (overage cost)

Order Quantity: Q* where P(Demand ≤ Q*) = Critical Ratio
```

**Application:** How many units to produce/order when you can't restock.

### Bullwhip Effect
Demand variability amplifies as you move upstream in the supply chain.

**Causes:**
1. Demand signal processing (each stage forecasts independently)
2. Order batching (periodic ordering creates lumpy demand)
3. Price fluctuations (forward buying during promotions)
4. Rationing and shortage gaming (over-ordering when supply is tight)

**Remedies:**
- Share demand information across the supply chain
- Reduce order batch sizes
- Stabilize pricing (EDLP over promotions)
- Allocate based on past sales, not orders

---

## 5. Lean Systems & Toyota Production System (TPS)

### Core Lean Principles
1. **Specify Value:** Define value from customer's perspective
2. **Map the Value Stream:** Identify all steps, eliminate non-value-added
3. **Create Flow:** Make value-creating steps flow without interruption
4. **Establish Pull:** Produce only what customer demands
5. **Pursue Perfection:** Continuous improvement (Kaizen)

### Seven Wastes (Muda)
| Waste | Description | Example (data platform; replace with your domain) |
|-------|-------------|----------------------|
| **Transport** | Unnecessary movement of materials | Data copying between systems |
| **Inventory** | Excess stock/WIP | Backlog of unprocessed data |
| **Motion** | Unnecessary movement of people | Context switching between tools |
| **Waiting** | Idle time between process steps | Pipeline waiting for upstream data |
| **Overproduction** | Making more than needed | Building reports nobody uses |
| **Over-processing** | More work than required | Cleaning data that's never queried |
| **Defects** | Errors requiring rework | Data quality issues caught downstream |

### Key TPS Tools
- **Just-in-Time (JIT):** Produce only what's needed, when needed, in the amount needed
- **Jidoka (Autonomation):** Stop the line when a defect is detected
- **Kanban:** Visual signals to control production flow
- **Poka-Yoke:** Error-proofing mechanisms
- **5S:** Sort, Set in order, Shine, Standardize, Sustain
- **Andon:** Visual management system for status/alerts
- **Gemba:** Go to the actual place where work happens

### Kaizen (Continuous Improvement)
```
Plan → Do → Check → Act (PDCA Cycle)
```
- Small, incremental improvements
- Everyone participates (not just management)
- Focus on process, not blame
- Standardize successful improvements

---

## Quick Reference: When to Use What

| Situation | Framework | Section |
|-----------|-----------|---------|
| "Where's our bottleneck?" | Process analysis, capacity | Process Analysis |
| "Why is the queue so long?" | VUT equation, utilization curve | Queueing Theory |
| "How much inventory to hold?" | EOQ, ROP, newsvendor | Inventory Management |
| "How to estimate throughput?" | Little's Law | Process Analysis |
| "How to reduce waste?" | Seven Wastes, 5S, Value Stream | Lean/TPS |
| "Pipeline is slow" | Bottleneck analysis, VUT | Process + Queueing |
| "How to plan capacity?" | Utilization targets, lead/lag/match | Capacity Planning |
| "Why is variability so bad?" | Bullwhip, VUT variability factor | Queueing + Inventory |

### Applying Operations to Data Engineering
Little's Law applies directly to data pipelines:
- I = records in pipeline, R = throughput, T = latency
- Bottleneck analysis → find the slowest DAG step
- VUT equation → why batch jobs queue up during peak hours
- Lean/waste → eliminate unused tables, redundant transformations
- Kanban → backlog management for sprint planning
- Kaizen → retrospective-driven improvements each sprint
