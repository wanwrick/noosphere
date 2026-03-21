# INVESTMENT BANKING QUICK REFERENCE
## Cornell EMBA | Applied Transactions Course | Instructor: Paroz Mehta

---

## THE CORE QUESTION
**How do we create equity value through debt-financed acquisitions and optimize transaction returns?**

---

## QUICK FORMULAS (Reference Sheet)

| Metric | Formula | Use |
|--------|---------|-----|
| **IRR** | Discount rate where NPV of equity cash flows = 0 | Equity investor return |
| **MOIC** | (Distributions + Exit Proceeds) / Initial Investment | Return multiple |
| **Leverage** | Total Debt / EBITDA | Debt burden metric |
| **Interest Coverage** | EBITDA / Interest Expense | Debt service ability |
| **DSCR** | FCF / (Interest + Principal) | Debt paydown capacity |
| **FCF** | Operating CF - CapEx - ΔWC | Available for debt service |
| **Accretion** | Target Net Income - After-Tax Debt Cost | EPS impact |
| **Synergy NPV** | Σ[Synergies_t / (1+r)^t] | Value creation |
| **EV** | Market Cap + Total Debt - Cash | Enterprise value |
| **EV/EBITDA** | EV / EBITDA | Valuation multiple |

---

## LBO MECHANICS (The Playbook)

### 1. Entry Analysis
```
Target EBITDA: $50M
Entry Multiple: 8.5x
Entry EV: $425M

Financing:
  Debt (4.0x Leverage): $200M
  Equity (Sponsor Cash): $225M

Sources & Uses:
  Purchase Price: $425M
  Debt Fees: $4M
  Transaction Costs: $8M
  TOTAL USES: $437M = TOTAL SOURCES ✓
```

### 2. Build 5-Year Forecast
```
Revenue Growth: 3-4% CAGR
EBITDA Margin: Hold flat or improve 50 bps/year
CapEx: 6-8% of revenue (maintenance)
Tax Rate: 25%
```

### 3. Debt Paydown Schedule
```
Year 1 FCF: $25M → Repay $25M principal
Year 2 FCF: $27M → Repay $27M principal
...
Exit Leverage: Target 2.0x (from 4.0x entry)
```

### 4. Calculate Equity Returns
```
Entry Equity: $225M
Exit EV: Year 5 EBITDA × 9.5x (exit multiple)
Exit Equity: Exit EV - Remaining Debt
IRR = Discount rate solving: -$225M + Exit Equity/(1+r)⁵ = 0
```

---

## LEVERAGE COVENANT FRAMEWORK

| Metric | Covenant | Healthy |
|--------|----------|---------|
| **Max Leverage** | 4.5x | <3.0x |
| **Min Interest Coverage** | 2.5x | >4.0x |
| **Min DSCR** | 1.15x | >1.25x |

**Breach Triggers**: Lender has right to accelerate debt; limits sponsor flexibility

---

## ACCRETION/DILUTION TEST (5 Steps)

**Step 1: Target Net Income Contribution**
```
Target EBIT × (1 - Tax Rate) = Contribution
Example: $30M × 75% = $22.5M
```

**Step 2: Debt Financing Cost**
```
Purchase Price × Interest Rate × (1 - Tax Rate)
Example: $400M × 5% × 75% = $15M after-tax cost
```

**Step 3: Net Accretion**
```
$22.5M - $15M = $7.5M net accretion
```

**Step 4: Per Share Impact**
```
$7.5M / Buyer Shares Outstanding
```

**Step 5: % Impact**
```
Per Share Accretion / Current EPS = % Impact
If +$0.15 per share on $2.00 EPS = +7.5% accretive
```

**Key Insight**: Deals dilutive Year 1 often become accretive Year 3-5 when synergies realized

---

## SYNERGY VALUATION (Reality Check)

### Revenue Synergies (Best Case: 50-70% realized)
```
Cross-sell to buyer's customer base:
  Buyer 10M customers × 5% adoption × $50 ARPU = $25M new revenue
  Realistic realization (50%): $12.5M annually
  NPV at 10% discount: ~$77M
```

### Cost Synergies (Typical: 80-100% realized)
```
Consolidate duplicate functions:
  Eliminate redundant execs: $5M/year
  Supply chain improvement: $10M/year
  Overhead: $8M/year
  Total: $23M cost synergies
  NPV at 8% discount: ~$150M
```

### Tax Synergies (Nearly 100% certain)
```
Use target's tax loss carryforwards:
  Tax losses: $100M
  Tax rate: 25%
  Value: $25M (mechanical)
```

**Synergy Discount Test**:
```
Buyer offering $500M
Standalone value: $450M
Premium paid: $50M

Synergies claimed: $75M NPV
Buyer needs >$50M to justify deal
At 50% realization (conservative): $37.5M value
REJECT or negotiate down price
```

---

## VALUATION METHODS COMPARISON

| Method | Best For | Key Input | Sensitivity |
|--------|----------|-----------|-------------|
| **DCF** | Long-term view | Terminal growth rate | High (TV = 60-70% of value) |
| **Comps** | Market benchmark | Peer multiples | Medium (multiples vary) |
| **Precedents** | Recent deals | Historical prices | Medium (data sparse) |
| **Sum-of-Parts** | Diversified company | Divisional multiples | High (requires segmentation) |

### Quick Decision Rule
```
IF (All three methods within 10-15% range)
  THEN → Use midpoint as fair value
ELSE → Outlier method likely has wrong assumption
      → Dig deeper before relying on it
```

---

## LEVERAGE DECISION TREE

```
Leverage Tradeoff:
  Higher leverage → Higher returns (25% → 30%+ IRR)
  Lower leverage → Lower risk (avoid covenant breaches)

Choose leverage based on:
  ✓ Business stability (stable = higher leverage OK)
  ✓ Cash flow visibility (predictable = take more debt)
  ✓ Downside protection (margin of safety important?)
  ✓ Exit optionality (more leverage = less flexibility)

Typical Guidelines:
  Stable, recurring business: 4.5-5.5x entry leverage
  Cyclical/commodity: 3.0-4.0x entry leverage
  Turnaround/high risk: 2.5-3.5x entry leverage
```

---

## DEAL SCREENING CHECKLIST

Before diving into full model:

- [ ] **Business Quality**: EBITDA >$50M? Margins >25%?
- [ ] **Capital Intensity**: CapEx <10% revenue?
- [ ] **Customer Base**: Diversified? No 1-2 large customers?
- [ ] **Growth Runway**: Stable or 3%+ growth?
- [ ] **Leverage Capacity**: Can support 4.0x+ debt?
- [ ] **Management**: Quality team can drive operations?
- [ ] **Synergy Potential**: Obvious cost/revenue opportunities?
- [ ] **Market**: Favorable for exit in 5-7 years?

**Score 6+/8 checks → Proceed to detailed analysis**

---

## 3-STATEMENT MODEL ARCHITECTURE

### Inputs Tab (One-way inputs; all formulas reference here)
```
Revenue CAGR: 3%
EBITDA Margin: 30% (improving 50 bps/year)
CapEx: 7% of revenue
Tax Rate: 25%
Entry Leverage: 4.0x
Debt Paydown: 80% of FCF
Exit Multiple: 9.5x
```

### P&L → Cash Flow → Balance Sheet (Link order)
```
P&L: Revenue → EBITDA → EBIT → Net Income
       ↓
CF: Net Income + D&A - ΔWC = Operating CF
      Operating CF - CapEx = FCF
       ↓
BS: Beginning Debt - FCF (repayment) = Ending Debt
    Interest Expense = Ending Debt × Rate
```

### Key Linkages
```
P&L Net Income → CF Operating Cash Flow
CF FCF → Debt schedule (determines paydown)
BS Ending Debt → P&L Interest (next year)
BS Cash balance feeds covenant testing
```

---

## COMMON MULTIPLES & RATIOS

| Metric | Conservative | Mid-Market | Aggressive |
|--------|--------------|-----------|-----------|
| **Entry Leverage** | 3.0x | 4.0-4.5x | 5.5-6.0x |
| **Exit Leverage** | 1.5x | 2.0-2.5x | 3.0x |
| **Interest Coverage** | >4.0x | 3.0-4.0x | 2.5x minimum |
| **Entry Multiple** | 7.0x | 9.0x | 11.0x+ |
| **Exit Multiple** | 8.5x | 10.0x | 11.5x+ |
| **Target IRR** | 18-20% | 24-28% | 30%+ |

---

## RETURNS SENSITIVITY MATRIX

**Base Case: 24% IRR at 4.0x entry, 9.5x exit, 4% growth**

| Entry Leverage | Exit Multiple 9.0x | Exit Multiple 9.5x | Exit Multiple 10.0x |
|---|---|---|---|
| **3.5x** | 21.3% | 23.1% | 24.9% |
| **4.0x** | 22.6% | 24.3% | 26.0% |
| **4.5x** | 23.9% | 25.5% | 27.1% |

**Each 0.5x leverage change = ~1.5% IRR change**
**Each 0.5x exit multiple change = ~2% IRR change**

---

## VALUATION MULTIPLE BENCHMARK

| Sector | EV/EBITDA Range | Exit vs Entry | IRR Implication |
|--------|-----------------|---------------|-----------------|
| **Business Services** | 10-14x | +1.5-2.0x | Multiple expansion adds 20-30% return |
| **Software (SaaS)** | 14-18x | +2-3x | High exit multiple supports lower leverage |
| **Manufacturing** | 7-10x | +0.5-1.5x | Limited multiple expansion; focus on deleveraging |
| **Healthcare** | 12-16x | +2-2.5x | Growth + multiple expansion = dual drivers |
| **Retail** | 6-9x | Flat to +0.5x | Modest multiple growth; leverage key |

---

## DEAL STRUCTURE MATRIX

| Structure | Typical Use | Pros | Cons |
|-----------|------------|------|------|
| **Stock Purchase** | Most common | Cleaner; target shareholders happy | Assume all liabilities |
| **Asset Purchase** | Avoiding liabilities | Select good assets | Higher tax cost; complex |
| **Merger** | Tax efficiency | Streamlined post-close | More regulatory scrutiny |
| **Recapitalization** | Existing portfolio | Sponsor gets capital out | Increases leverage; refinancing risk |

---

## FINANCING STRUCTURES (Typical 4.5x LBO = $450M Debt)

```
Senior Debt (60% of sources) = $270M
  Rate: LIBOR + 350-400 bps ~4.5%
  Tenor: 7 years
  Priority: First lien on assets

Mezzanine (20% of sources) = $90M
  Rate: 12-15% cash pay (+ PIK toggle)
  Tenor: 9 years (defer repayment)
  Priority: Second lien

Equity (20% of sources) = $90M
  Sponsor cash investment
  Expected return: 25-30% IRR
```

---

## COMMON MODELING MISTAKES

| Mistake | Impact | Fix |
|---------|--------|-----|
| Hard-coded numbers | Changes don't cascade | Use inputs tab + formulas |
| Wrong CapEx assumption | FCF overstated | Model as % of revenue |
| Ignored working capital | Cash flow inaccurate | Add ΔWC calculation |
| Interest on current-year debt | Next-period interest wrong | Use beginning or average debt |
| No covenant testing | Unknowingly violate covenants | Build covenant table |
| Inconsistent tax rate | Net income wrong | Use one tax rate throughout |

---

## SYNERGY REALIZATION RATES (Historical)

```
Cost Synergies: 80-100% realized (controllable)
  Integration: Year 1 = 30%, Year 2 = 70%, Year 3 = 100%

Revenue Synergies: 30-50% realized (harder)
  Integration: Year 1 = 10%, Year 2 = 30%, Year 3 = 40%

Tax Synergies: 95%+ realized (mechanical)
  Integration: Year 1 = 100%, Year 2 = 100%

Conservative Approach: Apply 50-70% factor to all synergies
```

---

## INVESTMENT DECISION FRAMEWORK

```
IF (Target financial metrics pass screening)
   AND (Valuation reasonable vs. comps/precedents)
   AND (Debt capacity sufficient; covenants maintainable)
   AND (Synergies credible; realization plan clear)
   AND (IRR >20%; MOIC >2.5x over 5 years)
THEN → RECOMMEND PROCEED
ELSE → PASS or NEGOTIATE BETTER TERMS
```

---

## QUICK DEAL MATH (5-Minute Screening)

**Given**: Target Revenue $100M, EBITDA Margin 25% (so $25M EBITDA)

**Valuation Check** (Comp Multiple 10x):
```
$25M × 10x = $250M enterprise value
Less: Net Debt $30M
Equity Value: $220M
```

**Leverage Check** (4.0x entry leverage target):
```
$25M × 4.0x = $100M debt capacity
Equity required: $220M - $100M = $120M
Equity % of sources: $120M / $220M = 55%
Debt % of sources: $100M / $220M = 45%
```

**Return Estimate** (Year 5, 20% IRR):
```
MOIC over 5 years at 20% IRR ≈ 2.5x
Exit Equity Value: $120M × 2.5x = $300M
```

**Downside Check** (Conservative scenario):
```
Year 5 EBITDA flat at $25M (no growth)
Exit multiple 8.0x (contraction) = $200M EV
Less: Remaining Debt $40M (after paydown)
Exit Equity: $160M
MOIC: $160M / $120M = 1.33x
IRR: ~6% (unacceptable - need growth or deleveraging)
```

---

## GLOSSARY (Key Terms)

| Term | Definition |
|------|-----------|
| **EBITDA** | Earnings before interest, taxes, D&A; operating profit |
| **Leverage** | Total Debt / EBITDA; measures debt burden |
| **FCF** | Free cash flow; available to service debt |
| **MOIC** | Multiple on invested capital; total return |
| **IRR** | Internal rate of return; annualized equity return |
| **Accretion** | EPS increases post-deal; positive impact |
| **Dilution** | EPS decreases post-deal; negative impact |
| **Synergies** | Value created by combining companies |
| **DSCR** | Debt service coverage ratio; debt paydown ability |
| **Entry Multiple** | EV/EBITDA at acquisition |
| **Exit Multiple** | EV/EBITDA at sale; drives equity return |
| **Covenant** | Debt restriction; breach = default risk |
| **Sources & Uses** | Statement matching financing to purchase price |

---

## QUICK DECISION RULES

```
✓ Leverage Test:
  Entry >5.5x = Very aggressive (high risk)
  4.0-5.0x = Standard LBO
  <3.0x = Conservative; lower returns

✓ Interest Coverage Test:
  >4.0x = Safe; room for errors
  2.5-4.0x = Standard; watch closely
  <2.0x = Danger; vulnerable to downturn

✓ IRR Test:
  <15% = Too low; don't do deal
  15-20% = Acceptable; strategic rationale important
  20-30% = Attractive; market standard for LBOs
  >30% = Exceptional; asymmetric return opportunity

✓ Accretion Test:
  Year 1 >5% = Immediately accretive (very attractive)
  0-5% = Mildly accretive; standard
  -5% to 0% = Mildly dilutive; acceptable if strategic
  <-5% = Significantly dilutive; needs strong synergies

✓ Synergy Test:
  Synergy NPV <10% of deal price = Insufficient
  10-20% of deal price = Moderate justification
  >20% of deal price = Strong synergy case
```

---

## EXAM/PITCH QUICK CHECKLIST

- [ ] **Model Built?** P&L, CF, BS linked correctly
- [ ] **Debt Schedule?** Year-by-year debt & interest calculated
- [ ] **Returns Calculated?** IRR and MOIC clear
- [ ] **Sensitivity Done?** Multiple, leverage, growth scenarios
- [ ] **Covenants Met?** Leverage, interest coverage, DSCR all pass
- [ ] **Synergies Quantified?** Revenue and cost synergies with realization %
- [ ] **Valuation Sense-checked?** Comps vs. DCF vs. precedents aligned
- [ ] **Story Clear?** Why buy? How create value? What returns?
- [ ] **Risks Identified?** Downside scenarios; what breaks deal?
- [ ] **Recommendation?** Proceed? Pass? Renegotiate?

---

*"In M&A and LBOs, the numbers tell the story. Build the model, test the assumptions, and follow the numbers to your decision."*

*—Paroz Mehta, Investment Banking, Cornell EMBA*
