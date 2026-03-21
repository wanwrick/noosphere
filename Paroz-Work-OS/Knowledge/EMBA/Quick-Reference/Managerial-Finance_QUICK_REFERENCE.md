# Managerial Finance — QUICK REFERENCE
## Cornell EMBA (NCCB 5060 / MBQCB821) | Professor Mao Ye | Spring 2025

---

## Core Formulas

```
FV = PV × (1+r)^n                    Future Value
PV = FV / (1+r)^n                    Present Value
PV(annuity) = C × [1 − (1+r)^−n] / r   Annuity PV
PV(perpetuity) = C / r               Perpetuity
PV(growing perp) = C / (r − g)       Growing Perpetuity
NPV = Σ [CFt / (1+r)^t]             Net Present Value

E(rᵢ) = rf + βᵢ × [E(rM) − rf]      CAPM
WACC = (E/V)×rE + (D/V)×rD×(1−T)    Weighted Avg Cost of Capital
βᵢ = Cov(rᵢ, rM) / σ²M              Beta

Enterprise Value = Σ [FCFt/(1+WACC)^t] + TV/(1+WACC)^n
Terminal Value = FCF(n+1) / (WACC − g)   Gordon Growth Model
Equity Value = Enterprise Value − Net Debt
```

---

## Topic Map (Quick Lookup)

| Session | Topic | Key Takeaway |
|---------|-------|-------------|
| 1 | TVM | Law of one price, PV/FV, annuities, perpetuities, NPV rule |
| 2 | Capital Budgeting | 9 principles of FCF forecasting, bottom-up vs top-down, incremental analysis |
| 3 | Valuation | DCF, IRR vs NPV, trading multiples, transaction multiples |
| 4 | Risk & Return | Variance, std dev, covariance, correlation, diversification |
| 5 | CAPM | Efficient frontier, CML, SML, beta, WACC |
| 6 | EMH | Weak/semi-strong/strong efficiency, anomalies, index investing |
| 7 | Integration | All concepts combined, Cornell Endowment case |

---

## Nine Principles of Cash Flow Forecasting

**Philosophical (3):** Forget sunk costs | Include opportunity costs | Include externalities

**Finance (1):** Separate investment & financing decisions

**Implementation (5):** Depreciation not cash flow (but tax shield) | Include CapEx | Include NWC changes | Use incremental CFs | Use after-tax CFs

---

## Free Cash Flow Template

```
  Revenue
− COGS
− Depreciation
− SG&A
= EBIT
− Cash Taxes on EBIT
= NOPAT
+ Depreciation (add back)
− Capital Expenditures
− Increase in Working Capital
= Free Cash Flow (FCF)
```

---

## Decision Tool Comparison

| Tool | Rule | Best For | Watch Out |
|------|------|----------|-----------|
| NPV | Accept if > 0 | Always reliable | Need discount rate |
| IRR | Accept if > cost of capital | Intuitive % return | Multiple IRRs; misleads on mutually exclusive |
| Payback | Accept if < target | Quick screening | Ignores TVM & later CFs |
| PI | Accept if > 1 | Capital rationing | Misleads on mutually exclusive |

**When NPV and IRR conflict → always follow NPV**

---

## Valuation Multiples Cheat Sheet

| Multiple | Formula | Use Case |
|----------|---------|----------|
| P/E | Price / EPS | Earnings-based comparison |
| EV/EBITDA | EV / EBITDA | Operating cash flow proxy |
| EV/Revenue | EV / Revenue | High-growth / pre-profit firms |
| P/B | Price / Book Value | Asset-heavy industries |

---

## Risk Formulas

| Measure | Formula |
|---------|---------|
| Expected Return | E(r) = Σ [p × r] |
| Variance | σ² = Σ [p × (r − E(r))²] |
| Std Deviation | σ = √(σ²) |
| Covariance | Cov = Σ [p × (r₁−E(r₁)) × (r₂−E(r₂))] |
| Correlation | ρ = Cov / (σ₁ × σ₂) |
| Portfolio Var | σ²p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov |

**Key insight:** When ρ < 1, diversification reduces risk below weighted average — the "free lunch"

---

## CAPM Components

| Component | Meaning | Typical Source |
|-----------|---------|---------------|
| rf | Risk-free rate | 10-yr Treasury yield |
| β | Sensitivity to market | Regression or comparable firms |
| E(rM)−rf | Market risk premium | Historical avg ~5-7% |
| E(rᵢ) | Required return = Cost of equity | Output of CAPM |

---

## EMH Three Forms

| Form | Info in Prices | What's Useless |
|------|---------------|---------------|
| Weak | Past prices/volume | Technical analysis |
| Semi-strong | All public info | Fundamental analysis |
| Strong | All info (public+private) | Even insider info |

**Professor Ye's advice:** Don't pick stocks — buy index funds.

---

## Excel Functions

| Function | Purpose |
|----------|---------|
| `FV(rate, nper, pmt, pv)` | Future value |
| `PV(rate, nper, pmt, fv)` | Present value |
| `PMT(rate, nper, pv, fv)` | Payment amount |
| `NPV(rate, values)` | Net present value |
| `IRR(values)` | Internal rate of return |

**Convention:** Investment = NEGATIVE, payout = POSITIVE

---

## Key Excel Models

| File | Session | Purpose |
|------|---------|---------|
| 1.2_solved.xlsx, 1.3_solved.xlsx | S1 | TVM calculations |
| Toothpaste.xlsx | S2 | Full capital budgeting model |
| Buy_vs_Make_EAC.xlsx | S2 | Make vs buy (EAC) |
| Session 3 solved.xlsx | S3 | DCF & relative valuation |
| Session 4 - Examples.xlsx | S4 | Risk/return calculations |
| Session 5.xlsx | S5 | Portfolio optimization, beta |
| Cornell Endowment Fund 2024.xlsx | S7 | Endowment allocation |
| Sample Final Exam.xlsx | Exam | Practice exam + solutions |

**Folder:** `Smith Cornell EMBA Classes/Managerial Finance/`
**SKILL File:** `EMBA-Code-Reference/context/Managerial-Finance.SKILL.md`
