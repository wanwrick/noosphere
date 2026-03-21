# Financial Accounting — SKILL Reference
## Cornell EMBA (NCCB 5000 / MBQC811) | Professor Brian White | Fall 2024

---

## Course Architecture

**10-topic structure** covering the full financial accounting cycle:

| Topic | Title | Core Concept |
|-------|-------|-------------|
| 1 | Introducing Financial Statements (Part 1) | Balance Sheet, Income Statement, accrual vs cash accounting |
| 2 | Introducing Financial Statements (Part 2) | Statement of Stockholders' Equity, debits & credits, journal entries, T-accounts |
| 3 | Gains/Losses, Adjusting Entries, Accounting Cycle | Gains vs revenue, adjusting journal entries, ROE decomposition |
| 4 | Statement of Cash Flows | Operating/Investing/Financing, indirect method, free cash flow |
| 5 | Revenue Recognition | ASC 606, multi-element arrangements, performance obligations |
| 6 | Accounts Receivable & Bad Debts | Allowance method, percent of sales, aging, DSO |
| 7 | Inventories | FIFO/LIFO/Average Cost, COGS, inventory turnover |
| 8 | Intercorporate Investments | Passive investments, equity method, consolidation |
| 9 | Long-Term Operating Assets & TVM | PP&E, depreciation methods, time value of money |
| 10 | Liabilities | Current/non-current, bonds, leases, contingencies |

**Real-Company Focus:** Apple (in-class problems) and Starbucks (homework) financial statements used throughout

**Grading:** Homework (24%) + Final Exam (56%) + Team FSA Project (20%)

---

## The Big Picture: Three Foundational Equations

### 1. The Balance Sheet Equation
```
Assets = Liabilities + Owners' Equity
```

### 2. The Expanded Accounting Equation
```
Assets − Liabilities = Permanent Owners' Equity + Revenues − Expenses + Gains − Losses
```

### 3. The Cash Flow Equation
```
Cash = Liabilities − All Other Assets + Permanent Owners' Equity + Net Income
```

**Key Insight:** Changes in cash can ONLY be explained by changes in non-cash balance sheet accounts. If you understand this algebra, the Statement of Cash Flows follows logically.

### Financial vs Managerial Accounting

| Financial Accounting | Managerial Accounting |
|---------------------|----------------------|
| External users (investors, creditors) | Internal users (managers) |
| Entire entity (consolidated) | Pieces of entity (disaggregated) |
| GAAP/IFRS rules | Flexible tools |
| Historical/stewardship | Future/decision-making |
| **RULES** | **TOOLS** |

---

## Topic 1 & 2: Introducing Financial Statements

### Accrual vs Cash Accounting

| Concept | Definition | Example |
|---------|-----------|---------|
| **Cash accounting** | Measure cash and changes in cash | Record revenue when cash received |
| **Accrual accounting** | Measure wealth and changes in wealth | Record revenue when earned, regardless of cash |
| **Accruals** | Record economic activity BEFORE cash flow | Accounts receivable (revenue before cash), Accounts payable (expense before cash) |
| **Deferrals** | Record economic activity AFTER cash flow | Prepaid rent (cash before expense), Deferred revenue (cash before revenue) |

### The Four Financial Statements

1. **Balance Sheet** (Statement of Financial Position)
   - Assets = Liabilities + Owners' Equity
   - Point in time snapshot
   - Current vs non-current classification

2. **Income Statement** (Statement of Operations)
   - Revenue − Expenses = Net Income
   - Period performance measure
   - Key line items: Net Sales, COGS, Gross Profit, SG&A, Operating Income, Net Income

3. **Statement of Stockholders' Equity**
   - Bridges beginning and ending equity
   - Permanent OE: Common Stock, APIC, Treasury Stock
   - Temporary OE: Retained Earnings (Net Income − Dividends), AOCI

4. **Statement of Cash Flows**
   - Operating + Investing + Financing = Change in Cash
   - Links accrual measures to cash reality

### Debits & Credits System

| Account Type | Normal Balance | Increase | Decrease |
|-------------|---------------|----------|----------|
| Assets | Debit | Debit | Credit |
| Contra-Assets | Credit | Credit | Debit |
| Liabilities | Credit | Credit | Debit |
| Owners' Equity | Credit | Credit | Debit |
| Revenue | Credit | Credit | Debit |
| Expenses | Debit | Debit | Credit |
| Gains | Credit | Credit | Debit |
| Losses | Debit | Debit | Credit |

**Rule:** Every journal entry must have equal debits and credits (double-entry bookkeeping).

---

## Topic 3: Gains/Losses, Adjusting Entries, Accounting Cycle

### Gains & Losses vs Revenue & Expenses

| Revenue/Expense | Gains/Losses |
|----------------|-------------|
| **Gross** changes in assets/liabilities | **Net** changes in assets/liabilities |
| From main business activities | From peripheral activities |
| Reported separately (Revenue line, COGS line) | Reported as single net amount |

**Example:** Bookstore sells books (Revenue & COGS). Bookstore sells old bookcase (Gain or Loss on Sale).

### Adjusting Journal Entries (AJEs)

Four types of AJEs performed at period end:
1. **Accrue revenue** — Revenue earned but not yet collected (Dr. Receivable, Cr. Revenue)
2. **Accrue expense** — Expense incurred but not yet paid (Dr. Expense, Cr. Payable)
3. **Defer revenue** — Cash received but not yet earned (Dr. Cash, Cr. Deferred Revenue → later: Dr. Deferred Revenue, Cr. Revenue)
4. **Defer expense** — Cash paid but not yet consumed (Dr. Prepaid, Cr. Cash → later: Dr. Expense, Cr. Prepaid)

### The DuPont ROE Decomposition

```
ROE = Net Income / Owners' Equity

ROE = (Net Income / Sales) × (Sales / Assets) × (Assets / Owners' Equity)

ROE = Profitability × Efficiency × Leverage
```

| Component | What It Measures | Key Ratios |
|-----------|-----------------|------------|
| **Profitability** (Net Profit Margin) | How much profit per dollar of sales | Gross margin, operating margin, net margin |
| **Efficiency** (Asset Turnover) | How effectively assets generate sales | Inventory turnover, DSO, PP&E turnover |
| **Leverage** (Equity Multiplier) | How much debt amplifies returns | Debt/equity, interest coverage |

**Key Insight:** A company can have high ROE through high margins (luxury brands), high turnover (Walmart), or high leverage (financial institutions). The decomposition reveals which driver is at work.

---

## Topic 4: Statement of Cash Flows

### Three Sections

| Section | Cash Inflows | Cash Outflows |
|---------|-------------|--------------|
| **Operating** | Cash from customers, interest/dividends received | Cash to suppliers, employees, government, interest paid |
| **Investing** | Sale of PP&E, sale of investments, maturity of securities | Purchase of PP&E, purchase of investments |
| **Financing** | Issuing stock, borrowing debt | Repurchasing stock, repaying debt, paying dividends |

### US GAAP vs IFRS Classification Differences

| Item | US GAAP | IFRS |
|------|---------|------|
| Interest paid | Operating | Operating OR Financing (choice) |
| Interest received | Operating | Operating OR Investing (choice) |
| Dividends received | Operating | Operating OR Investing (choice) |
| Dividends paid | Financing | Financing OR Operating (choice) |

### Indirect Method (Operating Section)

Start with Net Income, then adjust for:
1. **Non-cash charges** — Add back depreciation, amortization (non-cash expenses)
2. **Gains/losses** — Subtract gains, add losses (these belong in Investing section)
3. **Changes in working capital** — Adjust for changes in current assets and current liabilities

**Rule of thumb for working capital adjustments:**
- Increase in current asset → SUBTRACT (used cash)
- Decrease in current asset → ADD (generated cash)
- Increase in current liability → ADD (conserved cash)
- Decrease in current liability → SUBTRACT (used cash)

### Free Cash Flow
```
Free Cash Flow = Cash from Operations − Capital Expenditures
```
**Use:** Measures cash available for distribution to shareholders, debt repayment, or reinvestment beyond maintenance of existing operations.

---

## Topic 5: Revenue Recognition (ASC 606)

### The 5-Step Revenue Recognition Model

1. **Identify the contract** with the customer
2. **Identify the performance obligations** in the contract
3. **Determine the transaction price**
4. **Allocate the transaction price** to performance obligations
5. **Recognize revenue** when (or as) each performance obligation is satisfied

### Key Concepts

- **Performance obligation** = Promise to transfer a good or service
- **Satisfied over time** vs **satisfied at a point in time**
- **Contract assets** = Revenue recognized before billing (work done, not yet invoiced)
- **Contract liabilities** (Deferred Revenue) = Cash received before revenue is earned (e.g., gift cards, subscriptions, prepaid services)

### Multiple Performance Obligations

When a contract bundles goods + services (e.g., iPhone + 2 years of software updates):
- Determine standalone selling price of each obligation
- Allocate total transaction price proportionally
- Recognize revenue as each obligation is satisfied

---

## Topic 6: Accounts Receivable & Bad Debts

### The Allowance Method

Companies must estimate uncollectible receivables at period end:
```
Accounts Receivable, Net = Accounts Receivable, Gross − Allowance for Doubtful Accounts
```

### Two Estimation Approaches

| Method | Focus | Calculation |
|--------|-------|------------|
| **Percent of Sales** | Income Statement (Bad Debt Expense) | Bad Debt Expense = % × Credit Sales |
| **Aging Method** | Balance Sheet (Allowance balance) | Estimate required Allowance, back into Expense |

### Key Journal Entries

| Event | Entry |
|-------|-------|
| Record credit sale | Dr. A/R, Cr. Revenue |
| Record cash collection | Dr. Cash, Cr. A/R |
| Record bad debt estimate (AJE) | Dr. Bad Debt Expense, Cr. Allowance for Doubtful Accounts |
| Write off specific account | Dr. Allowance, Cr. A/R Gross (NO income statement effect) |

### Key Ratios
- **Days Sales Outstanding (DSO)** = (A/R ÷ Revenue) × 365
- **A/R Turnover** = Revenue ÷ Average A/R

---

## Topic 7: Inventories

### Cost Flow Assumptions

| Method | COGS Reflects | Ending Inventory Reflects | In Rising Prices |
|--------|-------------|-------------------------|-----------------|
| **FIFO** (First-In, First-Out) | Older costs | Newer costs | Lower COGS, Higher NI, Higher Inventory |
| **LIFO** (Last-In, First-Out) | Newer costs | Older costs | Higher COGS, Lower NI, Lower Inventory |
| **Average Cost** | Weighted average | Weighted average | Middle ground |

### The Inventory Equation
```
Beginning Inventory + Purchases = COGS + Ending Inventory
```
Rearranged: `COGS = Beginning Inventory + Purchases − Ending Inventory`

### LIFO Reserve (converting LIFO to FIFO)
```
FIFO Inventory = LIFO Inventory + LIFO Reserve
FIFO COGS = LIFO COGS − Change in LIFO Reserve
```
**Use:** Enables apples-to-apples comparison between companies using different methods.

### Key Ratios
- **Gross Profit Margin** = (Revenue − COGS) ÷ Revenue
- **Inventory Turnover** = COGS ÷ Average Inventory
- **Days Sales in Inventory** = 365 ÷ Inventory Turnover

---

## Topic 8: Intercorporate Investments

### Accounting Treatment by Ownership Level

| Ownership | Classification | Accounting Method | B/S Treatment | I/S Treatment |
|-----------|---------------|-------------------|--------------|--------------|
| < 20% | Passive | Fair Value | Mark to market | Unrealized G/L (I/S for equity; OCI for debt-AFS) |
| 20-50% | Significant Influence | Equity Method | Cost + share of NI − dividends | Share of investee's NI |
| > 50% | Control | Consolidation | Combine all assets/liabilities | Combine all revenues/expenses |

### Passive Investment Categories

| Category | Typical Holdings | Unrealized G/L |
|----------|-----------------|---------------|
| **Trading securities** | Short-term equity | Through Net Income |
| **Available-for-sale (AFS)** | Debt securities held | Through OCI (bypasses I/S) |
| **Held-to-maturity** | Debt held to maturity | Not recognized (amortized cost) |

### Equity Method Key Mechanics
```
Investment Balance = Initial Cost + Share of NI − Share of Dividends
```
- Dividends REDUCE investment balance (NOT income)
- Record proportional share of investee's net income as investment income

---

## Topic 9: Long-Term Assets & Time Value of Money

### Depreciation Methods

| Method | Annual Expense | When to Use |
|--------|---------------|------------|
| **Straight-line** | (Cost − Salvage) ÷ Useful Life | Even benefit pattern |
| **Double-declining balance** | 2 × (1/Life) × Book Value | Front-loaded benefits |
| **Units-of-production** | (Cost − Salvage) × (Units Used / Total Units) | Usage-based |

### Asset Impairment
- Test: If carrying value > undiscounted future cash flows → impaired
- Write-down to fair value
- Loss recorded on income statement
- Cannot be reversed under US GAAP

### Time Value of Money
- **Present Value:** PV = FV / (1+r)^n
- **Annuity PV:** PV = PMT × [(1 − (1+r)^−n) / r]
- **Perpetuity:** PV = PMT / r
- Used for: bond pricing, lease obligations, pension liabilities, impairment testing

---

## Topic 10: Liabilities

### Current Liabilities
- Accounts payable, accrued expenses, current portion of long-term debt, deferred revenue
- Due within one year or one operating cycle

### Long-Term Debt (Bonds)
- **Issued at par:** Coupon rate = Market rate
- **Issued at discount:** Coupon rate < Market rate (proceeds < face value)
- **Issued at premium:** Coupon rate > Market rate (proceeds > face value)
- Discount/premium amortized over bond life → Interest expense converges to market rate

### Lease Accounting (ASC 842)
- **Operating leases:** Right-of-use asset + Lease liability on B/S; straight-line expense on I/S
- **Finance leases:** Right-of-use asset + Lease liability on B/S; front-loaded expense (depreciation + interest)
- Both types now appear on balance sheet (major change from pre-ASC 842)

### Contingent Liabilities
- **Probable + estimable** → Accrue (record liability and expense)
- **Probable but not estimable** → Disclose in notes
- **Reasonably possible** → Disclose in notes
- **Remote** → No disclosure required

---

## DuPont ROE Decomposition — Full Framework

```
ROE = Profit Margin × Asset Turnover × Equity Multiplier

     = (NI/Sales)   × (Sales/Assets) × (Assets/OE)
```

### Detailed Decomposition (by Topic)

| ROE Component | Related Topics | Key Ratios |
|--------------|---------------|------------|
| **Profitability** | Revenue (T5), COGS/Inventory (T7), Operating Expenses | Gross margin, Operating margin, Net margin |
| **Asset Efficiency** | A/R (T6), Inventory (T7), PP&E (T9) | DSO, Inventory turnover, PP&E turnover, Total asset turnover |
| **Leverage** | Liabilities (T10), Equity (T2) | Debt/equity, Interest coverage, Equity multiplier |

---

## Session-by-Session Knowledge Map

| Session | Topics | Key Frameworks | Models/Tools | Cases/Companies |
|---------|--------|---------------|--------------|----------------|
| 1 | 1 & 2 | Accrual accounting, Balance Sheet equation, Debits/Credits | Day One Exercise, T-accounts | Apple, Starbucks |
| 2 | 1 & 2 cont. | Statement of Stockholders' Equity, Journal entries | Company Selection for FSA Project | Apple, Starbucks |
| 3 | 3 & 4 | Gains/Losses, AJEs, Accounting Cycle, Cash Flow Statement | ROE (DuPont), Indirect Method, Free Cash Flow | Apple, Bon-Ton Stores, Chuy's Holdings |
| 4 | 5 & 6 | Revenue Recognition (ASC 606), Receivables, Bad Debts | 5-Step Model, Aging Method, DSO | Apple, Starbucks, Crocs, Rocky Mountain Chocolate, HP Inc |
| 5 | 7 & 8 | Inventory Costing, Intercorporate Investments | FIFO/LIFO conversion, LIFO Reserve, Equity Method | Apple, Starbucks, Brunswick Corp |
| 6 | 9 & 10 | Depreciation, TVM, Liabilities, Leases | Straight-line/DDB, PV/FV formulas, Bond pricing | Apple, Starbucks |
| 7 | 10 + Review | Liabilities cont., Final exam review | Full DuPont framework, Comprehensive ratio analysis | Cummins (final exam company) |

---

## Excel Models & Templates

| File | Location | Purpose |
|------|----------|---------|
| FSA Ratio Analysis Spreadsheet (completed) | Financial Accounting/ | Complete ratio analysis template — DuPont decomposition, efficiency ratios, leverage ratios |
| FSA Ratio Analysis Spreadsheet BLANK | Financial Accounting/Introducing Financial Statements/ | Blank template for team project |
| Annotated Income Statement and Balance Sheet | Financial Accounting/Introducing Financial Statements/ | Annotated Apple financial statements with line-item explanations |
| Discounting a stream of cash flows | Financial Accounting/Topic 9 TVM/ | TVM calculation worksheet |
| Final Exam (Cummins 2023) | Financial Accounting/ | Practice exam based on Cummins financial statements |

---

## Cross-Domain Connections

| Related SKILL | Connection Point |
|--------------|-----------------|
| **Managerial Accounting** | Financial = external reporting (RULES); Managerial = internal decision-making (TOOLS). Cost concepts from Managerial feed into COGS on financial statements. |
| **Valuation** | DuPont ROE decomposition feeds valuation models. Revenue forecasting (Topic 5) and working capital analysis (Topics 6-7) are inputs to DCF. |
| **Managerial Finance** | TVM from Topic 9 is foundational to all finance courses. Cash flow statement analysis (Topic 4) connects to capital budgeting. |
| **Corporate Governance** | Financial statements are the primary accountability mechanism for boards. Earnings quality and estimation judgment (Topics 5-8) are governance concerns. |
| **Business Strategy** | Industry profit potential analysis requires understanding financial statements to assess competitor profitability, efficiency, and leverage. |

---

## Paroz's Deliverables

| Deliverable | File | Content |
|------------|------|---------|
| Topic 1-2 Homework | Topic 01 Homework Pages_Paroz.docx, Topic 02 Homework Pages_Paroz.docx | Balance sheet and income statement analysis of Starbucks |
| Topic 3-8 Homework | Topic 03-08 Homework Pages.docx (various) | Progressive accounting problem sets |
| FSA Ratio Analysis (completed) | FSA Ratio Analysis Spreadsheet Paroz (completed).xlsx | Full DuPont decomposition and ratio analysis for team project companies |
| Final Exam | Financial Accounting/ (on Canvas) | 3-hour comprehensive exam on Cummins 2023 financial statements |

---

## When to Use This SKILL

| Real-World Task | Relevant Topics | Key Concepts |
|----------------|----------------|-------------|
| Read & interpret a 10-K filing | All topics | Balance sheet, income statement, cash flow statement, notes |
| Analyze company financial health | Topics 3, 6, 7 | DuPont ROE, DSO, inventory turnover, leverage ratios |
| Assess revenue quality | Topic 5 | ASC 606, deferred revenue, contract assets/liabilities |
| Evaluate cash generation vs profitability | Topic 4 | Operating cash flow, free cash flow, indirect method adjustments |
| Compare companies in same industry | Topic 7 | LIFO/FIFO conversion, normalize for accounting method differences |
| Evaluate M&A target financials | Topics 8, 10 | Consolidation, equity method, off-balance sheet items, lease obligations |
| Build financial projections | Topics 5-7 | Revenue recognition timing, A/R collection patterns, inventory build cycles |
| Assess credit risk / lending decisions | Topics 6, 10 | A/R aging, allowance adequacy, debt covenants, contingent liabilities |
| Prepare for valuation work | Topics 3-4, 9 | Free cash flow, depreciation add-backs, TVM, working capital changes |
