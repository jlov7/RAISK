# D5: ISO/IEC 42001 Bridge Documentation

Map the Responsible GenAI Starter Kit to ISO/IEC 42001:2023 AI Management System requirements.

---

## Overview

This deliverable provides a comprehensive bridge between the technical artifacts in the Responsible GenAI Starter Kit (D1-D4) and ISO/IEC 42001:2023 compliance requirements. Organizations implementing this kit can accelerate ISO 42001 certification by leveraging pre-mapped controls and documentation.

### What is ISO/IEC 42001?

ISO/IEC 42001:2023 is the first international standard for AI Management Systems (AIMS). It specifies requirements for:
- Establishing AI governance and leadership commitment
- Managing AI risks throughout the system lifecycle
- Ensuring transparency, fairness, and accountability
- Demonstrating compliance to regulators, customers, and auditors

---

## Contents

### 1. [ISO42001-MAPPING.md](ISO42001-MAPPING.md)
**Comprehensive control mapping document**

- Maps all Starter Kit artifacts (D1-D4) to ISO 42001 Clauses 4-10 and Annex A
- Includes:
  - **Clause mappings**: Context (4), Leadership (5), Planning (6), Support (7), Operation (8), Performance (9), Improvement (10)
  - **Annex A mappings**: Design & Development, Verification, Deployment, Operation, Transparency, Human Oversight, Cybersecurity, Data Privacy
- For each control:
  - ISO requirement summary
  - Starter Kit artifact(s) that satisfy the requirement
  - Implementation guidance
  - Audit evidence to present
- Gap analysis template
- Integration guidance for ISO 27001, ISO 9001, NIST AI RMF, EU AI Act

**Use this for**: Understanding which Starter Kit artifacts map to which ISO 42001 requirements, preparing audit evidence packages.

---

### 2. [RACI-MATRIX.csv](RACI-MATRIX.csv)
**Roles and responsibilities assignment matrix**

- Defines RACI assignments (Responsible, Accountable, Consulted, Informed) for all compliance activities
- Roles included:
  - Data Scientist
  - ML Engineer
  - Security Team
  - Compliance Officer
  - Platform Engineer
  - Privacy Officer
  - CISO
  - Product Manager
  - DevOps/SRE
- Activities mapped to:
  - Deliverables (D1-D6)
  - ISO 42001 clauses
  - Specific technical implementations (governance, data management, testing, monitoring, etc.)

**Use this for**: Assigning ownership, communicating responsibilities, structuring your AI governance team.

**Action Required**: Populate the matrix with actual names/teams from your organization.

---

### 3. [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md)
**Step-by-step implementation guide**

- **Phase 1: Planning and Gap Analysis** (2-4 weeks)
  - Conduct gap analysis
  - Define scope statement
  - Create implementation roadmap
- **Phase 2: Implementation** (12-16 weeks)
  - Establish governance (Clause 5)
  - Implement data management (Clause 8.3)
  - Conduct risk assessment (Clause 6.1, 8.2)
  - Deploy evaluation harness (Clause 9.1)
  - Implement operational controls (Clause 8.1)
  - Implement transparency controls (Annex A.5)
- **Phase 3: Validation and Audit Preparation** (4-6 weeks)
  - Conduct internal audit
  - Management review
  - Prepare audit evidence package
  - Select certification body
- Includes:
  - Audit preparation checklist
  - Common pitfalls and solutions
  - Integration strategies (ISO 27001, ISO 9001, NIST AI RMF, EU AI Act)
  - Sample timelines (small and large organizations)

**Use this for**: Executing ISO 42001 implementation from planning through certification audit.

---

### 4. [compliance-checklist.yaml](compliance-checklist.yaml)
**Compliance tracking and audit tool**

- Structured YAML checklist covering:
  - All ISO 42001 Clauses 4-10
  - All Annex A controls (A.1-A.8)
- For each control:
  - `status`: not_started | in_progress | implemented | verified
  - `evidence`: Required artifacts/documentation
  - `responsible`: Role/person from RACI matrix
  - `notes`: Implementation details, exceptions, findings
- Summary metrics section (track completion percentage)
- Audit history log

**Use this for**: Tracking implementation progress, conducting internal audits, preparing for certification audits.

**Action Required**: Update `status` and `notes` fields as you implement controls.

---

## Quick Start

### Step 1: Understand Your Baseline
1. Read [ISO42001-MAPPING.md](ISO42001-MAPPING.md) Section 10 (Gap Analysis Template)
2. Assess which ISO 42001 requirements you already satisfy
3. Identify gaps requiring new implementations

### Step 2: Assign Ownership
1. Open [RACI-MATRIX.csv](RACI-MATRIX.csv)
2. Replace role titles with actual names/teams from your organization
3. Communicate assignments to your team

### Step 3: Follow the Implementation Guide
1. Read [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md)
2. Choose your timeline (small org: 6 months, large org: 9 months)
3. Execute Phase 1 → Phase 2 → Phase 3

### Step 4: Track Progress
1. Open [compliance-checklist.yaml](compliance-checklist.yaml)
2. Update `status` field as you complete controls
3. Use for internal audits and management reviews

---

## Key ISO 42001 Controls Addressed

This deliverable provides direct support for the following ISO 42001 requirements:

### Governance and Leadership
- **Clause 5.1**: Leadership and Commitment → D1 Governance Controls (`RAG-GOV-01`)
- **Clause 5.2**: AI Policy → D1 Acceptable Use Policy (`RAG-GOV-02`)
- **Clause 5.3**: Roles and Responsibilities → D5 RACI Matrix

### Risk Management
- **Clause 6.1**: Actions to Address Risks → D1 Risk Register, D1 MAP Controls
- **Clause 8.2**: AI Impact Assessment → D1 MAP Function (entire phase)

### Data Management
- **Clause 8.3**: Data Management for AI → D1 Data Controls (`RAG-MAP-02`, `RAG-MAP-03`, `RAG-GOV-03`)
- **Annex A.8**: Data Privacy → D1 PII Controls (`RAG-MEAS-03`, `RAG-MGT-02`)

### Testing and Validation
- **Annex A.1.3**: Testing and Validation → D2 Evaluation Harness, D1 MEASURE Controls
- **Annex A.2**: Verification and Validation → D1 Red Team (`RAG-MEAS-05`), D2 Harness

### Operational Controls
- **Clause 8.1**: Operational Planning → D3 CI/CD Workflows, D1 MANAGE Controls
- **Annex A.4**: Operation and Monitoring → D1 Monitoring (`RAG-MGT-06`), Logging (`RAG-MGT-04`)

### Transparency
- **Annex A.5**: Transparency and Explainability → D1 Model Card, D4 C2PA Provenance

### Cybersecurity
- **Annex A.7**: Cybersecurity → D1 Threat Modeling (`RAG-MAP-04`), D3 SBOM/SLSA/Scorecard

### Performance Evaluation
- **Clause 9.1**: Monitoring and Measurement → D2 Evaluation Harness, D1 `RAG-MGT-06`
- **Clause 9.2**: Internal Audit → D5 Compliance Checklist
- **Clause 9.3**: Management Review → D1 Governance Meetings

### Improvement
- **Clause 10.1**: Nonconformity and Corrective Action → D1 Incident Response (`RAG-MGT-05`)
- **Clause 10.2**: Continual Improvement → D1 Retraining (`RAG-MGT-06`)

---

## Integration with Other Standards

### ISO 27001 (Information Security)
- Shared controls: Policies (5.2), Logging (A.4.3), Supply Chain (A.7.3)
- Strategy: Extend ISO 27001 Statement of Applicability (SoA) with AI-specific controls from D1
- See [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Section 8.1

### ISO 9001 (Quality Management)
- Shared controls: Context (4.1), Internal Audit (9.2), Corrective Action (10.1)
- Strategy: Integrate D1 checklists into existing quality management processes
- See [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Section 8.2

### NIST AI RMF (AI Risk Management Framework)
- Direct alignment: D1 checklists implement NIST AI 600-1 Govern/Map/Measure/Manage functions
- Strategy: Use NIST AI RMF as implementation guide; ISO 42001 as certification standard
- See [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Section 8.3

### EU AI Act
- Alignment: D1 Model Cards satisfy AI Act documentation requirements (Article 11)
- Strategy: Leverage ISO 42001 certification for AI Act conformity assessment (pending harmonization)
- See [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Section 8.4

---

## Audit Evidence Summary

When preparing for ISO 42001 certification audit, you will need to present the following evidence:

### Documentation
- [ ] AI Policy (published, communicated)
- [ ] Governance Charter (signed by executives)
- [ ] RACI Matrix (populated with names)
- [ ] Scope Statement
- [ ] Risk Register (current, with owners and mitigations)
- [ ] Model Cards (one per AI system)

### Technical Evidence
- [ ] D1 Checklists (all controls completed with acceptance criteria met)
- [ ] D2 Evaluation Reports (baseline + historical trends)
- [ ] D3 SBOMs (SPDX/CycloneDX for all releases)
- [ ] D3 SLSA Attestations
- [ ] D3 OpenSSF Scorecard Results
- [ ] D4 C2PA Manifests

### Operational Evidence
- [ ] Monitoring Dashboards (accessible to auditor)
- [ ] Audit Logs (90+ days retention)
- [ ] Incident Response Runbook
- [ ] Tabletop Exercise Report

### Performance Evidence
- [ ] Internal Audit Reports (annual minimum)
- [ ] Management Review Minutes (quarterly, 12+ months)
- [ ] Corrective Action Records

See [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Section 6 for the complete audit preparation checklist.

---

## How This Deliverable Relates to Other Kit Components

### D1: GAI-RMF Implementation Kit
- **Relationship**: D1 provides the technical controls; D5 maps them to ISO 42001 requirements
- **Usage**: Execute D1 checklists → Track completion in D5 compliance checklist → Present as audit evidence
- **Key Link**: D1 checklist `control_id` and `acceptance_criteria` fields enable audit verification

### D2: Evaluation Harness
- **Relationship**: D2 implements ISO 42001 Clause 9.1 (Monitoring and Measurement) and Annex A.1.3 (Testing)
- **Usage**: Deploy D2 harness → Generate eval reports → Present as evidence of measurement capability
- **Key Link**: D2 scorers (PII, refusal, bias) directly satisfy D1 MEASURE controls

### D3: SSDF for GenAI CI/CD
- **Relationship**: D3 implements ISO 42001 Annex A.7.3 (Supply Chain Security) and Clause 8.1 (Operational Planning)
- **Usage**: Run D3 workflows → Generate SBOMs/SLSAs → Present as supply chain evidence
- **Key Link**: D3 automation operationalizes D1 controls as CI/CD gates

### D4: C2PA Provenance Demo
- **Relationship**: D4 implements ISO 42001 Annex A.5 (Transparency)
- **Usage**: Apply D4 C2PA watermarking → Publish C2PA manifests → Demonstrate content authenticity
- **Key Link**: C2PA manifests provide external transparency for AI-generated content

### D6: Education One-Pager
- **Relationship**: D6 supports ISO 42001 Clause 7.2 (Competence) and 7.3 (Awareness)
- **Usage**: Distribute D6 to users → Track training completion → Present as awareness evidence
- **Key Link**: Training records demonstrate compliance with competence requirements

---

## Timeline Expectations

### Small Organization (1-3 AI systems, 5-10 person team)
- **Gap Analysis**: 1-2 weeks
- **Implementation**: 12-16 weeks
- **Validation**: 4-6 weeks
- **Certification Audit**: 2-3 weeks
- **Total**: 5-6 months

### Large Organization (10+ AI systems, 50+ person team)
- **Gap Analysis**: 3-4 weeks
- **Pilot Implementation**: 8-12 weeks (on 1-2 systems)
- **Rollout**: 12-16 weeks (scale to all systems)
- **Validation**: 6-8 weeks
- **Certification Audit**: 3-4 weeks
- **Total**: 8-10 months

See [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Appendices B and C for detailed timelines.

---

## Success Metrics

Track these metrics to measure ISO 42001 implementation progress:

| Metric | Target | Tracking Method |
|--------|--------|-----------------|
| **Compliance Checklist Completion** | 100% | D5 compliance-checklist.yaml `status` field |
| **D1 Control Completion** | 100% of applicable controls | D1 checklist tracking |
| **Model Card Completeness** | All sections filled, reviewed | Model Card template completion |
| **Audit Readiness** | All evidence accessible in <1 hour | Mock audit exercise |
| **Internal Audit Findings** | 0 major non-conformities | Internal audit report |
| **Management Review Frequency** | Quarterly (minimum) | Meeting calendar |

---

## Common Questions

### Q: Do I need to implement ALL D1 checklist controls?
**A**: Only those applicable to your AI system pattern (RAG, Fine-Tuning, or Code Assistant). Select the checklist matching your architecture. However, you must complete ALL controls within your selected checklist(s) for ISO 42001 compliance.

### Q: Can I get ISO 42001 certified using only this starter kit?
**A**: The starter kit provides the technical foundation, but you must:
1. Customize artifacts to your organization (populate RACI with real names, update Model Cards with your system details)
2. Operate the system long enough to generate evidence (eval reports, monitoring data, incident logs)
3. Conduct internal audits and management reviews
4. Engage an accredited certification body for external audit

This kit significantly accelerates certification, but executive commitment and operational maturity are still required.

### Q: How does this relate to ISO 27001?
**A**: ISO 42001 is complementary to ISO 27001. Many controls overlap (e.g., logging, supply chain security). If you already have ISO 27001, you can integrate AI-specific controls from this kit into your existing Information Security Management System (ISMS). See [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Section 8.1.

### Q: What if my organization doesn't use all deliverables (e.g., we don't use C2PA)?
**A**: ISO 42001 allows flexibility in implementation methods. If you don't use D4 C2PA, document an alternative approach to transparency (Annex A.5) in your Model Card. However, some deliverables (D1, D2, D3) are essential for meeting core ISO 42001 requirements.

### Q: How often do I need to update compliance documentation?
**A**:
- **Model Cards**: Update on retraining, major feature changes, or incidents (quarterly review recommended)
- **Risk Register**: Review quarterly or when threat landscape changes
- **Compliance Checklist**: Update continuously as controls are implemented; full review during internal audits
- **RACI Matrix**: Update when roles change or new AI systems are added

---

## Support and Next Steps

### Next Steps
1. **Read the Mapping**: Start with [ISO42001-MAPPING.md](ISO42001-MAPPING.md) to understand the landscape
2. **Assign Roles**: Populate [RACI-MATRIX.csv](RACI-MATRIX.csv) with your team
3. **Follow the Guide**: Execute [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Phase 1 (Gap Analysis)
4. **Track Progress**: Use [compliance-checklist.yaml](compliance-checklist.yaml) for daily tracking

### Additional Resources
- **ISO 42001 Standard**: Purchase from https://www.iso.org/standard/81230.html
- **NIST AI 600-1**: https://doi.org/10.6028/NIST.AI.600-1
- **Full Citations**: `/docs/refs.md`

### Questions?
- Open an issue in the repository
- Consult with an ISO 42001 accredited auditor
- Review the [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md) Common Pitfalls section

---

## License

- **Documentation** (all .md files): CC-BY-4.0
- **Code/Templates** (.yaml, .csv): Apache-2.0

See main repository LICENSE for details.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-01-XX | Initial release |

---

**Document Owner**: Compliance Team
**Maintained By**: DocsWriter Agent
**Next Review**: 2025-07-XX (6 months)
