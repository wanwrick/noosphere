# Managerial Finance — SKILL Reference
## Cornell EMBA (NCCB 5060 / MBQCB821) | Professor Mao Ye | Spring 2025

---

## Course Architecture

**7-session structure** covering the two fundamental decisions in finance:

| Session | Title | Core Concept |
|---------|-------|-------------|
| 1 | Discounted Cash Flow Valuation | Law of one price, arbitrage, TVM, PV/FV, annuities, perpetuities, NPV |
| 2 | Capital Budgeting | Forecasting cash flows (9 principles), bottom-up vs top-down approach, incremental analysis |
| 3 | Valuation | IRR rule, NPV rule, DCF valuation, relative valuation (trading multiples, transaction multiples) |
| 4 | Risk and Return | Measuring risk (variance, standard deviation), scenario analysis, time series analysis, diversification |
| 5 | CAPM & Efficient Frontier | Portfolio optimization, efficient frontier, CML, Security Market Line, beta |
| 6 | Efficient Market Hypothesis | Three forms of EMH, anomalies, rational vs behavioral finance |
| 7 | Review & Advanced Topics | Integration of all concepts, Cornell Endowment Fund case, portfolio optimization exercise |

**Two Core Decisions:**
1. **Investment Decision** (Capital Budgeting): How much to invest and in what assets/projects?
2. **Financing Decision**: Where is the money going to come from?

**Grading:** Group Project (capital budgeting project) + Final Exam

**Guest Lecture:** Kraig H. Kayser, Chairman, Cornell Board of Trustees

---

## The Big Picture: Finance as Philosophy

Professor Ye's **Four Levels of Learning:**
1. Pass the exam
2. Have an understanding of finance
3. Apply the knowledge to your financial decisions
4. Finance is a philosophy — apply it to your personal life (your biggest asset is yourself)

**Central Insight:** In finance, we view assets as streams of cash flows. Our goal is to determine the value to place on these streams.

---

## Session 1: Time Value of Money (TVM)

### Law of One Price & Arbitrage

- **Law of One Price:** Equivalent assets must have the same price in competitive markets
- **Arbitrage:** An investment strategy requiring no outlay that generates positive cash flows (free lunch)
- **No-arbitrage pricing:** The equilibrium condition that eliminates free lunches — the foundation of all valuation

### Seven Core TVM Formulas

| Formula | Expression | Excel Function |
|---------|-----------|---------------|
| **Future Value** | FV = PV × (1+r)^n | `FV(rate, nper, pmt, pv)` |
| **Present Value** | PV = FV / (1+r)^n | `PV(rate, nper, pmt, fv)` |
| **FV of Annuity** | FV = C × [(1+r)^n − 1] / r | `FV(rate, nper, pmt)` |
| **PV of Annuity** | PV = C × [1 − (1+r)^−n] / r | `PV(rate, nper, pmt)` |
| **Periodic Payment** | PMT (inverting annuity formulas) | `PMT(rate, nper, pv, fv)` |
| **Perpetuity** | PV = C / r | Manual calc |
| **Growing Perpetuity** | PV = C / (r − g) | Manual calc |
| **NPV** | NPV = Σ [CFt / (1+r)^t] | `NPV(rate, values)` |

**Excel Convention:** Investment is NEGATIVE, payout is POSITIVE.

### Key Concepts
- **Discount rate (r)** = opportunity cost of capital (reflects time value + risk)
- **Compounding:** Interest on interest (exponential growth)
- **NPV Rule:** Accept project if NPV > 0; reject if NPV < 0

---

## Session 2: Capital Budgeting

### The Nine Principles of Forecasting Cash Flows

**Three Philosophical Principles:**
1. **Forget sunk costs** — Already spent money is irrelevant to future decisions
2. **Include opportunity costs** — Value of next-best alternative forgone
3. **Include externalities** — Spillover effects on other projects/products (cannibalization)

**One Finance Principle:**
4. **Separate investment and financing decisions** — Evaluate the project on its own merits; don't mix in how it's financed

**Five Implementation Details:**
5. **Depreciation is not a cash flow** — But it affects taxes (tax shield)
6. **Include investments in fixed assets** (CapEx)
7. **Include changes in operating working capital** (NWC)
8. **Use incremental cash flows** — Only cash flows that change because of the project
9. **Use after-tax cash flows**

### Cash Flow Calculation Template

```
  Revenue
− Cost of Goods Sold
− Depreciation
− Selling, General & Administrative
= Operating Profit (EBIT)
− Cash Taxes on Operating Profit
= Net Operating Profit After Tax (NOPAT)
+ Depreciation (add back non-cash)
− Capital Expenditures
− Increase in Working Capital
= Free Cash Flow (FCF)
```

### Two Approaches to FCF

| Approach | Method |
|----------|--------|
| **Bottom-Up** | Start with Net Income, add back non-cash charges, adjust for working capital |
| **Top-Down** | Start with Revenue, subtract all cash costs, subtract taxes |

### Capital Budgeting Decision Tools

| Tool | Rule | Advantage | Limitation |
|------|------|-----------|-----------|
| **NPV** | Accept if NPV > 0 | Accounts for TVM, gives dollar value added | Requires estimating discount rate |
| **IRR** | Accept if IRR > cost of capital | Intuitive percentage return | Multiple IRRs possible; can mislead with mutually exclusive projects |
| **Payback Period** | Accept if payback < target | Simple | Ignores TVM and cash flows after payback |
| **Profitability Index** | Accept if PI > 1 | Useful for capital rationing | Can mislead with mutually exclusive projects |

### Key Applications
- **Make vs Buy (EAC):** Compare Equivalent Annual Cost of making vs buying; normalize projects of different lives
- **Toothpaste Example:** Full bottom-up capital budgeting case

---

## Session 3: Valuation

### Three Valuation Approaches

| Approach | Method | When to Use |
|----------|--------|------------|
| **DCF (Discounted Cash Flow)** | Forecast FCFs, discount at WACC, add terminal value | Gold standard for intrinsic valuation |
| **Trading Multiples** | Use current market prices of comparable firms | Quick relative valuation |
| **Transaction Multiples** | Use prices from past M&A deals | Valuation with control premium |

### DCF Valuation Framework
```
Enterprise Value = Σ [FCFt / (1+WACC)^t] + Terminal Value / (1+WACC)^n

Terminal Value = FCF(n+1) / (WACC − g)    [Gordon Growth Model]

Equity Value = Enterprise Value − Net Debt
```

### Common Trading Multiples

| Multiple | Formula | What It Measures |
|----------|---------|-----------------|
| **P/E** | Price / EPS | How much investors pay per dollar of earnings |
| **EV/EBITDA** | Enterprise Value / EBITDA | Valuation relative to operating cash flow proxy |
| **EV/Revenue** | Enterprise Value / Revenue | Valuation relative to top line (high-growth firms) |
| **P/B** | Price / Book Value | Market vs accounting value |

### IRR vs NPV Decision Rules

- **NPV Rule:** Accept if NPV > 0 (always reliable)
- **IRR Rule:** Accept if IRR > cost of capital (can give wrong answer with non-conventional cash flows or mutually exclusive projects)
- **When they conflict:** Always follow NPV

### Value Creation Principles
- A firm creates value when it invests in projects with returns exceeding the cost of capital
- **Growth without value creation:** Reinvesting at returns below cost of capital destroys value even if the firm grows
- **Reinvestment matters:** Value = existing assets + NPV of future growth opportunities (PVGO)

---

## Session 4: Risk and Return

### Measuring Return
- **Expected Return:** E(r) = Σ [probability × return] (scenario analysis) OR average of historical returns (time series)
- **Holding Period Return:** HPR = (End Price − Begin Price + Dividends) / Begin Price

### Measuring Risk
- **Variance:** σ² = Σ [p × (r − E(r))²]
- **Standard Deviation:** σ = √(σ²) — the primary measure of risk
- **Risk = Bad:** Higher variance means more uncertainty about outcomes

### Two Assets: Diversification
- **Covariance:** Cov(r₁, r₂) = Σ [p × (r₁ − E(r₁)) × (r₂ − E(r₂))]
- **Correlation:** ρ = Cov(r₁, r₂) / (σ₁ × σ₂), ranges from −1 to +1
- **Portfolio Variance:** σ²p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(r₁,r₂)

**Key Insight:** When ρ < 1, combining assets reduces portfolio risk below the weighted average of individual risks. This is the **free lunch of diversification**.

### Many Assets: Systematic vs Unsystematic Risk
- **Diversifiable (unsystematic) risk:** Firm-specific risk that disappears in a large portfolio
- **Non-diversifiable (systematic) risk:** Market-wide risk that cannot be diversified away
- **Only systematic risk is compensated** with higher expected returns

---

## Session 5: CAPM & Efficient Frontier

### The Efficient Frontier
- Set of portfolios offering the **maximum expected return for a given level of risk**
- Adding the risk-free asset creates the **Capital Market Line (CML)** — the best possible risk-return tradeoff
- **Tangency portfolio** = the market portfolio (optimal mix of risky assets)

### Capital Asset Pricing Model (CAPM)

```
E(rᵢ) = rf + βᵢ × [E(rM) − rf]
```

| Component | Meaning |
|-----------|---------|
| E(rᵢ) | Expected return of asset i (= cost of equity) |
| rf | Risk-free rate |
| βᵢ | Beta — sensitivity of asset i to market movements |
| E(rM) − rf | Market risk premium |

### Beta (β)

```
βᵢ = Cov(rᵢ, rM) / σ²M = ρ(rᵢ, rM) × σᵢ / σM
```

| Beta | Meaning |
|------|---------|
| β = 1 | Moves with the market |
| β > 1 | More volatile than the market (aggressive) |
| β < 1 | Less volatile than the market (defensive) |
| β = 0 | Uncorrelated with the market |

### Security Market Line (SML) vs Capital Market Line (CML)

| Feature | CML | SML |
|---------|-----|-----|
| X-axis | Total risk (σ) | Systematic risk (β) |
| Applies to | Efficient portfolios only | All assets and portfolios |
| Slope | Sharpe ratio of market portfolio | Market risk premium |

### WACC (Weighted Average Cost of Capital)
```
WACC = (E/V) × rE + (D/V) × rD × (1 − T)
```
Where: E = equity, D = debt, V = E+D, rE from CAPM, rD = cost of debt, T = tax rate

---

## Session 6: Efficient Market Hypothesis (EMH)

### Three Forms of Market Efficiency

| Form | Information Reflected in Prices | Implication |
|------|-------------------------------|------------|
| **Weak** | Past trading data (prices, volume) | Technical analysis is useless |
| **Semi-strong** | All publicly available information | Fundamental analysis is useless |
| **Strong** | All information (public + private) | Even insider info is reflected |

### Key Takeaway (Professor Ye's advice)
- **Do not try to pick stocks** — Buy index funds
- Stock prices follow a **random walk** (unpredictable changes)
- New information is, by definition, unpredictable

### Anomalies & Behavioral Finance

| Anomaly | Description |
|---------|-----------|
| Momentum | Past winners continue to outperform short-term |
| Value premium | Low P/E, low P/B stocks outperform over time |
| Size effect | Small-cap stocks have historically higher returns |
| January effect | Stocks tend to rise in January |

**Two Camps:** Rational (risk-based explanations) vs Behavioral (cognitive bias explanations)

---

## Session 7: Integration & Review

Comprehensive review covering:
- Arbitrage and law of one price
- Capital budgeting with risk (WACC as discount rate)
- Valuation (DCF + multiples)
- Portfolio optimization
- CAPM application
- Cornell Endowment Fund case study

---

## Session-by-Session Knowledge Map

| Session | Topics | Key Frameworks | Excel Models | Key Examples |
|---------|--------|---------------|--------------|-------------|
| 1 | TVM, NPV | PV/FV, Annuities, Perpetuities, NPV | 1.2_solved.xlsx, 1.3_solved.xlsx | IRA retirement planning, mortgage |
| 2 | Capital Budgeting | 9 Principles, Bottom-Up/Top-Down FCF | Toothpaste.xlsx, Buy_vs_Make_EAC.xlsx | Toothpaste launch, make vs buy |
| 3 | Valuation | DCF, IRR, Trading Multiples, Transaction Multiples | Session 3 solved.xlsx | Two-period investment, Gordon Growth |
| 4 | Risk & Return | Variance, Std Dev, Covariance, Correlation, Diversification | Session 4 - Examples.xlsx | Lululemon as benchmark |
| 5 | CAPM | Efficient Frontier, CML, SML, Beta, WACC | Session 5.xlsx | Portfolio optimization |
| 6 | EMH | Three forms, Random Walk, Anomalies | — | Index fund investing |
| 7 | Integration | All frameworks combined | Cornell Endowment Fund.xlsx, Capital Budgeting with Risk.xlsx, Portfolio Optimization.xlsx | Cornell endowment allocation |

---

## Excel Models & Templates

| File | Location | Purpose |
|------|----------|---------|
| 1.2_solved.xlsx, 1.3_solved.xlsx | Session 1/ | TVM calculations — annuities, perpetuities, NPV |
| Toothpaste.xlsx (+ solved) | Session 2/ | Full capital budgeting model (bottom-up FCF) |
| Buy_vs_Make_EAC.xlsx (template + solved) | Session 2/ | Make vs buy decision using Equivalent Annual Cost |
| Session 3 solved.xlsx | Session 3/ | DCF valuation and relative valuation examples |
| Session 4 - Examples.xlsx | Session 4/ | Risk/return calculations, variance, standard deviation |
| Session 5.xlsx (+ solved) | Session 5/ | Portfolio optimization, efficient frontier, beta calculation |
| Cornell Endowment Fund 2024.xlsx | Session 7/ | Real endowment allocation optimization |
| Capital Budgeting with Risk 2025.xlsx | Session 7/ | Integrating WACC into capital budgeting decisions |
| Portfolio Optimization 2025.xlsx | Session 7/ | Full portfolio optimization exercise |
| Sample Final Exam.xlsx (+ solution) | Final Prep/ | Practice exam with worked solutions |
| Assignment 4 2025.xlsx | Root/ | Course assignment |
| Final Exam 2025.Paroz Mehta.xlsx | Root/ | Paroz's completed final exam |

---

## Cross-Domain Connections

| Related SKILL | Connection Point |
|--------------|-----------------|
| **Financial Accounting** | TVM (Topic 9 in Fin Acc = Session 1 here); Cash flow statement (Fin Acc Topic 4) feeds capital budgeting FCF calculations |
| **Valuation** | Managerial Finance provides the theoretical foundation (DCF, WACC, CAPM) that the Valuation course applies in depth |
| **Corporate Financial Policy** | Financing decision (capital structure, M&A, dividend policy) is the second pillar of this course |
| **Managerial Accounting** | Cash flow forecasting for capital budgeting uses cost concepts from Managerial Accounting |
| **Business Strategy** | Strategy analysis informs revenue/cost assumptions in capital budgeting; competitive dynamics affect discount rates |
| **Business Decision Models** | Decision trees (BDM Session 5) complement capital budgeting under uncertainty |

---

## Paroz's Deliverables

| Deliverable | File | Content |
|------------|------|---------|
| Session Excel work | Various solved xlsx per session | Worked through TVM, capital budgeting, valuation problems |
| Assignment 4 | Assignment 4 2025.xlsx | Course assignment |
| Final Exam | Final Exam 2025.Paroz Mehta.xlsx | Comprehensive finance exam |
| Team Assignment | Managerial Finance Team Assignment/ | Group project files |

---

## When to Use This SKILL

| Real-World Task | Relevant Session | Key Concepts |
|----------------|-----------------|-------------|
| Evaluate a capital investment (new project, equipment) | S1-S2 | NPV, IRR, FCF forecasting, 9 principles |
| Value a company or asset | S1, S3 | DCF, trading multiples, transaction multiples |
| Calculate cost of equity / WACC | S4-S5 | CAPM, beta, risk premium, WACC formula |
| Make vs buy decision | S2 | EAC, incremental cash flow analysis |
| Assess investment risk | S4 | Variance, standard deviation, diversification |
| Build a portfolio allocation | S5, S7 | Efficient frontier, CML, portfolio optimization |
| Evaluate whether to pick stocks or index | S6 | EMH, random walk, anomaly evidence |
| Retirement / personal financial planning | S1 | Annuities, FV, compound interest |
| Determine terminal value in a model | S3 | Gordon Growth Model, perpetuity with growth |
| Estimate discount rate for any project | S4-S5 | Risk-free rate + beta × market premium |
