# No LAC Architecture — Bronze → Platinum

> *Land it once. Land it well. Get out of the business's way.* The medallion stack as a single platform, contract-driven.

```mermaid
flowchart LR
    SRC[Source Systems<br/>OLTP · Files · APIs · CDC]
    BRZ[Bronze<br/>Schema-on-read<br/>Raw + lineage]
    SLV[Silver<br/>Conformed · DLT expectations<br/>Quality enforced]
    GLD[Gold<br/>Business marts<br/>Domain-aligned]
    PLT[Platinum<br/>AI-ready views<br/>Semantic + masked]
    AI[AI Consumers<br/>Genie · RAG · Agents]
    BI[BI Consumers<br/>Dashboards · Reports]

    SRC --> BRZ --> SLV --> GLD --> PLT
    PLT --> AI
    GLD --> BI

    classDef bronze fill:#D3D3D3,stroke:#555,color:#000
    classDef silver fill:#AEC6CF,stroke:#333,color:#000
    classDef gold fill:#FDFD96,stroke:#666,color:#000
    classDef platinum fill:#C3B1E1,stroke:#444,color:#000
    classDef consumer fill:#B7E4C7,stroke:#333,color:#000

    class BRZ bronze
    class SLV silver
    class GLD gold
    class PLT platinum
    class AI,BI consumer
```

**Source IP:** `ip/authored/no-lac-principle.md`. **Curated underpinning:** Shi 5 Pillars · Mahboub Metadata-Driven Ingestion.
