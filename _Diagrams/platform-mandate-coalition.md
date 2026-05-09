# Platform-Mandate Coalition Sequence

> How a platform formalization gets ratified. Engineers → adjacent leaders → manager → decision-maker. Coalition before announcement.

```mermaid
sequenceDiagram
    autonumber
    participant E as Engineers
    participant A as Adjacent Leaders<br/>(security · finance · domain)
    participant M as Engineering Manager
    participant D as Decision-Maker<br/>(CDO · VP Eng)

    E->>E: Draft mandate (No LAC + Platinum)
    E->>A: Brief 1-on-1: pre-empt objections
    A-->>E: Reservations · adjustments
    E->>E: Revise — incorporate feedback
    E->>M: Brief manager with adjacent endorsements
    M-->>E: Refine fee model · scope · timeline
    E->>D: Pitch with coalition signal stack
    D-->>E: Conditional yes · ratification path
    E->>A: Confirm ratification
    E->>M: Confirm ratification
    Note over E,D: Announcement only after ratification
```

**Source IP:** `ip/authored/platform-mandate-playbook.md`.
**Pairs with:** `Workflows/executive-briefing.md` · `Workflows/negotiation-prep.md`.
