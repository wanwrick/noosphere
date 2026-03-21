# AI Fluency - SKILL Reference
## Cornell EMBA (Supplemental) | Rick Dakan, Joseph Feller & Anthropic

---

## Course Architecture

Supplemental AI fluency program designed to build practical competence with generative AI across business domains.

**Core Framework:** The 4 Ds of AI Fluency

| D | Focus | Key Question |
|---|-------|-------------|
| **Delegation** | What to give to AI vs. human | Which tasks benefit from AI involvement? |
| **Description** | How to tell AI what you want | How do I communicate effectively with AI? |
| **Discernment** | How to evaluate AI output | Is this output accurate, appropriate, and useful? |
| **Diligence** | How to use AI responsibly | Am I using AI ethically and transparently? |

---

## D1: Delegation Framework

### Task-AI Fit Assessment

| Factor | AI-Suitable | Human-Required |
|--------|-------------|----------------|
| **Creativity** | First drafts, brainstorming, variations | Original vision, strategic direction |
| **Analysis** | Pattern recognition, summarization, synthesis | Judgment calls, ethical decisions |
| **Communication** | Drafting, translation, format conversion | Relationship-dependent work, negotiation |
| **Research** | Literature review, data exploration | Novel/unprecedented situations |
| **Code** | Generation, debugging, refactoring | Architecture decisions, security review |

### Three Interaction Modes

| Mode | Description | Human Role | When to Use |
|------|-------------|------------|-------------|
| **Automation** | AI performs specific tasks from specific instructions | Define what needs doing | Repetitive, well-defined tasks |
| **Augmentation** | Human + AI collaborate as thinking partners | Iterative back-and-forth | Complex analysis, creative work |
| **Agency** | AI works independently on your behalf | Establish knowledge and behavioral patterns | Workflow orchestration, monitoring |

### Delegation Decision Matrix

```
                    High Ambiguity
                         |
         AUGMENT         |         AVOID
    (think together)     |    (human judgment)
                         |
  Low Stakes ------------|------------ High Stakes
                         |
         AUTOMATE        |         VERIFY
    (let AI run)         |    (AI drafts, human checks)
                         |
                    Low Ambiguity
```

---

## D2: Description (Prompt Engineering)

### Prompt Architecture: Three Layers

| Layer | What to Define | Example |
|-------|---------------|---------|
| **Product Description** | Output format, audience, style | "Write a 500-word executive summary for the CFO" |
| **Process Description** | Step-by-step approach | "First analyze the data, then identify trends, then recommend" |
| **Performance Description** | Behavioral style | "Be concise and challenge my assumptions" |

### Core Prompt Engineering Techniques

| Technique | What It Does | When to Use |
|-----------|-------------|-------------|
| **Chain-of-Thought** | AI works through problem step by step | Complex reasoning, multi-step problems |
| **Few-Shot (N-Shot)** | Show examples of desired input-output | When format/style matters, hard to describe |
| **Role/Persona** | Specify character or expertise | Domain-specific tasks, audience matching |
| **Output Constraints** | Specify format, length, structure | Consistent deliverables, integration |
| **Think-First** | AI reasons before answering | Important decisions, nuanced analysis |
| **Decomposition** | Break complex task into subtasks | Large projects, multi-part deliverables |
| **Adversarial** | Ask AI to critique its own output | Quality assurance, risk identification |

### Prompt Quality Checklist

1. Context: Does the AI know the situation?
2. Task: Is the request specific and unambiguous?
3. Format: Is the desired output format clear?
4. Constraints: Are boundaries defined (length, tone, audience)?
5. Examples: Would a sample help clarify expectations?

---

## D3: Discernment (Evaluating AI Output)

### Three-Layer Evaluation

| Layer | Question | Red Flags |
|-------|----------|-----------|
| **Product Discernment** | Is the output accurate, relevant, coherent? | Hallucinated facts, outdated info, logical gaps |
| **Process Discernment** | Did the AI reason correctly? | Skipped steps, circular logic, false premises |
| **Performance Discernment** | Is the style effective for your needs? | Wrong tone, too verbose, missed audience |

### Hallucination Detection Strategies

1. **Cross-reference:** Verify specific claims against known sources
2. **Consistency check:** Ask the same question differently; do answers align?
3. **Confidence probing:** Ask AI to rate its own confidence and explain uncertainty
4. **Edge case testing:** Test boundary conditions where AI is more likely to err
5. **Domain expertise:** Apply your own knowledge as a filter (especially critical for finance, legal, regulatory)

### AI Output Quality Tiers

| Tier | Use Case | Verification Level |
|------|----------|-------------------|
| **Draft** | Internal brainstorming, exploration | Light review |
| **Refined** | Team-facing documents, analysis | Full review + edit |
| **Published** | Client/exec-facing, regulatory | Expert verification + sign-off |

---

## D4: Diligence (Responsible AI Use)

### Three Pillars of AI Diligence

| Pillar | Principle | Action |
|--------|-----------|--------|
| **Creation Diligence** | Be thoughtful about which AI systems you use | Evaluate privacy, security, data handling |
| **Transparency Diligence** | Be honest about AI involvement | Disclose AI use where appropriate |
| **Deployment Diligence** | Take responsibility for outputs you use | Verify, validate, and vouch for shared work |

### Enterprise AI Risk Framework

| Risk Category | Description | Mitigation |
|--------------|-------------|------------|
| **Hallucination** | AI confidently states incorrect information | Verification protocols, domain expert review |
| **Data Exposure** | Sensitive data sent to AI providers | Data classification, approved tool policies |
| **Bias Amplification** | AI reproduces or amplifies training biases | Diverse testing, fairness audits |
| **Over-reliance** | Teams stop verifying AI output | Mandatory review workflows, skill maintenance |
| **Accountability Gap** | Unclear who owns AI-generated decisions | Clear RACI for AI-assisted workflows |
| **Regulatory** | AI use in regulated domains (finance, health) | Legal review, compliance frameworks |

---

## Strategic AI Frameworks (Beyond Fluency)

### AI Investment Decision Framework

| Question | Framework | Tool |
|----------|-----------|------|
| Should we build this with AI? | Build vs. Buy vs. Partner | Cost-benefit + capability assessment |
| What is the ROI? | AI ROI Model | Time saved x labor cost + quality improvement + error reduction |
| Is this defensible? | Competitive Moat Analysis | Data moat, workflow integration, switching costs |
| What are the risks? | Risk/Reward Matrix | Probability x Impact for each risk category |

### AI ROI Calculation Model

```
AI ROI = (Value Created - Cost of AI) / Cost of AI

Value Created:
  + Time savings (hours saved x hourly cost)
  + Quality improvement (error reduction x cost per error)
  + Speed to market (faster delivery x revenue impact)
  + New capabilities (previously impossible tasks now possible)

Cost of AI:
  + Tool/API costs
  + Integration and development
  + Training and change management
  + Ongoing maintenance and monitoring
  + Risk mitigation (verification, compliance)
```

### AI Maturity Model for Organizations

| Level | Stage | Characteristics |
|-------|-------|----------------|
| 1 | **Experimentation** | Individual tool use, no governance, ad-hoc adoption |
| 2 | **Departmental** | Team-level use cases, basic guidelines, some training |
| 3 | **Operational** | Approved tools, governance policies, workflow integration |
| 4 | **Strategic** | AI embedded in strategy, competitive advantage, data flywheel |
| 5 | **Transformational** | AI-first operating model, organizational redesign around AI capabilities |

### Defending AI Spend (Board-Level)

When justifying AI investment to executives (cross-ref: Notion page `3067b88e336f8118990bcb951fdfc6eb`):

| Argument | Evidence Pattern |
|----------|-----------------|
| **Cost reduction** | "AI reduced X process from Y hours to Z hours, saving $N/year" |
| **Quality improvement** | "Error rate dropped from X% to Y% after AI-assisted review" |
| **Competitive necessity** | "Competitors A, B, C have deployed AI for [use case]; we risk falling behind" |
| **Revenue enablement** | "AI-powered feature Z drives N% increase in customer engagement" |
| **Regulatory compliance** | "AI monitoring catches N% more violations than manual review" |

---

## AI Technical Concepts

| Term | Definition |
|------|-----------|
| **LLM** | Large language model trained on vast text data to understand/generate language |
| **Parameters** | Mathematical values (billions) determining how model processes information |
| **Transformer** | 2017 architecture enabling parallel text processing with attention mechanisms |
| **Context Window** | Maximum information AI considers at once (conversation + documents) |
| **Hallucination** | AI confidently states plausible but incorrect information |
| **Knowledge Cutoff** | Date after which AI has no built-in world knowledge |
| **Temperature** | Controls randomness: high = creative/varied, low = predictable/focused |
| **RAG** | Retrieval Augmented Generation: connects AI to external knowledge sources |
| **Fine-tuning** | Additional training on specific data for domain specialization |
| **Scaling Laws** | Empirical: larger models + more data = consistent performance improvements |
| **Agents** | AI systems that can plan, use tools, and take actions autonomously |
| **MCP** | Model Context Protocol: standard for connecting AI to external tools and data |
| **Embeddings** | Numerical representations of text that capture semantic meaning |
| **Token** | Basic unit of text processing (roughly 3/4 of a word in English) |

---

## Cross-Domain Connections

| AI Fluency Concept | Related EMBA Course | Application |
|--------------------|-------------------|-------------|
| Delegation (task design) | Operations Management | Process design, automation decisions |
| Discernment (output eval) | Critical Thinking | Problem-solving rigor, System 2 thinking |
| Diligence (responsible use) | Corporate Governance | Ethics, accountability, board oversight |
| Augmentation mode | Consulting | Collaborative problem-solving |
| Prompt engineering | Presentations | Communication clarity, audience awareness |
| AI ROI | Managerial Finance | DCF, cost-benefit analysis for AI projects |
| AI Maturity Model | MIS | Digital transformation stages |
| Competitive moats | Business Strategy | VRIN applied to AI capabilities |

---

## When to Use This SKILL

| Real-World Task | Relevant Section |
|----------------|-----------------|
| Evaluate whether to use AI for a task | Delegation Framework + Decision Matrix |
| Write better prompts | Description section + Prompt Engineering Techniques |
| Review AI-generated content | Discernment section + Hallucination Detection |
| Build an AI governance policy | Diligence section + Enterprise Risk Framework |
| Justify AI investment to leadership | AI ROI Model + Defending AI Spend |
| Assess organizational AI readiness | AI Maturity Model |
| Choose build vs. buy for AI capability | AI Investment Decision Framework |

---

*Cross-references: [technology.md](../technology.md) for broader digital transformation context, [Critical-Thinking.SKILL.md](./Critical-Thinking.SKILL.md) for evaluation rigor, [Corporate-Governance.SKILL.md](./Corporate-Governance.SKILL.md) for AI ethics at board level*
