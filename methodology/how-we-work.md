# How We Work

## Session Protocol (every interaction)

1. **Load context** — read `GOALS.md`, `_Logs/feedback.md`, `_Registry/Cadences.md`. Identify which domain(s) the session touches.
2. **Plan before execute** — for any non-trivial request, state the plan first: which files to read, which frameworks to apply, what output shape. Get confirmation (or adjust) before producing the deliverable.
3. **Execute with verification** — produce the work, then run three passes:
   - **Framework check** — Is the framework named? Are all components addressed? Is the conclusion derived from the framework, not retrofitted?
   - **BLUF check** — Does the first sentence state the recommendation? Sentences ≤25 words? Banned words absent?
   - **Action check** — Does every action item have an owner + due date or trigger?
4. **Close the loop** — corrections logged to `_Logs/feedback.md`; decisions logged to `Knowledge/Decisions/`; gaps logged to `_Logs/evolution.md` if structural.
5. **Self-improvement check** — gap surfacing 3+ times → trigger autoresearch loop in `Workflows/self-improvement.md`.

If any verification pass fails: revise; re-check; do not deliver a failing output.

## Producer-side PO model

This practice operates from the producer side of a data mesh. Implications:

- We own ingestion + transformation + Platinum publication. Consumer teams own analytical and ML workloads.
- Every data product carries a `data-contract.yml`; consumer teams inherit guarantees, not assumptions.
- The default mental model for any new request is: *what's the contract?* before *how do we build it?*
- Self-serve is the default destination. Tickets are the failure mode.

## Data mesh stance

Adopted principles (sober, not zealous):

- **Domain-aligned ownership.** Bronze/Silver patterns are reusable; domain opinion lives at Gold (No LAC).
- **Data as a product.** Every Platinum publication is a product with an owner, a contract, and a contract-validation gate.
- **Federated governance.** Producer teams ship the contract; central governance ships the policy specs (PII classification, masking taxonomy, regulatory regime).
- **Self-serve infrastructure.** The DABs Data-Contract Golden Path **is** the self-serve infrastructure for new data products.

The mesh is a means to an end (No LAC + AI-Ready Platinum). It is not the end.

## Verification loops live everywhere

Every Template carries a Pre-Delivery Verification section. Every Workflow carries a Verification Loop section. Every Skill carries explicit verification steps. The discipline is uniform.

This is the same loop as `Workflows/self-improvement.md`. Repeating until it's automatic.

## When this practice diverges from the textbook

- **No LAC over Lag-first.** Latency is a derived property; capability is the design goal.
- **Custom code at Gold only.** Most teams allow domain logic in Silver; we don't.
- **Sanitization as Invariant #0.** Most templates don't ship a sanitization protocol; we do, because the practice is a public artifact.
- **AI Consumption Contract is mandatory in PRDs.** Most teams treat AI consumption as a downstream concern; we treat it as a producer obligation.

## Cross-references

- `attribution-policy.md` — authored vs curated rule.
- `repository-conventions.md` — the operational discipline of the repo itself.
- `practice-context/voice-and-style.md` — what *good* output looks like.
- `Workflows/self-improvement.md` — the autoresearch loop.
- `Workflows/sanitization-pass.md` — the sanitization discipline.
