# Microeconomics & Game Theory -- SKILL Reference
## Queen's EMBA (NCCB 5020 / MBQC 841) | Professor Henry Schneider

## Course Overview

**Professor**: Henry Schneider (henry.schneider@queensu.ca)
**Institution**: Queen's University, Executive MBA Americas Program
**Core Philosophy**: Economics is about thoughtful decision-making—rigorously evaluating the costs and benefits of decisions as individuals and managers.

### When to Use This Skill

- Demand and supply analysis
- Market equilibrium calculations
- Price elasticity questions
- Demand/supply shifter identification
- Game theory problems (Nash equilibrium, payoff matrices)
- Prisoner's dilemma and collusion analysis
- Strategic business interactions
- Graphical economic analysis

---

## Topic 1: Demand, Supply, and Markets

### Perfectly Competitive Markets (Benchmark)

Three key characteristics:
1. **Many small firms** - No single firm affects market
2. **Homogeneous goods** - Products are identical
3. **Free entry and exit** - No barriers

**Important consequence**: Market price unaffected by actions of single firm → Firms are **price-takers**

---

### Demand

#### What a Demand Curve Tells Us

1. How much quantity consumers are willing to buy at price P
2. What price consumers are willing to pay for the Qth unit

#### The Law of Demand
As price goes down, quantity demanded goes up (demand curves slope downward).

#### From Individual to Market Demand
Market demand = horizontal sum of all individual consumer demand curves. It tells you how many units consumers will purchase at any given price.

#### Slides vs. Shifts (CRITICAL DISTINCTION)

| Change Type | What Changes | Effect | Example |
|-------------|--------------|--------|---------|
| **Slide** (Change in Quantity Demanded) | Price of the good | Move along the demand curve | Price drops from $10 to $8 |
| **Shift** (Change in Demand) | Anything other than price | Entire curve moves left or right | Negative review shifts demand left |

**Key Rule**: The price of the good is NOT a demand shifter—it causes slides, not shifts.

#### Demand Shifters

| Shifter | Effect | Examples |
|---------|--------|----------|
| **Income (Normal Goods)** | Demand increases with income | Restaurant meals, vacations |
| **Income (Inferior Goods)** | Demand decreases with income | Instant noodles, bus passes |
| **Price of Substitutes** | ↑ price of substitute → ↑ demand | Margarine price up → butter demand up |
| **Price of Complements** | ↑ price of complement → ↓ demand | Printer price up → ink demand down |
| **Advertising** | Shifts preferences | Ad campaign increases demand |
| **Population** | More consumers → more demand | Population growth |

**Substitutes**: Goods where ↑ price of one → ↑ demand for other (butter/margarine, Coke/Pepsi)

**Complements**: Goods where ↑ price of one → ↓ demand for other (beer/beer nuts, printers/ink)

#### The Demand Function

**Linear Demand Function**: 
```
Qd = a - bP
```
Where:
- Qd = quantity demanded
- P = price
- a = intercept (captures demand shifters: a = f(income, advertising, etc.))
- b = slope (responsiveness to price)

**Inverse Demand Function** (solving for P):
```
P = (a/b) - (Qd/b)
```

**Example**: If Qd = 36 - 4P
- Inverse demand: 4P = 36 - Qd → P = 9 - (Qd/4)

---

### Price Elasticity of Demand

#### Definition
The percentage change in quantity demanded following a 1% increase in price:

```
εd = (%ΔQ) / (%ΔP) = (ΔQ/ΔP) × (P/Q)
```

#### Key Characteristics

| Elasticity Type | Magnitude | Interpretation | Demand Response |
|-----------------|-----------|----------------|-----------------|
| **Elastic** | \|εd\| > 1 | Demand very sensitive to price | Changes a lot |
| **Inelastic** | \|εd\| < 1 | Demand not very sensitive to price | Changes little |
| **Perfectly Inelastic** | εd = 0 | Demand completely insensitive | Vertical curve |
| **Perfectly Elastic** | εd = ∞ | Demand infinitely sensitive | Horizontal curve |
| **Unit Elastic** | \|εd\| = 1 | Proportional response | |

**Note**: Elasticity is always negative (price up → quantity down), but we often discuss in terms of absolute value (magnitude).

#### Revenue Implications

| Elasticity | Price Increase Effect | Price Decrease Effect |
|------------|----------------------|----------------------|
| Elastic (\|εd\| > 1) | Revenue ↓ | Revenue ↑ |
| Inelastic (\|εd\| < 1) | Revenue ↑ | Revenue ↓ |
| Unit Elastic (\|εd\| = 1) | Revenue unchanged | Revenue unchanged |

#### Calculation Example
If a 3% price increase in corn flakes causes a 6% decline in quantity demanded:
```
εd = -6% / 3% = -2 (magnitude = 2)
```
Since magnitude > 1, demand is **elastic**.

#### Typical Elasticities by Product Category (from course materials)

Products with **inelastic demand** (necessities, few substitutes):
- Salt, gasoline, medical services

Products with **elastic demand** (luxuries, many substitutes):
- Restaurant meals, foreign travel, specific brands

---

### Supply

#### What a Supply Curve Tells Us

1. How much quantity producers are willing to sell at price P
2. What price producers must receive to supply the Qth unit

#### Supply Behavior
As price goes up, quantity supplied goes up (supply curves slope upward).

#### From Producer to Market Supply
Market supply = horizontal sum of all individual producer supply curves.

#### Slides vs. Shifts for Supply

| Change Type | What Changes | Effect |
|-------------|--------------|--------|
| **Slide** (Change in Quantity Supplied) | Price of the good | Move along the supply curve |
| **Shift** (Change in Supply) | Anything other than price | Entire curve moves |

**Key Rule**: The price of the good is NOT a supply shifter.

#### Supply Shifters

| Shifter | Effect on Supply | Example |
|---------|------------------|---------|
| **Input Prices** | ↑ input costs → supply shifts left | Higher fuel prices → fewer airline seats |
| **Technological Change** | Better tech → supply shifts right | GM crops produce more at same cost |
| **Government Regulations** | More regulation → supply shifts left | Environmental requirements |
| **Number of Firms** | More firms → supply shifts right | New entrants |
| **Taxes** | Higher taxes → supply shifts left | |

#### The Supply Function

**Linear Supply Function**:
```
Qs = α + βP
```
Where:
- Qs = quantity supplied
- P = price
- α = intercept (captures supply shifters: α = f(input prices, technology, etc.))
- β = slope

**Inverse Supply Function**:
```
P = -(α/β) + (Qs/β)
```

---

### Price Elasticity of Supply

#### Definition
```
εs = (%ΔQs) / (%ΔP) = (ΔQs/ΔP) × (P/Qs)
```

| Elasticity Type | Interpretation |
|-----------------|----------------|
| **Inelastic Supply** | Producers can't easily adjust output |
| **Elastic Supply** | Producers can easily adjust output |
| **Perfectly Inelastic** | Fixed quantity (vertical curve) |
| **Perfectly Elastic** | Any quantity at fixed price (horizontal curve) |

---

### Market Equilibrium

#### Definition
Market equilibrium occurs at the intersection of supply and demand curves, where:
- Quantity demanded = Quantity supplied
- No excess supply or demand
- No pressure for price to change

#### Market Mechanism

| Condition | Market Force | Result |
|-----------|--------------|--------|
| **Price above equilibrium** | Excess supply (surplus) | Price falls |
| **Price below equilibrium** | Excess demand (shortage) | Price rises |
| **Price at equilibrium** | Supply = Demand | Price stable |

**Key Insight**: If you let the market do its job, you tend to end up at equilibrium (Q*, P*).

#### Solving for Equilibrium

**Step 1**: Set Qd = Qs and solve for P*

**Step 2**: Plug P* into either equation to get Q*

**Example**: Processed pork in Canada
```
Supply: Qs = 88 + 40P
Demand: Qd = 286 - 20P
```

Solve for P*:
```
88 + 40P = 286 - 20P
60P = 198
P* = $3.30 per kg
```

Solve for Q*:
```
Q* = 88 + 40(3.30) = 220 million kg
```

---

### Analyzing Market Changes

#### Framework for Shift Analysis

1. **Identify** what changed (demand shifter? supply shifter?)
2. **Determine** direction of shift (left or right)
3. **Draw** the new equilibrium
4. **Compare** new P* and Q* to original

#### Case Analysis: Sideways Movie Effect on Pinot Noir

**Scenario**: Movie creates positive buzz about pinot noir
- Demand shifts **right** (more people want pinot at any price)
- At original P₀, now excess demand
- Price rises, quantity rises
- New equilibrium at higher P₁, higher Q₁

#### Case Analysis: GM Foods in US vs. Europe

| Market | Consumer Attitude | Demand Shift | Supply Shift | Result |
|--------|-------------------|--------------|--------------|--------|
| **US** | Unconcerned | None/Small left | Right (lower costs) | P down, Q up |
| **Europe** | Very concerned | Large left | Right (lower costs) | P down significantly, Q down |

---

## Game Theory

### What is Game Theory?

The study of rational behavior in interactive or interdependent situations—a framework for thinking about strategic interactions.

**When Game Theory Applies**:
- When your outcomes depend on others' choices
- When others' outcomes depend on your choices
- Example: Two newspaper publishers choosing prices

**When Game Theory Does NOT Apply**:
- Facing impersonal market forces
- Being a price-taker in competitive markets
- Actions have no effect on others

### Key Elements of Any Game

| Element | Description | Questions to Ask |
|---------|-------------|------------------|
| **Players** | Decision-makers | Who is involved? (Customers, suppliers, rivals, allies) |
| **Strategies** | Available actions | What choices does each player have? |
| **Payoffs** | Outcomes (not always $$) | What does each player get from each outcome? |
| **Timing** | Simultaneous or sequential | Do players move at the same time or in order? |

### Timing of Games

**Simultaneous-Move Games** (course focus):
- Players take actions at the same time, OR
- Players move at different times BUT without knowing others' actions
- Both are analytically equivalent

**Sequential-Move Games** (not covered in detail):
- Players move in order, observing previous moves

---

### Payoff Matrices

#### Structure
- Rows = strategies for row player
- Columns = strategies for column player
- Each cell shows: (Row player's payoff, Column player's payoff)
- **Row player's payoff listed FIRST**

#### Example Matrix

|  | Column: Left | Column: Center | Column: Right |
|--|--------------|----------------|---------------|
| **Row: Top** | 3, 1 | 2, 3 | 10, 2 |
| **Row: High** | 4, 5 | 3, 0 | 6, 4 |
| **Row: Low** | 2, 2 | **5, 4** | 12, 3 |
| **Row: Bottom** | 5, 6 | 4, 5 | 9, 7 |

---

### Nash Equilibrium

#### Definition
Players play strategies that are **mutually best responses** to each other:
- No player benefits from unilaterally changing their strategy
- Given everyone else's strategy, each player is doing their best

#### Finding Nash Equilibrium

**Method**: For each cell, check if BOTH players are playing their best response:
1. Fix column player's choice → What's row player's best response?
2. Fix row player's choice → What's column player's best response?
3. Find cells where both conditions are satisfied

#### Example Analysis

From matrix above, is (Low, Center) an equilibrium?
- If Column plays Center: Row's best response is Low (5 > 4 > 2 > 3) ✓
- If Row plays Low: Column's best response is Center (4 > 3 > 2) ✓
- **YES**, (Low, Center) is a Nash equilibrium with payoff (5, 4)

Is (High, Left) an equilibrium?
- If Column plays Left: Row's best response is Bottom (5 > 4) ✗
- **NO**, row would deviate to Bottom

Is (Bottom, Left) an equilibrium?
- If Row plays Bottom: Column's best response is Right (7 > 6) ✗
- **NO**, column would deviate to Right

#### Important Properties of Nash Equilibrium

1. **Need not be the best outcome** - (Bottom, Right) gives (9, 7) but isn't equilibrium
2. **Doesn't require strict preference** - Ties are okay; player just needs no incentive to deviate
3. **May have multiple equilibria** - Some games have 0, 1, 2, or more
4. **May have no equilibrium** - In pure strategies (course doesn't cover mixed strategies)

---

### Rationality and Common Knowledge

#### Rationality Assumption
- Players know rules of the game and all payoffs
- Players choose actions that maximize their payoffs
- In practice, requires significant computational ability

#### Common Knowledge of Rationality
- Each player is rational
- Each player knows that each player is rational
- Each player knows that each player knows... (infinite regress)

**Implication**: Equilibrium analysis assumes everyone thinks through the full implications.

---

### Keynesian Beauty Contest

A demonstration of iterative reasoning and equilibrium thinking.

**Rules**:
1. Pick a number between 0 and 100
2. Average all numbers = X
3. Calculate Y = (2/3) × X
4. Closest to Y wins

**Nash Equilibrium**: All players choose 0

**Reasoning**:
- Optimal can never exceed 67 (= 2/3 × 100)
- If others are rational, they won't exceed 67 → you won't exceed 45
- If others know this, they won't exceed 45 → you won't exceed 30
- Continue iterating → converges to 0

**Practical Insight**:
- Most people don't choose 0 initially
- With experience/repetition, choices converge toward equilibrium
- To win, you only need to be one step ahead of average
- Demonstrates bounded rationality in practice

---

### Dominant Strategies

#### Definition
A strategy is **dominant** if it outperforms all other choices **no matter what opposing players do**.

A strategy is **dominated** if there exists another strategy that always does better.

#### Why Dominant Strategies Matter
- **No need for complex reasoning** about opponents
- Doesn't require belief in others' rationality
- Just play the dominant strategy—period

**Rule**: Never play a dominated strategy (it does worse regardless of rivals' play).

#### Advertising Game Example

|  | Bell: Light | Bell: Heavy |
|--|-------------|-------------|
| **Rogers: Light** | 5, 5 | 2, 6 |
| **Rogers: Heavy** | 6, 2 | 3, 3 |

**Setup**:
- Each firm earns $5B from existing customers
- Heavy advertising costs $2B
- Heavy advertising captures $3B from competitor

**Analysis for Rogers**:
- If Bell chooses Light: Heavy (6) > Light (5)
- If Bell chooses Heavy: Heavy (3) > Light (2)
- **Heavy is dominant** for Rogers

Same logic applies to Bell → **Nash equilibrium**: (Heavy, Heavy) with payoffs (3, 3)

---

### Prisoner's Dilemma

#### Conditions for Prisoner's Dilemma

1. Each player can **cooperate** or **defect** (cheat)
2. Dominant strategy for both is to **defect**
3. Both defecting gives **worse outcome** than both cooperating

#### Classic Structure

|  | Column: Cooperate | Column: Defect |
|--|-------------------|----------------|
| **Row: Cooperate** | Good, Good | Terrible, Great |
| **Row: Defect** | Great, Terrible | Bad, Bad |

Where: Great > Good > Bad > Terrible

**The Dilemma**: Individually rational behavior (defect) leads to collectively suboptimal outcome.

#### Identifying Prisoner's Dilemmas

From payoff matrix:
- Find the Nash equilibrium
- Check if both players would be better off at a different outcome
- If yes → Prisoner's dilemma

#### Business Examples

**Price Competition (Bertrand Game)**:
- Undifferentiated products
- Undercutting rivals steals demand
- Nash equilibrium: Price = Marginal Cost
- Both firms would prefer higher prices but can't sustain them

**The Problem**:
- Profit-maximizing (monopoly) price is NOT a Nash equilibrium
- Hard to coordinate even though everyone benefits
- Individual incentive to undercut destroys cooperation

---

### Repeated Prisoner's Dilemma

#### Single Period: Bleak Outcome
Both players defect (Nash equilibrium).

#### Two Periods: Unraveling
**Proposed strategy**: "Don't defect in either period; if either defects in period 1, defect in period 2"

**Why it fails** (backward induction):
1. In period 2, no future carrot → both defect
2. Knowing period 2 outcome, no deterrent in period 1 → both defect in period 1

**Conclusion**: With **fixed finite** number of periods, defection in every period.

#### Infinite/Indefinite Horizon: Hope

When game is expected to continue **forever** (or end time is uncertain):
- Unraveling doesn't occur
- Cooperation **can** be sustained
- Future punishment provides deterrent

**Key Insight**: Uncertainty about ending enables cooperation.

---

### Collusion and Cartels

#### What is Collusion?
Explicit or implicit agreement among competitors to:
- Fix prices
- Fix quantities (sales quotas, market shares)
- Allocate exclusive territories
- Divide large clients

#### Tacit vs. Hardcore Collusion

| Type | Description | Legal Status |
|------|-------------|--------------|
| **Tacit Collusion** | Implicit cooperation via indirect means (media announcements, price signaling) | Mostly legal |
| **Hardcore Collusion** | Explicit communication or coordination | Mostly illegal |

#### Why Study Collusion?

1. **It happens frequently** - Industries from maple syrup to marine hoses
2. **Know what to look for** - You may be a victim as buyer/seller/rival
3. **Know what NOT to do** - It's usually illegal

#### Industries Where Collusion is Common

**Common characteristics**:
- **Commodities/homogeneous products** - More intense competition → larger benefit from collusion
- **Obscure industries** - Under the radar
- **Small input cost share** - Less likely to raise complaints

**Examples from course materials**:
Packaged ice, cement, generic pharmaceuticals, chocolate, milk, electricity, airline fuel surcharges, air freight, asphalt, flat glass

**Major companies caught**:
Colgate-Palmolive, Unilever, P&G, Hershey's, Samsung, Sony, Bayer AG, Qantas, British Airways

---

## Quick Reference: Problem-Solving Strategies

### For Equilibrium Problems

1. Write down supply and demand functions
2. Set Qd = Qs
3. Solve for P*
4. Substitute P* to find Q*
5. Verify by checking both equations give same Q*

### For Shift Analysis

1. Identify the event
2. Is it a demand shifter or supply shifter?
3. Which direction does the curve shift?
4. Draw original and new equilibrium
5. Describe changes in P* and Q*

### For Elasticity Calculations

```
ε = (ΔQ/ΔP) × (P/Q) = (%ΔQ) / (%ΔP)
```

1. Identify % changes or calculate from data
2. Divide % quantity change by % price change
3. Interpret magnitude: >1 elastic, <1 inelastic

### For Game Theory Problems

1. Identify players, strategies, payoffs
2. Construct payoff matrix (row player payoff first)
3. For each cell, check if both players are playing best responses
4. Cells where both are → Nash equilibrium
5. Check for dominant strategies (simplifies analysis)
6. Check for prisoner's dilemma structure

### For Identifying Prisoner's Dilemma

1. Find Nash equilibrium
2. Is there another outcome where BOTH players are better off?
3. Does each player have dominant strategy to defect?
4. If yes to all → Prisoner's dilemma

---

## Formulas Summary

### Demand and Supply

| Formula | Description |
|---------|-------------|
| Qd = a - bP | Linear demand function |
| P = (a/b) - (Qd/b) | Inverse demand function |
| Qs = α + βP | Linear supply function |
| P = -(α/β) + (Qs/β) | Inverse supply function |

### Elasticity

| Formula | Description |
|---------|-------------|
| εd = (%ΔQ) / (%ΔP) | Price elasticity of demand |
| εd = (ΔQ/ΔP) × (P/Q) | Point elasticity formula |
| εs = (%ΔQs) / (%ΔP) | Price elasticity of supply |

### Equilibrium

| Condition | Solution Method |
|-----------|-----------------|
| Market clears | Set Qd(P) = Qs(P), solve for P* |
| Equilibrium quantity | Q* = Qd(P*) = Qs(P*) |

---

## Glossary of Key Terms

| Term | Definition |
|------|------------|
| **Complement** | Good where ↑ price of one → ↓ demand for other |
| **Demand curve** | Shows quantity consumers buy at each price |
| **Demand shifter** | Factor (other than price) that moves entire demand curve |
| **Dominant strategy** | Strategy that's best regardless of opponents' choices |
| **Dominated strategy** | Strategy that's always worse than another available choice |
| **Elastic demand** | \|εd\| > 1; demand responsive to price |
| **Equilibrium** | Point where supply equals demand; no pressure to change |
| **Excess demand** | Shortage; quantity demanded > quantity supplied |
| **Excess supply** | Surplus; quantity supplied > quantity demanded |
| **Inferior good** | Good where demand decreases as income rises |
| **Inelastic demand** | \|εd\| < 1; demand unresponsive to price |
| **Inverse demand** | Demand expressed as P as function of Q |
| **Nash equilibrium** | Outcome where all players play mutual best responses |
| **Normal good** | Good where demand increases as income rises |
| **Payoff matrix** | Table showing outcomes for all strategy combinations |
| **Price elasticity** | % change in quantity per % change in price |
| **Price-taker** | Firm that cannot affect market price |
| **Prisoner's dilemma** | Game where individual rationality leads to collective harm |
| **Substitute** | Good where ↑ price of one → ↑ demand for other |
| **Supply curve** | Shows quantity producers sell at each price |
| **Supply shifter** | Factor (other than price) that moves entire supply curve |
| **Tacit collusion** | Implicit coordination without explicit agreement |

---

## Course Assessment Information

**Grading**:
- Final exam: 72 points (or more if assignments skipped/dropped)
- 7 optional individual assignments: up to 28 points (4 each)
- Total: 100 points maximum

**Assignment Policy**:
- Skipped assignments → points shift to final exam
- Assignments scoring below final exam % → dropped, points shift to final
- Assignments can only help your grade

**Exam Format**:
- 2 hours, take any time during one-week period
- One double-sided page of notes allowed
- Tests material in slides
