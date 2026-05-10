# 10Q Discovery Flow

> The 10-question intake interview that turns a fuzzy "we need this data" request into a deployable contract.

```mermaid
flowchart TB
    Q1[Q1 Producer<br/>domain · owner]
    Q2[Q2 Consumers<br/>agents · dashboards]
    Q3[Q3 Use Case<br/>one sentence]
    Q4[Q4 Source System<br/>type · CDC · freshness]
    Q5[Q5 Schema<br/>columns · keys]
    Q6[Q6 Classification<br/>4-tier CDMC]
    Q7[Q7 Quality<br/>nulls · uniqueness · SLA]
    Q8[Q8 Access<br/>UC ABAC tags]
    Q9[Q9 Retention<br/>regulated · GDPR]
    Q10[Q10 AI Consumption<br/>agentic · RAG · feature]

    OUT[data-contract.yml<br/>+ 2-page intake brief]
    GATE{regulated:true<br/>or pii:true?}
    GOV[Run governance-audit skill]
    DABS[Run dabs-template-init skill]

    Q1 --> Q2 --> Q3 --> Q4 --> Q5 --> Q6 --> Q7 --> Q8 --> Q9 --> Q10 --> OUT --> GATE
    GATE -- yes --> GOV --> DABS
    GATE -- no --> DABS

    classDef question fill:#AEC6CF,stroke:#333,color:#000
    classDef artifact fill:#FDFD96,stroke:#666,color:#000
    classDef decision fill:#C3B1E1,stroke:#444,color:#000
    classDef action fill:#B7E4C7,stroke:#333,color:#000

    class Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10 question
    class OUT artifact
    class GATE decision
    class GOV,DABS action
```

**Source IP:** `ip/authored/10q-framework.md` · `ip/authored/10q-toolkit/`. **Skill:** `data-source-10q-intake`.
