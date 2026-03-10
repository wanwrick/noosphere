# Root Cause Analysis: Template

> Blameless post-incident review. Based on Crisis Communication and After Action Review frameworks.

---

**Incident:** [Title] | **Severity:** SEV-1 / SEV-2 / SEV-3
**Date:** YYYY-MM-DD | **Duration:** [X hours/minutes]
**Author:** [Your Name] | **Review Date:** YYYY-MM-DD

---

## 1. Summary

**What happened:** [2-3 sentences: what broke, when, and the user/business impact]

**Impact:**
- Users affected: [number/scope]
- Duration: [time]
- Revenue/compliance impact: [if applicable]
- Data affected: [tables, pipelines, reports]

---

## 2. Timeline

| Time | Event | Action Taken |
|------|-------|-------------|
| HH:MM | [First sign of issue] | |
| HH:MM | [Detection/alert] | |
| HH:MM | [Incident declared] | |
| HH:MM | [Root cause identified] | |
| HH:MM | [Fix deployed] | |
| HH:MM | [All clear] | |

**Detection time:** [Time from incident start to detection]
**Resolution time:** [Time from detection to resolution]

---

## 3. Root Cause

### What went wrong
[Describe the technical root cause]

### 5 Whys Analysis

> **When to stop:** Stop when you reach a cause that is (a) actionable and within your control, and (b) a system/process issue rather than an individual behavior. If you go past 5 and are still at human error, you have not gone deep enough into the system.

1. **Why** did [symptom] happen? -> [cause 1]
2. **Why** did [cause 1] happen? -> [cause 2]
3. **Why** did [cause 2] happen? -> [cause 3]
4. **Why** did [cause 3] happen? -> [cause 4]
5. **Why** did [cause 4] happen? -> [root cause]

### Contributing Factors
- [ ] Process gap
- [ ] Missing monitoring/alerting
- [ ] Documentation gap
- [ ] Capacity/scaling issue
- [ ] Dependency failure
- [ ] Human error (blameless: focus on system that allowed it)

---

## 4. After Action Review (AAR)

| Question | Answer |
|----------|--------|
| **What was supposed to happen?** | |
| **What actually happened?** | |
| **Why was there a difference?** | |
| **What will we do differently?** | |

---

## 5. Action Items

| # | Action | Owner | Priority | Due Date | Status |
|---|--------|-------|----------|----------|--------|
| 1 | | | P0/P1/P2 | | |
| 2 | | | P0/P1/P2 | | |
| 3 | | | P0/P1/P2 | | |

---

## 6. Lessons Learned

**What went well:**
- [Things that worked during the response]

**What to improve:**
- [Gaps identified]

**Process changes:**
- [New runbook, alert, or process to prevent recurrence]

---

*This RCA was reviewed with: [names/teams] on [date]*
