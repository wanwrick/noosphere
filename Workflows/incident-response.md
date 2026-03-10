# Incident Response Workflow

> SEV-based playbook for data platform incidents. Integrates crisis communication, stakeholder notification, and blameless post-mortem.

---

## Severity Classification

| Level | Definition | Response Time | Example |
|-------|-----------|--------------|---------|
| **SEV-1** | Critical: production data loss (>1000 rows), compliance breach, complete pipeline failure affecting >50% of consumers | Immediate (< 15 min) | Gold layer down, regulatory report missed |
| **SEV-2** | Major: significant degradation (>2 hours), key pipeline delayed past SLA, data quality score drops below 95% | < 1 hour | Silver layer SLA missed, dashboard stale > 4 hours |
| **SEV-3** | Minor: non-critical pipeline failure (<5 tables), cosmetic issue, workaround available | < 4 hours | Single non-critical table delayed, formatting issue |

---

## Phase 1: Detection & Triage (0-15 minutes)

### Trigger Sources
- Automated alert (DLT failure, freshness SLA breach, quality expectation violation)
- User report (Slack, email, ticket)
- Monitoring dashboard anomaly

### Immediate Actions
1. **Acknowledge** the alert/report within 5 minutes
2. **Classify severity** using the table above
3. **Declare incident** in Slack: `#inc-YYYY-MM-DD-[topic]`
4. **Assign Incident Commander (IC)**: for SEV-1/2, this is the team lead unless delegated
5. **Post initial status:**
   ```
   INCIDENT DECLARED: [Title]
   Severity: SEV-[X]
   IC: [Name]
   Impact: [Who/what is affected]
   Status: Investigating
   Next update: [time]
   ```

---

## Phase 2: Investigation & Containment (15 min - 2 hours)

### IC Responsibilities
- Own the communication cadence (updates every 30 min for SEV-1, 1 hour for SEV-2)
- Coordinate responders: don't fix, orchestrate
- Keep a running timeline in the incident channel
- Escalate if needed (VP Engineering for SEV-1)

### Investigation Checklist
- [ ] Check pipeline event log for error details
- [ ] Review governance audit logs for recent changes
- [ ] Check cluster/warehouse compute health
- [ ] Verify source system status (core system, streaming, APIs)
- [ ] Compare to last known good state
- [ ] Check for recent deployments or config changes

### Containment Options
| Strategy | When to Use |
|----------|-------------|
| **Rollback** | Bad deployment or config change caused the issue |
| **Failover** | Hardware/compute failure, switch to backup |
| **Isolate** | Issue spreading; contain to affected domain |
| **Workaround** | Manual process to maintain business continuity |

---

## Phase 3: Resolution & Communication

### Stakeholder Notification Matrix
| Severity | Who to Notify | Channel | When |
|----------|--------------|---------|------|
| SEV-1 | VP Engineering, CTO, Compliance | Slack DM + Email | Immediately |
| SEV-1 | Affected business units | Email | Within 30 min |
| SEV-2 | VP Engineering, affected team leads | Slack | Within 1 hour |
| SEV-3 | Team channel | Slack thread | Next standup |

### Resolution Update Template
```
INCIDENT RESOLVED: [Title]
Duration: [X hours/minutes]
Root Cause: [One sentence]
Fix Applied: [What was done]
Remaining Risk: [Any lingering issues]
Post-mortem: Scheduled for [date]
```

---

## Phase 4: Post-Mortem (within 48 hours)

1. **Schedule blameless review** with all involved parties
2. **Use RCA template** (`Templates/rca-template.md`)
3. **Complete 5 Whys** and After Action Review
4. **Assign action items** with owners and due dates
5. **Share learnings** at next sprint retrospective
6. **Update runbooks** with new knowledge

### Post-Mortem Ground Rules
- Blameless: focus on systems, not individuals
- Assume good intent: everyone did their best with available information
- Focus on prevention: how do we make this impossible to repeat?
- Document everything: future team members need this context

---

## Quick Reference: Escalation Path

```
Data Engineer -> Team Lead (IC) -> VP Engineering -> CTO
                      |
                Compliance (if data governance/regulatory)
                      |
                Business stakeholders (if user-facing impact)
```
