# Skills Registry

> Inventory of all skills available to Claude when using this Work OS. Skills are specialized instruction sets that improve output quality for specific task types.

---

## Core Document Skills
| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `docx` | Word documents, .docx | Creates/edits professional Word documents |
| `pptx` | Presentations, slides, .pptx | Creates/edits PowerPoint decks |
| `xlsx` | Spreadsheets, Excel, .xlsx | Creates/edits Excel workbooks |
| `pdf` | PDF files, forms, .pdf | Creates/reads/fills PDF documents |

## EMBA Knowledge Skills (by Domain)
| Skill | Domain | Key Frameworks |
|-------|--------|---------------|
| `financial-accounting-cornell-emba` | Finance | GAAP, ASC 606, financial statements |
| `managerial-accounting-cornell-emba` | Finance | CVP, ABC, variance analysis, EVA |
| `managerial-finance-cornell-emba` | Finance | DCF, CAPM, WACC, portfolio theory |
| `corporate-financial-policy-cornell-emba` | Finance | M&M, capital structure, dividends, M&A |
| `valuation-cornell-emba` | Finance | DCF, comps, precedent transactions |
| `investment-banking-cornell-emba` | Finance | LBO, accretion/dilution, deal math |
| `business-strategy-cornell-emba` | Strategy | Porter's 5F, VRIN, game theory, platforms |
| `role-of-gm-cornell-emba` | Strategy | Blue ocean, discovery-driven planning, change mgmt |
| `global-strategy-cornell-emba` | Strategy | CAGE, AAA, Hofstede, entry modes |
| `new-venture-mgmt-cornell-emba` | Strategy | Lean startup, Sahlman, MVP, pitch prep |
| `cornell-mgmt-simulation-cornell-emba` | Strategy | Strategy Diamond, simulation, EPS |
| `consulting-cornell-emba` | Strategy | MECE, issue trees, domain design |
| `marketing-management-cornell-emba` | Marketing | STP, 4Ps, CLV, brand equity |
| `marketing-strategy-cornell-emba` | Marketing | JTBD, consumer journey, A/B testing |
| `managing-leading-orgs-cornell-emba` | Leadership | Congruence Model, EQ, accountability |
| `transformational-leadership-cornell-emba` | Leadership | Full-Range Model, 4 I's, charisma |
| `leadership-teams-cornell-emba` | Leadership | Lencioni, DiSC, psychological safety |
| `effective-presentations-cornell-emba` | Leadership | Monroe's, RAMP, SUCCESS, STAR |
| `critical-thinking-cornell-emba` | Leadership | System 1/2, 10-10-10, IDEALS |
| `operations-management-cornell-emba` | Operations | Little's Law, VUT, EOQ, lean/TPS |
| `microeconomics-cornell-emba` | Economics | Supply/demand, game theory, oligopoly |
| `macro-economics-cornell-emba` | Economics | GDP, inflation, monetary/fiscal policy |
| `mgmt-info-systems-cornell-emba` | Technology | IS/IT/IM, digital transformation |
| `ai-fluency-cornell-emba` | Technology | ML, LLMs, AI governance, prompt eng |
| `sustainability-cornell-emba` | Technology | ESG, decarbonization, circular economy |
| `corporate-governance-cornell-emba` | Governance | Agency theory, board, compensation, activism |
| `cornell-program-cornell-emba` | Program | Course catalog, program navigation |
| `negotiation-cornell-emba` | Negotiation | BATNA, ZOPA, interest-based |
| `business-decision-models-cornell-emba` | Analytics | Probability, regression, optimization |

## Professional Skills (Deployed)
| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `datawizards-leadership` | Team management, strategic planning | DataWizards-specific leadership frameworks |
| `databricks-data-engineering-reference` | Databricks, lakehouse, Unity Catalog | Technical reference for data platform |
| `paroz-communication` | Emails, stakeholder comms | Paroz's communication system |
| `paroz-presentations` | Presentation prep | EMBA presentation frameworks |
| `agile-story-creator` | User stories, Jira tickets, spikes, epics | DataWizards ticket system: decision gate (flat task/spike/story/epic), lean-first rules, DLT quality patterns, SQL migration templates, team roster with domain ownership, testing standards. Core: `Knowledge/Work/agile-ticket-system.md` + `agile-examples.md` + `testing-patterns.md` |
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

## Professional Skills (Local-Only, No Deployed Counterpart)
| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `performance-self-eval` | Self-assessment, performance review, IDP | Attribute-based self-evaluation with SMART metrics and evidence mapping |
| `mckinsey-growth-audit` | Business audit, growth strategy, bottleneck analysis | Scorecard-based business audit with bottleneck identification and 90-day roadmap |
| `mckinsey-industry-analysis` | Industry analysis, market research, competitive landscape | 13-section deep-dive industry report with Porter's Five Forces integration |
| `company-research` | Company overview, due diligence, competitive intelligence | 360-degree company research template covering strategy, culture, financials, and risks |
| `feedback-analysis` | Feedback synthesis, multi-team insights, review analysis | Extracts actionable insights from multi-source feedback data with priority clustering |
| `career-development` | Resume, interview prep, cover letter, networking, job application | Full application workflow: paste a JD to generate tailored resume (.docx + .pdf), cover letter (.docx + .pdf), LinkedIn outreach, company brief, interview prep, and Notion Hunt Hub tracking. Uses `docx`/`pdf` skills. See `Workflows/job-application.md` for the 10-step orchestrator. |

## Utility & Design Skills
| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `schedule` | Recurring tasks, scheduled prompts | Create scheduled tasks that run on intervals |
| `mcp-builder` | Building MCP servers | Guide for creating MCP servers to integrate external APIs |
| `theme-factory` | Styling artifacts with themes | Apply pre-set or custom themes to slides, docs, reports |
| `slack-gif-creator` | Animated GIFs for Slack | Create optimized animated GIFs for Slack |

## Notion Skills
| Skill | What It Does |
|-------|-------------|
| `notion-research-documentation` | Search Notion → synthesize → create research page |
| `notion-spec-to-implementation` | Spec page → implementation tasks in Notion |
| `notion-meeting-intelligence` | Prep meeting materials from Notion context |
| `notion-knowledge-capture` | Conversation → structured Notion page |

## Workflow Skills
| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `job-application-workflow` | Pasted job description, "apply to [company]" | End-to-end application package: JD analysis, resume + cover letter (.docx/.pdf), LinkedIn outreach, company brief, interview prep, Notion Hunt Hub logging. Orchestrator: `Workflows/job-application.md` |

---

## Reference-Only SKILL Files (Not Triggerable)
| File | Purpose |
|------|---------|
| `Individual-Project.SKILL.md` | Capstone MCP/NVP project guidance (reference, not an invokable skill) |

---

*Last updated: 2026-03-18*
