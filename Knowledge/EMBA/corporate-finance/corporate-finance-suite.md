# Corporate Finance Suite — WACC · NPV/IRR · Capital Structure · EVA · M&A Valuation

> Foundational corporate-finance frameworks. Used in business-case ROI work, investment decisions, and M&A diligence.

## WACC — Weighted Average Cost of Capital

The discount rate used to value a firm or project, weighted by capital-structure mix:

```
WACC = (E/V × Re) + (D/V × Rd × (1 - Tc))

E = market value of equity
D = market value of debt
V = E + D
Re = cost of equity (CAPM: Rf + β(Rm - Rf))
Rd = cost of debt (yield on outstanding debt)
Tc = corporate tax rate
```

WACC is the hurdle rate. Projects with IRR < WACC destroy value; projects with IRR > WACC create it.

## NPV / IRR / Payback

| Metric | What it tells you | When to prefer |
|---|---|---|
| **NPV** (Net Present Value) | Absolute $ value created at WACC discount rate | Default for accept/reject decisions |
| **IRR** (Internal Rate of Return) | Discount rate that makes NPV = 0 | Comparing to hurdle rate; communicating to non-finance audiences |
| **Payback Period** | Years to recover initial investment | Liquidity-constrained firms; quick screen |

```
NPV = Σ [CF_t / (1 + WACC)^t] − Initial Investment
```

NPV > 0 → accept. IRR > WACC → accept. The two usually agree; conflict arises with non-conventional cash flows (multiple sign changes) — prefer NPV.

## Capital Structure (Modigliani-Miller + extensions)

**M&M Proposition I** (no taxes): firm value is independent of capital structure.

**M&M with taxes**: debt creates value via the **interest tax shield**:

```
Tax shield = D × Tc
```

But debt also creates **financial distress costs** (bankruptcy, agency, lost flexibility). Optimal capital structure balances:

```
Optimal D/E where: ∂Tax shield value / ∂D = ∂Distress cost / ∂D
```

In practice: industry capital structure is a strong prior. Stable cash flows → more debt. Volatile cash flows → less debt.

## EVA — Economic Value Added

```
EVA = NOPAT − (Capital × WACC)
```

- NOPAT = Net Operating Profit After Taxes
- Capital = Invested capital (debt + equity)

Positive EVA = value creation above the cost of capital. Use for:
- Business unit performance evaluation.
- Capital allocation (which BU earns its cost of capital?).
- Compensation design (pay for value creation, not just earnings).

## M&A Valuation — Three approaches

Triangulate across three methods:

| Method | What it captures | Caveats |
|---|---|---|
| **DCF** (Discounted Cash Flow) | Intrinsic value based on projected free cash flow | Heavy assumptions; sensitive to terminal growth + WACC |
| **Trading Comps** | Public-market multiples (EV/EBITDA, P/E) | Assumes target should trade like its peers |
| **Precedent Transactions** | Recent M&A multiples in same sector | Includes control premium; deal-specific dynamics distort |

**Range, not point estimate.** DCF says X; comps say Y; precedents say Z. The defensible valuation is the overlap.

**Synergy value** is separate and earned, not given. Cost synergies are more reliable than revenue synergies; both should be discounted for execution risk.

## When to use

- Business case ROI for any initiative > $500K.
- Defending data platform spend (Defending AI Spend 12-Q Q1 + Q2).
- Evaluating vendor / build-vs-buy.
- Strategic option valuation.

## Cross-references

- `../../Frameworks/finance.md` — broader finance frameworks (financial accounting, managerial accounting, valuation, IB).
- `../../../ip/curated/defending-ai-spend-12q.md` — Q1, Q2, Q7, Q8 are corporate-finance questions in disguise.
