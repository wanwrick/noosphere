# Valuation Skills - Comprehensive Reference Guide

## Overview

This skill provides comprehensive guidance for corporate valuation analysis, covering relative valuation (multiples), discounted cash flow (DCF) valuation, cost of capital calculations, and real options. Based on Cornell EMBA Americas NBAB 6560/MBQC 804 Valuation course materials from Professor Pamela Moulton, Spring 2025.

## When to Use This Skill

Use this skill when:
- Performing company or asset valuations
- Analyzing comparable companies (comp sets)
- Calculating valuation multiples (P/E, P/S, P/B, EV/EBITDA, etc.)
- Building DCF models
- Computing Free Cash Flow to Firm (FCFF)
- Calculating Weighted Average Cost of Capital (WACC)
- Estimating cost of equity using CAPM
- Valuing non-public or high-growth firms
- Analyzing terminal/continuing value
- Evaluating real options and flexibility

---

# PART 1: FOUNDATIONAL CONCEPTS

## 1.1 The Core Principle of Valuation

**Valuation = Story + Numbers**

A good valuation integrates qualitative narrative with quantitative analysis:

| Component | Pros | Cons |
|-----------|------|------|
| **Story** | Memorable, provides context, explains "why" | Can be vague, hard to test |
| **Numbers** | Precise, testable, comparable | Can miss qualitative factors, easy to manipulate |

### Valuation Steps
1. **Develop a narrative**: How do you see the business developing over time?
2. **Test narrative**: Is it possible? Plausible? Probable?
3. **Convert narrative into drivers of value** (valuation assumptions)
4. **Use drivers of value to perform numerical valuation**
5. **Keep feedback loop open**: Fine-tune narrative → assumptions → valuation

### Example: Ferrari IPO
- **Numbers alone**: 4% revenue growth, 18.2% operating margin, €1.42 revenue per €1 invested
- **Story alone**: Luxury auto maker charging high prices due to exclusivity
- **Valuation**: Links the two - low growth tied to maintaining exclusivity; huge margins tied to wealthy buyers unaffected by economic cycles

---

## 1.2 When Valuation is Useful

```
Firm or Entrepreneur ←→ Other Firms/Assets ←→ Capital Markets
       ↓                        ↓                    ↓
   Divestiture              Acquisition          Raising Capital
                                                 (VC, PE, IPO, SEO)
                                                      ↓
                                              Return to Security Holders
```

**Applications**:
- Stock selection and portfolio management
- IPO pricing
- M&A transactions
- Private equity investments
- Divestitures
- Strategic planning

---

## 1.3 Two Main Valuation Approaches

| Approach | Big Idea | Key Inputs |
|----------|----------|------------|
| **Relative Valuation** | Value based on similar assets | Comparable firms, multiples |
| **DCF Valuation** | Value = PV of future cash flows | Cash flow projections, discount rate |

Both approaches should theoretically yield similar values if done correctly—they capture the same fundamentals (cash flows, growth, risk).

---

# PART 2: MANAGERIAL FINANCE FOUNDATIONS

## 2.1 Discounting Cash Flows

### Single Cash Flow
```
PV = CF_t / (1 + r)^t
```

**Where:**
- `PV` = Present Value (today's value of future cash flow)
- `CF_t` = Cash flow at time t
- `r` = Discount rate per period (required return)
- `t` = Number of periods until cash flow occurs

### Multiple Cash Flows
```
PV = Σ [CF_t / (1 + r)^t] for t = 1 to n
```

**Where:**
- `n` = Total number of periods

---

## 2.2 Perpetuities

### Constant Perpetuity
```
PV = CF / r
```

**Where:**
- `CF` = Constant cash flow (beginning one period from now)
- `r` = Discount rate

**Use case**: Valuing infinite stream of equal cash flows

### Growing Perpetuity (Gordon Growth Model)
```
PV = CF₁ / (r - g)
```

**Where:**
- `CF₁` = Next cash flow (one period from now)
- `g` = Constant growth rate
- **Critical requirement**: r > g

**Use case**: Foundation for most valuation formulas

---

## 2.3 Capital Asset Pricing Model (CAPM)

### The Concept of Risk

| Risk Type | Also Called | Examples | Compensated? |
|-----------|-------------|----------|--------------|
| **Systematic** | Market risk, non-diversifiable | Economic growth, recession, inflation, Fed policy | YES |
| **Unsystematic** | Idiosyncratic, diversifiable | Corporate earnings surprise, lawsuit, M&A | NO |

**Key insight**: Investors are compensated ONLY for risks they cannot diversify away.

### Beta (β)
- Measures how much an asset's return changes per change in market return
- β_market = 1.00 (by definition)
- β_risk-free = 0.00 (no systematic risk)
- β > 1: More volatile than market
- β < 1: Less volatile than market

### CAPM Equation
```
r_i = r_f + β_i × (r_mkt - r_f)
```

**Where:**
- `r_i` = Required return on asset i
- `r_f` = Risk-free rate
- `β_i` = Beta of asset i
- `r_mkt` = Market return
- `(r_mkt - r_f)` = Market risk premium (MRP)

**Interpretation**: Required return = Risk-free rate + (Amount of systematic risk) × (Market risk premium)

---

## 2.4 Capital Structure

### Value of Firm
```
V = E + D
```
- V = Total firm value
- E = Value of Equity
- D = Value of Debt

### Impact of Leverage
- Adding debt makes equity riskier (debt gets paid first)
- Higher D/E ratio → Higher required return on equity (r_e)
- Equity holders are "residual claimants"

---

## 2.5 Weighted Average Cost of Capital (WACC)

```
WACC = w_e × r_e + w_d × r_d × (1 - t_c)
```

**Where:**
- `w_e` = Weight of equity = E / (E + D)
- `r_e` = Required return on equity
- `w_d` = Weight of debt = D / (E + D)
- `r_d` = Required return on debt (yield, NOT coupon)
- `t_c` = Corporate tax rate
- `(1 - t_c)` = Tax shield on interest payments

**Note**: The (1 - t_c) factor accounts for the tax deductibility of interest payments.

---

## 2.6 Accounting Definitions

| Term | Definition | Formula |
|------|------------|---------|
| **EBIT** | Earnings Before Interest and Taxes | Revenue - Operating Costs - Depreciation |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation & Amortization | Revenue - Operating Costs |
| **Operating Margin** | Operating efficiency | EBIT / Sales Revenue |
| **Profit Margin** | Bottom-line profitability | Net Income / Sales Revenue |
| **ROE** | Return on Equity | Net Income / Book Equity |
| **ROIC** | Return on Invested Capital | NOPAT / Invested Capital |

---

# PART 3: RELATIVE VALUATION

## 3.1 Core Concept

**Big Idea**: Value an asset based on how similar assets are priced in the market.

**Requirements**:
1. Find comparable assets
2. Standardize prices using a multiple
3. Control for differences in key value drivers

---

## 3.2 Valuation Multiples Framework

```
Multiple = Market Value / Fundamental
```

### Market Value Options
- Value of equity (per share: P, or total: Market Cap)
- Value of firm (E + D)
- Enterprise Value (EV = Market Value of Operating Assets)

### Fundamental Options
- Earnings (E)
- Sales (S)
- Book Value (B)
- EBIT, EBITDA, NOPAT
- Invested Capital

**Critical Consistency Rule**: Numerator and denominator must be consistent:
- P/E: Both per share (equity level)
- EV/EBITDA: Both operating assets/operating income

---

## 3.3 Price-to-Earnings (P/E) Ratio

### Three Common Versions
| Version | Formula | Use Case |
|---------|---------|----------|
| **Forward P/E (P/E₁)** | Price / Next Year's Earnings | Most common, forward-looking |
| **Current P/E (P/E₀)** | Price / Last Reported Earnings | Historical perspective |
| **Trailing P/E** | Price / Average Historical Earnings | Smooths volatility |

### Fundamental Derivation
Starting from Gordon Growth Model:
```
P = FCFE₁ / (r_e - g) = E₁(1 - k) / (r_e - g)
```

**Therefore:**
```
P/E₁ = (1 - k) / (r_e - g)
```

**Where:**
- `k` = Plowback ratio = Net Investment / Net Income
- `(1 - k)` = Payout ratio (available to equity holders)
- `r_e` = Cost of equity
- `g` = Earnings growth rate

### Key Value Drivers for P/E
| Driver | Direction | Explanation |
|--------|-----------|-------------|
| Growth (g) ↑ | P/E ↑ | Higher growth justifies higher multiple |
| Risk (r_e) ↑ | P/E ↓ | Higher required return = lower multiple |
| Plowback (k) ↑ | P/E ↓ | Less payout = lower multiple (but may enable higher g) |

### Proxies for Value Drivers
- **g**: Historical earnings/sales growth, analyst forecasts
- **r_e**: Beta, industry risk
- **k**: Historical reinvestment patterns, dividend policy

---

## 3.4 Price-to-Sales (P/S) Ratio

### Formula
```
P/S₁ = Profit Margin × P/E₁
```

**Or in full:**
```
P/S₁ = [Profit Margin × (1 - k)] / (r_e - g)
```

### Key Value Drivers
- **Profit Margin** (critical additional driver)
- Growth rate (g)
- Risk (r_e)
- Plowback ratio (k)

### Advantages
- Works for firms with negative or zero earnings
- Sales revenues may be more comparable across firms

### Disadvantages
- Assumes profit margins are similar across comp firms
- Inconsistency: Sales benefit all investors (D + E), not just equity
- **Solution**: Use EV/S₁ multiple instead

---

## 3.5 Price-to-Book (P/B) Ratio

### Formula
```
P/B₀ = (ROE - g) / (r_e - g)
```

**Alternative form:**
```
P/B₀ = 1 + [(ROE - r_e) / (r_e - g)]
```

### Key Insights
| Condition | Result | Interpretation |
|-----------|--------|----------------|
| ROE > r_e | P/B > 1 | Firm creates value |
| ROE < r_e | P/B < 1 | Firm destroys value |
| ROE = r_e | P/B = 1 | Firm earns exactly cost of capital |

### Best Use Cases
- Financial institutions (banks)
- Capital-intensive businesses
- Firms where book value reflects economic value

### Disadvantages
- Book value affected by accounting decisions
- May not reflect earning power of assets
- Less relevant for service firms, tech firms

---

## 3.6 Enterprise Value (EV) Multiples

### Enterprise Value Definition
```
EV = MV of Equity + MV of Debt - Excess Cash - Other Non-operating Assets
```

**EV represents**: Market value of Invested Capital (operating assets only)

### Economic Balance Sheet View
```
┌─────────────────────────────┬─────────────────────────────┐
│    TOTAL CAPITAL (Uses)     │  TOTAL INVESTOR FUNDS       │
├─────────────────────────────┼─────────────────────────────┤
│                             │         Equity              │
│  Invested Capital =         ├─────────────────────────────┤
│  Operating Assets           │         Debt                │
│  (supports core operations) │                             │
│          ↓                  ├─────────────────────────────┤
│    Net Enterprise           │                             │
│    Value (EV)               │  Non-operating Assets       │
│          ↓                  │  (including excess cash)    │
│   Free Cash Flows           │                             │
│   to Firm (FCFF)            │                             │
└─────────────────────────────┴─────────────────────────────┘
```

### EV/NOPAT Multiple
```
EV/NOPAT₁ = (1 - b) / (WACC - g)
```

**Where:**
- `NOPAT` = Net Operating Profit After Taxes = EBIT × (1 - τ)
- `b` = Reinvestment rate = Net Investment / NOPAT
- `(1 - b)` = Available to all investors
- `WACC` = Weighted average cost of capital
- `g` = NOPAT growth rate

### EV/Sales Multiple
```
EV/S₁ = Operating Margin × EV/NOPAT₁
```

### EV/Invested Capital (EV/IC)
Analogous to P/B but at firm level

### Advantages of EV Multiples
- Value total firm (independent of capital structure)
- Better for comparing firms with different leverage
- Appropriate for divisional valuation (sum of parts)

---

## 3.7 Comparable Company Selection

### What Makes a Good Comp?
- Similar business model
- Similar key value drivers (g, risk, k or b)
- Similar industry/sector

### The Trade-off
| More Firms | Fewer Firms |
|------------|-------------|
| Better statistical reliability | Better match quality |
| More diverse characteristics | More homogeneous |
| May dilute relevance | May miss outliers |

### Comp Set Selection Criteria

**For P/E₁:**
- Growth rate (g)
- Cost of equity (r_e) / Beta (β)
- Plowback rate (k)

**Potential Proxies:**
- Industry, business model, technology
- Customer base
- Firm size (Market Cap)
- Financial leverage (D/E)
- Stock beta (β)

### Using Regression for Disparate Comps

When no close comps exist, use regression to control for differences:

**Example:**
```
P/E₁ = 14.9 + 39.9 × g    (R² = 0.4720)
```

Adding beta:
```
P/E₁ = 19.5 + 42.4 × g - 8.1 × Beta    (R² = 0.5703)
```

---

## 3.8 Using Multiples to Value an Asset

### Step-by-Step Process
1. **Choose the multiple** (P/E₁, P/S₁, EV/EBITDA, etc.)
2. **Choose comparable firms** for comp set
3. **Compute typical multiple** for comp set (mean or median)
4. **Project fundamental measure** for target (E₁, S₁, etc.)
5. **Multiply**: Typical Multiple × Projected Fundamental
6. **Result** = Estimated Value

### Mean vs. Median
- **Mean**: Influenced by outliers; use when distribution is normal
- **Median**: Robust to outliers; use when distribution is skewed

---

## 3.9 Sum of Parts Valuation

### Concept
Most large companies have business units in different industries/sub-industries with:
- Different competitive dynamics
- Different returns and growth rates

### Method
1. Identify pure-play multiples for each division
2. Calculate EV for each division
3. Sum divisional EVs

**Example:**
| Business Unit | NOPAT₁ | EV/NOPAT (High) | EV/NOPAT (Low) | Value (High) | Value (Low) |
|---------------|--------|-----------------|----------------|--------------|-------------|
| Unit 1 | $410M | 16.0 | 14.5 | $6,560M | $5,945M |
| Unit 2 | $299M | 13.9 | 12.5 | $4,156M | $3,738M |
| Unit 3 | $504M | 9.7 | 9.4 | $4,889M | $4,738M |
| **Total** | $1,213M | | | **$15,605M** | **$14,420M** |

---

## 3.10 Non-Financial Multiples

### Examples
| Industry | Multiple | Consideration |
|----------|----------|---------------|
| Oil & Gas | EV/Barrel of reserves | Must match on extraction costs, reserve quality |
| Tech/Digital | EV/Users, EV/Subscribers | Must match on monetization potential |
| Retail | EV/Store, EV/Sq. Footage | Must match on sales productivity |

### Customer-Based Multiples (Dot-Com Era Example)
```
MktCap/Customer = f(GrossProfit/Customer - Marketing/Customer)
```

**Lesson**: Non-financial multiples only work when underlying economics are comparable.

---

## 3.11 Trading vs. Transaction Multiples

### Trading Multiples
- Reflect current stock trading prices
- Available daily
- Liquid market prices

### Transaction Multiples (Precedent Transactions)
- Reflect past M&A or IPO transactions
- Include control premium (M&A) or IPO discount
- Limited by number of comparable transactions

### Special Considerations

**IPO Multiples:**
- First-day returns average 10-20% (underpricing)
- IPO prices typically at discount to trading comps

**M&A Multiples:**
- Include control premium (typically 20-40% above market)
- Reflects synergy value, strategic value

---

## 3.12 When Relative Valuation Works Best

**Easiest to use when:**
- Large number of comparable assets
- Prices are established by market
- Key value drivers are similar

**Works best for investors who:**
- Accept market consensus as baseline
- Want quick, market-based estimates
- Use as sanity check for DCF

---

# PART 4: DISCOUNTED CASH FLOW (DCF) VALUATION

## 4.1 Core Concept

**Big Idea**: Value of any asset = Present Value of expected future cash flows

```
V = Σ [E(CF_t) / (1 + r)^t] for t = 1 to ∞
```

**Value is higher when expected cash flows are:**
- Larger
- Sooner
- Less risky (lower discount rate)

---

## 4.2 DCF Valuation Steps

1. **Forecast FCFF** (explicit forecast period, typically 5-10 years)
2. **Use ROIC** to check reasonableness of forecasts
3. **Estimate Terminal Value** (assumes constant growth eventually)
4. **Estimate forward-looking cost of capital** (WACC)
5. **Compute value**

---

## 4.3 Firm Value Using Free Cash Flows

```
V = Σ [E(FCFF_t) / (1 + WACC)^t] for t = 1 to T + [TV_T / (1 + WACC)^T]
```

**Where:**
- First term = PV of FCFF during explicit forecast period
- Second term = PV of Terminal Value (cash flows after explicit period)

---

## 4.4 Free Cash Flow to Firm (FCFF)

### The Concept
```
┌─────────────────────────────┐   ┌─────────────────────────────┐
│     Investment Bucket       │   │   Free Cash Flow Bucket     │
│                             │   │         (FCFF)              │
│  - Working Capital          │   │                             │
│  - Fixed Assets             │   │  b = % of NOPAT reinvested  │
│                             │   │  (1-b) = % available to     │
│                             │   │          pay out            │
└─────────────────────────────┘   └─────────────────────────────┘
```

### FCFF Formula (Multiple Forms)

**Method 1 - Simple:**
```
FCFF = NOPAT - Net Investment
```

**Method 2 - Detailed:**
```
FCFF = (Sales - OC - Dep)(1 - τ) + Dep - (CAPEX + ΔNOWC)
       └──────────────────────┘   └───────────────────────┘
               NOPAT                   Net Investment
```

**Method 3 - From EBIT:**
```
FCFF = EBIT(1 - τ) - Net Investment
```

### NOPAT Calculation
```
  Sales Revenue
- Cost of Goods Sold (COGS)
- Selling, General & Administrative (SG&A)
- Depreciation
────────────────────────────────────────
= EBIT (Operating Income)
× (1 - τ)
────────────────────────────────────────
= NOPAT
```

### Net Investment Calculation
```
  CAPEX (from Cash Flow Statement)
- Depreciation
+ ΔNOWC (change in Net Operating Working Capital)
────────────────────────────────────────
= Net Investment
```

### Why "Add Back Depreciation"?
- Depreciation is a non-cash expense
- Already subtracted in calculating NOPAT
- Add back because it's not an actual cash outflow
- CAPEX captures actual cash spent on fixed assets

---

## 4.5 Net Operating Working Capital (NOWC)

### Formula
```
NOWC = Operating Current Assets - Operating Current Liabilities
```

### Operating Current Assets (OCA)
| Item | Notes |
|------|-------|
| Operating Cash | Rule of thumb: 2% of revenues |
| Accounts Receivable | Credit sales not yet collected |
| Inventory | Goods held for sale |
| Prepaid Expenses | Payments made in advance |

### Operating Current Liabilities (OCL)
| Item | Notes |
|------|-------|
| Accounts Payable | Credit purchases not yet paid |
| Accrued Expenses | Expenses incurred but not paid |
| Unearned Revenue | Payments received in advance |
| Current Taxes Payable | Taxes owed |

### NOT Included in NOWC
- **Excess cash/marketable securities** (non-operating)
- **Short-term debt** (financing, not operating)
- **Current portion of long-term debt** (financing)

### Change in NOWC
```
ΔNOWC = NOWC_t - NOWC_(t-1)
```

- **Increase** in NOWC → Cash outflow (reduces FCFF)
- **Decrease** in NOWC → Cash inflow (increases FCFF)

---

## 4.6 FCFF Calculation Example (Chipotle)

### Step 1: Compute NOPAT
```
Effective tax rate (τ) = Income Tax Expense / EBT
                       = 391.769 / 1,661.917 = 23.57%

NOPAT = EBIT × (1 - τ)
      = 1,596.183 × (1 - 0.2357) = $1,220.0 million
```

### Step 2: Calculate NOWC
```
                              2022        2023        2024
Operating Cash (2% Rev)      172.7       197.4       226.3
Accounts Receivable          106.9       115.5       144.0
Other Receivables             47.7        53.0        67.2
Inventory                     35.7        39.3        48.9
Prepaid Expenses              86.4       117.5        97.5
────────────────────────────────────────────────────────────
Total OCA                    449.4       522.7       583.9

Accounts Payable             184.6       197.6       210.7
Accrued Expenses             318.0       375.2       441.7
Taxes Payable                  0.0         0.0         0.0
Unearned Revenue             183.1       209.7       238.6
────────────────────────────────────────────────────────────
Total OCL                    685.7       782.5       891.0

NOWC                        -236.3      -259.8      -307.1
```

### Step 3: Calculate Net Investment
```
CAPEX                        560.7
- Depreciation               319.4
+ ΔNOWC (-259.8 - (-236.3))  -23.5
────────────────────────────────────
Net Investment               217.8
```

### Step 4: Calculate FCFF
```
FCFF = NOPAT - Net Investment
     = 1,220.0 - 217.8 = $1,002.2 million
```

---

## 4.7 Forecasting FCFF

### Two Main Approaches

**Option 1: Project Each Line Item Individually**
- Higher accuracy potential
- More time-consuming
- Requires detailed knowledge

**Option 2: Project Key Line Item, Then Ratios**
- Project revenues
- Express other items as % of revenues
- Simpler, but requires stable ratios

### Common Forecast Drivers

| Income Statement Item | Typical Driver |
|----------------------|----------------|
| COGS | Revenue |
| SG&A | Revenue |
| Depreciation | Revenue or Net PP&E_(t-1) |

| Balance Sheet Item | Typical Driver |
|-------------------|----------------|
| Operating Cash | Revenue (2%) |
| Accounts Receivable | Revenue |
| Inventory | Revenue or COGS |
| Accounts Payable | Revenue or COGS |
| Accrued Expenses | Revenue |
| Net PP&E | Revenue |

### Projecting Revenues

**Bottom-up Approach (Micro):**
- Unit sales × Price per unit
- Customer count × Revenue per customer
- Store count × Sales per store

**Top-down Approach (Macro):**
- Total market size × Market share
- Industry growth × Relative performance

**Information Sources:**
- Historical financial statements (10-Ks, Capital IQ)
- Industry experts/trade groups
- Management guidance
- Analyst forecasts

### Growth Rate Calculation

**Single Period:**
```
g = (Sales_t+1 / Sales_t) - 1
```

**Compound Average Growth Rate (CAGR):**
```
g = (Sales_t+n / Sales_t)^(1/n) - 1
```

---

## 4.8 Return on Invested Capital (ROIC)

### Formula
```
ROIC = NOPAT / Invested Capital
```

### Purpose
- Measures capital efficiency
- Sanity check on forecasts
- Key driver of value creation

### ROIC vs. WACC
| Condition | Implication |
|-----------|-------------|
| ROIC > WACC | Firm creates value; value should increase |
| ROIC < WACC | Firm destroys value; value should decrease |
| ROIC = WACC | Firm earns exactly cost of capital |

### ROIC Benchmarks (Best-of-Breed)

| Firm Type | ROIC Range | Operating Margin | Characteristics |
|-----------|------------|------------------|-----------------|
| Coca-Cola | 38-42% | 23-24% | Strong brand, entry barrier, asset-light |
| UPS | 13-19% | 12-13% | Entry barrier, asset-heavy |
| Home Depot | 15-26% | 11-15% | Strong brand, specialty, asset-heavy |
| Walmart | 11-14% | 4.5-5.9% | Commodities, economies of scale |

### ROIC Distribution (All Firms)
- Median: ~10%
- Most firms: 5-15%
- Top quartile: >20%
- Challenge forecasts with ROIC >30% long-term

---

## 4.9 Terminal Value

### Concept
- Captures value of cash flows beyond explicit forecast period
- Often 60-80% of total firm value
- Critical to get assumptions right

### Formula (Gordon Growth Model)
```
TV_T = FCFF_(T+1) / (WACC - g)
```

**Or using ROIC:**
```
TV_T = NOPAT_(T+1) × (1 - g/ROIC) / (WACC - g)
```

**Where:**
- `T` = Last year of explicit forecast
- `g` = Terminal growth rate (perpetual)
- `ROIC` = Long-term return on invested capital
- `b = g/ROIC` = Required reinvestment rate

### Choosing Terminal Growth Rate (g)

**Key Principles:**
- Cash flows are nominal (include inflation)
- g should be nominal (not real)
- Cannot exceed long-term economic growth
- Typical range: 2-4%

**Cautionary Tales:**
- g = 0% implies firm shrinks in real terms
- g > WACC is mathematically impossible
- g > GDP growth long-term is implausible

### Relationship: g, b, and ROIC
```
g = b × ROIC
```
Therefore:
```
b = g / ROIC
```

**Example:**
- If ROIC = 30% and g = 3%, then b = 10% (reinvest only 10%)
- If ROIC = 15% and g = 3%, then b = 20% (reinvest 20%)

---

## 4.10 From Enterprise Value to Equity Value

### Step-by-Step
| Step | Description | Notes |
|------|-------------|-------|
| 1 | Value operating assets (EV) | Discount FCFF at WACC |
| 2 | + Excess cash & marketable securities | Non-operating cash |
| 3 | + Value of holdings in other firms | Minority investments |
| 4 | + Value of other non-operating assets | Real estate, etc. |
| 5 | = **Value of Firm** | Total enterprise value |
| 6 | - Value of Debt | Market value of debt |
| 7 | = **Value of Equity** | Total equity value |
| 8 | ÷ Shares Outstanding | |
| 9 | = **Equity Value per Share** | Intrinsic value |

---

# PART 5: COST OF CAPITAL

## 5.1 WACC Components

```
WACC = (E/V) × r_E + (D/V) × r_D × (1 - τ)
```

| Component | Definition | How to Estimate |
|-----------|------------|-----------------|
| E/V | Weight of equity | Market Cap / (Market Cap + Debt) |
| D/V | Weight of debt | Debt / (Market Cap + Debt) |
| r_E | Cost of equity | CAPM |
| r_D | Cost of debt | Yield approach or Spread approach |
| τ | Marginal tax rate | Statutory rate (typically 21% US) |

---

## 5.2 Capital Structure Weights

### Equity Weight
```
E/V = Market Capitalization / (Market Cap + Market Value of Debt)
```

**Market Cap** = Share Price × Shares Outstanding

### Debt Weight
```
D/V = Market Value of Debt / (Market Cap + Market Value of Debt)
```

**Market Value of Debt:**
- Sum of market values for all bonds outstanding
- If no market value available, use book value as proxy
- Bond MV = Amount Outstanding × (Current Price / 100)

---

## 5.3 Cost of Debt (r_D)

### Method 1: Actual Yield Approach
Calculate yields of all outstanding bonds:
```
Price = Σ [C_t / (1 + y)^t] + Par / (1 + y)^T
```

Then: r_D = Value-weighted average yield (y)

### Method 2: Spread Approach

**Step 1:** Look up credit rating (Capital IQ → Fixed Income/Summary → "Local Currency LT")

**Step 2:** Find credit spread from FRED:
- https://fred.stlouisfed.org/categories/32348

**Step 3:** Calculate:
```
r_D = Treasury Yield + Credit Spread
```

**Example:**
```
r_D = 4.52% (10Y Treasury) + 0.99% (BBB spread) = 5.51%
```

### Credit Spread Benchmarks
| Rating | Typical Spread |
|--------|----------------|
| AAA | 0.40-0.60% |
| AA | 0.50-0.80% |
| A | 0.80-1.20% |
| BBB | 1.00-1.80% |
| BB | 2.00-3.50% |
| B | 3.50-5.50% |
| CCC | 6.00%+ |

---

## 5.4 Cost of Equity (r_E) - CAPM

```
r_E = r_f + β × (r_m - r_f)
```

**Where:**
- `r_f` = Risk-free rate (10-Year Treasury yield)
- `β` = Equity beta
- `(r_m - r_f)` = Market risk premium

### Risk-Free Rate
- Use current 10-Year Treasury yield
- Source: WSJ (https://www.wsj.com/market-data/bonds) or Bloomberg

### Market Risk Premium
- Historical US average (1928-2024): **7.00%**
- Standard error: 2.12%
- Alternative estimates: 5-8%

### Beta Sources
- Capital IQ (Company Summary → Tearsheet)
- Bloomberg
- Run your own regression

---

## 5.5 Beta Estimation

### From Regression
```
r_it = α_i + β_i × r_mt + ε_it
```

- Use 12-60 months of return data
- β = Slope coefficient

### Why Betas Differ

**High Beta (β > 1):**
- Tesla: 2.34
- Macy's: 2.09
- Cyclical, high operating leverage

**Medium Beta (β ≈ 1):**
- 3M Company: 1.00
- International Paper: 0.99

**Low Beta (β < 1):**
- Walmart: 0.55
- Colgate-Palmolive: 0.43
- Defensive, stable demand

### Fundamental Determinants of Beta

1. **Nature of Business**
   - Sensitivity of product demand to economic cycles
   - Discretionary vs. non-discretionary products

2. **Operating Leverage**
   - Higher fixed costs → More volatile earnings → Higher beta

3. **Financial Leverage**
   - Higher debt → More volatile net income → Higher equity beta

---

## 5.6 Adjusting Beta for Capital Structure

### The Problem
- Observed betas reflect firm's specific capital structure
- Need to compare betas across different leverage levels
- Private firms have no observable beta

### Step 1: Unlever Comp Firm Betas
```
β_U = β_L / [1 + (D/E)(1 - τ)]
```

**Where:**
- `β_U` = Unlevered beta (asset beta)
- `β_L` = Levered beta (observed equity beta)
- `D/E` = Debt-to-equity ratio
- `τ` = Tax rate

### Step 2: Average Unlevered Betas
```
Avg β_U = Σ β_U,n / N
```

### Step 3: Relever for Target Firm (if needed)
```
β_L = Avg β_U × [1 + (D/E)(1 - τ)]
```

### Example: Estimating Beta from Comps

**Target:** Red Corp (private), D/E = 0.7, τ = 21%

**Comps:**
- Blue Corp: β = 1.75, D/E = 2.2
- Yellow Corp: β = 1.10, D/E = 1.5

**Step 1: Unlever**
```
Blue: β_U = 1.75 / [1 + 2.2(0.79)] = 0.64
Yellow: β_U = 1.10 / [1 + 1.5(0.79)] = 0.50
```

**Step 2: Average**
```
Avg β_U = (0.64 + 0.50) / 2 = 0.57
```

**Step 3: Relever for Red Corp**
```
β_L = 0.57 × [1 + 0.7(0.79)] = 0.89
```

---

## 5.7 WACC Calculation Example (GAP)

### Step 1: Cost of Equity
- Risk-free rate: 4.52%
- Beta: 1.86
- Market risk premium: 7.00%

```
r_E = 4.52% + 1.86 × 7.00% = 17.54%
```

### Step 2: Cost of Debt
- Credit rating: BB
- BB spread: 2.27%

```
r_D = 4.52% + 2.27% = 6.79%
```

### Step 3: Capital Structure Weights
- Market Cap: $8,556 million
- Market Value of Debt: $2,679 million

```
E/V = 8,556 / (8,556 + 2,679) = 76.15%
D/V = 2,679 / (8,556 + 2,679) = 23.85%
```

### Step 4: WACC
- Tax rate: 25%

```
WACC = 76.15% × 17.54% + 23.85% × 6.79% × (1 - 0.25)
     = 13.36% + 1.21%
     = 14.57%
```

---

# PART 6: SPECIAL VALUATION TOPICS

## 6.1 Valuing Non-Public Firms

### Key Challenges
- No observable stock price
- No observable beta
- Limited financial disclosure

### Approaches

**For Beta:**
1. Industry average beta
2. Pure-play comparable firms (unlever/relever)

**For Valuation:**
1. DCF (same methodology, different data sources)
2. Transaction multiples (precedent transactions)
3. Comparable public company multiples (with discount)

---

## 6.2 Valuing High-Growth Firms

### Challenges
- Negative current earnings/cash flows
- High uncertainty
- Limited historical data

### Strategy Differences

| Established Firm | High-Growth Firm |
|------------------|------------------|
| Begin with historical performance | Begin with the future |
| Work forward to project | Work backward to connect to today |
| Historical ratios inform forecasts | Create multiple scenarios |

### High-Growth Valuation Approach

**Start from the End:**
1. Estimate terminal value at time T (5-10 years)
2. Use plausible g, ROIC for mature firm
3. Benchmark to established industries

**Work Backward:**
1. What market size and share are needed?
2. What margins are achievable?
3. What investments are required?
4. Connect to current state

### Useful Historical Ratios (Even for Negative Earnings)
- NOWC/Sales
- Net PP&E/Sales
- These may continue even if margins are negative

---

## 6.3 SaaS & High-Growth Company Valuation

Traditional DCF and relative valuation methods require adaptation for SaaS (Software-as-a-Service) and subscription-based businesses. Recurring revenue models, negative near-term cash flows, and rapid growth rates make standard earnings-based multiples unreliable. This section covers the metrics, multiples, and early-stage methods needed to value these firms.

**Cross-references:** New Venture Management (Opportunity Screening, Lean Startup), Business Strategy (competitive advantage, moats), Managerial Finance (NPV/IRR), Business Decision Models (Monte Carlo simulation for scenario analysis).

---

### 6.3.1 Key SaaS Metrics

#### ARR (Annual Recurring Revenue)
```
ARR = MRR × 12
```
- **MRR** = Monthly Recurring Revenue = sum of all active subscription revenue in a given month
- Excludes one-time fees, professional services, and usage-based overages (unless contracted)
- ARR is the foundational top-line metric for SaaS valuation; it replaces traditional revenue in most SaaS multiples
- **Why it matters:** ARR reflects predictable, contracted revenue and is the denominator in most SaaS valuation multiples

#### NRR (Net Revenue Retention)
```
NRR = (Beginning ARR + Expansion - Contraction - Churn) / Beginning ARR × 100
```

| Component | Definition |
|-----------|------------|
| **Beginning ARR** | ARR from existing customers at start of period |
| **Expansion** | Revenue gained from upsells, cross-sells, price increases within existing customers |
| **Contraction** | Revenue lost from downgrades within existing customers |
| **Churn** | Revenue lost from customers who cancelled entirely |

**Benchmarks:**
| NRR Range | Interpretation |
|-----------|---------------|
| > 130% | Elite (e.g., Snowflake, Twilio at peak) |
| > 120% | Best-in-class |
| > 110% | Excellent |
| 100-110% | Good — existing customers stable |
| < 100% | Leaky bucket — losing more than gaining from existing base |

**Key insight:** NRR > 100% means the company grows even without acquiring new customers. This is the single most important indicator of product-market fit and pricing power in SaaS.

#### Rule of 40
```
Rule of 40 Score = Revenue Growth Rate (%) + Profit Margin (%)
```
- **Target:** Score >= 40 indicates a healthy SaaS company
- **Profit Margin** typically uses EBITDA margin or FCF margin
- Allows trade-off: a company growing at 60% with -20% margin (score = 40) is valued comparably to one growing at 20% with +20% margin (score = 40)

| Score | Interpretation |
|-------|---------------|
| >= 60 | Elite — commands premium multiples |
| 40-60 | Strong — healthy growth/profitability balance |
| 20-40 | Acceptable — needs improvement in growth or margins |
| < 20 | Concerning — neither growing fast nor profitable |

#### LTV (Customer Lifetime Value)
```
LTV = ARPU × Gross Margin / Churn Rate
```

| Variable | Definition |
|----------|------------|
| **ARPU** | Average Revenue Per User (or Account) per period |
| **Gross Margin** | Revenue minus cost of delivering the service (typically 70-85% for SaaS) |
| **Churn Rate** | Percentage of customers (or revenue) lost per period |

**Example:**
```
ARPU = $1,000/month, Gross Margin = 80%, Monthly Churn = 2%
LTV = $1,000 × 0.80 / 0.02 = $40,000
```

#### CAC (Customer Acquisition Cost)
```
CAC = Total Sales & Marketing Expense / Number of New Customers Acquired
```
- Include all fully-loaded costs: salaries, commissions, advertising, tools, events
- Typically calculated on a quarterly or annual basis
- Some firms distinguish **blended CAC** (all customers) from **paid CAC** (excluding organic/referral)

#### LTV/CAC Ratio
```
LTV/CAC = Customer Lifetime Value / Customer Acquisition Cost
```

| Ratio | Interpretation |
|-------|---------------|
| >= 5:1 | May be under-investing in growth — could spend more to acquire customers |
| >= 3:1 | Healthy — strong unit economics |
| 1-3:1 | Caution — margins thin, may not be sustainable |
| < 1:1 | Unsustainable — spending more to acquire than customer is worth |

#### CAC Payback Period
```
CAC Payback Period (months) = CAC / (ARPU × Gross Margin)
```
- Measures how long until a customer's contribution margin repays the acquisition cost
- **Benchmark:** < 12 months excellent, < 18 months good, > 24 months concerning
- Investors prefer shorter payback because it reduces capital intensity and risk

#### Churn Rates
| Type | Formula | What It Measures |
|------|---------|-----------------|
| **Logo Churn** (Customer Churn) | Lost Customers / Beginning Customers | % of customers lost |
| **Revenue Churn** (Gross) | Lost MRR / Beginning MRR | % of revenue lost from cancellations + downgrades |
| **Net Revenue Churn** | (Lost MRR - Expansion MRR) / Beginning MRR | Net revenue impact (can be negative if expansion > churn) |

**Benchmarks:**
| Segment | Acceptable Annual Logo Churn |
|---------|------------------------------|
| Enterprise SaaS | < 5% |
| Mid-market SaaS | 5-10% |
| SMB SaaS | 10-20% |
| Consumer SaaS | 20-40% |

**Key insight:** Revenue churn matters more than logo churn. Losing many small customers is less damaging than losing a few large ones.

---

### 6.3.2 SaaS Valuation Multiples (by Stage)

The dominant valuation metric for SaaS companies is **EV/ARR** (Enterprise Value / Annual Recurring Revenue). Unlike EV/EBITDA or P/E, ARR multiples work for pre-profit companies.

| Stage | Typical EV/ARR Multiple | Key Characteristics |
|-------|------------------------|---------------------|
| **Seed / Series A** | 10-20x ARR | High uncertainty, option value dominates, product-market fit unproven |
| **Series B / C** | 8-15x ARR | Proven product-market fit, repeatable sales motion, scaling |
| **Growth Stage** | 6-12x ARR | Scaling rapidly, approaching or achieving profitability |
| **Public SaaS** | 5-15x ARR | Varies significantly with growth rate, margins, and market conditions |

#### Rule of Thumb for ARR Multiples
```
ARR Multiple ≈ 2 × Revenue Growth Rate (%)
```
- A company growing at 40% YoY might trade at ~8x ARR
- A company growing at 80% YoY might trade at ~16x ARR
- This relationship is approximate and adjusts for: NRR, Rule of 40 score, gross margins, TAM, competitive moat

#### Multiple Drivers (What Pushes Multiples Higher or Lower)

| Driver | Higher Multiple | Lower Multiple |
|--------|----------------|----------------|
| Revenue growth | > 40% YoY | < 20% YoY |
| NRR | > 120% | < 100% |
| Gross margin | > 80% | < 65% |
| Rule of 40 score | > 50 | < 20 |
| TAM (Total Addressable Market) | > $10B | < $1B |
| Net new ARR acceleration | Accelerating | Decelerating |
| Free cash flow margin | Positive / improving | Deeply negative / worsening |

---

### 6.3.3 Early-Stage Valuation Methods

When a company has little or no revenue, traditional DCF and multiples approaches fail. The following methods are standard for seed, angel, and early VC rounds.

#### Venture Capital Method (Most Common for VC)

**Core Idea:** Start from the end — estimate the exit value, then discount back at VC-required returns.

**Steps:**
1. **Estimate terminal value at exit** (typically 5-7 years out)
   ```
   Exit Value = Projected Revenue at Exit × Exit Multiple
   ```
2. **Discount back at VC required return** to get post-money valuation today
   ```
   Post-Money Valuation Today = Exit Value / (1 + r)^n
   ```
3. **Subtract investment to get pre-money**
   ```
   Pre-Money = Post-Money - Investment Amount
   ```
4. **Calculate ownership**
   ```
   VC Ownership % = Investment / Post-Money Valuation
   ```

**VC Required Returns by Stage:**
| Stage | Required Annual Return | Rationale |
|-------|----------------------|-----------|
| Seed | 30-50% | Very high failure rate (~90%+), illiquidity, long hold |
| Series A | 20-30% | High failure rate (~70%+), product risk |
| Series B | 15-25% | Execution risk, scaling risk |
| Growth / Pre-IPO | 10-20% | Lower risk, closer to exit |

**Example:**
```
Projected Revenue in Year 5: $50M
Exit Multiple: 8x revenue
Exit Value: $400M

VC required return (Series A): 25%
Post-Money Today: $400M / (1.25)^5 = $131.1M
Investment: $10M
Pre-Money: $131.1M - $10M = $121.1M
VC Ownership: $10M / $131.1M = 7.6%
```

#### Scorecard Method

**Core Idea:** Adjust the average pre-money valuation for the region/stage by comparing the startup to peer characteristics.

**Steps:**
1. Determine average pre-money valuation for comparable deals (e.g., $5M for seed in target market)
2. Score the target company against weighted factors:

| Factor | Weight | Range |
|--------|--------|-------|
| Strength of management team | 30% | 0.5x - 1.5x |
| Size of opportunity (TAM) | 25% | 0.5x - 1.5x |
| Product/technology | 15% | 0.5x - 1.5x |
| Competitive environment | 10% | 0.5x - 1.5x |
| Marketing/sales channels | 10% | 0.5x - 1.5x |
| Need for additional investment | 5% | 0.5x - 1.5x |
| Other (timing, regulatory) | 5% | 0.5x - 1.5x |

3. Multiply: Adjusted Valuation = Average Pre-Money × Sum of (Weight × Score)

#### Berkus Method

**Core Idea:** Assign a dollar value (up to a cap, typically $500K each) to each major risk element the startup has addressed.

| Risk Element | If Addressed (Up to) | What It Validates |
|-------------|----------------------|-------------------|
| Sound idea / business model | $500K | Basic value proposition |
| Prototype / technology | $500K | Technology risk reduced |
| Quality management team | $500K | Execution risk reduced |
| Strategic relationships | $500K | Market access / partnerships |
| Product rollout / early sales | $500K | Market risk reduced |
| **Maximum Pre-Revenue Valuation** | **$2.5M** | |

**Note:** The Berkus Method is most applicable at the angel/pre-seed stage. It provides a quick, structured way to assign value before revenue exists. Dollar caps vary by market (higher in SF/NYC, lower in smaller markets).

#### Pre-Money / Post-Money Mechanics

These are fundamental to every venture investment:

```
Post-Money Valuation = Pre-Money Valuation + Investment Amount
Investor Ownership % = Investment Amount / Post-Money Valuation
Founder Ownership % = Pre-Money Valuation / Post-Money Valuation
```

**Example:**
```
Pre-Money: $8M
Investment: $2M
Post-Money: $8M + $2M = $10M
Investor owns: $2M / $10M = 20%
Founders retain: $8M / $10M = 80%
```

**Dilution across rounds:** Each subsequent round dilutes earlier investors unless they participate pro-rata.
```
Post-Round Ownership = Pre-Round Ownership × (1 - New Investor %)
```

---

### 6.3.4 SAFE & Convertible Note Terms

SAFEs (Simple Agreement for Future Equity) and convertible notes are the most common instruments for early-stage (pre-priced round) financing. They defer valuation to a future priced round.

#### SAFE (Simple Agreement for Future Equity)
- **Not debt** — no interest rate, no maturity date, no repayment obligation
- Created by Y Combinator (2013) to simplify seed investing
- Converts to equity at the next priced round

#### Convertible Note
- **Is debt** — has interest rate (typically 2-8%), maturity date (12-24 months)
- Converts to equity at the next priced round
- If no priced round before maturity, the note may be repaid or renegotiated

#### Key Terms

| Term | Definition | Typical Range |
|------|------------|---------------|
| **Valuation Cap** | Maximum valuation at which the instrument converts to equity (protects early investor from excessive dilution) | $2M - $20M+ (varies by stage/market) |
| **Discount Rate** | Percentage discount to the price-per-share in the next priced round | 15-25% (most common: 20%) |
| **Conversion Trigger** | Event that causes conversion (typically a qualified financing above a minimum threshold) | Varies by agreement |

#### How Conversion Works

The SAFE or note converts at the **lower of:**
1. The valuation cap price
2. The discount to the priced round price

```
Cap Price Per Share = Valuation Cap / Pre-Money Shares Outstanding
Discount Price Per Share = Priced Round Price × (1 - Discount Rate)
Conversion Price = MIN(Cap Price, Discount Price)
Shares Issued = Investment Amount / Conversion Price
```

**Example:**
```
SAFE terms: $5M cap, 20% discount
Investment: $500K
Priced round (Series A): $10M pre-money, $1.00/share

Cap Price: $5M / 10M shares = $0.50/share
Discount Price: $1.00 × (1 - 0.20) = $0.80/share
Conversion Price: MIN($0.50, $0.80) = $0.50/share
Shares Issued: $500K / $0.50 = 1,000,000 shares

(Investor effectively enters at $5M valuation, not $10M)
```

**Key insight for valuation:** SAFEs and convertible notes create future dilution that must be modeled in cap table analysis. A company with $2M in outstanding SAFEs at a $5M cap will see significant dilution at the priced round, reducing the effective pre-money for existing shareholders.

---

### 6.3.5 Integrating SaaS Metrics with Traditional Valuation

SaaS metrics complement (not replace) traditional valuation methods:

| Valuation Approach | How SaaS Metrics Integrate |
|-------------------|---------------------------|
| **DCF** | Use ARR growth to project revenues; model gross margin expansion; NRR informs customer-base revenue trajectory; churn rate drives terminal growth assumptions |
| **Relative Valuation** | Use EV/ARR as primary multiple; Rule of 40 and NRR as comp-matching criteria (replace traditional growth/risk/margin drivers) |
| **VC Method** | ARR growth rate and NRR validate exit revenue projections; LTV/CAC validates unit economics and scalability of go-to-market |
| **Sum of Parts** | Value recurring revenue stream separately from professional services or usage-based revenue at different multiples |

**Decision Framework: Which Method to Use**
| Company Stage | Primary Method | Secondary Method |
|--------------|---------------|-----------------|
| Pre-revenue | Berkus, Scorecard | VC Method |
| < $1M ARR | VC Method | Scorecard |
| $1M - $10M ARR | VC Method, EV/ARR comps | DCF (scenario-based) |
| $10M - $100M ARR | EV/ARR comps, DCF | VC Method (for exit modeling) |
| > $100M ARR | DCF, EV/ARR comps | Sum of Parts, Rule of 40 screening |

---

## 6.4 Non-Operating Assets

### Types

**1. Excess Cash & Marketable Securities**
- Operating cash = ~2% of revenues
- Everything else = non-operating
- Value at face value (or market value if securities)

**2. Holdings in Other Firms**

| Ownership | Accounting Method | Balance Sheet | Income Statement |
|-----------|-------------------|---------------|------------------|
| < 20% | Cost method | Historical cost | Dividends only |
| 20-50% | Equity method | Historical cost | Share of profits |
| > 50% | Consolidated | Full consolidation | Full consolidation |

**3. Other Non-Operating Assets**
- Excess real estate
- Unutilized operating assets
- Tax loss carryforwards

### Equity Valuation with Subsidiaries
```
  Value of core operating assets (DCF of FCFF)
+ Value of excess cash & non-operating assets
+ Value of minority holdings (% × subsidiary value)
- Value of non-controlling interests ((1-%) × consolidated subsidiary)
= Value of Firm
- Value of Debt
= Value of Equity
```

---

## 6.4 Tax Loss Carryforwards

### Concept
- Deferred tax asset on balance sheet
- Represents future tax savings
- Most relevant for firms with historical losses

### Valuation Considerations
1. Likelihood of use (will firm be profitable?)
2. Timing of use (sooner = more valuable)
3. Don't double-count (if already in forecasts)

---

## 6.5 Flexibility and Real Options

### Concept
- **Uncertainty**: Future is hard to predict
- **Flexibility**: Ability to choose between alternatives based on events

**Key Insight**: Only flexibility adds value, not uncertainty alone.

### Types of Real Options

| Option Type | Description | Value When |
|-------------|-------------|------------|
| **Investment Timing** | Wait to invest until uncertainty resolves | High uncertainty, reversible |
| **Option to Expand** | Scale up if successful | Uncertain demand |
| **Option to Suspend** | Pause operations temporarily | Variable demand/costs |
| **Option to Abandon** | Exit if unsuccessful | High downside risk |

### What Drives Real Option Value
1. **Volatility of outcomes** - Higher volatility → Higher option value
2. **Time until decision** - More time → More value
3. **Cost of exercise** - Lower cost → Higher value

### Real Option Valuation Example

**Simplicity Inc.:**
- Decision in 1 year whether to invest $3M
- If successful (50%): $500k/year forever
- If unsuccessful (50%): $100k/year forever
- WACC = 15%

**Without Flexibility (DCF):**
```
Expected CF = 0.5(500) + 0.5(100) = $300k/year
PV = -3,000/(1.15) + 300/0.15 = $285,714
```

**With Flexibility (Option to Wait):**
```
If successful: PV = -3,000/(1.15) + 500/0.15 = $4,285,714 → Invest
If unsuccessful: PV = -3,000/(1.15) + 100/0.15 = -$3,714,286 → Don't invest

With option:
PV = 0.5($4,285,714) + 0.5($0) = $2,142,857
```

**Value of Deferral Option:**
```
$2,142,857 - $285,714 = $1,857,143
```

---

# PART 7: VALUATION PROJECT REQUIREMENTS

## 7.1 Project Overview

| Attribute | Details |
|-----------|---------|
| **Type** | Individual project (not group) |
| **Weight** | 40% of total course grade |
| **Purpose** | Integrates nearly everything learned |
| **Submission** | Canvas by 11:59 PM Pacific |

## 7.2 Part 1: Multiples Valuation (15%)

**Due:** Monday, May 5, 11:59 PM Pacific

**Length:** 1-2 pages including tables (+ optional appendices)

### Requirements
1. **Select comparable firms** with justification
2. **Identify key value drivers** for chosen multiples
3. **Calculate multiples** from comp set (mean/median)
4. **Estimate valuation** based on multiples analysis

### What to Include
- Comp selection criteria and rationale
- Key value driver comparison
- Multiple calculations with source data
- Final valuation estimate with range

---

## 7.3 Part 2: Financial Data & Historical FCFF (8%)

**Due:** Monday, May 19, 11:59 PM Pacific

**Length:** 2-3 pages plus appendices

### Requirements
1. **Gather historical financial data** (3-5 years)
2. **Calculate FCFF** for each historical year
3. **Compute ROIC** for each year
4. **Analyze trends**

### FCFF Calculation Steps
| Step | Calculation |
|------|-------------|
| 1 | τ = Tax Expense / EBT |
| 2 | NOPAT = EBIT × (1 - τ) |
| 3 | NOWC = OCA - OCL |
| 4 | ΔNOWC = NOWC_t - NOWC_(t-1) |
| 5 | Net Investment = CAPEX - Dep + ΔNOWC |
| 6 | FCFF = NOPAT - Net Investment |

### Data Sources
- **SEC EDGAR**: 10-K, 10-Q filings
- **Capital IQ**: Standardized data, analyst forecasts

---

## 7.4 Part 3: Projected FCFF & DCF Valuation (17%)

**Due:** Thursday, June 5, 11:59 PM Pacific

**Length:** 2-3 pages plus appendices

### Requirements

**1. Revenue Projections**
- Bottom-up or top-down approach
- Growth rate assumptions with justification
- Link to valuation story

**2. FCFF Forecasts**
- Project 5-10 years
- Use ratios to revenues
- Show calculations for each year

**3. Terminal Value**
- Terminal growth rate (g): 3-4%
- Terminal ROIC: Benchmark to industry
- Gordon Growth Model calculation

**4. WACC Calculation**
- Cost of equity (CAPM)
- Cost of debt (spread approach)
- Capital structure weights
- Tax rate

**5. Valuation Calculation**
```
  Enterprise Value (PV of FCFF + PV of TV)
+ Excess cash
+ Other non-operating assets
- Debt
= Equity Value
÷ Shares Outstanding
= Equity Value per Share
```

**6. Comparison & Conclusion**
- Compare to Part 1 multiples
- Compare to current market price
- Sensitivity analysis (recommended)
- Final recommendation with supporting story

---

# PART 8: SYMBOLS & ABBREVIATIONS GLOSSARY

## English Letters/Abbreviations

| Symbol | Definition |
|--------|------------|
| AP | Accounts Payable |
| AR | Accounts Receivable |
| b | % of NOPAT reinvested in IC |
| C | Bond coupon |
| CAPEX | Capital Expenditure |
| CF | Cash Flow |
| COGS | Cost of Goods Sold |
| D/E | Debt to Equity ratio |
| DCF | Discounted Cash Flow |
| Dep | Depreciation |
| E | Earnings (= Net Income / # shares) |
| EBIT | Earnings Before Interest and Taxes |
| EBITDA | Earnings Before Interest, Taxes, Depreciation & Amortization |
| E(FCFE) | Expected Free Cash Flow to Equity |
| EV | (Net) Enterprise Value |
| EV/IC₀ | Enterprise Value / Beginning Invested Capital |
| EV/NOPAT₁ | Enterprise Value / Next Year's NOPAT |
| EV/S₁ | Enterprise Value / Next Year's Sales |
| FCFE | Free Cash Flow to Equity |
| FCFF | Free Cash Flow to the Firm |
| g | Growth rate |
| IC | Invested Capital (= Operating Assets) |
| IPO | Initial Public Offering |
| k | Plowback ratio (% of NI reinvested) |
| M&A | Merger and Acquisition |
| MRP | Market Risk Premium = (r_m - r_f) |
| NI | Net Income |
| NOPAT | Net Operating Profit After Taxes |
| NOWC | Net Operating Working Capital |
| OC | Operating Costs |
| OCA | Operating Current Assets |
| OCL | Operating Current Liabilities |
| P | Stock Price |
| P/B | Price/Book ratio |
| PE | Private Equity |
| P/E | Price/Earnings ratio |
| P/E₁ | Forward P/E (next year's earnings) |
| P/E₀ | Current P/E (last year's earnings) |
| PP&E | Property, Plant, and Equipment |
| P/S | Price/Sales ratio |
| r | Discount rate |
| r_d | Cost of Debt |
| r_e | Cost of Equity |
| r_f | Risk-free rate |
| r_m | Return on the Market |
| ROE | Return on Equity |
| ROIC | Return on Invested Capital |
| SEO | Secondary Equity Offering |
| SG&A | Selling, General & Administrative expenses |
| t | Tax rate |
| TV | Terminal Value |
| V | Total Value of Firm = E + D |
| VC | Venture Capital |
| WACC | Weighted Average Cost of Capital |
| y | Bond yield |

## Greek Letters/Symbols

| Symbol | Name | Definition |
|--------|------|------------|
| β | Beta | Asset's sensitivity to systematic risk |
| Δ | Delta | Change |
| Σ | Sigma | Summation |
| τ | Tau | Effective tax rate = Taxes Paid / EBT |

---

# PART 9: DATA SOURCES & TOOLS

## 9.1 Primary Data Sources

| Source | Content | Access |
|--------|---------|--------|
| **SEC EDGAR** | 10-K, 10-Q filings, footnotes | https://www.sec.gov/edgar/search-and-access |
| **Capital IQ** | Standardized financials, analyst forecasts, betas | https://johnson.library.cornell.edu/ |
| **Bloomberg** | Real-time prices, yields, analytics | Terminal access |
| **FRED** | Credit spreads, Treasury yields | https://fred.stlouisfed.org/ |
| **WSJ** | Treasury yields, market data | https://www.wsj.com/market-data/bonds |

## 9.2 Capital IQ Key Locations

| Data | Navigation |
|------|------------|
| Financial statements | Financials → Annual/Quarterly |
| Beta | Company Summary → Tearsheet |
| Credit rating | Fixed Income → Summary → "Local Currency LT" |
| Bond prices | Fixed Income → Securities Summary |
| Analyst forecasts | Estimates |

## 9.3 FRED Credit Spread Data

**URL:** https://fred.stlouisfed.org/categories/32348?t=option-adjusted%20spread

| Series | Description |
|--------|-------------|
| BAMLC0A1CAAA | AAA Corporate Spread |
| BAMLC0A2CAA | AA Corporate Spread |
| BAMLC0A3CA | A Corporate Spread |
| BAMLC0A4CBBB | BBB Corporate Spread |
| BAMLH0A1HYBB | BB High Yield Spread |
| BAMLH0A2HYB | B High Yield Spread |

---

# PART 10: BEST PRACTICES & COMMON PITFALLS

## 10.1 Relative Valuation Best Practices

✅ **Do:**
- Match comp firms on key value drivers (growth, risk, margins)
- Use multiple multiples for cross-validation
- Consider both mean and median
- Adjust for special circumstances (IPO discount, control premium)

❌ **Don't:**
- Use only industry classification for comp selection
- Ignore fundamental differences between comps
- Mix trading and transaction multiples without adjustment
- Forget to check for outliers

## 10.2 DCF Best Practices

✅ **Do:**
- Link projections to business story
- Use ROIC as sanity check
- Sensitivity analysis on key assumptions
- Cross-check with relative valuation

❌ **Don't:**
- Use terminal growth rate > long-term economic growth
- Ignore capital structure changes
- Project unrealistic margins indefinitely
- Forget non-operating assets and liabilities

## 10.3 WACC Best Practices

✅ **Do:**
- Use current market values for weights
- Use current risk-free rate (10-year Treasury)
- Unlever/relever betas when comparing firms
- Use marginal tax rate

❌ **Don't:**
- Use book values for capital structure
- Use historical average risk-free rates
- Compare levered betas across different capital structures
- Use effective tax rate for WACC

## 10.4 Forecasting Best Practices

✅ **Do:**
- Use 3-5 years of historical data
- Check ratios for stability before projecting
- Consider industry trends and competitive dynamics
- Document all assumptions

❌ **Don't:**
- Project current extraordinary items
- Assume constant growth forever without justification
- Ignore working capital needs
- Extrapolate short-term trends indefinitely

---

# PART 11: ACADEMIC INTEGRITY REQUIREMENTS

## 11.1 Course Requirements

- All work must be original
- Cannot use spreadsheets/code/analyses from others
- Cannot use materials from previous students
- Must cite all outside sources

## 11.2 GAI (Generative AI) Policy

**Permitted Uses:**
- Brainstorming initial ideas
- Editing for grammar and clarity

**Required:**
- Must disclose any GAI use in submission
- Example: "We used ChatGPT to assist in editing our final draft"

**Prohibited:**
- Submitting GAI-generated work as your own
- Using GAI for quantitative calculations
- Using GAI to generate analysis without disclosure

## 11.3 Late Policy

- **Penalty:** 5% per day of lateness
- All submissions via Canvas by 11:59 PM Pacific

---

# APPENDIX A: QUICK REFERENCE FORMULAS

## Equity Valuation
```
P = E₁(1-k) / (r_e - g)
P/E₁ = (1-k) / (r_e - g)
P/S₁ = Profit Margin × P/E₁
P/B₀ = (ROE - g) / (r_e - g)
```

## Enterprise Valuation
```
EV = MV Equity + MV Debt - Excess Cash
EV/NOPAT₁ = (1-b) / (WACC - g)
EV/S₁ = Operating Margin × EV/NOPAT₁
```

## Free Cash Flow
```
FCFF = NOPAT - Net Investment
NOPAT = EBIT × (1 - τ)
Net Investment = CAPEX - Dep + ΔNOWC
NOWC = OCA - OCL
```

## Cost of Capital
```
WACC = (E/V) × r_E + (D/V) × r_D × (1 - τ)
r_E = r_f + β × (r_m - r_f)
r_D = r_f + Credit Spread
```

## Beta Adjustment
```
β_U = β_L / [1 + (D/E)(1 - τ)]
β_L = β_U × [1 + (D/E)(1 - τ)]
```

## Terminal Value
```
TV_T = FCFF_(T+1) / (WACC - g)
TV_T = NOPAT_(T+1) × (1 - g/ROIC) / (WACC - g)
```

## Growth Relationships
```
g = k × ROE (for equity)
g = b × ROIC (for firm)
b = g / ROIC
```

---

*Last Updated: Based on NBAB 6560/MBQC 804 Spring 2025 Course Materials*
*Professor Pamela Moulton, Cornell Johnson Graduate School of Management*
