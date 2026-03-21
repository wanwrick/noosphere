# Valuation Quick Reference Card

## RELATIVE VALUATION FORMULAS

### Equity Multiples
| Multiple | Formula | Key Value Drivers |
|----------|---------|-------------------|
| **P/E₁** | (1-k)/(r_e-g) | Growth (g), Risk (r_e), Plowback (k) |
| **P/S₁** | Profit Margin × P/E₁ | + Profit Margin |
| **P/B₀** | (ROE-g)/(r_e-g) | ROE relative to r_e |

### Enterprise Multiples
| Multiple | Formula | Key Value Drivers |
|----------|---------|-------------------|
| **EV/NOPAT₁** | (1-b)/(WACC-g) | Growth (g), WACC, Reinvestment (b) |
| **EV/S₁** | Operating Margin × EV/NOPAT₁ | + Operating Margin |

---

## DCF VALUATION

### Firm Value
```
V = Σ [FCFF_t / (1+WACC)^t] + TV_T / (1+WACC)^T
```

### FCFF Calculation
```
FCFF = NOPAT - Net Investment
     = EBIT(1-τ) - (CAPEX - Dep + ΔNOWC)
```

| Component | Formula |
|-----------|---------|
| NOPAT | EBIT × (1 - τ) |
| Net Investment | CAPEX - Depreciation + ΔNOWC |
| NOWC | Operating Current Assets - Operating Current Liabilities |
| ROIC | NOPAT / Invested Capital |

### Terminal Value
```
TV = FCFF_(T+1) / (WACC - g)
   = NOPAT_(T+1) × (1 - g/ROIC) / (WACC - g)
```

**Terminal g**: Use 2-4% (cannot exceed long-term GDP growth)

---

## COST OF CAPITAL

### WACC
```
WACC = (E/V) × r_E + (D/V) × r_D × (1-τ)
```

### Cost of Equity (CAPM)
```
r_E = r_f + β × (r_m - r_f)
```

| Input | Typical Source |
|-------|----------------|
| r_f | 10-Year Treasury yield (WSJ) |
| β | Capital IQ, Bloomberg |
| r_m - r_f | 7.00% (historical average) |

### Cost of Debt
```
r_D = Treasury Yield + Credit Spread
```
Source: FRED for credit spreads by rating

---

## BETA ADJUSTMENT

### Unlever (remove capital structure effect)
```
β_U = β_L / [1 + (D/E)(1-τ)]
```

### Relever (apply target capital structure)
```
β_L = β_U × [1 + (D/E)(1-τ)]
```

---

## FROM EV TO EQUITY VALUE

```
  Enterprise Value (PV of FCFF + PV of TV)
+ Excess Cash & Marketable Securities
+ Holdings in Other Firms
+ Other Non-Operating Assets
= FIRM VALUE
- Market Value of Debt
= EQUITY VALUE
÷ Shares Outstanding
= EQUITY VALUE PER SHARE
```

---

## KEY RELATIONSHIPS

| Relationship | Formula | Use |
|--------------|---------|-----|
| Growth from reinvestment | g = b × ROIC | Terminal value |
| Reinvestment rate | b = g / ROIC | Terminal FCFF |
| Value creation | ROIC > WACC | Sanity check |
| P/B interpretation | P/B > 1 if ROE > r_e | Value creation |

---

## NOWC COMPONENTS

### Include (Operating)
| OCA | OCL |
|-----|-----|
| Operating Cash (2% Rev) | Accounts Payable |
| Accounts Receivable | Accrued Expenses |
| Inventory | Unearned Revenue |
| Prepaid Expenses | Current Taxes Payable |

### Exclude (Non-Operating/Financing)
- Excess cash & marketable securities
- Short-term debt
- Current portion of long-term debt

---

## TYPICAL BENCHMARKS

| Metric | Range | Notes |
|--------|-------|-------|
| Terminal g | 2-4% | Cannot exceed GDP growth |
| Market Risk Premium | 5-8% | Historical avg: 7.0% |
| ROIC (median) | ~10% | Top quartile: >20% |
| Operating Cash | 2% Rev | Rule of thumb |

---

## VALUATION PROJECT PARTS

| Part | Content | Weight | Due |
|------|---------|--------|-----|
| 1 | Multiples Valuation | 15% | May 5 |
| 2 | Historical FCFF & ROIC | 8% | May 19 |
| 3 | DCF Valuation | 17% | June 5 |

---

## COMMON PITFALLS TO AVOID

❌ Terminal g > WACC (mathematically impossible)  
❌ Terminal g > GDP growth (implausible)  
❌ Comparing levered betas across different capital structures  
❌ Using book values instead of market values for WACC weights  
❌ Including excess cash in operating assets  
❌ Including short-term debt in operating liabilities  
❌ Forgetting to add back depreciation (non-cash expense)  
❌ Double-counting non-operating assets
