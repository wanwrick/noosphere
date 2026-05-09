# Medallion Layers — Property Table

> One row per layer. Property differences are deliberate, not historical accident.

```mermaid
flowchart TB
    subgraph BRZ[Bronze]
        B1[Schema: source-mirroring]
        B2[Quality: schema-on-read]
        B3[Access: engineering only]
        B4[Retention: long · auditable]
    end

    subgraph SLV[Silver]
        S1[Schema: conformed]
        S2[Quality: DLT expectations]
        S3[Access: engineering + analytics]
        S4[Retention: regulatory-driven]
    end

    subgraph GLD[Gold]
        G1[Schema: business marts]
        G2[Quality: SLA-bound]
        G3[Access: domain consumers]
        G4[Retention: business-driven]
    end

    subgraph PLT[Platinum]
        P1[Schema: consumption-shaped]
        P2[Quality: DLT-inherited]
        P3[Access: AI consumers · ABAC]
        P4[Retention: consumption-driven]
    end

    BRZ --> SLV --> GLD --> PLT

    classDef bronze fill:#D3D3D3,stroke:#555,color:#000
    classDef silver fill:#AEC6CF,stroke:#333,color:#000
    classDef gold fill:#FDFD96,stroke:#666,color:#000
    classDef platinum fill:#C3B1E1,stroke:#444,color:#000

    class B1,B2,B3,B4 bronze
    class S1,S2,S3,S4 silver
    class G1,G2,G3,G4 gold
    class P1,P2,P3,P4 platinum
```

**Rule:** if a layer cannot answer all four properties, it does not exist yet — it is aspirational.

**Source IP:** `ip/authored/no-lac-principle.md` · `ip/authored/ai-ready-platinum-layer.md`.
