# Finance -- Knowledge Base

> Integrates Financial Accounting, Managerial Accounting, Managerial Finance, Corporate Financial Policy, Valuation, and Investment Banking.

---

## 1. Financial Accounting

### The Accounting Equation
```
Assets = Liabilities + Stockholders' Equity
```

### GAAP Principles
- **Revenue Recognition (ASC 606):** 5-step model
  1. Identify the contract
  2. Identify performance obligations
  3. Determine transaction price
  4. Allocate price to obligations
  5. Recognize revenue when/as obligations satisfied
- **Matching Principle:** Expenses recognized in same period as related revenue
- **Historical Cost:** Assets recorded at acquisition cost
- **Conservatism:** When in doubt, recognize losses early, gains late

### Financial Statements
- **Income Statement:** Revenue → COGS → Gross Profit → Operating Expenses → Operating Income → Net Income
- **Balance Sheet:** Assets (Current + Non-current) = Liabilities (Current + Long-term) + Equity
- **Cash Flow Statement:** Operating + Investing + Financing = Net Change in Cash
- **Statement of Stockholders' Equity:** Beginning balance + Net income - Dividends ± Other comprehensive income

### Key Adjusting Entries
- **Accrued Revenue:** DR Accounts Receivable / CR Revenue
- **Accrued Expense:** DR Expense / CR Accounts Payable
- **Deferred Revenue:** DR Unearned Revenue / CR Revenue (as earned)
- **Prepaid Expense:** DR Expense / CR Prepaid (as consumed)
- **Depreciation:** DR Depreciation Expense / CR Accumulated Depreciation

### Inventory Methods
- **FIFO:** First In, First Out -- higher ending inventory, lower COGS in rising prices
- **LIFO:** Last In, First Out -- lower ending inventory, higher COGS (tax benefit)
- **Weighted Average:** Blended cost per unit

### Investment Accounting
- **Trading Securities:** Fair value, gains/losses on income statement
- **Available-for-Sale:** Fair value, gains/losses in OCI
- **Held-to-Maturity:** Amortized cost
- **Equity Method (20-50% ownership):** Proportional share of income

### Cash Flow Classification
| Activity | Examples |
|----------|----------|
| Operating | Net income adjustments, AR/AP changes, depreciation add-back |
| Investing | Purchase/sale of assets, acquisitions |
| Financing | Debt issuance/repayment, stock issuance, dividends |

---

## 2. Managerial Accounting

### Cost Behavior
- **Variable Costs:** Change proportionally with volume (materials, direct labor)
- **Fixed Costs:** Constant regardless of volume (rent, salaries)
- **Mixed Costs:** Have both components (utilities)
- **Step Costs:** Fixed within a range, jump at thresholds

### Cost-Volume-Profit (CVP) Analysis
```
Break-Even (units) = Fixed Costs / (Price - Variable Cost per Unit)
Break-Even ($) = Fixed Costs / Contribution Margin Ratio
CM Ratio = (Price - Variable Cost) / Price
Target Profit Units = (Fixed Costs + Target Profit) / CM per Unit
```

### Activity-Based Costing (ABC)
1. Identify activities that consume resources
2. Assign costs to activity cost pools
3. Determine cost drivers for each pool
4. Calculate activity rates
5. Assign costs to products based on activity consumption

**ABC vs. Traditional:** ABC allocates overhead based on actual cost drivers, not arbitrary volume measures. More accurate for diverse product lines.

### Standard Costing & Variance Analysis
```
Material Price Variance = (Actual Price - Standard Price) × Actual Quantity
Material Quantity Variance = (Actual Qty - Standard Qty) × Standard Price
Labor Rate Variance = (Actual Rate - Standard Rate) × Actual Hours
Labor Efficiency Variance = (Actual Hours - Standard Hours) × Standard Rate
```

### Capital Budgeting
- **NPV:** Sum of discounted future cash flows minus initial investment. Accept if NPV > 0.
- **IRR:** Discount rate that makes NPV = 0. Accept if IRR > cost of capital.
- **Payback Period:** Time to recover initial investment. Ignores time value and cash flows after payback.
- **Profitability Index:** NPV / Initial Investment. Useful for capital rationing.

### Economic Value Added (EVA)
```
EVA = NOPAT - (Capital × WACC)
EVA = Operating Profit × (1 - Tax Rate) - (Total Capital × WACC)
```
Where: NOPAT = Net Operating Profit After Tax ($), Capital = Total Invested Capital ($), WACC = Weighted Average Cost of Capital (%).

Positive EVA = Creating shareholder value. Negative EVA = Destroying value.

### Target Costing
```
Target Cost = Market Price - Required Profit Margin
```
Design product to meet target cost, not cost-plus pricing.

---

## 3. Managerial Finance

### Time Value of Money
```
FV = PV × (1 + r)^n
PV = FV / (1 + r)^n
Annuity PV = PMT × [(1 - (1+r)^-n) / r]
Perpetuity PV = PMT / r
Growing Perpetuity PV = PMT / (r - g)
```
Where: PV/FV = present/future value ($), r = discount rate (decimal), n = number of periods, PMT = payment per period ($), g = growth rate (decimal).

### Bond Valuation
```
Bond Price = Σ [Coupon / (1+r)^t] + [Face Value / (1+r)^n]
```
- Price and yield move inversely
- Duration measures interest rate sensitivity
- Longer maturity = more sensitive to rate changes

### CAPM (Capital Asset Pricing Model)
```
E(R) = Rf + β × (Rm - Rf)
```
- Rf = Risk-free rate
- β = Systematic risk (market sensitivity)
- Rm - Rf = Market risk premium (~5-7%)

### Portfolio Theory
- **Diversification:** Unsystematic risk can be eliminated; systematic cannot
- **Efficient Frontier:** Set of portfolios offering highest return for given risk
- **Sharpe Ratio:** (Portfolio Return - Risk-Free Rate) / Portfolio Std Dev

### Efficient Market Hypothesis (EMH)
- **Weak Form:** Prices reflect all past trading data
- **Semi-Strong:** Prices reflect all publicly available information
- **Strong:** Prices reflect all information including private

### Cost of Capital
```
WACC = (E/V × Re) + (D/V × Rd × (1-T))
```
Where: E = equity value, D = debt value, V = E+D, Re = cost of equity, Rd = cost of debt, T = tax rate

---

## 4. Corporate Financial Policy

### Capital Structure Theory

**Modigliani-Miller (No Taxes):** Capital structure is irrelevant -- firm value is independent of how it's financed.

**M&M (With Taxes):** Debt creates tax shield, so optimal structure is 100% debt (in theory).
```
Value of Tax Shield = Tax Rate × Debt
```

**Trade-Off Theory:** Optimal leverage balances tax benefits of debt against costs of financial distress.

**Pecking Order Theory:** Firms prefer: (1) Internal funds → (2) Debt → (3) Equity. Not about optimal structure but information asymmetry.

### Leverage Decisions
- **Financial Leverage:** Use of debt magnifies returns (and losses)
- **Operating Leverage:** High fixed costs magnify operating income sensitivity
- **Combined Leverage:** DOL × DFL = Total risk amplification

### Dividend & Payout Policy
- **Dividend Irrelevance (M&M):** In perfect markets, dividend policy doesn't affect value
- **Bird-in-Hand:** Investors prefer certain dividends over uncertain capital gains
- **Tax Clientele:** Different investors prefer different payout policies based on tax treatment
- **Signaling:** Dividend changes signal management's confidence in future earnings
- **Share Buybacks:** Tax-advantaged alternative to dividends; increases EPS

### Cash Management
- **Optimal Cash = f(Transaction costs, Opportunity costs, Precautionary needs)**
- **Working Capital = Current Assets - Current Liabilities**
- **Cash Conversion Cycle = DSO + DIO - DPO**

### Merger & Acquisition Value Creation
- Sources: Revenue synergies, cost synergies, tax benefits, improved management
- **Acquirer's value creation** = Synergies captured - Premium paid
- Hubris hypothesis: Managers overpay due to overconfidence

---

## 5. Valuation

### DCF Valuation
```
Enterprise Value = Σ [FCF_t / (1 + WACC)^t] + [Terminal Value / (1 + WACC)^n]
Equity Value = Enterprise Value - Net Debt + Cash
Share Price = Equity Value / Shares Outstanding
```

### Free Cash Flow
```
FCF = EBIT × (1-T) + Depreciation - CapEx - ΔWorking Capital
   = NOPAT + Non-cash charges - Investments
```
Where: EBIT = Earnings Before Interest & Taxes, T = tax rate, CapEx = capital expenditures, ΔWorking Capital = change in net working capital.

### Terminal Value (Two Methods)
```
Gordon Growth: TV = FCF_(n+1) / (WACC - g)
Exit Multiple: TV = EBITDA_n × EV/EBITDA multiple
```
Terminal value typically = 60-80% of total enterprise value. Be very careful with growth rate assumptions.

### Relative Valuation (Trading Multiples)
| Multiple | When to Use | Calculation |
|----------|-------------|-------------|
| EV/EBITDA | Most common, capital-structure neutral | Enterprise Value / EBITDA |
| P/E | Profitable companies | Price / Earnings per Share |
| EV/Revenue | High-growth, pre-profit | Enterprise Value / Revenue |
| P/B | Financial institutions | Price / Book Value per Share |
| PEG | Growth companies | P/E / Expected Growth Rate |

### Comparable Company Analysis (Comps)
1. Select peer universe (industry, size, growth, geography)
2. Calculate trading multiples for each peer
3. Determine range (mean, median, quartiles)
4. Apply to target company's metrics
5. Adjust for company-specific differences

### Precedent Transactions
1. Identify comparable M&A deals
2. Calculate transaction multiples (include premium)
3. Adjust for market conditions at time of deal
4. Apply to current target
5. Typically yields higher values than trading comps (control premium)

### Real Options Valuation
- **Option to expand:** Value of growth opportunity
- **Option to abandon:** Value of exit flexibility
- **Option to delay:** Value of waiting for better information
- Use when: High uncertainty, staged investment, managerial flexibility

---

## 6. Investment Banking (Elective)

### LBO (Leveraged Buyout) Mechanics
```
Entry: Acquire company using mostly debt (60-80% leverage)
Operate: Improve operations, pay down debt, grow EBITDA
Exit: Sell at higher multiple or IPO (3-7 year hold)

Returns = f(Entry multiple, Exit multiple, Debt paydown, EBITDA growth)
MOIC = Exit equity / Entry equity
IRR = Annualized return rate
```

### Sources & Uses
```
Sources:               Uses:
Senior Debt   $XXM     Purchase Price  $XXM
Mezzanine     $XXM     Fees            $XXM
Sponsor Equity $XXM    Cash to B/S     $XXM
─────────────────      ─────────────────
Total Sources $XXM     Total Uses      $XXM
```

### Accretion/Dilution Analysis
```
If: Combined EPS > Acquirer's standalone EPS → Accretive (good)
If: Combined EPS < Acquirer's standalone EPS → Dilutive (bad)

Key drivers:
- P/E of acquirer vs. target
- Financing mix (cash/stock/debt)
- Synergy realization timeline
```

### Synergy Estimation
- **Revenue synergies:** Cross-sell, pricing power, market access (harder to realize)
- **Cost synergies:** Headcount, facilities, procurement, IT (easier to quantify)
- **Rule of thumb:** Market believes ~50-75% of announced synergies will materialize
- **Integration planning:** Start pre-close, day-one readiness critical

### Deal Screening Criteria
- EBITDA margin stability/growth
- Defensible market position
- Low customer concentration
- Recurring revenue characteristics
- Capital-light business model
- Clear operational improvement levers

---

## Quick Reference: When to Use What

| Situation | Framework | File Section |
|-----------|-----------|-------------|
| "Should we invest in this project?" | NPV/IRR, Capital Budgeting | Managerial Accounting |
| "What is this company worth?" | DCF + Comps + Precedents | Valuation |
| "How should we finance this?" | Trade-off theory, WACC | Corporate Financial Policy |
| "Is this acquisition accretive?" | Accretion/dilution, synergies | Investment Banking |
| "Are we creating shareholder value?" | EVA, ROIC vs WACC | Managerial Accounting |
| "What does the income statement tell us?" | Revenue recognition, matching | Financial Accounting |
| "Where is the money going?" | ABC, variance analysis | Managerial Accounting |
| "What's the right capital structure?" | M&M, trade-off, pecking order | Corporate Financial Policy |
| "What discount rate should I use?" | CAPM → WACC | Managerial Finance |
| "Should we do this LBO?" | Entry/exit multiples, MOIC, IRR | Investment Banking |
