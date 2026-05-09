# AI-Ready Platinum — 5 Principles + 6-Question Rubric

> *1× publish → 1× govern → 5+ consume.* The Platinum layer as the runtime semantic layer for AI agents.

```mermaid
flowchart LR
    P1[Semantic Clarity<br/>Names match glossary]
    P2[Joinability Declared<br/>Keys + cardinality]
    P3[Consumption-Shaped<br/>One row per question]
    P4[Masked at Source<br/>Tier-1/2 pre-masked]
    P5[Observable<br/>Read logs · drift]

    PLT[Platinum View]
    AGT[AI Agent]

    P1 --> PLT
    P2 --> PLT
    P3 --> PLT
    P4 --> PLT
    P5 --> PLT
    PLT --> AGT

    classDef principle fill:#C3B1E1,stroke:#444,color:#000
    classDef artifact fill:#AEC6CF,stroke:#333,color:#000
    classDef agent fill:#B7E4C7,stroke:#333,color:#000

    class P1,P2,P3,P4,P5 principle
    class PLT artifact
    class AGT agent
```

## 6-Question Metadata Rubric

```mermaid
mindmap
  root((Platinum<br/>Metadata))
    Meaning
      What does this column mean?
      What does it NOT mean?
    Contracts
      Freshness contract
      Volume contract
      Quality contract
      Access contract
```

**Source IP:** `ip/authored/ai-ready-platinum-layer.md`. **Curated underpinning:** Tekiner Context Wall · Bain 3-Layer Agentic.
