# Data Storytelling Workflow

> Transform data into compelling narratives. Integrates Insight Pyramid, three-act structure, and visualization best practices.

---

## Step 1: Define the Story Purpose

| Question | Answer |
|----------|--------|
| **Who is the audience?** | [Technical / Business / Executive] |
| **What should they do after seeing this?** | [Specific action] |
| **What's the one thing they should remember?** | [Core message] |
| **Format?** | Dashboard / Presentation / Report / Slack update |

---

## Step 2: Build the Insight Pyramid

Work bottom-up, present top-down:

```
          [SO WHAT -- Action / Recommendation]
                    ↑
        [INSIGHT -- What the data means]
                    ↑
      [OBSERVATION -- What the data shows]
                    ↑
         [DATA -- Raw numbers and facts]
```

### Example
- **Data:** Pipeline latency increased from 12 min to 47 min over 3 weeks
- **Observation:** Latency tripled, concentrated in Silver layer transforms
- **Insight:** Schema drift from [Core System Name] CDC is causing reprocessing loops
- **So What:** We need schema validation gates in Bronze before it impacts Gold SLAs → budget 1 sprint

---

## Step 3: Structure the Narrative

### Three-Act Structure for Data Stories

**Act 1 -- Setup (Context)**
- What's the current state?
- What's the baseline the audience expects?
- One anchoring metric or visual

**Act 2 -- Conflict (Insight)**
- What changed? What's unexpected?
- Show the contrast: before vs. after, us vs. benchmark, expected vs. actual
- This is where the story earns attention

**Act 3 -- Resolution (Action)**
- What should we do about it?
- Quantified recommendation
- Clear next step

---

## Step 4: Choose the Right Visualization

### Chart Selection Guide
| Question to Answer | Best Chart |
|-------------------|-----------|
| How does it compare? | Bar chart (horizontal for many categories) |
| What's the trend over time? | Line chart |
| What's the composition? | Stacked bar or area chart |
| What's the distribution? | Histogram or box plot |
| What's the relationship? | Scatter plot |
| What's the flow? | Sankey diagram |
| How does it rank? | Sorted bar chart |
| What's the proportion? | Pie chart (only for 2-3 categories) |
| What explains the change? | Waterfall chart |
| What's the pattern across two dimensions? | Heatmap |

### Visualization Principles
1. **Title states the insight**, not the chart type ("Revenue grew 23% in Q3" not "Q3 Revenue Chart")
2. **Remove clutter**: no gridlines, minimal axis labels, no 3D effects
3. **Highlight what matters**: use color for emphasis, gray for context
4. **Consistent scales**: don't mislead with truncated axes
5. **Accessible colors**: test for colorblind safety
6. **Direct labeling**: put labels on data, avoid legends when possible
7. **One message per visual**: if it says two things, make two charts

### Color Strategy
| Purpose | Approach |
|---------|----------|
| Emphasis | One bold color + gray for everything else |
| Comparison | 2-3 distinct colors max |
| Sequential | Light-to-dark gradient of one hue |
| Diverging | Two-hue gradient (red-blue, orange-teal) |
| Alert | Red for bad, green for good (use sparingly) |

---

## Step 5: Assemble the Deliverable

### Dashboard Layout (if applicable)
```
┌─────────────────────────────────────┐
│  Key Message / Headline Metric      │  ← Top: SO WHAT
├──────────────┬──────────────────────┤
│  KPI Card 1  │  KPI Card 2  │ KPI 3│  ← Summary metrics
├──────────────┴──────────────────────┤
│  Main Visualization (trend/compare) │  ← The core story
├──────────────┬──────────────────────┤
│  Supporting  │  Supporting          │  ← Context and detail
│  Chart 1     │  Chart 2             │
├──────────────┴──────────────────────┤
│  Detail Table / Drill-down          │  ← For the curious
└─────────────────────────────────────┘
```

### Report / Presentation Flow
1. **Headline:** The one thing (action-oriented)
2. **Context:** Why this matters now (1-2 sentences)
3. **Key visual:** The chart that tells the story
4. **Supporting evidence:** 2-3 additional data points
5. **Recommendation:** What to do (specific, actionable)
6. **Appendix:** Methodology, data sources, caveats

---

## Step 6: Review Checklist

- [ ] Can someone understand the key message in 5 seconds?
- [ ] Does every visual have a conclusion title?
- [ ] Is the "so what" obvious without explanation?
- [ ] Have I removed everything that doesn't support the story?
- [ ] Are numbers accurate and sourced?
- [ ] Would this make sense to someone seeing it for the first time?
- [ ] Is the recommended action clear and specific?
