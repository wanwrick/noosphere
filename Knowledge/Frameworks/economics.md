# Economics -- Knowledge Base

> Integrates Microeconomics and Macroeconomics.

---

## 1. Microeconomics

### Supply and Demand

**Demand:** Quantity consumers are willing and able to buy at each price.
- Demand curve slopes downward (higher price → lower quantity demanded)
- Shifts from: income changes, preferences, substitutes/complements, expectations, population

**Supply:** Quantity producers are willing and able to sell at each price.
- Supply curve slopes upward (higher price → higher quantity supplied)
- Shifts from: input costs, technology, expectations, number of sellers, government policy

**Equilibrium:** Where supply meets demand. Price adjusts to clear the market.

### Price Elasticity of Demand
```
Ed = % Change in Quantity Demanded / % Change in Price
```
| Elasticity | Meaning | Examples |
|-----------|---------|----------|
| |Ed| > 1 | Elastic: sensitive to price | Luxury goods, many substitutes |
| |Ed| < 1 | Inelastic: insensitive to price | Necessities, few substitutes |
| |Ed| = 1 | Unit elastic | Revenue-maximizing point |

**Revenue implications:**
- Elastic demand → lower price to increase revenue
- Inelastic demand → raise price to increase revenue

### Consumer & Producer Surplus
- **Consumer Surplus:** Difference between what consumers willing to pay and what they actually pay
- **Producer Surplus:** Difference between price received and minimum price willing to accept
- **Total Surplus = CS + PS** (maximized at competitive equilibrium)
- **Deadweight Loss:** Surplus destroyed by market distortions (taxes, price controls, monopoly)

### Market Structures
| Structure | Firms | Product | Entry | Price Setter? | Example |
|-----------|-------|---------|-------|--------------|---------|
| Perfect Competition | Many | Identical | Free | No (price taker) | Commodities |
| Monopolistic Competition | Many | Differentiated | Free | Some | Restaurants |
| Oligopoly | Few | Identical or differentiated | Barriers | Interdependent | Airlines |
| Monopoly | One | Unique | High barriers | Yes | Utilities |

### Game Theory

**Nash Equilibrium:** A set of strategies where no player can improve their payoff by unilaterally changing strategy.

**Prisoner's Dilemma:**
```
                Player B
              Cooperate  Defect
Player A  Cooperate  (3,3)    (0,5)
          Defect     (5,0)    (1,1)
```
Both defect is Nash equilibrium, but both cooperate is socially optimal. Cooperation is hard without enforcement or repeated interaction.

**Business context:** Pricing wars between airlines, cloud providers, or retailers often follow Prisoner's Dilemma dynamics. Each firm is individually rational to cut prices, but industry profits suffer. Repeated interaction (ongoing competition) and credible retaliation (trigger strategies) can sustain cooperation.

**Oligopoly Dynamics:**
- **Collusion:** Firms agree to restrict output, raise prices (illegal but profitable)
- **Cheating incentive:** Individual firm profits from secretly increasing output
- **Trigger strategies:** Cooperate until someone defects, then punish
- **Tacit collusion:** Parallel behavior without explicit agreement

**Strategic Moves:**
- **Credible commitment:** Make your strategy irreversible (e.g., burn bridges)
- **First-mover advantage:** Set the game structure in your favor
- **Signaling:** Use observable actions to convey private information
- **Screening:** Design choices that make others reveal their type

---

## 2. Macroeconomics

### GDP (Gross Domestic Product)
```
GDP = C + I + G + (X - M)
```
- C = Consumer spending (~70% of US GDP)
- I = Business investment (equipment, structures, inventories)
- G = Government spending
- X - M = Net exports (exports minus imports)

**Real vs. Nominal GDP:**
- Nominal: Measured in current prices
- Real: Adjusted for inflation (constant prices)
- GDP Deflator = Nominal GDP / Real GDP × 100

### Inflation
```
Inflation Rate = (CPI_current - CPI_previous) / CPI_previous × 100
```

**Types:**
- **Demand-Pull:** Too much money chasing too few goods
- **Cost-Push:** Rising input costs push prices up
- **Built-In:** Wage-price spiral from expectations

**Hyperinflation:** >50% monthly. Destroys monetary system. Historical examples: Zimbabwe, Venezuela, Weimar Germany.

### Labor Markets
- **Unemployment Rate = Unemployed / Labor Force × 100**
- **Labor Force Participation Rate = Labor Force / Working-Age Population × 100**
- **Types:** Frictional (between jobs), Structural (skills mismatch), Cyclical (recession)
- **Natural Rate of Unemployment:** Frictional + Structural (when economy at full employment)
- **Phillips Curve:** Inverse relationship between unemployment and inflation (short-run)

### Monetary Policy (Central Banks)
**Tools:**
- **Interest Rates:** Lower rates → stimulate borrowing/spending. Higher rates → cool economy.
- **Open Market Operations:** Buy bonds → inject money. Sell bonds → withdraw money.
- **Reserve Requirements:** Lower → banks can lend more. Higher → restrict lending.
- **Quantitative Easing (QE):** Central bank buys long-term assets to lower long-term rates.

**Transmission Mechanism:**
```
Central bank action → Interest rates → Borrowing/lending → Spending/investment → Output/inflation
```

### Fiscal Policy (Government)
- **Expansionary:** Increase spending or cut taxes → stimulate economy
- **Contractionary:** Cut spending or raise taxes → cool economy
- **Automatic Stabilizers:** Progressive taxes, unemployment insurance (activate without legislation)
- **Crowding Out:** Government borrowing raises interest rates, reducing private investment

### Trade & Currency
- **Comparative Advantage:** Countries benefit from specializing in what they produce at lowest opportunity cost
- **Exchange Rates:** Floating (market-determined) vs. Fixed (pegged to another currency)
- **Currency Appreciation:** Makes exports more expensive, imports cheaper
- **Balance of Payments:** Current Account + Capital Account = 0

### Interest Rates & Investment
- **Fisher Equation:** Nominal Rate ≈ Real Rate + Expected Inflation
- **Yield Curve:** Normal (upward) signals growth; Inverted signals recession risk
- **Central Bank Rate:** Foundation for all other interest rates in the economy

### Business Cycles
```
Expansion → Peak → Contraction (Recession) → Trough → Recovery → Expansion
```
- **Leading Indicators:** Stock prices, building permits, consumer confidence, yield curve
- **Lagging Indicators:** Unemployment rate, corporate profits, CPI
- **Coincident Indicators:** Industrial production, personal income, retail sales

---

## Quick Reference: When to Use What

| Situation | Framework | Section |
|-----------|-----------|---------|
| "How should we price this?" | Elasticity, market structure | Micro |
| "What will competitors do?" | Game theory, Nash equilibrium | Micro |
| "Is the economy heading for recession?" | Business cycle, leading indicators | Macro |
| "How will interest rate changes affect us?" | Monetary policy, Fisher equation | Macro |
| "Should we expand internationally?" | Trade, exchange rates, comparative advantage | Macro |
| "Why are input costs rising?" | Supply/demand, inflation types | Both |
| "How does government policy affect our industry?" | Fiscal policy, regulation, deadweight loss | Both |
