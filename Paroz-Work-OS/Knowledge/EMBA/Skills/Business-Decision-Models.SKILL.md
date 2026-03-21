# Business Decision Models — SKILL Reference
## Cornell EMBA (NCCB 5010 / MBQC 862) | Professor Paul Roman | 2024-2025
### Smith School of Business — Queen's University

---

## Course Architecture

**7-session structure** covering quantitative techniques and modeling methods for management decision-making:

| Session | Title | Core Concept |
|---------|-------|-------------|
| 1 | Models & Descriptive Statistics | What is a model, data description, central tendency, dispersion, Excel data tools |
| 2 | Probability & Distributions | Probability fundamentals, discrete/continuous distributions, normal distribution, Central Limit Theorem |
| 3 | Statistical Inference | Hypothesis testing, confidence intervals, z-tests, t-tests, p-values |
| 4 | Regression & Correlation | Simple/multiple regression, correlation, R², forecasting, model diagnostics |
| 5 | Decision Trees | Decision analysis under uncertainty, expected value, TreePlan (Excel add-in), utility functions, certainty equivalents |
| 6 | Optimization | Linear programming, Excel Solver, transportation problems, integer programming, project selection |
| 7 | Multi-Criteria Decision Making (AHP) | Analytical Hierarchy Process, pairwise comparisons, weight calculations, portfolio allocation |

**Textbook:** "Analysis-Based Decision Making" by A.J. "Hamish" Taylor and J.I. "Jeff" McGill (Queen's University custom coursepack)

**Core Philosophy:** Models are guides, not prescriptions. They are approximations of reality that (hopefully) contain all elements important for a decision and exclude the rest. The question is not "Does this model reproduce reality?" but "Does this model approximate reality closely enough to improve our decisions?"

**Grading:** Individual Assignments + Group BDM Project + Final Assignment

---

## Session 1: Models & Descriptive Statistics

### What Is a Model?

A model is an approximation of reality that contains all elements important for a decision and excludes the rest. Key features:
- **Control variables:** Choices the organization can make (price, production qty, etc.)
- **Uncontrollable variables:** External factors (demand, competitor actions)
- **Constraints:** Limitations on practical solutions
- **Objective function:** What we're trying to optimize

### Types of Models

| Type | Description | Example |
|------|-------------|---------|
| **Physical** | Tangible representation | Wind tunnel aircraft model |
| **Mathematical** | Equations relating variables | Cost = Price × Quantity |
| **Simulation** | Computer-based "what-if" scenarios | Monte Carlo simulation |
| **Optimization** | Find best solution given constraints | Linear programming |

### Descriptive Statistics

| Measure | Type | Formula/Purpose |
|---------|------|----------------|
| **Mean** | Central tendency | Sum / n — average value |
| **Median** | Central tendency | Middle value when sorted — robust to outliers |
| **Mode** | Central tendency | Most frequent value |
| **Range** | Dispersion | Max − Min |
| **Variance** | Dispersion | Σ(x − x̄)² / (n−1) for sample |
| **Standard Deviation** | Dispersion | √Variance — same units as data |
| **IQR** | Dispersion | Q3 − Q1 — interquartile range |

### Excel Tools for Data Analysis

- **Data Analysis ToolPak:** Descriptive statistics, histograms, regression
- **Pivot Tables:** Data summarization and cross-tabulation
- **Charts:** Histograms, scatter plots, box plots for visualization

---

## Session 2: Probability & Distributions

### Fundamentals of Probability

| Concept | Definition |
|---------|-----------|
| **Sample Space** | Set of all possible outcomes |
| **Event** | A subset of the sample space |
| **P(A)** | Probability of event A; 0 ≤ P(A) ≤ 1 |
| **Complement** | P(A') = 1 − P(A) |
| **Addition Rule** | P(A∪B) = P(A) + P(B) − P(A∩B) |
| **Multiplication Rule** | P(A∩B) = P(A) × P(B|A) |
| **Conditional Probability** | P(A|B) = P(A∩B) / P(B) |
| **Independence** | P(A∩B) = P(A) × P(B) |
| **Bayes' Theorem** | P(A|B) = P(B|A)×P(A) / P(B) |

### Key Distributions

| Distribution | Type | Key Parameters | Use Case |
|-------------|------|---------------|----------|
| **Binomial** | Discrete | n (trials), p (success prob) | Pass/fail, yes/no outcomes |
| **Poisson** | Discrete | λ (mean rate) | Rare events, arrivals per period |
| **Normal** | Continuous | μ (mean), σ (std dev) | Most natural phenomena |
| **Uniform** | Continuous | a (min), b (max) | Equally likely outcomes |

### Normal Distribution & Z-scores

```
Z = (X − μ) / σ

68-95-99.7 Rule:
  68% of data within ±1σ of mean
  95% of data within ±2σ of mean
  99.7% of data within ±3σ of mean
```

### Central Limit Theorem (CLT)

Regardless of the population distribution, the distribution of sample means approaches a normal distribution as sample size increases. The standard error of the mean = σ/√n.

---

## Session 3: Statistical Inference

### Hypothesis Testing Framework

```
1. State null hypothesis (H₀) and alternative (H₁)
2. Choose significance level (α — typically 0.05)
3. Calculate test statistic (z or t)
4. Find p-value or compare to critical value
5. Reject H₀ if p-value < α (or test stat exceeds critical value)
```

### Z-test vs T-test

| Feature | Z-test | T-test |
|---------|--------|--------|
| Population σ | Known | Unknown (use sample s) |
| Sample size | Large (n ≥ 30 rule of thumb) | Any, but especially small (n < 30) |
| Distribution | Standard normal | t-distribution (fatter tails) |

### Confidence Intervals

```
CI = x̄ ± z(α/2) × σ/√n        (z-interval, σ known)
CI = x̄ ± t(α/2,df) × s/√n     (t-interval, σ unknown)
```

### Key Concepts

- **Type I Error (α):** Rejecting H₀ when it's true (false positive)
- **Type II Error (β):** Failing to reject H₀ when it's false (false negative)
- **p-value:** Probability of observing test results at least as extreme as actual results, assuming H₀ is true
- **Statistical vs Practical Significance:** A result can be statistically significant but practically meaningless

---

## Session 4: Regression & Correlation

### Correlation

```
Correlation (r): Measures linear association between two variables
Range: −1 to +1
r² (R-squared): Proportion of variance in Y explained by X
```

### Simple Linear Regression

```
Y = β₀ + β₁X + ε

Where:
  β₀ = intercept
  β₁ = slope (change in Y per unit change in X)
  ε = error term
```

### Multiple Regression

```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε
```

### Model Diagnostics

| Metric | What It Tells You |
|--------|------------------|
| **R²** | % of variation in Y explained by the model |
| **Adjusted R²** | R² adjusted for number of predictors |
| **p-value (coefficient)** | Whether each predictor is statistically significant |
| **F-statistic** | Whether the overall model is significant |
| **Residual plots** | Whether model assumptions are met (linearity, constant variance) |

### Key Cases

- **C&A Data (Session 3):** Statistical inference applied to business data
- **Oakridge Corporation:** Regression-based business analysis
- **Estevan Express:** Forecasting/regression application
- **Weston Case:** Multi-variable regression analysis

---

## Session 5: Decision Trees & Decision Analysis

### Decision Problem Formulation (5 Steps)

1. **Understand the problem** — Define what the real problem is (not symptoms)
2. **State goals** — What are we trying to achieve?
3. **Identify criteria** — Measurable criteria corresponding to goals
4. **Describe actions** — Range of choices and their impacts on criteria
5. **Identify uncertainty** — Sources of uncertainty in actions and outcomes

### Decision Tree Components

| Element | Symbol | Meaning |
|---------|--------|---------|
| **Decision Node** | Square □ | Point where decision-maker makes a choice |
| **Event/Chance Node** | Circle ○ | Point where uncertainty is resolved |
| **Terminal Node** | Triangle △ | Endpoint with outcome value |
| **Branch** | Line | Connects nodes; labeled with description + probability/value |

### Decision Criteria

| Criterion | Rule | Best For |
|-----------|------|----------|
| **Expected Monetary Value (EMV)** | Choose option with highest expected value | Risk-neutral decision-makers |
| **Maximin** | Choose option with best worst-case outcome | Risk-averse (conservative) |
| **Maximax** | Choose option with best best-case outcome | Risk-seeking (aggressive) |
| **Minimax Regret** | Minimize maximum opportunity cost | Moderate risk aversion |

### Expected Value Calculation

```
EMV = Σ (probability × outcome) for each branch from a chance node
```

### Rollback Method

Solve decision trees **right to left**:
1. At event nodes: calculate expected value
2. At decision nodes: choose branch with best expected value
3. Continue backward to the root

### Utility Functions & Risk Attitudes

| Concept | Definition |
|---------|-----------|
| **Certainty Equivalent (CE)** | Guaranteed amount that makes you indifferent to the gamble |
| **Risk Premium (RP)** | EMV − CE (amount you'd pay to avoid the risk) |
| **Risk Averse** | CE < EMV (concave utility function) |
| **Risk Neutral** | CE = EMV (linear utility function) |
| **Risk Seeking** | CE > EMV (convex utility function) |

### TreePlan Excel Add-in

- Builds decision trees directly in Excel worksheets
- Automatically includes formulas for rollback calculations
- Shortcut: Ctrl+Shift+T (Windows)
- Key: Never add/delete rows or columns in the tree diagram area

---

## Session 6: Optimization (Linear Programming)

### Linear Programming Framework

```
Maximize (or Minimize):  Z = c₁x₁ + c₂x₂ + ... + cₙxₙ   (Objective Function)

Subject to:
  a₁₁x₁ + a₁₂x₂ + ... ≤ b₁                               (Constraints)
  a₂₁x₁ + a₂₂x₂ + ... ≤ b₂
  ...
  xᵢ ≥ 0                                                    (Non-negativity)
```

### Components of an LP Model

| Component | Description | Example |
|-----------|-------------|---------|
| **Decision Variables** | What we control | Units to produce of each product |
| **Objective Function** | What we optimize | Maximize profit or minimize cost |
| **Constraints** | Resource limitations | Labor hours, raw materials, demand |
| **Non-negativity** | Can't produce negative | x ≥ 0 |

### Excel Solver

1. Set up decision variables in cells
2. Create objective function formula
3. Create constraint formulas
4. Open Solver: Data → Solver
5. Set objective cell, decision variable cells, constraints
6. Select "Simplex LP" for linear problems
7. Click Solve

### Special LP Applications

| Type | Description | Key Feature |
|------|-------------|-------------|
| **Transportation Problem** | Minimize shipping cost across origins/destinations | Supply/demand balance |
| **Integer Programming (IP)** | Decision variables must be integers | Yes/no decisions (0 or 1) |
| **Project Selection** | Choose portfolio of projects within budget | Binary variables × NPV |

### Sensitivity Analysis

- **Shadow Price:** Value of one additional unit of a constrained resource
- **Reduced Cost:** How much the objective coefficient must improve before a variable enters the solution
- **Allowable Increase/Decrease:** Range over which the solution structure stays the same

### Key Cases

- **Woodworker:** Classic LP product mix problem
- **Cement Transportation:** Transportation LP
- **IP Project Selection:** Binary integer programming for project portfolio
- **Starr Pets:** Optimization application
- **Libbey-Owens-Ford:** Real-world LP case — integrated production, distribution, inventory; $2M+ annual savings

---

## Session 7: Multi-Criteria Decision Making (AHP)

### Analytical Hierarchy Process (AHP)

Developed by Thomas Saaty (Wharton School) — structured approach for multi-criteria, multi-stakeholder decisions.

### AHP Three Steps

1. **Structure Complexity** — Build hierarchy: Goal → Criteria → Alternatives
2. **Measurement** — Pairwise comparisons using Fundamental Scale (1-9)
3. **Synthesis** — Calculate weights, evaluate alternatives, determine overall ranking

### Fundamental Scale of Absolute Numbers

| Intensity | Definition |
|-----------|-----------|
| 1 | Equal importance |
| 3 | Moderate importance |
| 5 | Strong importance |
| 7 | Very strong importance |
| 9 | Extreme importance |
| 2,4,6,8 | Intermediate values |

### AHP Process

```
1. Define goal and alternatives
2. Identify evaluation criteria
3. Pairwise compare criteria (which is more important? by how much?)
4. Build comparison matrix
5. Calculate priority weights (normalize columns, average rows)
6. Check consistency ratio (CR should be < 0.10)
7. Rate each alternative against each criterion
8. Calculate overall scores: Σ(weight × alternative rating)
9. Rank alternatives by overall score
```

### Consistency Check

- **Consistency Ratio (CR):** Measures whether pairwise comparisons are logically consistent
- CR < 0.10 is acceptable; CR > 0.10 suggests revisiting judgments
- Some inconsistency is natural and doesn't prevent calculation

---

## Additional Topics

### Forecasting (Chapter 8)

- **Time Series Methods:** Moving averages, exponential smoothing
- **Causal Methods:** Regression-based forecasting
- **Accuracy Measures:** MAD, MSE, MAPE

### Simulation (Chapter 9)

- **Monte Carlo Simulation:** Random sampling to model uncertainty
- Use random number generation to simulate outcomes
- Run many iterations to build probability distributions of results
- Excel: `RAND()` function + lookup tables or inverse distributions

### Analytics 3.0 Framework (Davenport, HBR)

| Era | Focus | Key Feature |
|-----|-------|-------------|
| **Analytics 1.0** | Business Intelligence | Internal data, backward-looking, data warehouses |
| **Analytics 2.0** | Big Data | Unstructured data, new sources, internet/social |
| **Analytics 3.0** | Data Products | Embed analytics into products/services, prescriptive |

---

## Session-by-Session Knowledge Map

| Session | Topics | Key Frameworks | Excel Models | Key Cases |
|---------|--------|---------------|-------------|-----------|
| 1 | Models, Descriptive Stats | Model types, central tendency, dispersion | 1.1 Study_Time, 1.2 Hourly wages, 1.3 Breakout Templates | Session One MiniCases |
| 2 | Probability & Distributions | Normal, Binomial, CLT, Bayes | 2.2 Service Times, 2.3 Distance | Session 2 Mini-Cases |
| 3 | Statistical Inference | Hypothesis testing, CI, z/t-tests | 3.1 C&A data, 3.3 Oakridge data | Oakridge Corporation |
| 4 | Regression & Correlation | Simple/multiple regression, R² | 4.2 Estevan Express, 4.3 Longevity, 4.4 SKIERS, 4.5b Weston Data | Weston Case, Podium & Post |
| 5 | Decision Trees | EMV, rollback, utility, CE, risk premium | 5.3 Investment 1 or 2, TreePlan-222 | WildCat Decision Tree |
| 6 | Optimization (LP/IP) | LP, Solver, transportation, IP, sensitivity | 6.1 Woodworker, 6.2 Cement transportation, 6.3 IP Project Selection, Starr Pets | Libbey-Owens-Ford |
| 7 | AHP (Multi-Criteria) | Pairwise comparisons, Fundamental Scale, consistency | Break-out Weight Calculations | AHP Paper (Gilmour) |

---

## Excel Models & Templates

| File | Location | Purpose |
|------|----------|---------|
| 1.1-1.3 xlsx files | Session 1/ | Descriptive statistics exercises |
| 2.2 Service Times, 2.3 Distance | Session 2/ | Probability & distribution problems |
| 3.1 C&A data, 3.3 Oakridge data | Session 3/ | Hypothesis testing datasets |
| 4.2-4.5 xlsx files | Session 4/ | Regression/correlation models |
| 5.3 Investment, TreePlan-222-Example | Session 5/ | Decision tree analysis |
| 6.1-6.3 xlsx files, Starr Pets | Session 6/ | LP/IP optimization models |
| Break-out Weight Calculations | Session 7/ | AHP weight calculations |
| Textbook Excel Files/ | Textbook Excel Files/ | 15+ chapter exercise datasets |
| BDM Final Assignment.xlsx | Assignments/ | Final assignment workbook |
| BDM Project Solver_Paroz_v3.xlsx | Root | Paroz's BDM project (Solver-based) |
| BDM Project Workbookv4.xlsx | BDM Project/ | Group project workbook |

---

## Cross-Domain Connections

| Related SKILL | Connection Point |
|--------------|-----------------|
| **Managerial Finance** | Decision trees (Session 5) complement capital budgeting under uncertainty; regression for forecasting cash flows |
| **Operations Management** | Optimization (Session 6) directly applies to capacity planning, production scheduling; simulation for queue analysis |
| **Business Strategy** | Multi-criteria decisions (AHP, Session 7) for strategic option evaluation |
| **Managerial Accounting** | Regression for cost estimation; variance analysis uses statistical inference |
| **Marketing** | Regression analysis for demand forecasting; hypothesis testing for A/B testing / market research |
| **Corporate Financial Policy** | Decision trees for M&A go/no-go decisions; optimization for capital allocation |

---

## Paroz's Deliverables

| Deliverable | File | Content |
|------------|------|---------|
| Individual Assignment 1 | Assignment One - Individual- Paroz.xlsx | Statistics and inference problems |
| Individual Assignment 2 | BDM Assignment Two - Paroz.xlsx | Regression/decision analysis |
| BDM Project | BDM Project Solver_Paroz_v3.xlsx | Solver-based optimization project (school enrollment/capacity) |
| BDM Final Assignment | BDM Final Assignment.xlsx | Comprehensive final |
| BDM Notes | BDM Notes.xlsx | Personal notes and working |

---

## When to Use This SKILL

| Real-World Task | Relevant Session | Key Concepts |
|----------------|-----------------|-------------|
| Analyze data to find patterns | S1-S2 | Descriptive stats, distributions, visualization |
| Test whether a change had a real effect | S3 | Hypothesis testing, p-values, confidence intervals |
| Predict outcomes from historical data | S4 | Regression, R², forecasting |
| Make decisions under uncertainty | S5 | Decision trees, EMV, sensitivity analysis |
| Optimize resource allocation | S6 | Linear programming, Solver, sensitivity/shadow prices |
| Choose among options with multiple criteria | S7 | AHP, pairwise comparisons, weighted scoring |
| Build a financial model with uncertainty | S5, S9 (Ch.9) | Decision trees + Monte Carlo simulation |
| Evaluate A/B test results | S3 | Hypothesis testing, p-values |
| Forecast demand or costs | S4, Ch.8 | Regression, time series methods |
| Select optimal project portfolio | S6 | Integer programming, binary variables |
