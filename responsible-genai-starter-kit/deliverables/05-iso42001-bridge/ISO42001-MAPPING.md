# ISO/IEC 42001:2023 Mapping for Responsible GenAI Starter Kit

**Version**: 0.1.0
**Date**: 2025-01-XX
**Purpose**: Map technical deliverables (D1-D4) to ISO/IEC 42001 AI Management System (AIMS) controls

---

## Executive Summary

This document provides a comprehensive mapping between the Responsible GenAI Starter Kit artifacts and ISO/IEC 42001:2023 requirements. Organizations implementing this starter kit can use this mapping to:

1. **Demonstrate compliance** during ISO 42001 audits
2. **Identify gaps** in their AI management system
3. **Accelerate certification** by leveraging pre-mapped artifacts
4. **Integrate with existing** ISO 27001 or ISO 9001 management systems

### Standards Referenced

- **ISO/IEC 42001:2023**: Information technology — Artificial intelligence — Management system ([ISO overview](https://www.iso.org/standard/81230.html))
  - *Note: This mapping references control themes and clause numbers only. Organizations should purchase the official standard from ISO for complete requirements text.*
- **NIST AI 600-1**: Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (https://doi.org/10.6028/NIST.AI.600-1)
- **NIST SP 800-218A**: SSDF for GenAI and Dual-Use Foundation Models (https://doi.org/10.6028/NIST.SP.800-218A)
- **C2PA Specification v2.2**: Coalition for Content Provenance and Authenticity Technical Specification

> **Copyright Notice**: This document does not reproduce ISO/IEC 42001:2023 text. Control mappings reference publicly available clause numbers and themes only. Organizations must obtain the official ISO standard for certification purposes.

---

## Mapping Structure

Each mapping entry includes:
- **ISO 42001 Control**: Clause number and control theme (refer to official ISO standard for complete requirement text)
- **Requirement Summary**: General description of control objectives (not verbatim from standard)
- **Starter Kit Artifact(s)**: Specific deliverable(s) that support control implementation
- **Implementation Guidance**: How to use the artifact for compliance
- **Audit Evidence**: What to present to auditors

---

## 1. Context of the Organization (Clause 4)

### 4.1 Understanding the Organization and Its Context

**ISO 42001 Requirement**: Determine external and internal issues relevant to AIMS purpose and affecting ability to achieve intended outcomes.

**Starter Kit Artifacts**:
- **D1: Model Card Template** (`/deliverables/01-gai-rmf-kit/templates/model-card.md`)
  - Section: "Intended Use" → Documents organizational context for AI deployment
  - Section: "Ethical Considerations" → Maps external regulatory/societal issues
- **D1: RAG Checklist** - Control `RAG-MAP-01` (System context documentation)
- **D1: Risk Register Template** (`/deliverables/01-gai-rmf-kit/templates/risk-register.csv`)

**Implementation Guidance**:
1. Complete Model Card "Intended Use" section for each AI system
2. Use Risk Register to document external factors (regulations, stakeholder expectations)
3. Execute `RAG-MAP-01` to define system boundaries and operational context

**Audit Evidence**:
- Completed Model Cards with context section
- Risk Register showing external issues (GDPR, AI Act, sector-specific regulations)
- System context documents from D1 checklists

---

### 4.2 Understanding the Needs and Expectations of Interested Parties

**ISO 42001 Requirement**: Determine interested parties relevant to AIMS and their requirements.

**Starter Kit Artifacts**:
- **D1: Model Card Template** - Section "Stakeholder Engagement"
- **D5: RACI Matrix** (`/deliverables/05-iso42001-bridge/RACI-MATRIX.csv`)
- **D1: Governance Controls** (`RAG-GOV-01`, `RAG-GOV-02`)

**Implementation Guidance**:
1. Document stakeholders in Model Card (data subjects, regulators, users, operators)
2. Use RACI Matrix to assign responsibilities to stakeholders
3. Implement governance committee per `RAG-GOV-01` with stakeholder representation

**Audit Evidence**:
- Stakeholder registry (from Model Cards)
- RACI Matrix showing accountability
- Governance committee meeting minutes

---

### 4.3 Determining the Scope of the AIMS

**ISO 42001 Requirement**: Define boundaries and applicability of AIMS.

**Starter Kit Artifacts**:
- **D1: Checklists** - Pattern-specific scope definitions (RAG, Fine-Tuning, Code Assistant)
- **D1: Model Card** - Section "Out-of-Scope Uses"

**Implementation Guidance**:
1. Select applicable checklist(s) matching your AI system architecture
2. Document scope boundaries in Model Card
3. Explicitly list excluded systems or lifecycle phases

**Audit Evidence**:
- Scope statement referencing specific D1 checklists
- Model Card "Out-of-Scope Uses" section
- System inventory showing which AI systems are in/out of scope

---

### 4.4 AI Management System

**ISO 42001 Requirement**: Establish, implement, maintain, and continually improve AIMS per ISO 42001.

**Starter Kit Artifacts**:
- **D1: Complete Checklist Suite** (Govern, Map, Measure, Manage functions)
- **D3: CI/CD Workflows** (`/deliverables/03-ssdf-genai-ci/workflows/`)
- **D5: Implementation Guide** (`IMPLEMENTATION-GUIDE.md`)

**Implementation Guidance**:
1. Use D1 checklists as AIMS process documentation
2. Integrate D3 CI/CD workflows for automated control execution
3. Follow D5 Implementation Guide for step-by-step setup

**Audit Evidence**:
- D1 checklist completion records
- D3 workflow execution logs
- AIMS documentation package (D1+D3+D5)

---

## 2. Leadership (Clause 5)

### 5.1 Leadership and Commitment

**ISO 42001 Requirement**: Top management demonstrates leadership and commitment to AIMS.

**Starter Kit Artifacts**:
- **D1: Governance Controls** (`RAG-GOV-01`, `FT-GOV-01`, `CA-GOV-01`)
  - Establishes governance committee with executive authority
- **D1: Model Card** - Section "Approved by"

**Implementation Guidance**:
1. Execute `RAG-GOV-01` to establish governance committee with C-level representation
2. Require executive sign-off on Model Cards (demonstrates leadership accountability)
3. Document governance charter with executive sponsor

**Audit Evidence**:
- Governance charter signed by CEO/CTO/CISO
- Model Cards approved by executive leadership
- Meeting minutes showing executive participation

---

### 5.2 AI Policy

**ISO 42001 Requirement**: Establish AI policy appropriate to organization's purpose and context.

**Starter Kit Artifacts**:
- **D1: Acceptable Use Policy Controls** (`RAG-GOV-02`, `CA-GOV-02`)
- **D1: Model Card** - Sections "Intended Use" and "Out-of-Scope Uses"

**Implementation Guidance**:
1. Use `RAG-GOV-02` to draft Acceptable Use Policy
2. Codify policy in Model Card "Intended Use" section
3. Ensure policy covers prohibited use cases (harmful content, discrimination)

**Audit Evidence**:
- Published AI Policy document
- Model Cards referencing policy
- User training records (AUP acknowledgment)

---

### 5.3 Organizational Roles, Responsibilities, and Authorities

**ISO 42001 Requirement**: Assign and communicate responsibilities for AIMS.

**Starter Kit Artifacts**:
- **D5: RACI Matrix** (`RACI-MATRIX.csv`)
- **D1: Checklist `owner_role` fields** (every control has assigned owner)

**Implementation Guidance**:
1. Populate RACI Matrix with actual names/teams from your organization
2. Map D1 checklist `owner_role` values to real job titles
3. Publish RACI matrix to intranet for organizational visibility

**Audit Evidence**:
- Completed RACI Matrix
- Job descriptions referencing AI responsibilities
- Organizational chart showing AI governance structure

---

## 3. Planning (Clause 6)

### 6.1 Actions to Address Risks and Opportunities

**ISO 42001 Requirement**: Plan actions to address AIMS risks and opportunities.

**Starter Kit Artifacts**:
- **D1: Risk Register Template** (`/deliverables/01-gai-rmf-kit/templates/risk-register.csv`)
- **D1: MAP Function Controls** (all `*-MAP-*` controls across checklists)
- **D1: Threat Modeling** (`RAG-MAP-04` references threat model)

**Implementation Guidance**:
1. Complete Risk Register for each AI system
2. Execute all MAP-phase controls from applicable D1 checklist
3. Conduct threat modeling per `RAG-MAP-04` (attack surface analysis)

**Audit Evidence**:
- Risk Register with risk owners, likelihood, impact, mitigations
- Threat model diagrams
- Completed MAP controls from D1 checklists

---

### 6.2 AI Objectives and Planning to Achieve Them

**ISO 42001 Requirement**: Establish measurable AI objectives aligned with AI policy.

**Starter Kit Artifacts**:
- **D1: MEASURE Function Controls** (all `*-MEAS-*` controls)
  - Example: `RAG-MEAS-01` establishes baseline metrics and thresholds
- **D2: Evaluation Harness** (`/deliverables/02-eval-harness/`) - Measurement infrastructure

**Implementation Guidance**:
1. Define quantitative objectives (e.g., "Refusal rate ≥98%" from `RAG-MEAS-02`)
2. Use D2 eval harness to measure objectives continuously
3. Document objectives in Model Card "Evaluation" section

**Audit Evidence**:
- AI objectives documented in Model Cards (e.g., accuracy, fairness, safety thresholds)
- D2 eval reports showing objective achievement
- Monitoring dashboards tracking objectives over time

---

## 4. Support (Clause 7)

### 7.1 Resources

**ISO 42001 Requirement**: Provide resources needed for AIMS establishment, implementation, maintenance, and improvement.

**Starter Kit Artifacts**:
- **D1: Model Card** - Section "Compute Infrastructure"
- **D1: Training Procedure Documentation** (Model Card section)
- **D3: CI/CD Workflows** - Automate resource allocation for testing/deployment

**Implementation Guidance**:
1. Document compute resources in Model Card (GPUs, training time, carbon footprint)
2. Use D3 workflows to codify resource provisioning as infrastructure-as-code
3. Track resource allocation in project plans

**Audit Evidence**:
- Model Card compute infrastructure sections
- Infrastructure-as-code configs (D3 workflows)
- Budget/cost tracking for AI resources

---

### 7.2 Competence

**ISO 42001 Requirement**: Ensure personnel are competent based on education, training, or experience.

**Starter Kit Artifacts**:
- **D1: Governance Controls** - `RAG-GOV-02` (User training completion records)
- **D6: Education One-Pager** (`/deliverables/06-education-onepager/`) - Training material

**Implementation Guidance**:
1. Require D6 training for all personnel working with AI systems
2. Track training completion per `RAG-GOV-02`
3. Document competency requirements in job descriptions

**Audit Evidence**:
- Training completion records
- D6 one-pager distribution logs
- Competency assessments (e.g., post-training quizzes)

---

### 7.3 Awareness

**ISO 42001 Requirement**: Ensure persons are aware of AI policy, AIMS requirements, and their contributions.

**Starter Kit Artifacts**:
- **D1: Acceptable Use Policy** (`RAG-GOV-02`)
- **D5: RACI Matrix** (role-based awareness)

**Implementation Guidance**:
1. Distribute D1 AUP to all users
2. Use RACI Matrix to communicate role-specific responsibilities
3. Conduct awareness sessions using D6 education material

**Audit Evidence**:
- AUP acknowledgment records
- Awareness training attendance logs
- Internal communications (emails, intranet posts)

---

### 7.4 Communication

**ISO 42001 Requirement**: Determine internal and external communications relevant to AIMS.

**Starter Kit Artifacts**:
- **D1: Model Card** - Section "Contact" (communication channels)
- **D1: Incident Response** (`RAG-MGT-05`) - Escalation paths
- **D4: C2PA Provenance** - External communication of AI-generated content

**Implementation Guidance**:
1. Use Model Card "Contact" section to define communication owners
2. Implement incident runbook per `RAG-MGT-05` with escalation procedures
3. Apply D4 C2PA watermarking for transparent external communication

**Audit Evidence**:
- Communication plan document
- Incident escalation flowcharts
- C2PA-signed content disclosing AI generation

---

### 7.5 Documented Information

**ISO 42001 Requirement**: AIMS includes documented information required by ISO 42001 and determined necessary.

**Starter Kit Artifacts**:
- **D1: Complete Artifact Suite** (checklists, templates, crosswalks)
- **D1: Model Card** (comprehensive system documentation)
- **D3: SBOM** (`/deliverables/03-ssdf-genai-ci/`) - Supply chain documentation
- **D4: C2PA Manifest** - Provenance documentation

**Implementation Guidance**:
1. Treat D1 checklists as mandatory documented procedures
2. Complete Model Card for each AI system (living document)
3. Generate SBOMs per D3 for dependency tracking
4. Use D4 C2PA for content authenticity documentation

**Audit Evidence**:
- Document repository with D1-D4 artifacts
- Version-controlled Model Cards
- SBOMs and SLSA attestations (D3)
- C2PA manifests (D4)

---

## 5. Operation (Clause 8)

### 8.1 Operational Planning and Control

**ISO 42001 Requirement**: Plan, implement, and control processes needed to meet AIMS requirements.

**Starter Kit Artifacts**:
- **D1: Lifecycle Stage Mappings** (every checklist control has `lifecycle_stage` field)
- **D3: CI/CD Workflows** - Operationalize controls as automation
- **D1: MANAGE Function Controls** (all `*-MGT-*` controls)

**Implementation Guidance**:
1. Map D1 `lifecycle_stage` values (design/dev/deploy/monitor) to your SDLC phases
2. Automate operational controls via D3 CI/CD (e.g., PII scanning, SBOM generation)
3. Execute all MANAGE-phase controls from applicable D1 checklist

**Audit Evidence**:
- Operational procedures documented in D1 checklists
- D3 workflow execution logs showing automated control execution
- Runbooks for manual MANAGE controls

---

### 8.2 AI System Impact Assessment

**ISO 42001 Requirement**: Conduct impact assessments for AI systems.

**Starter Kit Artifacts**:
- **D1: MAP Function Controls** (entire MAP phase is impact assessment)
  - `RAG-MAP-01`: Context and sensitivity assessment
  - `RAG-MAP-03`: PII/PHI identification
  - `RAG-MAP-04`: Security impact (threat modeling)
- **D1: Risk Register Template**

**Implementation Guidance**:
1. Execute all MAP-phase controls as impact assessment process
2. Document findings in Risk Register
3. Include impact assessment summary in Model Card "Ethical Considerations"

**Audit Evidence**:
- Completed MAP controls from D1 checklists
- Risk Register showing impact analysis (likelihood, severity)
- Model Card ethical considerations section

---

### 8.3 Data Management for AI Systems

**ISO 42001 Requirement**: Manage data throughout AI system lifecycle.

**Starter Kit Artifacts**:
- **D1: Data Governance Controls**:
  - `RAG-GOV-03`: Data steward assignment
  - `RAG-MAP-02`: Data source inventory
  - `RAG-MAP-03`: PII/PHI classification
- **D1: Model Card** - Section "Training Data"
- **D3: SBOM** - Dependency tracking (data tool chains)

**Implementation Guidance**:
1. Assign data steward per `RAG-GOV-03`
2. Create data lineage diagram per `RAG-MAP-02`
3. Document data sources in Model Card with licenses and limitations
4. Generate SBOMs (D3) to track data processing dependencies

**Audit Evidence**:
- Data steward appointment letter
- Data lineage diagrams
- Model Card training data section with provenance
- SBOMs showing data pipeline dependencies

---

## 6. Performance Evaluation (Clause 9)

### 9.1 Monitoring, Measurement, Analysis, and Evaluation

**ISO 42001 Requirement**: Monitor and measure AIMS processes and AI system performance.

**Starter Kit Artifacts**:
- **D1: MEASURE Function Controls** (all `*-MEAS-*` controls)
- **D2: Evaluation Harness** (`/deliverables/02-eval-harness/`)
- **D1: Monitoring Controls** (`RAG-MGT-06` - continuous drift monitoring)
- **D3: OpenSSF Scorecard** - Security posture monitoring

**Implementation Guidance**:
1. Deploy D2 eval harness for continuous measurement
2. Execute `RAG-MEAS-01` to establish baseline and thresholds
3. Implement `RAG-MGT-06` monitoring dashboard
4. Run D3 OpenSSF Scorecard weekly

**Audit Evidence**:
- D2 eval reports (historical trend data)
- Monitoring dashboards (screenshots or live access)
- D3 Scorecard results
- Incident reports showing measurement-triggered responses

---

### 9.2 Internal Audit

**ISO 42001 Requirement**: Conduct internal audits to verify AIMS conformity.

**Starter Kit Artifacts**:
- **D5: Compliance Checklist** (`compliance-checklist.yaml`)
- **D1: Acceptance Criteria** (every control has `acceptance_criteria` field for audit verification)
- **D5: Implementation Guide** - Audit preparation section

**Implementation Guidance**:
1. Use D5 Compliance Checklist as internal audit program
2. Verify each D1 control's `acceptance_criteria` is met
3. Follow D5 Implementation Guide audit preparation steps

**Audit Evidence**:
- Internal audit schedule and reports
- D5 Compliance Checklist completion records
- Corrective action plans for non-conformities

---

### 9.3 Management Review

**ISO 42001 Requirement**: Top management reviews AIMS at planned intervals.

**Starter Kit Artifacts**:
- **D1: Governance Controls** (`RAG-GOV-01` - committee meets monthly)
- **D1: Model Card** - Section "Next review" (review cadence)
- **D9 Monitoring Dashboards** (from `RAG-MGT-06`)

**Implementation Guidance**:
1. Schedule quarterly management reviews per `RAG-GOV-01`
2. Review agenda includes: D2 eval results, D3 security metrics, Model Card updates
3. Document review outputs (decisions, action items) in meeting minutes

**Audit Evidence**:
- Management review meeting minutes
- Action items with owners and due dates
- Updated AI policy/objectives post-review

---

## 7. Improvement (Clause 10)

### 10.1 Nonconformity and Corrective Action

**ISO 42001 Requirement**: React to nonconformity, take action, and implement corrective measures.

**Starter Kit Artifacts**:
- **D1: Incident Response Controls** (`RAG-MGT-05`, `FT-MGT-05`, `CA-MGT-04`)
- **D1: Model Card** - Section "Incident Response"
- **D3: CI/CD Quality Gates** - Prevent nonconforming releases

**Implementation Guidance**:
1. Implement incident runbook per `RAG-MGT-05`
2. Use D3 quality gates to block deployment on nonconformity (e.g., failed PII test)
3. Track corrective actions in issue tracker

**Audit Evidence**:
- Incident response runbook
- Incident logs with root cause analysis
- D3 workflow logs showing blocked deployments
- Corrective action closure records

---

### 10.2 Continual Improvement

**ISO 42001 Requirement**: Continually improve AIMS suitability, adequacy, and effectiveness.

**Starter Kit Artifacts**:
- **D1: Retraining Controls** (`RAG-MGT-06` - drift-triggered retraining)
- **D1: Model Card** - Section "Update Cadence"
- **D2: Evaluation Harness** - Enables A/B testing of improvements
- **D3: CI/CD Workflows** - Automate continuous deployment

**Implementation Guidance**:
1. Establish retraining triggers per `RAG-MGT-06` (e.g., accuracy drops >5%)
2. Use D2 harness to validate improvements before rollout
3. Document improvement cycles in Model Card changelog

**Audit Evidence**:
- Model Card version history showing improvements
- D2 eval reports comparing model versions
- Retraining logs and triggers
- Continuous improvement metrics (e.g., incident MTTR trend)

---

## 8. AI System Lifecycle Controls (Annex A)

ISO 42001 Annex A provides detailed AI lifecycle controls. The following sections map starter kit artifacts to Annex A requirements.

### A.1 Design and Development

**ISO 42001 Controls**:
- A.1.1 Data Management
- A.1.2 Model Development
- A.1.3 Testing and Validation

**Starter Kit Artifacts**:
- **D1: MAP + MEASURE Controls** (design-phase and development-phase items)
- **D2: Evaluation Harness** (A.1.3 testing)
- **D1: Model Card** - Sections "Training Data", "Training Procedure", "Evaluation"

**Mapping Table**:

| ISO A.1 Control | D1 Control(s) | D2 Artifact | Audit Evidence |
|-----------------|---------------|-------------|----------------|
| A.1.1 Data provenance | `RAG-MAP-02` (data inventory), `RAG-GOV-03` (data steward) | N/A | Data lineage diagram, Model Card training data section |
| A.1.1 Data quality | `RAG-GOV-03` (data quality SLA) | Data quality eval in harness | SLA document, quality metrics |
| A.1.2 Model versioning | N/A (implicit in Model Card) | N/A | Model Card version field, Git tags |
| A.1.2 Training reproducibility | Model Card "Training Procedure" | N/A | Training hyperparameters, random seeds |
| A.1.3 Test coverage | `RAG-MEAS-01` (baseline metrics), all MEAS controls | D2 eval harness | Test reports, coverage metrics |
| A.1.3 Bias testing | `RAG-MEAS-*` fairness evals | D2 demographic parity scorer | Model Card fairness section |

**Implementation Guidance**:
1. Execute all D1 MAP and MEASURE controls during design/dev phases
2. Use D2 harness for A.1.3 testing requirements
3. Document all A.1 evidence in Model Card

---

### A.2 Verification and Validation

**ISO 42001 Controls**:
- A.2.1 Independent Testing
- A.2.2 Validation Against Requirements

**Starter Kit Artifacts**:
- **D2: Evaluation Harness** (independent automated testing)
- **D1: Red Team Controls** (`RAG-MEAS-05` - third-party adversarial testing)
- **D1: Acceptance Criteria** (requirements validation)

**Mapping Table**:

| ISO A.2 Control | D1 Control(s) | D2 Artifact | Audit Evidence |
|-----------------|---------------|-------------|----------------|
| A.2.1 Independent evaluation | `RAG-MEAS-05` (red team), `FT-MEAS-06` (external audit) | D2 harness (automated) | Red team report, D2 eval logs |
| A.2.2 Requirements traceability | All D1 `acceptance_criteria` fields | N/A | Traceability matrix (control_id → acceptance_criteria → test) |

**Implementation Guidance**:
1. Use D2 harness for continuous automated validation
2. Conduct red team exercises per `RAG-MEAS-05` for independent testing
3. Create traceability matrix linking D1 controls to D2 tests

---

### A.3 Deployment

**ISO 42001 Controls**:
- A.3.1 Deployment Planning
- A.3.2 Rollback Capability
- A.3.3 Access Control

**Starter Kit Artifacts**:
- **D1: MANAGE Function Controls** (deployment-phase items)
- **D3: CI/CD Workflows** (deployment automation)
- **D1: Access Control** (`RAG-MGT-07` - RBAC)

**Mapping Table**:

| ISO A.3 Control | D1 Control(s) | D3 Artifact | Audit Evidence |
|-----------------|---------------|-------------|----------------|
| A.3.1 Deployment checklist | D1 lifecycle_stage="deployment" controls | D3 CI/CD workflows | Deployment runbook, workflow logs |
| A.3.2 Rollback procedure | Model Card "Version control" | D3 rollback workflow | Rollback test report, Model Card |
| A.3.3 RBAC implementation | `RAG-MGT-07` (access controls) | N/A | RBAC config, pentest report |

**Implementation Guidance**:
1. Execute all D1 deployment-phase controls before go-live
2. Automate deployment via D3 workflows (with manual approval gates)
3. Test rollback procedure in staging per Model Card guidance

---

### A.4 Operation and Monitoring

**ISO 42001 Controls**:
- A.4.1 Performance Monitoring
- A.4.2 Incident Management
- A.4.3 Logging and Auditability

**Starter Kit Artifacts**:
- **D1: Monitoring Controls** (`RAG-MGT-06`, `RAG-MGT-04` logging)
- **D1: Incident Response** (`RAG-MGT-05`)
- **D3: OpenSSF Scorecard** (security monitoring)

**Mapping Table**:

| ISO A.4 Control | D1 Control(s) | D3 Artifact | Audit Evidence |
|-----------------|---------------|-------------|----------------|
| A.4.1 Real-time monitoring | `RAG-MGT-06` (drift monitoring) | N/A | Dashboard screenshots, alert configs |
| A.4.2 Incident runbook | `RAG-MGT-05` (incident response plan) | N/A | Runbook doc, tabletop exercise report |
| A.4.3 Tamper-evident logs | `RAG-MGT-04` (audit logging) | N/A | Log retention policy, WORM storage config |

**Implementation Guidance**:
1. Implement `RAG-MGT-06` monitoring dashboard
2. Test incident runbook (`RAG-MGT-05`) via tabletop exercises
3. Configure tamper-evident logging per `RAG-MGT-04`

---

### A.5 Transparency and Explainability

**ISO 42001 Controls**:
- A.5.1 Documentation for Users
- A.5.2 Explainability Mechanisms

**Starter Kit Artifacts**:
- **D1: Model Card** (primary transparency artifact)
- **D4: C2PA Provenance** (content transparency)
- **D1: Citation Accuracy** (`RAG-MEAS-04` - explainability via citations)

**Mapping Table**:

| ISO A.5 Control | D1 Control(s) | D4 Artifact | Audit Evidence |
|-----------------|---------------|-------------|----------------|
| A.5.1 User-facing documentation | Model Card (public version) | C2PA manifest (content metadata) | Published Model Card, C2PA-signed content |
| A.5.2 Explainability | `RAG-MEAS-04` (citation accuracy) | C2PA "ai_generative_training" assertion | Citation test report, C2PA manifest JSON |

**Implementation Guidance**:
1. Publish Model Card to public documentation site
2. Apply D4 C2PA watermarking to all AI-generated content
3. Implement citation mechanisms per `RAG-MEAS-04` for explainability

---

### A.6 Human Oversight

**ISO 42001 Controls**:
- A.6.1 Human-in-the-Loop
- A.6.2 Override Mechanisms

**Starter Kit Artifacts**:
- **D1: Human Oversight Controls** (Model Card "Human oversight" section)
- **D1: Output Filtering** (`RAG-MGT-02` - human review triggers)

**Mapping Table**:

| ISO A.6 Control | D1 Control(s) | Audit Evidence |
|-----------------|---------------|----------------|
| A.6.1 Human review | Model Card "Ethical Considerations - Mitigations" (e.g., "Requires review for customer-facing outputs") | Human review logs, approval workflows |
| A.6.2 Override capability | `RAG-MGT-02` (output filtering with manual override) | Override logs, escalation records |

**Implementation Guidance**:
1. Document human oversight requirements in Model Card
2. Implement human review gates for high-risk outputs (`RAG-MGT-02`)
3. Log all human overrides for auditability

---

### A.7 Cybersecurity

**ISO 42001 Controls**:
- A.7.1 Threat Modeling
- A.7.2 Security Testing
- A.7.3 Supply Chain Security

**Starter Kit Artifacts**:
- **D1: Security Controls** (`RAG-MAP-04` threat modeling, `RAG-MEAS-05` red team)
- **D3: SSDF for GenAI** (entire D3 deliverable maps to A.7)
- **D3: SBOM + SLSA Provenance**

**Mapping Table**:

| ISO A.7 Control | D1 Control(s) | D3 Artifact | Audit Evidence |
|-----------------|---------------|-------------|----------------|
| A.7.1 Threat model | `RAG-MAP-04` (threat modeling) | N/A | Threat model doc, attack tree |
| A.7.2 Security testing | `RAG-MEAS-05` (red team), `RAG-MGT-01` (input validation) | N/A | Red team report, pentest results |
| A.7.3 SBOM | `RAG-MGT-08` (vendor vetting) | D3 SBOM (SPDX/CycloneDX) | SBOM files, vendor assessments |
| A.7.3 Provenance | N/A | D3 SLSA attestation | SLSA provenance JSON |
| A.7.3 Scorecard | N/A | D3 OpenSSF Scorecard | Scorecard report (weekly) |

**Implementation Guidance**:
1. Conduct threat modeling per `RAG-MAP-04` during design phase
2. Execute red team testing per `RAG-MEAS-05`
3. Generate SBOMs and SLSA attestations via D3 workflows
4. Run D3 OpenSSF Scorecard weekly; remediate findings

---

### A.8 Data Privacy

**ISO 42001 Controls**:
- A.8.1 PII Minimization
- A.8.2 Data Subject Rights

**Starter Kit Artifacts**:
- **D1: Privacy Controls**:
  - `RAG-MAP-03` (PII identification)
  - `RAG-MEAS-03` (PII detection)
  - `RAG-MGT-02` (PII redaction)

**Mapping Table**:

| ISO A.8 Control | D1 Control(s) | D2 Artifact | Audit Evidence |
|-----------------|---------------|-------------|----------------|
| A.8.1 PII inventory | `RAG-MAP-03` (PII scan), `RAG-MAP-02` (data minimization plan) | N/A | PII scan report, minimization plan |
| A.8.1 PII detection | `RAG-MEAS-03` (automated PII scorer) | D2 PII scorer | Test report showing 0% leakage |
| A.8.1 PII redaction | `RAG-MGT-02` (output filtering) | N/A | Redaction test report |
| A.8.2 Data deletion | Model Card "Retirement Plan" | N/A | Data retention policy, deletion logs |

**Implementation Guidance**:
1. Execute `RAG-MAP-03` to inventory PII in training data
2. Deploy D2 PII scorer per `RAG-MEAS-03` in CI/CD pipeline
3. Implement output redaction per `RAG-MGT-02`
4. Document data retention in Model Card; automate deletion

---

## 9. Integration with ISO 27001 (Information Security)

Organizations with existing ISO 27001 certification can integrate AI-specific controls:

| ISO 27001 Control | ISO 42001 Equivalent | Starter Kit Artifact |
|-------------------|----------------------|----------------------|
| A.5.1 Information security policies | 5.2 AI Policy | D1 `RAG-GOV-02` (AUP) |
| A.8.2 Information classification | 4.1 Context, 8.3 Data Management | D1 `RAG-MAP-03` (PII classification) |
| A.12.6 Logging and monitoring | A.4.3 Logging | D1 `RAG-MGT-04` (audit logging) |
| A.14.2 Secure development | A.1 Design and Development | D3 SSDF workflows |
| A.15.1 Supply chain security | A.7.3 Supply Chain Security | D3 SBOM + SLSA |

**Integration Strategy**:
1. Extend ISO 27001 risk register with D1 Risk Register Template (AI-specific risks)
2. Add D1 controls to ISO 27001 Statement of Applicability (SoA)
3. Merge D3 SBOM requirements into ISO 27001 supplier management processes

---

## 10. Gap Analysis Template

Use this table to assess your organization's compliance:

| ISO 42001 Clause | Requirement | Starter Kit Artifact | Status | Gap | Action |
|------------------|-------------|----------------------|--------|-----|--------|
| 4.1 Context | Document external/internal issues | D1 Model Card, Risk Register | 🟢 Implemented | None | Maintain |
| 4.2 Stakeholders | Identify interested parties | D5 RACI Matrix | 🟡 Partial | Need to populate with real names | Assign owners by Q2 |
| 5.1 Leadership | Executive commitment | D1 `RAG-GOV-01` | 🔴 Missing | No governance committee | Establish committee by end of month |
| ... | ... | ... | ... | ... | ... |

**Status Legend**:
- 🟢 Implemented: Artifact exists and is complete
- 🟡 Partial: Artifact exists but needs customization
- 🔴 Missing: Artifact does not exist; action required

---

## 11. Audit Preparation Checklist

Before an ISO 42001 audit, ensure the following artifacts are ready:

### Document Repository
- [ ] All D1 checklists completed (RAG/Fine-Tune/Code Assistant as applicable)
- [ ] Model Card completed for each in-scope AI system
- [ ] Risk Register populated with current risks
- [ ] RACI Matrix with real names/teams

### Technical Evidence
- [ ] D2 eval harness deployed; historical test results available
- [ ] D3 CI/CD workflows running; logs retained for 90+ days
- [ ] D3 SBOMs generated for all releases
- [ ] D3 SLSA attestations available
- [ ] D4 C2PA manifests for AI-generated content

### Governance Evidence
- [ ] Governance committee meeting minutes (12+ months)
- [ ] AI Policy published and communicated
- [ ] Training records (D6 one-pager distribution)
- [ ] Incident response runbook tested (tabletop exercise report)

### Performance Evidence
- [ ] Monitoring dashboards accessible to auditor
- [ ] Internal audit reports (at least one annual audit)
- [ ] Management review meeting minutes (quarterly)
- [ ] Corrective action closure records

---

## 12. References

### Standards
- **ISO/IEC 42001:2023**: Information technology — Artificial intelligence — Management system
  - Purchase: https://www.iso.org/standard/81230.html
- **ISO/IEC 23894:2023**: Artificial intelligence — Guidance on risk management
- **ISO/IEC 27001:2022**: Information security management systems — Requirements

### NIST Publications
- **NIST AI 600-1**: Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (https://doi.org/10.6028/NIST.AI.600-1)
- **NIST SP 800-218A**: SSDF for GenAI and Dual-Use Foundation Models (https://doi.org/10.6028/NIST.SP.800-218A)

### Starter Kit Deliverables
- **D1**: `/deliverables/01-gai-rmf-kit/` - GAI-RMF Implementation Kit
- **D2**: `/deliverables/02-eval-harness/` - Evaluation Harness
- **D3**: `/deliverables/03-ssdf-genai-ci/` - SSDF for GenAI CI/CD
- **D4**: `/deliverables/04-c2pa-provenance-demo/` - C2PA Provenance Demo
- **D5**: `/deliverables/05-iso42001-bridge/` - This document
- **D6**: `/deliverables/06-education-onepager/` - Education One-Pager

### Additional Resources
- **Full citations**: `/docs/refs.md`
- **C2PA Specification v2.2**: https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-01-XX | Initial release |

---

**Document Owner**: Compliance Team
**Next Review**: 2025-07-XX (6 months)
**Maintained By**: DocsWriter Agent

---

*This mapping is provided for guidance purposes and does not constitute legal or compliance advice. Organizations should consult with qualified ISO 42001 auditors and legal counsel for certification requirements.*
