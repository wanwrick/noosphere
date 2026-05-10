# Sanitization Flow — Invariant #0

> The pre-commit gate that keeps employer / team / stakeholder / JIRA / vendor / workspace IDs out of every commit.

```mermaid
flowchart LR
    DEV[Developer<br/>git commit -m '...']
    HOOK[.pre-commit-config.yaml]
    LINT[scripts/lint_sanitization.sh<br/>banned-token regex]
    LEAKS[gitleaks scan]
    GATE{All gates<br/>pass?}
    BLOCK[Commit blocked<br/>findings → developer]
    OK[Commit accepted]
    PUSH[git push]
    CI[.github/workflows/sanitization.yml<br/>re-runs gate]
    AUDIT[_Logs/sanitization-audit.md]

    DEV --> HOOK
    HOOK --> LINT
    HOOK --> LEAKS
    LINT --> GATE
    LEAKS --> GATE
    GATE -- fail --> BLOCK
    GATE -- pass --> OK --> PUSH --> CI --> AUDIT

    classDef dev fill:#FDFD96,stroke:#666,color:#000
    classDef gate fill:#AEC6CF,stroke:#333,color:#000
    classDef decision fill:#C3B1E1,stroke:#444,color:#000
    classDef block fill:#D3D3D3,stroke:#555,color:#000
    classDef pass fill:#B7E4C7,stroke:#333,color:#000

    class DEV dev
    class HOOK,LINT,LEAKS,CI,AUDIT gate
    class GATE decision
    class BLOCK block
    class OK,PUSH pass
```

**Source IP:** `Workflows/sanitization-pass.md` · `scripts/lint_sanitization.sh` · `_Logs/sanitization-audit.md`.
