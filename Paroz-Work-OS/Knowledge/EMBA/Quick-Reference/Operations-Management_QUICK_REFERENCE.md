# Operations Management — QUICK REFERENCE
## Cornell EMBA (NCCB 5080 / MBQC 941) | Prof. Yao Cui

---

## Core Formulas

```
Little's Law:         I = R × T  (Inventory = Throughput Rate × Flow Time)
Days of Inventory:    Inventory / (COGS/365)
Inventory Turns:      COGS / Inventory

VUT (single server):  Tq = [(CVa² + CVp²)/2] × [u/(1-u)] × p
Utilization:          u = p / (m × a)
CV:                   CV = σ / μ

Newsvendor:           SL* = Cu / (Cu + Co)
EOQ:                  Q* = √(2DS / H)
ROP:                  ROP = d×L + z×σd×√L
```

---

## Module Map (Quick Lookup)

| # | Module | Key Tool |
|---|--------|----------|
| 1 | Process Analysis | Flow diagrams, bottleneck, capacity |
| 2 | Capacity Planning | Little's Law, LP (Solver), inventory buildup |
| 3 | Waiting Time Mgmt | VUT equation, variability, utilization |
| 4 | Inventory Mgmt | Newsvendor (single-period), EOQ/ROP (multi-period) |
| 5 | Lean Operations | 7 wastes, JIT, 5 Whys, TPS |
| 6 | Supply Chain | Beer Game, bullwhip effect |

---

## Process Analysis Steps

1. Draw process flow diagram (□ activities, △ buffers, → flow)
2. Identify bottleneck (lowest capacity step)
3. Calculate: Flow Time, Capacity, Throughput Rate, Utilization

---

## VUT Quick Guide

**Three levers to reduce waiting:**

| Lever | How | Example |
|-------|-----|---------|
| **V** (Variability) | Reduce CVa or CVp | Appointment scheduling, standardize service |
| **U** (Utilization) | Add capacity or reduce demand | Add servers, cross-train workers |
| **T** (Service time) | Speed up processing | Automation, process redesign |

**Critical:** As u → 1, wait time → ∞. Keep u well below 1 in variable systems.

---

## Newsvendor Quick Guide

```
Cu = underage cost (lost margin per unit of unmet demand)
Co = overage cost (loss per unsold unit)
SL* = Cu / (Cu + Co)
Order Q* where P(Demand ≤ Q*) = SL*
```

---

## EOQ Quick Guide

```
Q* = √(2DS/H)       S = order cost, D = demand rate, H = holding cost
TC = (Q/2)H + (D/Q)S + CD
```

**Robust:** If demand doubles, EOQ up only ~41%. Flat cost curve near optimum.

---

## Seven Wastes (Muda)

1. Overproduction
2. Excess Inventory
3. Waiting
4. Overprocessing
5. Unnecessary Motion
6. Unnecessary Transport
7. Defects/Rework

**Lean Cycle:** Identify Waste → Root Cause (5 Whys) → Remove Sustainably → Repeat

---

## OM Triangle

```
     Inventory
    /         \
Capacity --- Information
```

Three interchangeable buffers against uncertainty.

---

## Order Winners

| Dimension | Capability | Example |
|-----------|-----------|---------|
| Price | Low cost | Walmart |
| Quality | High quality | Toyota |
| Time | Speed | Amazon |
| Flexibility | Variety/customization | Dell |

---

## Key Cases

| Case | Core Concept |
|------|-------------|
| Kristen's Cookie | Process flow, bottleneck, batch sizing |
| National Cranberry | Inventory buildup, seasonal capacity |
| Mihocko Inc. | LP with tightening emission constraints |
| Manzana Insurance | Service waiting times, priority rules |
| Beer Game | Bullwhip effect, supply chain coordination |
| TPS Reading | Lean principles, 7 wastes, JIT |

---

## Key Excel Calculators

| Calculator | Use |
|-----------|-----|
| VUT_Calculator.xlsx | Waiting time analysis |
| Newsvendor_Calculator.xlsm | Single-period inventory optimization |
| EOQ_ROP_Calculator.xlsx | Multi-period inventory policy |

**Folder:** `Smith Cornell EMBA Classes/Operations Management/`
**SKILL File:** `EMBA-Code-Reference/context/Operations-Management.SKILL.md`
