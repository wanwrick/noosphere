# Governance Audit Flow — Invariant #2

> Phase advance is blocked unless the 7-check audit passes. State diagram of the gate.

```mermaid
stateDiagram-v2
    [*] --> Triggered: phase advance requested<br/>(regulated:true OR pii:true)

    Triggered --> Check1: DPIA exists + current
    Check1 --> Check2: Classification declared
    Check2 --> Check3: Masking validated
    Check3 --> Check4: Retention enforced
    Check4 --> Check5: Erasure path tested
    Check5 --> Check6: Access matches contract
    Check6 --> Check7: Cross-jurisdictional SCC

    Check1 --> Failed: any unknown
    Check2 --> Failed: untagged column
    Check3 --> Failed: no MCP-path test
    Check4 --> Failed: drift vs register
    Check5 --> Failed: no dry-run in 90d
    Check6 --> Failed: ABAC drift
    Check7 --> Failed: missing SCC

    Check7 --> Passed: all 7 pass

    Passed --> Advanced: dpia_completed=true<br/>phase++
    Failed --> Remediation: punch list with owners + dates
    Remediation --> Triggered: re-audit when gaps closed

    Advanced --> [*]
```

**Source IP:** Skill `governance-audit` (`.claude/skills/governance-audit/SKILL.md`). **Pairs with:** `governance/compliance-register.yaml` · `_Logs/sanitization-audit.md`.
