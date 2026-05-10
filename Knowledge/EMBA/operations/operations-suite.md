# Operations Suite — Lean · Theory of Constraints · Queueing · Capacity · Six Sigma DMAIC

> Foundational operations-management frameworks. Used for process design, throughput optimization, and quality programs.

## Lean (Toyota Production System)

**Five principles** (Womack & Jones):

1. **Specify value** from the customer's perspective.
2. **Map the value stream**; eliminate waste (the 7 wastes: defects, overproduction, waiting, non-utilized talent, transport, inventory, motion, extra-processing — DOWNTIME).
3. **Create flow** — work moves continuously; minimize batch size.
4. **Pull (not push)** — produce only when downstream demand exists.
5. **Pursue perfection** — kaizen (continuous improvement) is built into the routine.

**Key tactics:** 5S workplace organization · Kanban for visual flow · Andon (stop-the-line authority) · Heijunka (production leveling).

## Theory of Constraints (Eli Goldratt — *The Goal*)

The throughput of a system is limited by its single biggest constraint. Improving anywhere **except** the constraint adds no throughput.

**Five focusing steps:**

1. **Identify** the constraint.
2. **Exploit** it (get the most out of it without adding capacity).
3. **Subordinate** everything else to the constraint.
4. **Elevate** the constraint (add capacity if exploitation isn't enough).
5. **Repeat** — once removed, a new constraint emerges. Don't let inertia set in.

**Key insight:** local efficiency improvements off-constraint are usually waste. Optimize the constraint; ignore the rest until the constraint shifts.

## Queueing — Little's Law + VUT

**Little's Law:** L = λW

- L = average number in system
- λ = arrival rate
- W = average time in system

In simple terms: WIP = throughput × cycle time. To reduce cycle time, either reduce WIP or increase throughput.

**VUT formula** (variability × utilization × time) — wait time grows non-linearly as utilization approaches 1:

```
Wait_q ≈ (V × ρ²) / (μ(1 - ρ))
```

Operating at 95% utilization sounds efficient but produces 19× the wait time of 50% utilization. The lesson: **slack capacity is feature, not bug.**

## Capacity Planning — EOQ + Safety Stock

**Economic Order Quantity:**

```
EOQ = √(2DS/H)

D = annual demand
S = setup cost per order
H = holding cost per unit per year
```

EOQ trades off ordering cost vs holding cost. Below EOQ → too many orders. Above EOQ → too much inventory.

**Safety stock** = buffer against variability in demand or lead time:

```
Safety stock = Z × σ × √L

Z = service-level multiplier (e.g., 1.65 for 95%)
σ = demand variability per period
L = lead time periods
```

## Six Sigma DMAIC

Five-phase quality-improvement methodology:

| Phase | Purpose |
|---|---|
| **D**efine | Project scope · stakeholders · CTQs (Critical To Quality) · charter |
| **M**easure | Baseline performance · MSA (Measurement System Analysis) · process capability (Cp, Cpk) |
| **A**nalyze | Root cause via 5 Whys · fishbone · Pareto · regression / hypothesis testing |
| **I**mprove | Implement changes · pilot · A/B test |
| **C**ontrol | SPC (Statistical Process Control) · monitoring · standardize · handover |

**Six Sigma target:** 3.4 defects per million opportunities. Implies process capability index Cpk ≥ 2.0.

## When to use

- **Lean** — process redesign, waste elimination, end-to-end value-stream optimization.
- **TOC** — throughput optimization with one obvious constraint.
- **Queueing** — capacity planning under variability; service-level SLAs.
- **Capacity** — inventory + supply-chain decisions.
- **DMAIC** — recurring-defect problems; quality programs; regulated processes.

## Cross-references

- `../../Frameworks/operations.md` — broader operations content (the existing frameworks file).
- `../../../ip/authored/no-lac-principle.md` — Bronze→Platinum architecture treats data pipelines as a queueing system; Little's Law + VUT apply.
- `../../../ip/curated/data-product-architecture-5-pillars.md` — Pillar 5 (Quality Framework) is DMAIC for data products.
