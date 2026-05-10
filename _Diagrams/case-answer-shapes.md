# Case Answer Shapes

> Four prompt types → framework combos. Pick the shape before picking the frameworks.

```mermaid
flowchart LR
    P[Prompt arrives]

    P --> T1{Prompt<br/>type?}
    T1 -- diagnose --> S1[Diagnostic Shape<br/>Issue tree → MECE → root cause]
    T1 -- design --> S2[Design Shape<br/>Cascade → Where to Play → How to Win]
    T1 -- defend --> S3[Defence Shape<br/>BLUF → 3 alternatives → kill criterion]
    T1 -- decide --> S4[Decision Shape<br/>Options → criteria → score → recommend]

    S1 --> F1[Frameworks: 5 Forces · MECE · root cause]
    S2 --> F2[Frameworks: Cascade · Strategy Diamond · Cornell 5-Phase]
    S3 --> F3[Frameworks: Hewing 12Q · 10-10-10 · pre-mortem]
    S4 --> F4[Frameworks: weighted scoring · System 2 · 10-10-10]

    classDef prompt fill:#FDFD96,stroke:#666,color:#000
    classDef shape fill:#AEC6CF,stroke:#333,color:#000
    classDef framework fill:#B7E4C7,stroke:#333,color:#000
    classDef decision fill:#C3B1E1,stroke:#444,color:#000

    class P prompt
    class T1 decision
    class S1,S2,S3,S4 shape
    class F1,F2,F3,F4 framework
```

**Source IP:** `Knowledge/Strategy/case-answer-shapes.md`. **Pairs with:** `practice-context/voice-and-style.md`.
