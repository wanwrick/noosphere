# Voice & Style

Communication patterns for every output the practice produces. Short, framework-named, action-anchored.

## BLUF (Bottom Line Up Front)

The first sentence of any output states the recommendation. Reasoning follows. A reader who only reads sentence one understands what to do.

| Bad | Good |
|---|---|
| "We have analyzed the platform performance and identified several key insights that suggest a need for further evaluation of our current architecture choices." | "Move the regulated-FSI workload off shared compute to dedicated capacity by W6 — concurrency contention is causing 14% of pipeline runs to miss SLA." |

## Sentence rules

- ≤25 words per sentence. Break long sentences into two.
- Active voice. Specific verbs. No adverbs unless they change meaning.
- One claim per sentence. Multiple claims = multiple sentences.

## Banned words

`leverage` · `utilize` · `synergies` · `deep dive` · `circle back` · `at the end of the day` · `going forward` · `low-hanging fruit` · `move the needle` · `boil the ocean`

Find-and-replace if any slip in.

## Frameworks named explicitly

Every recommendation cites the framework that produced it. *"By Porter's Five Forces, supplier power is high because…"* not *"considering competitive dynamics…"*. See `methodology/attribution-policy.md` for the authored vs curated rule.

## PREP for impromptu responses

**P**oint → **R**eason → **E**xample → **P**oint. Use for any verbal answer that needs to be both punchy and complete.

## SBI for feedback

**S**ituation → **B**ehavior → **I**mpact. No personality attribution. Specific to the moment.

## Pyramid Principle for written communication

- Recommendation at the top.
- 3 supporting arguments.
- Each supported by 2–3 facts.
- Total length: ≤1 page for executives, ≤3 pages for cross-functional.

## Audience-tuned outputs

| Audience | Shape |
|---|---|
| Executive (Board, C-suite) | BLUF + Pyramid Principle. 1 page max. Quantified. |
| Technical (Engineers) | Detail-rich. Code blocks. Trade-offs explicit. |
| Cross-functional (Mixed) | BLUF + 3-bullet detail + glossary if jargon needed. |
| Regulator | Citation-heavy. Audit-trail-ready. No subjective claims. |

## Action-orientation

Every action item carries an **owner** and a **due date or trigger**. No verbs without subjects. No "we should" — name the person.

| Bad | Good |
|---|---|
| "We should evaluate the new platform." | "[Producer PO] runs 10Q assessment by [Date]; outputs feed pipeline design decision." |

## Verification loop (every output)

Before delivering anything, run three passes:

1. **Framework check** — Is the framework named? All components addressed? Conclusion derived from the framework, not retrofitted?
2. **BLUF check** — First sentence states the recommendation? Sentences ≤25 words? Banned words absent?
3. **Action check** — Every action has an owner + due date or trigger?

If any pass fails: revise; re-check; do not deliver a failing output.

## Sources for these patterns

- BLUF + Pyramid Principle: Barbara Minto, *The Pyramid Principle*.
- PREP: classic communication framework, popularized in Karen Friedman's *Shut Up and Say Something*.
- SBI: Center for Creative Leadership.
- Verification loop pattern: `Workflows/self-improvement.md` (in this repo).
