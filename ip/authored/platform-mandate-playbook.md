# Platform-Mandate Playbook

> Pattern for formalizing a producer-side platform team's mandate when the work is already happening but no formal owner has been assigned. Stakeholder-name-free; pattern only.

This is the political-strategic side of platform engineering. It is not about technology — it is about getting the *right team* assigned the *right scope* before the next migration wave forces an ad-hoc decision.

---

## When to use

- A platform layer has no formal owner but the work exists.
- Multiple migrations are about to land and inconsistent patterns will emerge if no team owns the standard.
- A reorg is approaching and the producer team's scope is being decided.
- Cross-functional friction is bottlenecking delivery (e.g., cloud infra owns the substrate, governance owns policy, but no team owns the application layer).

---

## The five-claim argument structure (Risa Mish's Congress Model)

The Cornell EMBA argumentation pattern. Five claims, each verifiable, building to a single ask. The fifth claim is the load-bearing one — *formalization, not expansion*.

| # | Claim | Status | Evidence type |
|---|---|---|---|
| 1 | No formal owner exists for [Layer X] | ✅ Verified | Statements from leadership; absence of named team in org chart |
| 2 | The [Producer Team] already built the artifacts in question | ✅ Verified | List of artifacts with status (LIVE / IN-FLIGHT / PLANNED) |
| 3 | The ownership gap causes measurable delivery failures | ✅ Verified | Cycle-time data; incident attribution; cost-attribution gaps |
| 4 | The proposal fits within the existing operating model | ✅ Verified | Direct mapping to leadership's stated org design |
| 5 | This is **formalization** of existing work, NOT scope expansion | ⚠️ Hold the line | Discipline: never say "give us"; say "assign this work a formal owner" |

The five-claim shape matters because each claim is independently verifiable and the audience can walk the chain in either direction.

### Strategic fiction (TODAY vs FUTURE STATE)

Before-and-after side-by-side. Names what breaks today and what's true after the formalization.

| TODAY (without formal owner) | FUTURE STATE (with formal owner) |
|---|---|
| Each migration team builds its own pattern | Any team initializes a compliant project in one command |
| Gap-blockers with no clear accountability | PII masking applied automatically |
| Manual handoffs between governance and platform | Migrations start from a golden template |
| FinOps lacks attribution | FinOps tags standard across all bundles |
| No CI/CD compliance gate | CI/CD gate rejects non-compliant bundles |
| No formal owner for what the team proved | Q+1 migrations have a formal engine |

---

## The negotiation map (Shai Dubey, Cornell EMBA)

Map every party's interests honestly. Their stated position is rarely their underlying interest.

| Party | Stated position | Underlying interest |
|---|---|---|
| You (producer team) | "Formal mandate for what we already do" | Mandate · template control · career positioning · capability building · removing dependencies |
| Adjacent team (e.g., cloud infra) | "We already own [adjacent thing]" | Maintain relevance · justify headcount · clean executable scope · not be the bottleneck |
| Decision-maker (MD / Director) | "We need clean ownership" | Platform formalization · no manager wars · consumer self-serve · clear compliance escalation |

The producer team's BATNA: *the artifacts already exist.* You win technically either way. The question is whether the mandate is formal — with the title, headcount, and authority that follows — or whether you do the work without the title.

### Coalition-building sequence

```
Internal alignment (engineers) → adjacent-team brief (heads-up, not negotiation)
    → manager calibration → coordinated ask to the decision-maker
```

The "heads-up, not negotiation" line is critical. Adjacent teams need to know what you're going to ask before the decision-maker hears it, but the briefing is informational. You are not asking permission; you are confirming you have not surprise-stepped on their scope.

---

## The ownership table (clean lines, no overlaps)

Adapt the row labels to your organization. The discipline is: every artifact has exactly one owner; "executes" and "defines" are different ownership types.

| Artifact | Cloud Infra | Producer Team | Governance |
|---|---|---|---|
| Cloud substrate (VPC / KMS / IAM / object store) | **Owns** | – | – |
| CI/CD runner execution | **Owns** | – | – |
| Terraform state + pipeline execution | **Owns** | – | – |
| **Terraform modules for UC objects** | Executes via shared pipeline | **Authors + maintains** | – |
| **Bundle template library + validation logic** | – | **Owns** | – |
| **Cluster policy definitions** | – | **Owns** | – |
| **Unity Catalog schemas, grants, external locations** | – | **Owns** | – |
| Masking functions deployment | – | **Deploys (transitional)** | **Defines specs · owns long-term** |
| Tag taxonomy | – | **Implements (transitional)** | **Defines · owns long-term** |
| Pipeline patterns + DLT expectations | – | **Owns** (reusable across all domains) | – |
| Platform-agnostic utility library | – | **Owns** | – |
| Databricks-native library | – | **Owns** (does not travel) | – |
| Observability standards | – | **Owns** | – |
| Compliance policy specs | – | – | **Owns** |

The row "Terraform modules for UC objects" is the load-bearing one: same principle as DABs — one team **executes**, the other **defines what gets executed**. Different expertise, different accountability.

---

## Kotter's 8-step change-management overlay

Apply the 8 steps to the mandate proposal:

1. **Urgency is real.** Do not manufacture it. Real urgency = upcoming migrations need a standard NOW; without one, sprawl is guaranteed.
2. **Build coalition laterally before going vertical.** Engineers → adjacent-team brief → manager calibration → decision-maker.
3. **Anchor in architecture, not the team's growth.** The standard domain teams deploy from IS the change. The team owning it is the practical answer, not the headline.
4. **Short-term win is built.** Walk in with the working artifact, not a proposal. Working code is a different kind of evidence.
5. **Communicate the vision.** The 8-slide structure (next section) is the carrier for the vision.
6. **Empower others to act.** Ship the golden template; other teams can use it Day 1.
7. **Generate short-term wins (week 1).** Pick a Q+1 migration; ship it on the new pattern; publish the result.
8. **Anchor in the culture.** Update the team OS (this repo), the onboarding docs, and the leadership cadence to reference the new ownership.

---

## The 8-slide presentation structure

| # | Slide | Content |
|---|---|---|
| 1 | The Congruence Gap (DIAGNOSTIC) | 4 boxes: Strategy ✅ · People ✅ · Work ✅ · **Structure ❌** (the gap) |
| 2 | Leadership's Vision — Already Defined (CONTEXT) | Direct quotes / paraphrases from leadership's existing comms; nothing is new |
| 3 | What We Built — Proof Not Proposal (EVIDENCE) | Artifact list with status (LIVE / IN-FLIGHT / PLANNED) |
| 4 | The Ownership Gap (PROBLEM) | Specific incidents; ownership table with the gap highlighted |
| 5 | The Strategic Fiction (VISION) | Today column vs Future State column |
| 6 | The Clean Line (SOLUTION) | The corrected ownership table — clean lines, no overlaps |
| 7 | The Argument — Five Claims (LOGIC) | The five-claim Congress Model summary |
| 8 | The Ask — One Decision (ACTION) | One sentence. What requires / does not require leadership action. Why now. |

---

## Critical framing rules — memorize

- ❌ Do NOT say "give [Producer Team]" → ✅ say "assign this work a formal owner."
- ❌ Do NOT position as career / growth ask → ✅ position as **structural gap with operational consequences**.
- ❌ Do NOT name your favored initiative directly — let technical work imply it.
- ✅ Open with the **gap**, not the solution.
- ✅ Show the **working artifact** — leaders are technical; theory alone is insufficient.
- ✅ Let the decision-maker draw the line themselves.

---

## Anti-patterns

- **Asking for the title before showing the work.** Reverse the order.
- **Naming individuals on the slides.** Adjacent teams will read this as a turf war. Use roles.
- **Walking in without coalition.** The decision-maker should hear your ask third, not first.
- **Treating it as a one-time win.** Mandate without follow-through (cadence, weekly review, rotation model) decays.

---

## Verification

Before the meeting:

- [ ] Five claims independently verifiable.
- [ ] Strategic fiction concrete — every TODAY row maps to a real incident or cost.
- [ ] Ownership table reviewed with adjacent-team leads.
- [ ] BATNA explicit (artifacts already exist).
- [ ] 8-slide deck reviewed by a peer who will challenge the framing.
- [ ] Anti-patterns checked.

After the meeting (if GO):

- [ ] Decision logged in `Knowledge/Decisions/`.
- [ ] Cadence established (weekly review for first 90 days).
- [ ] Ownership table published org-wide.

---

## Cross-references

- `Knowledge/EMBA/argumentation/congress-model-risa-mish.md` — the underlying argument framework.
- `Knowledge/EMBA/negotiation/negotiation-map-shai-dubey.md` — the negotiation pattern.
- `Knowledge/EMBA/change/kotter-8-step.md` — change management overlay.
- `Knowledge/EMBA/organization/congruence-model.md` — the Slide 1 framing.
- `playbooks/change-mgmt/stakeholder-mandate-playbook.md` — operational walk-through (this is the IP page; the playbook is the runbook).

---

*Owned by: any producer-side data PM facing a platform-formalization conversation. Stakeholder-name-free by construction.*
