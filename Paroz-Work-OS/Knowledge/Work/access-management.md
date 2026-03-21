# Data Product Access Management Framework

> Three-pillar access control model for QuestBank and the broader QFG data platform. Defines WHO can access WHAT, through which ASSIGNMENT mechanisms, with full audit traceability.

**Source:** Adam Neus strategic sessions (Dec 5, Dec 29 2025; Jan 21 2026)
**Notion Source IDs:** `2d87b88e-336f-80bf-a79f-fcee1d0b3bd3`, `2c07b88e-336f-805d-ba19-ca732fb1a7d5`
**Snapshotted:** 2026-03-11

---

## Design Principles

1. **Data Products First:** All access is scoped to data products, not raw tables
2. **Publisher/Subscriber Boundaries:** Clear separation between data producers and consumers
3. **Consumer-Centric Bias:** Optimize for subscriber (consumer) experience; producer tools come second
4. **Read-Left, Write-Right:** In the medallion model, consumers read from left (curated layers); producers write to the right (raw layers)
5. **Simple Systems Scale:** Start with the simplest viable access model, add sophistication as adoption grows
6. **User-Centric Design:** Every access flow should feel self-serve; minimize manual approvals

---

## Three-Pillar Access Control Model

### Pillar 1: WHO (Identity)

| Component | Description |
|-----------|-------------|
| **Source of Truth** | Microsoft Entra ID (Azure AD) |
| **Identity Types** | Human users, service principals, managed identities |
| **Group Strategy** | Role-based Entra groups mapped to data access levels |
| **SSO Integration** | Entra ID federated to Databricks and BigQuery |

**Key Decision:** Entra ID is the single source of truth for all identity. No local user management in Databricks or BigQuery.

### Pillar 2: WHAT (Data Classification)

CDMC-aligned classification applied to every data product:

| Level | Label | Description | Access Approach |
|-------|-------|-------------|-----------------|
| 1 | **Public** | Non-sensitive, freely shareable | Open access within platform |
| 2 | **Internal** | Business-internal, low sensitivity | Team-level group access |
| 3 | **Confidential** | PII, financial data, customer records | Role-based with steward approval |
| 4 | **Restricted** | Regulatory, AML, OSFI-mandated | Named-user access with audit trail |

**Key Data Points:**
- ~85% of QuestBank data contains PII (classified as Confidential or Restricted)
- Data classification doubled from June to December 2025
- LOS/LMS dictionaries completed; Terminus pending

### Pillar 3: ASSIGNMENT (How Access Is Granted)

| Mechanism | Use Case | Approval |
|-----------|----------|----------|
| **Self-serve catalog** | Public and Internal data | Automatic |
| **Request workflow** | Confidential data | Data steward approval |
| **Named-user provisioning** | Restricted data | Domain owner + compliance approval |
| **Time-boxed access** | Ad-hoc analysis, audits | Auto-expiry with renewal option |

---

## Access Control Phasing

### Phase 1 (Current): Power BI Controls
- Access governed at the Power BI report/workspace level
- No fine-grained column or row-level security at the lakehouse layer
- Acceptable for initial launch; not scalable

### Phase 2 (Q1-Q2 2026): ABAC + RBAC
- **ABAC (Attribute-Based Access Control):** Column masking for PII fields based on data classification attributes
- **RBAC (Role-Based Access Control):** Row filtering based on user roles (e.g., department, business unit)
- Enforced in Unity Catalog; applies to all downstream consumers (Power BI, notebooks, SQL endpoints)

### Phase 3 (Future): Full Data Mesh Access
- Decentralized steward approval workflows
- AI-assisted access recommendations
- Cross-domain access negotiation between publishers and subscribers

---

## Secure Data Tenants

Per-persona compute and storage environments:

| Tenant Type | Users | Access Level | Compute |
|-------------|-------|-------------|---------|
| **Analyst** | Business analysts, report builders | Gold/Platinum layers, read-only | SQL Warehouse (shared) |
| **Science** | Data scientists, ML engineers | Silver + Gold layers, read-write to ML schemas | ML Clusters (dedicated) |
| **Engineering** | Data engineers (DataWizards) | Full medallion access (Bronze through Platinum) | DLT Pipelines, Jobs Clusters |
| **External** | Vendors, partners, regulators | Sandboxed views of approved data products | Isolated SQL Warehouse |

**Architecture Note:** Each tenant type maps to a Databricks workspace configuration with appropriate Unity Catalog permissions, compute policies, and network isolation.

---

## Data Exchange Hub

Central mechanism for data product discovery, access request, and lifecycle management.

### Exchange Functions

| Function | Description |
|----------|-------------|
| **Discovery** | Searchable catalog of all published data products with metadata, lineage, quality scores |
| **Access Request** | Self-serve request flow with automated routing to appropriate steward |
| **Approval** | Steward-based approval for Confidential/Restricted; automatic for Public/Internal |
| **Subscriber Management** | Track who consumes what; usage analytics for publishers |
| **Quality Signals** | Three-tier certification: Standards-based, Automated controls, White-glove |

### AI-Assisted Workflows

- **Publisher side:** AI generates data descriptions, suggests classification, auto-populates metadata
- **Subscriber side:** AI recommends relevant data products based on query patterns and role
- **Governance side:** AI flags anomalous access patterns, suggests access reviews

### Private Exchange vs. External Marketplace

| Aspect | Private Exchange | External Marketplace |
|--------|-----------------|---------------------|
| **Scope** | Internal QFG data products | Partner and vendor data |
| **Governance** | Internal stewards | Legal + compliance approval |
| **Platform** | Unity Catalog + Databricks | Databricks Marketplace (future) |
| **Priority** | Q1-Q2 2026 | Q3+ 2026 |

---

## Catalog Hierarchy

### Unity Catalog (Databricks)
```
Metastore
  > Catalog (per domain / business unit)
       > Schema (per data product or subject area)
            > Table / View / Function / Model
```

### BigQuery (GCP, brokerage side)
```
Organization
  > Project (per domain)
       > Dataset (per subject area)
            > Table / View / Routine
```

### Cross-Platform Governance
- Unity Catalog is the primary governance control plane
- BigQuery projects mapped to equivalent Unity Catalog catalogs
- Collibra evaluated for cross-platform catalog sync (bi-directional sync in public preview)
- Entra ID groups applied consistently across both platforms

---

## PII Classification Implementation (QB-9079) — March 2026

Active implementation of ABAC column masking and row-level security for QuestBank. Mariano Barrionuevo leads; Nilanjana as governance partner.

### Two-Phase Approach

**Phase 1: Immediate Protection (Sprint 5, running now)**
Goal: Protect QuestBank data products before go-live. 5-step sequence:

| Step | Ticket | Description | Effort |
|------|--------|-------------|--------|
| 1 | QB-9115 | Create governance.* schema + PI LDM as code | 1.5 days |
| 2 | QB-9113 | Databricks AI classification scan + domain mapping sessions | 1 day + 4x2hr sessions |
| 3 | QB-9114 | Define UC governed tag taxonomy + apply PII tags via Terraform | 1.5 days |
| 4 | QB-9098 | Implement 8 masking functions + column policies via Terraform | 3 days |
| 5 | QB-9099 | Build dual data products, Row-Level Security + domain sign-off | 2 days + 0.5/engineer |

**Blockers:** Nilanjana needs Databricks admin access; Fran/Mauro needed for managed tags approval.
**Authority:** Daniel Dininio's PI LDM spreadsheet. All 39 PI attributes are Confidential + Highly Valuable.

**Phase 2: Repeatable Automated Framework (Sprint 6+)**
Goal: Build a scalable, automated classification and masking framework across all domains.
- Focus sessions with Databricks (Monty) being arranged
- Dependent on Phase 1 completion
- Will extend the 5-step sequence into a reusable template for future data domains
- Owned by: Mariano + Nilanjana + Cam (Cam in learning mode to reduce Mariano load)

### Entra ID Group Provisioning

Kriti Sood (Platform Team) owns Entra ID group creation for PII access:

| Group | Scope | Status |
|-------|-------|--------|
| pii_full_access | Regulatory, audit, compliance teams | Provisioning in progress |
| pii_analytics | All analysts, BI, reporting teams | Provisioning in progress |
| pii_superuser | Governance + platform engineers (PAM-controlled) | Deferred to Sprint 6 |
| questbank_rls | All QB users | Row filter: business_entity = 'questbank' |

### Databricks Cluster Incident (March 2026)

Root cause identified and resolved. Relevant to access management because it affected data product availability:
- **Root cause:** DLT creates 1 cluster per job; 12+ simultaneous pipelines = 12+ clusters exceeding shared cluster limits on PCI endpoint
- **Cost impact:** Approximately $4,000-5,000 in unexpected compute costs
- **Resolution:** Cluster configuration fixed; post-mortem scheduled (Paroz + Gabriel + Fran)
- **Deferred action:** Cluster tagging deferred until post-bank-launch
- **Lesson:** Shared clusters on PCI endpoint are the forced path until GCP serverless private endpoint becomes available (expected end of March or mid-April)

---

## Audit and Compliance Requirements

| Requirement | Implementation |
|-------------|---------------|
| **Access logging** | All data access events logged to Unity Catalog system tables |
| **Query auditing** | Full SQL query history retained (90+ days) |
| **Steward approvals** | Approval chain captured with timestamp, approver, justification |
| **Classification enforcement** | Automated checks that classified data has appropriate controls |
| **Regulatory reporting** | OSFI and PIPEDA audit trails exportable on demand |
| **Access reviews** | Quarterly access certification by domain stewards |

**Success Metrics:**
- Time to access < 2 business days (from request to provisioned)
- 100% audit coverage for Confidential and Restricted data
- 50%+ data access via self-serve catalog (vs. manual provisioning)
- 0 compliance findings related to data access

---

## Glossary

| Term | Definition |
|------|-----------|
| **Data Product** | A curated, governed, discoverable dataset published for consumption |
| **Publisher** | Team that owns, produces, and maintains a data product |
| **Subscriber** | Team or individual that consumes a published data product |
| **Steward** | Domain expert responsible for approving access and ensuring quality |
| **Medallion** | Layered architecture (Bronze, Silver 0-3, Gold, Platinum) for progressive data refinement |
| **ABAC** | Attribute-Based Access Control: fine-grained policies based on data and user attributes |
| **RBAC** | Role-Based Access Control: access based on user role assignments |
| **CDMC** | Cloud Data Management Capabilities framework for data classification |
| **Unity Catalog** | Databricks governance layer for data, ML models, and access control |
| **Data Exchange** | Internal marketplace for data product discovery, request, and provisioning |

---

*Cross-references: [q1-strategy.md](./q1-strategy.md) for initiative context, [data-mesh-vision.md](./data-mesh-vision.md) for architectural philosophy, [databricks.md](./databricks.md) for technical patterns*

*Snapshotted from Notion 2026-03-11. For live updates, fetch page IDs above.*
