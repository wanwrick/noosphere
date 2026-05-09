# DABs Data-Contract Golden Path — Contract Flow

> One `data-contract.yml` → Bronze ingestion + Silver DLT + UC ABAC + Platinum views + CI/CD. The mechanical bottom of contract-first data engineering.

```mermaid
flowchart LR
    CTR[data-contract.yml<br/>Producer + consumer + schema<br/>+ classification + DQ + access]

    BRZ[Bronze ingestion<br/>schema-on-read]
    SLV[Silver DLT<br/>quality expectations]
    UC[UC permissions<br/>ABAC tags by tier]
    PLT[Platinum views<br/>masked + AI-shaped]
    AIC[AI Consumption<br/>Contract per agent]
    CI[CI/CD<br/>validate · pytest · lint]

    CTR --> BRZ
    CTR --> SLV
    CTR --> UC
    CTR --> PLT
    CTR --> AIC
    CTR --> CI

    classDef contract fill:#FDFD96,stroke:#666,color:#000
    classDef render fill:#AEC6CF,stroke:#333,color:#000
    classDef gate fill:#B7E4C7,stroke:#333,color:#000

    class CTR contract
    class BRZ,SLV,UC,PLT,AIC render
    class CI gate
```

**Time to deployable dev product:** under 30 minutes given a complete contract.
**Source IP:** `ip/authored/dabs-data-contract-golden-path.md` · `templates/dabs-data-product-template/`.
**Curated:** Data Contracts Producer-Consumer · Mahboub Metadata-Driven Ingestion · DABs CI/CD.
