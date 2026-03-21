# Business Decision Models — QUICK REFERENCE
## Cornell EMBA (NCCB 5010 / MBQC 862) | Prof. Paul Roman

---

## Core Formulas

```
Mean: x̄ = Σxᵢ / n
Variance: s² = Σ(xᵢ − x̄)² / (n−1)
Std Dev: s = √(s²)

Z-score: Z = (X − μ) / σ
Confidence Interval: x̄ ± z(α/2) × σ/√n   (or t for unknown σ)

Regression: Y = β₀ + β₁X + ε
R²: proportion of variance in Y explained by X

Expected Value: EMV = Σ(pᵢ × outcomeᵢ)
Risk Premium: RP = EMV − CE
```

---

## Session Map (Quick Lookup)

| # | Topic | Key Tool |
|---|-------|----------|
| 1 | Descriptive Statistics | Mean, median, std dev, histograms |
| 2 | Probability & Distributions | Normal, Binomial, CLT, Bayes |
| 3 | Statistical Inference | z-test, t-test, confidence intervals, p-values |
| 4 | Regression | Simple/multiple regression, R², forecasting |
| 5 | Decision Trees | EMV, rollback, TreePlan, utility functions |
| 6 | Optimization | Linear programming, Excel Solver, IP |
| 7 | AHP | Pairwise comparisons, weighted scoring |

---

## Hypothesis Testing Quick Guide

```
1. State H₀ and H₁
2. Choose α (typically 0.05)
3. Calculate test statistic
4. Find p-value
5. Reject H₀ if p-value < α
```

| Error | Definition | Symbol |
|-------|-----------|--------|
| Type I | False positive (reject true H₀) | α |
| Type II | False negative (fail to reject false H₀) | β |

---

## Decision Tree Rules

- **Decision nodes** (□): Choose best branch
- **Event nodes** (○): Calculate expected value
- **Solve right to left** (rollback method)
- EMV = Σ(probability × outcome)

| Decision Rule | Logic | Risk Attitude |
|--------------|-------|--------------|
| EMV | Max expected value | Neutral |
| Maximin | Max of worst cases | Averse |
| Maximax | Max of best cases | Seeking |

---

## Linear Programming Template

```
Maximize:   Z = c₁x₁ + c₂x₂ + ...    (Objective)
Subject to: Constraints (≤, ≥, =)
            xᵢ ≥ 0                      (Non-negativity)
```

**Solver:** Data → Solver → Set objective → Decision cells → Constraints → Simplex LP → Solve

**Shadow Price:** Value of one more unit of constrained resource

---

## AHP (Analytical Hierarchy Process)

```
Goal → Criteria → Alternatives

Scale: 1 (equal) ... 9 (extreme importance)
Consistency Ratio (CR) < 0.10 = acceptable
```

Steps: Structure → Pairwise compare → Calculate weights → Rate alternatives → Rank

---

## Regression Diagnostics

| Metric | Good Sign |
|--------|-----------|
| R² | High (close to 1) |
| p-value (F-test) | < 0.05 |
| p-value (coefficients) | < 0.05 for each |
| Residual plot | Random scatter (no pattern) |

---

## Key Excel Tools

| Tool | Menu Path | Use |
|------|-----------|-----|
| Data Analysis ToolPak | Data → Data Analysis | Descriptive stats, regression, histograms |
| Solver | Data → Solver | Optimization (LP, IP) |
| TreePlan | TreePlan ribbon (add-in) | Decision trees |
| NORM.DIST / NORM.INV | Formula | Normal distribution calculations |
| T.DIST / T.INV | Formula | T-distribution calculations |
| RAND() | Formula | Random number generation (simulation) |

---

## Files in Course Folder

| File | Use |
|------|-----|
| Business Decision Models Textbook.pdf | Full coursepack (Ch 1-11) |
| Session 1-7 folders | Session-specific exercises, cases, slides |
| Textbook Excel Files/ | 15+ chapter exercise datasets |
| BDM Project Solver_Paroz_v3.xlsx | Paroz's Solver optimization project |
| Assignments/ | Individual + final assignments |

**Folder:** `Smith Cornell EMBA Classes/Business Decision Models/`
**SKILL File:** `EMBA-Code-Reference/context/Business-Decision-Models.SKILL.md`
