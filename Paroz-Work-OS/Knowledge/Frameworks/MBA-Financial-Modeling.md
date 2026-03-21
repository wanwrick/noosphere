# Financial Modeling Reference for Startups

## Core Principle

"Sales are for vanity, profit is for sanity, cash is king."

Always prioritize cash flow analysis. Many profitable-on-paper companies fail due to cash timing.

## Unit Economics Fundamentals

### Customer Acquisition Cost (CAC)

Formula: Total Sales & Marketing Spend ÷ Number of New Customers Acquired

Include:
- Marketing spend (ads, content, events)
- Sales salaries and commissions
- Tools and software
- Agency fees

Benchmark: Varies by industry; <$100 for DTC consumer, $500-2,000 for B2B SaaS

### Customer Lifetime Value (LTV)

For subscription:
LTV = (Average Monthly Revenue per Customer × Gross Margin %) ÷ Monthly Churn Rate

For transactional:
LTV = Average Order Value × Purchase Frequency × Average Customer Lifespan × Gross Margin %

### LTV:CAC Ratio

Target: >3:1 (for every $1 spent acquiring, get $3+ back)
- <1:1 = Losing money on every customer
- 1:1-3:1 = Marginal, needs improvement
- 3:1-5:1 = Healthy
- >5:1 = May be under-investing in growth

### CAC Payback Period

Formula: CAC ÷ (Monthly Revenue per Customer × Gross Margin %)

Target: <12 months for most businesses, <18 months acceptable for high LTV products

## Break-Even Analysis

### Unit Break-Even

Break-Even Units = Fixed Costs ÷ Contribution Margin per Unit

Where: Contribution Margin = Price - Variable Cost per Unit

### Revenue Break-Even

Break-Even Revenue = Fixed Costs ÷ Contribution Margin Ratio

Where: Contribution Margin Ratio = (Price - Variable Cost) ÷ Price

### Time to Break-Even

Project monthly cash flows, identify when cumulative cash flow turns positive.

## Startup Financial Model Structure

### Revenue Model

Build bottom-up, not top-down:
- Number of customers/units × Price
- By segment/channel/product line
- Monthly detail for Year 1, quarterly for Years 2-3

Key assumptions to state explicitly:
- Customer acquisition rate
- Conversion rates (if applicable)
- Average transaction size
- Growth rate and drivers

### Cost Model

Variable Costs:
- COGS (materials, manufacturing, shipping)
- Payment processing fees
- Sales commissions
- Fulfillment costs

Fixed Costs:
- Rent/facilities
- Salaries (core team)
- Software/tools
- Insurance
- Professional services

Semi-Variable:
- Marketing (scales with growth but has floor)
- Customer support (scales with customer base)
- Infrastructure (step-function increases)

### Cash Flow Projection

Timing matters more than amounts:
- When do customers pay? (Upfront, 30-day, 60-day)
- When do you pay suppliers?
- When are salaries due?
- When do big expenses hit?

Include:
- Operating cash flow
- Investment cash flow (equipment, development)
- Financing cash flow (investment, loans)

### Scenario Analysis

Build three scenarios:
- **Conservative**: Slower growth, higher costs, delayed milestones
- **Base**: Most likely outcomes
- **Optimistic**: Faster growth, lower costs, accelerated milestones

Vary key assumptions ±20-30%:
- Customer acquisition rate
- Average revenue per customer
- Churn rate
- Major cost items

## Financial Model Best Practices

### Excel Structure

```
Tab 1: Assumptions (all inputs here, colored cells)
Tab 2: Revenue Model (links to assumptions)
Tab 3: Cost Model (links to assumptions)
Tab 4: P&L Summary
Tab 5: Cash Flow
Tab 6: Scenario Analysis
Tab 7: Charts/Dashboard
```

### Formatting Standards

- Input cells: Light yellow background (#FFFFE0)
- Calculation cells: Light grey background (#F5F5F5)
- Headers: Bold, dark blue (#000080)
- Currency: Consistent format, no decimals for large numbers
- Percentages: One decimal place maximum
- All formulas: Link to assumptions, never hard-code numbers
- Comments: On every major assumption explaining source/rationale

### Common Formulas

Revenue Growth:
`=Prior_Month * (1 + Growth_Rate)`

Customer Count:
`=Prior_Month + New_Customers - Churned_Customers`

Churned Customers:
`=Prior_Month_Customers * Churn_Rate`

Contribution Margin:
`=Revenue - Variable_Costs`

Gross Margin %:
`=(Revenue - COGS) / Revenue`

## Valuation Basics (For Ask Sizing)

### Pre-Revenue Startups

Valuation drivers:
- Team quality and experience
- Market size and growth
- Traction/validation evidence
- Competitive positioning
- IP/technology defensibility

Typical ranges: $1-5M pre-money for seed stage

### Revenue-Stage Startups

Revenue multiples vary by:
- Industry (SaaS: 5-15x, DTC: 1-3x, Services: 1-2x)
- Growth rate (higher growth = higher multiple)
- Margin profile
- Retention metrics

### Funding Calculation

Amount to Raise = Monthly Burn Rate × Runway Months × Safety Factor

Where:
- Runway: 18-24 months typical
- Safety Factor: 1.2-1.5x (things take longer)

Dilution Planning:
- Seed: 15-25% dilution typical
- Series A: 20-30% dilution typical

## Red Flags in Financial Models

- Revenue grows faster than market without explanation
- Margins improve dramatically without driver
- No customer churn assumed
- Marketing spend doesn't scale with growth
- No hiring despite 10x growth
- Break-even in Year 1 (rarely realistic)
- All costs are fixed (nothing scales)
- No seasonality when industry has it
- Hockey stick without inflection driver
