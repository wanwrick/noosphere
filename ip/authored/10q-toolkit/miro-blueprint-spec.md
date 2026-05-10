# 10Q — Miro Blueprint Spec

> Visual workshop blueprint for running the 10Q discovery session in Miro (or FigJam / Mural). Designed for a 90-minute session with source owner + producer engineer + (optional) consumer observer.

## Frame layout (left → right)

```
+----------------------------------------------------------------+
|  CONTEXT       |  THE 10 QUESTIONS                |  DECISION  |
|  (10 min)      |  (60 min)                        |  (20 min)  |
+----------------+----------------------------------+------------+
|  Source name   | Q1 Volume      Q2 Freshness      | Cost band  |
|  Use case      | Q3 Schema      Q4 Quality        | Freshness  |
|  Consumer      | Q5 Source type Q6 Incremental    | tier       |
|  Stakeholders  | Q7 PII         Q8 Rate limits    | GO/NO/SB   |
|                | Q9 Replay      Q10 Gotchas       |            |
+----------------+----------------------------------+------------+
```

## Sticky note conventions

| Color | Meaning |
|---|---|
| 🟢 Green | Answered confidently |
| 🟡 Yellow | Partial / "we think so" |
| 🔴 Red | Unknown / contested |
| 🔵 Blue | Producer engineer's note (pattern, risk, cost flag) |
| 🟣 Purple | Decision / commitment |

## RACI overlay

In a separate frame, place a 4x10 grid:

| Question | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Q1 Volume | Source eng | Source owner | Producer eng | Consumer team |
| Q2 Freshness | Consumer team | Source owner | Producer eng | Source eng |
| … | … | … | … | … |

Use this to prevent the question "but who actually owns this?" from derailing the session.

## Decision tree (separate frame)

A simple flow:

```
            +--------------------+
            | All 10 answered?    |
            +----------+----------+
                       |
            yes        |        no
       +-------+       |        +--------------------+
       |       |       |        | red_flag_count > 0 |
       |       v       |        +---------+----------+
       |  Cost band    |                  |
       |  agreed?      |          yes     |   no
       |  +------+-----+                  |
       |  |      |                        |
       |  v      v                        v
       | yes    no                   SEND BACK
       |       NO-GO                 (with specific Qs)
       |
       v
       GO  -> proceed to Design
```

## Tools

- **Miro template ID:** create a workspace template named "10Q Discovery — v1.2.0" with the frame layout above.
- **Export:** at session end, export to PDF and attach to the intake tracker row.
- **Photos:** if running in person, photo every frame and attach.

## Anti-patterns

- **Skipping the Context frame.** "We all know what this is." Five minutes later you're 20 minutes deep on Q1 because the use case was unclear.
- **Letting one person fill in all the stickies.** The point is to surface multi-stakeholder disagreement.
- **Erasing red stickies after the session.** Red is signal. Capture in the tracker, don't hide.
