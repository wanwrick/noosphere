# Skills Registry

> Inventory of all skills available to Claude when using this Noosphere. Skills are specialized instruction sets that improve output quality for specific task types.

---

## Core Document Skills
| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `docx` | Word documents, .docx | Creates/edits professional Word documents |
| `pptx` | Presentations, slides, .pptx | Creates/edits PowerPoint decks |
| `xlsx` | Spreadsheets, Excel, .xlsx | Creates/edits Excel workbooks |
| `pdf` | PDF files, forms, .pdf | Creates/reads/fills PDF documents |

## Business Frameworks Skills (by Domain)
| Skill | Domain | Key Frameworks |
|-------|--------|---------------|
| `financial-accounting` | Finance | GAAP, ASC 606, financial statements |
| `managerial-accounting` | Finance | CVP, ABC, variance analysis, EVA |
| `managerial-finance` | Finance | DCF, CAPM, WACC, portfolio theory |
| `corporate-financial-policy` | Finance | M&M, capital structure, dividends, M&A |
| `valuation` | Finance | DCF, comps, precedent transactions |
| `investment-banking` | Finance | LBO, accretion/dilution, deal math |
| `business-strategy` | Strategy | Porter's 5F, VRIN, game theory, platforms |
| `role-of-gm` | Strategy | Blue ocean, discovery-driven planning, change mgmt |
| `global-strategy` | Strategy | CAGE, AAA, Hofstede, entry modes |
| `new-venture-mgmt` | Strategy | Lean startup, Sahlman, MVP, pitch prep |
| `management-simulation` | Strategy | Strategy Diamond, simulation, EPS |
| `consulting` | Strategy | MECE, issue trees, domain design |
| `marketing-management` | Marketing | STP, 4Ps, CLV, brand equity |
| `marketing-strategy` | Marketing | JTBD, consumer journey, A/B testing |
| `managing-leading-orgs` | Leadership | Congruence Model, EQ, accountability |
| `transformational-leadership` | Leadership | Full-Range Model, 4 I's, charisma |
| `leadership-teams` | Leadership | Lencioni, DiSC, psychological safety |
| `effective-presentations` | Leadership | Monroe's, RAMP, SUCCESS, STAR |
| `critical-thinking` | Leadership | System 1/2, 10-10-10, IDEALS |
| `operations-management` | Operations | Little's Law, VUT, EOQ, lean/TPS |
| `microeconomics` | Economics | Supply/demand, game theory, oligopoly |
| `macro-economics` | Economics | GDP, inflation, monetary/fiscal policy |
| `mgmt-info-systems` | Technology | IS/IT/IM, digital transformation |
| `ai-fluency` | Technology | ML, LLMs, AI governance, prompt eng |
| `sustainability` | Technology | ESG, decarbonization, circular economy |
| `corporate-governance` | Governance | Agency theory, board, compensation, activism |
| `negotiation` | Negotiation | BATNA, ZOPA, interest-based |
| `business-decision-models` | Analytics | Probability, regression, optimization |

## Professional Skills
| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `performance-self-eval` | Self-assessment, performance review, IDP | Attribute-based self-evaluation with SMART metrics and evidence mapping |
| `mckinsey-growth-audit` | Business audit, growth strategy, bottleneck analysis | Scorecard-based business audit with bottleneck identification and 90-day roadmap |
| `mckinsey-industry-analysis` | Industry analysis, market research, competitive landscape | 13-section deep-dive industry report with Porter's Five Forces integration |
| `company-research` | Company overview, due diligence, competitive intelligence | 360-degree company research template covering strategy, culture, financials, and risks |
| `feedback-analysis` | Feedback synthesis, multi-team insights, review analysis | Extracts actionable insights from multi-source feedback data with priority clustering |
| `career-development` | Resume, interview prep, cover letter, networking | Resume (XYZ formula), interview prep (CARL framework), cover letters, coffee chat planning |
| `team-leadership` | Team management, strategic planning | [Team Name]-specific leadership frameworks |
| `databricks-data-engineering-reference` | Databricks, lakehouse, Unity Catalog | Technical reference for data platform |
| `communication` | Emails, stakeholder comms | Communication system |
| `presentations` | Presentation prep | Presentation frameworks |
| `agile-story-creator` | User stories, Jira tickets | Agile story + subtask generation |
| `data-product-prd` | PRD, product requirements | Data product PRD creation |
| `async-excellence` | Documentation, Slack, async | Async communication frameworks |
| `executive-influence` | Board decks, C-suite comms | Executive communication |
| `crisis-communication` | Incidents, outages | Crisis management playbook |
| `metrics-governance` | KPIs, SLAs, monitoring | Metrics frameworks |
| `data-storytelling` | Dashboards, reports, insights | Data narrative frameworks |
| `negotiation-advanced` | Budget, scope, vendor negotiations | Advanced negotiation tactics |
| `internal-comms` | Status reports, newsletters | Internal communication formats |
| `mba-entrepreneurship` | Startup analysis, pitch decks | New venture evaluation |
| `canvas-design` | Posters, visual art | Visual design creation |
| `algorithmic-art` | Generative art, p5.js | Code-based art |
| `skill-creator` | Creating/editing skills | Skill development tooling |
| `web-artifacts-builder` | Complex React artifacts | Multi-component web artifacts |

## Notion Skills
| Skill | What It Does |
|-------|-------------|
| `notion-research-documentation` | Search Notion, synthesize, create research page |
| `notion-spec-to-implementation` | Spec page to implementation tasks in Notion |
| `notion-meeting-intelligence` | Prep meeting materials from Notion context |
| `notion-knowledge-capture` | Conversation to structured Notion page |

## Practice OS Skills (v1.2.0)

Practice-defining skills shipped with the Noosphere v1.2.0 Practice OS extension.
Source: `.claude/skills/<name>/SKILL.md`. Invoke via `/<name>` or by
referencing the skill in a prompt.

| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `claude-md-bootstrap` | Forking Noosphere, new repo onto Noosphere conventions | Generates the ~480-token CLAUDE.md routing brain (three-layer model + routing table + invariants + skills + IP catalog) |
| `data-source-10q-intake` | Onboarding a new data source, drafting a contract | Runs the 10-question intake interview; produces a `data-contract.yml` + 2-page intake brief |
| `dabs-template-init` | Bootstrapping a DABs project from a contract | Forks `templates/dabs-data-product-template/`, fills placeholders, runs validation + 9 unit tests, generates initial AI Consumption Contract |
| `governance-audit` | Phase advance for `regulated: true` or `pii: true` | 7-check pre-advance audit (DPIA, classification, masking, retention, erasure, access, jurisdiction); pass / conditional / fail verdict |
| `ai-consumption-contract` | Granting an AI agent Platinum read access | Authors per-agent contract against AI-Ready Platinum 5 Principles + 6-question metadata rubric |
| `defending-ai-spend-memo` | CFO / Board / Architecture Council asks "why this AI spend?" | One-page memo + dense appendix using Hewing 12-question framework + No LAC + Platinum defence |
| `weekly-practice-synthesis` | Friday end-of-week ritual | Pulls week's commits, feedback, evolution, governance items; produces synthesis page with punch list |

## Practice OS Atomic Subagents (v1.2.0)

Single-purpose subagents invoked from Practice OS skills (or directly when a
focused lens is needed). Source: `.claude/agents/<name>.md`.

| Subagent | Single Job | Boundary |
|----------|------------|----------|
| `dq-validator` | Validate the `quality:` section of a data contract against DLT expectations | Does not review schema, classification, or AI consumption |
| `schema-reviewer` | Review the `schema:` section against authored modeling IP (No LAC + AI-Ready Platinum) and curated principles (Shi 5 Pillars, Dataplex 6) | Does not validate DQ, classification, or governance |
| `compliance-checker` | Cross-reference contract / archetype against `governance/compliance-register.yaml` (classification, masking, retention, erasure, access, DPIA, cross-jurisdiction) | Does not validate DQ or schema; does not write a DPIA |

---

*Last updated: 2026-05-09 (v1.2.0 — Practice OS skills + atomic subagents added)*
