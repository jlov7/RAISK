# ISO/IEC 42001 Implementation Guide

**Version**: 0.1.0
**Date**: 2025-01-XX
**Audience**: Compliance Officers, AI Governance Leads, Implementation Teams

---

## Table of Contents

1. [Overview](#1-overview)
2. [Getting Started](#2-getting-started)
3. [Phase 1: Planning and Gap Analysis](#3-phase-1-planning-and-gap-analysis)
4. [Phase 2: Implementation](#4-phase-2-implementation)
5. [Phase 3: Validation and Audit Preparation](#5-phase-3-validation-and-audit-preparation)
6. [Audit Preparation Checklist](#6-audit-preparation-checklist)
7. [Common Pitfalls](#7-common-pitfalls)
8. [Integration Strategies](#8-integration-strategies)
9. [Appendices](#9-appendices)

---

## 1. Overview

### 1.1 Purpose

This guide provides step-by-step instructions for implementing ISO/IEC 42001:2023 AI Management System (AIMS) requirements using the Responsible GenAI Starter Kit.

### 1.2 What is ISO/IEC 42001?

ISO/IEC 42001 is the first international standard for AI management systems. It specifies requirements for:
- Establishing an AI governance framework
- Managing AI risks throughout the system lifecycle
- Ensuring transparency, fairness, and accountability
- Demonstrating compliance to regulators and customers

### 1.3 Who Should Use This Guide?

- **Compliance Officers**: Leading ISO 42001 certification efforts
- **AI Governance Teams**: Establishing AI policies and oversight
- **Implementation Teams**: Technical staff deploying AI systems
- **Auditors**: Internal audit teams preparing for certification

### 1.4 Prerequisites

Before starting, ensure you have:
- [ ] Executive sponsorship for ISO 42001 certification
- [ ] Budget allocated for implementation (tools, training, audit)
- [ ] Access to the Responsible GenAI Starter Kit deliverables (D1-D6)
- [ ] Basic understanding of AI/ML concepts
- [ ] Familiarity with ISO management system standards (helpful but not required)

---

## 2. Getting Started

### 2.1 Download and Review Starter Kit

**Action**: Clone or download the Responsible GenAI Starter Kit repository.

```bash
git clone https://github.com/jlov7/responsible-genai-starter-kit.git
cd responsible-genai-starter-kit
```

**Review these deliverables first**:
1. **D1**: `/deliverables/01-gai-rmf-kit/` - Checklists and templates
2. **D5**: `/deliverables/05-iso42001-bridge/` - This document and mapping
3. `/docs/refs.md` - Canonical references

### 2.2 Identify Your AI Systems

**Action**: Create an inventory of AI systems in scope for ISO 42001.

Use this template:

| System Name | Type | Business Unit | Risk Level | D1 Checklist | Status |
|-------------|------|---------------|------------|--------------|--------|
| Customer Support Bot | RAG | Customer Service | Medium | `rag.yaml` | In Production |
| Code Copilot | Code Assistant | Engineering | High | `code-assistant.yaml` | Pilot |
| Sentiment Analyzer | Fine-Tuned | Marketing | Low | `fine-tune.yaml` | Planned |

**Risk Level Criteria**:
- **High**: Processes sensitive data, impacts legal/safety, customer-facing
- **Medium**: Internal use, moderate data sensitivity
- **Low**: Non-critical, anonymized data, human-reviewed outputs

### 2.3 Select Applicable D1 Checklists

**Action**: Match each AI system to the appropriate D1 checklist:

- **RAG systems** → `/deliverables/01-gai-rmf-kit/checklists/rag.yaml`
- **Fine-tuned models** → `/deliverables/01-gai-rmf-kit/checklists/fine-tune.yaml`
- **Code assistants** → `/deliverables/01-gai-rmf-kit/checklists/code-assistant.yaml`

**Note**: You may apply multiple checklists if your system combines patterns (e.g., fine-tuned RAG).

### 2.4 Assemble Your Team

**Action**: Use the RACI Matrix to identify required roles.

**Core Roles** (from `/deliverables/05-iso42001-bridge/RACI-MATRIX.csv`):
- **CISO**: Accountable for governance and security controls
- **Compliance Officer**: Responsible for audit coordination and gap closure
- **ML Engineer**: Responsible for technical implementation (D2, D3)
- **Data Scientist**: Responsible for model development and evaluation
- **Privacy Officer**: Responsible for PII/data privacy controls
- **Platform Engineer**: Responsible for infrastructure and CI/CD

**Action**: Populate the RACI Matrix with real names from your organization.

---

## 3. Phase 1: Planning and Gap Analysis

**Timeline**: 2-4 weeks

### 3.1 Conduct Gap Analysis

**Objective**: Identify which ISO 42001 requirements are already satisfied and which need work.

**Tool**: Use the Gap Analysis Template from `/deliverables/05-iso42001-bridge/ISO42001-MAPPING.md` (Section 10).

**Steps**:

1. **Review ISO 42001 Clauses 4-10 and Annex A**
   - Read ISO 42001 standard (purchase from https://www.iso.org/standard/81230.html)
   - Understand requirements for each clause

2. **Map Existing Controls**
   - For each ISO 42001 requirement, identify existing organizational controls
   - Check if Starter Kit artifacts cover the gap (see ISO42001-MAPPING.md)

3. **Assess Maturity**
   - 🟢 **Implemented**: Control exists, documented, and operational
   - 🟡 **Partial**: Control exists but needs enhancement (e.g., incomplete documentation)
   - 🔴 **Missing**: Control does not exist; requires new implementation

4. **Prioritize Gaps**
   - Focus on high-risk systems first
   - Prioritize Clause 5 (Leadership), Clause 6 (Planning), Annex A.7 (Cybersecurity)

**Example Gap Analysis Entry**:

| ISO Clause | Requirement | Current State | Starter Kit Artifact | Gap | Action | Owner | Due Date |
|------------|-------------|---------------|----------------------|-----|--------|-------|----------|
| 5.1 | Governance committee | 🔴 Missing | D1 `RAG-GOV-01` | No committee exists | Establish committee, charter | CISO | 2025-02-15 |
| 8.2 | Impact assessment | 🟡 Partial | D1 MAP controls | Process informal, not documented | Execute D1 MAP controls, document in Model Card | Compliance | 2025-03-01 |
| A.7.3 | SBOM | 🟢 Implemented | D3 SBOM workflow | None | Maintain current process | Platform Eng | Ongoing |

### 3.2 Define Scope Statement

**Objective**: Document the boundaries of your AIMS.

**Template**:

> The AI Management System covers [organization name]'s [list AI system types, e.g., "customer-facing generative AI systems"] deployed in [business units/geographies].
>
> **In Scope**:
> - AI System 1 (RAG-based customer support)
> - AI System 2 (Fine-tuned sentiment analyzer)
>
> **Out of Scope**:
> - Traditional ML systems (non-generative)
> - Third-party SaaS AI tools not customized by [org]
> - Research/experimental models (pre-production)
>
> **Applicable Standards**:
> - ISO/IEC 42001:2023
> - NIST AI 600-1 (Generative AI Profile)
> - NIST SP 800-218A (SSDF for GenAI)

**Action**: Save scope statement and get executive approval.

### 3.3 Create Implementation Roadmap

**Objective**: Plan the sequence of implementation activities.

**Sample 6-Month Roadmap**:

| Phase | Duration | Activities | Deliverables |
|-------|----------|------------|--------------|
| **Planning** | Weeks 1-4 | Gap analysis, scope definition, team assembly | Gap analysis report, RACI matrix |
| **Foundation** | Weeks 5-8 | Establish governance, define AI policy, assign roles | Governance charter, AI policy, RACI with names |
| **Technical Implementation** | Weeks 9-16 | Execute D1 checklists, deploy D2 harness, configure D3 CI/CD | Completed checklists, eval reports, SBOMs |
| **Documentation** | Weeks 17-20 | Complete Model Cards, risk registers, procedures | Model Cards, risk registers, SOPs |
| **Validation** | Weeks 21-24 | Internal audit, management review, corrective actions | Internal audit report, mgmt review minutes |
| **Certification Audit** | Week 25-26 | External audit by accredited certification body | ISO 42001 certificate |

**Action**: Adjust timeline based on your organization's size and complexity.

---

## 4. Phase 2: Implementation

**Timeline**: 12-16 weeks

### 4.1 Establish Governance (ISO Clause 5)

#### 4.1.1 Create AI Governance Committee

**ISO Requirement**: Clause 5.1 (Leadership and Commitment)

**Starter Kit Artifacts**: D1 `RAG-GOV-01`, `FT-GOV-01`, `CA-GOV-01`

**Steps**:

1. **Draft Governance Charter**
   - **Purpose**: Oversee AI risk management, approve AI policies, review high-risk deployments
   - **Membership**: CISO (Chair), CTO, General Counsel, Chief Privacy Officer, Head of AI/ML
   - **Meeting Cadence**: Monthly (minimum)
   - **Authority**: Veto power over AI deployments that fail risk assessment

2. **Hold Kickoff Meeting**
   - Agenda: Review charter, assign roles, set meeting schedule
   - Output: Signed charter, meeting minutes

3. **Integrate with Existing Governance**
   - If you have ISO 27001 or ISO 9001, integrate AI governance into existing committees
   - Ensure AI-specific expertise is represented

**Audit Evidence**:
- Governance charter (signed by executives)
- Meeting minutes (12+ months for certification audit)

#### 4.1.2 Define AI Policy

**ISO Requirement**: Clause 5.2 (AI Policy)

**Starter Kit Artifacts**: D1 `RAG-GOV-02` (Acceptable Use Policy)

**Steps**:

1. **Draft AI Policy Document**
   - Use D1 `RAG-GOV-02` guidance
   - Include:
     - Permitted AI use cases
     - Prohibited uses (e.g., biometric surveillance, social scoring)
     - Ethical principles (transparency, fairness, accountability)
     - Compliance requirements (GDPR, AI Act, industry regulations)

2. **Example Policy Excerpt**:

   > **AI Acceptable Use Policy**
   >
   > **Permitted Uses**:
   > - Customer support automation (with human escalation)
   > - Internal code assistance for software development
   > - Marketing content generation (with human review)
   >
   > **Prohibited Uses**:
   > - Automated hiring decisions without human review
   > - Processing biometric data without explicit consent
   > - Generating misleading or harmful content
   >
   > **Accountability**: All AI systems must have a designated Model Owner responsible for compliance with this policy.

3. **Publish and Communicate**
   - Post to intranet
   - Require user acknowledgment (track via D1 `RAG-GOV-02`)

**Audit Evidence**:
- Published AI policy
- User acknowledgment records

#### 4.1.3 Assign Roles and Responsibilities

**ISO Requirement**: Clause 5.3 (Roles and Responsibilities)

**Starter Kit Artifacts**: D5 RACI Matrix

**Steps**:

1. **Populate RACI Matrix**
   - Use `/deliverables/05-iso42001-bridge/RACI-MATRIX.csv` as template
   - Replace role titles with actual names/teams
   - Example:
     - "Data Scientist" → "Dr. Jane Smith (AI Research Team)"
     - "Platform Engineer" → "DevOps Team (John Doe, lead)"

2. **Update Job Descriptions**
   - Add AI-specific responsibilities to relevant roles
   - Example for ML Engineer: "Responsible for executing D1 MEASURE controls and deploying D2 evaluation harness"

3. **Communicate Assignments**
   - Hold team meetings to clarify RACI roles
   - Post RACI matrix to project wiki

**Audit Evidence**:
- Completed RACI matrix (with names)
- Job descriptions referencing AI duties

### 4.2 Implement Data Management (ISO Clause 8.3)

#### 4.2.1 Inventory Data Sources

**ISO Requirement**: Clause 8.3 (Data Management for AI Systems)

**Starter Kit Artifacts**: D1 `RAG-MAP-02` (Data inventory), Model Card "Training Data" section

**Steps**:

1. **Execute D1 `RAG-MAP-02`**
   - List all data sources feeding AI system (databases, APIs, documents)
   - Create data lineage diagram showing flow: source → processing → vector DB/training set

2. **Document in Model Card**
   - Use Model Card "Training Data" section
   - Example:

   | Source | Size | Description | License |
   |--------|------|-------------|---------|
   | Internal KB | 50K docs | Product documentation | Proprietary |
   | Stack Overflow | 100K Q&A | Public programming Q&A | CC-BY-SA-4.0 |

3. **Classify Data**
   - Label data sensitivity: Public, Internal, Confidential, Restricted
   - Apply data classification per ISO 27001 A.8.2 if already implemented

**Audit Evidence**:
- Data lineage diagram
- Model Card training data section
- Data classification labels

#### 4.2.2 Identify and Protect PII

**ISO Requirement**: Annex A.8 (Data Privacy)

**Starter Kit Artifacts**: D1 `RAG-MAP-03` (PII identification), `RAG-MEAS-03` (PII detection), `RAG-MGT-02` (PII redaction)

**Steps**:

1. **Execute D1 `RAG-MAP-03`**
   - Scan training data for PII (names, emails, SSNs, etc.)
   - Use automated tools (e.g., Microsoft Presidio, spaCy NER)
   - Manual review for domain-specific PII (e.g., patient IDs in healthcare)

2. **Create Data Minimization Plan**
   - Remove unnecessary PII before training
   - Pseudonymize where possible (e.g., hash user IDs)

3. **Deploy PII Detection (D1 `RAG-MEAS-03`)**
   - Integrate D2 PII scorer in evaluation harness
   - Run on every release candidate
   - Block deployment if PII leakage detected

4. **Implement Output Redaction (D1 `RAG-MGT-02`)**
   - Deploy runtime PII filter (regex + NER model)
   - Test redaction on 100+ PII examples (target: 100% redaction rate)

**Audit Evidence**:
- PII scan report
- Data minimization plan
- D2 PII detection test results
- Redaction test report

#### 4.2.3 Assign Data Steward

**ISO Requirement**: Clause 8.3 (Data Management)

**Starter Kit Artifacts**: D1 `RAG-GOV-03`

**Steps**:

1. **Execute D1 `RAG-GOV-03`**
   - Appoint a named Data Steward responsible for data quality and provenance
   - Define Data Quality SLA (e.g., "Vector DB refreshed monthly; stale documents flagged")

2. **Document in RACI Matrix**
   - Assign Data Steward as "Accountable" for data inventory and quality activities

**Audit Evidence**:
- Data steward appointment letter
- Data quality SLA
- Quarterly audit reports from data steward

### 4.3 Implement Risk Assessment (ISO Clause 6.1, 8.2)

#### 4.3.1 Conduct Impact Assessment

**ISO Requirement**: Clause 8.2 (AI System Impact Assessment)

**Starter Kit Artifacts**: D1 MAP function controls, Risk Register Template

**Steps**:

1. **Execute All D1 MAP Controls**
   - For RAG systems: `RAG-MAP-01` through `RAG-MAP-04`
   - For Fine-Tuning: `FT-MAP-01` through `FT-MAP-04`
   - For Code Assistants: `CA-MAP-01` through `CA-MAP-05`

2. **Document Findings in Risk Register**
   - Use `/deliverables/01-gai-rmf-kit/templates/risk-register.csv`
   - Example entry:

   | Risk ID | Description | Likelihood | Impact | Mitigation | Owner | Status |
   |---------|-------------|------------|--------|------------|-------|--------|
   | RAG-001 | PII leakage via RAG retrieval | Medium | High | Deploy PII redaction (RAG-MGT-02) | ML Engineer | Open |
   | RAG-002 | Prompt injection attack | High | Medium | Input validation (RAG-MGT-01), red team (RAG-MEAS-05) | Security Team | Mitigated |

3. **Conduct Threat Modeling (D1 `RAG-MAP-04`)**
   - Map attack surface (user inputs, retrieval context, system prompts)
   - Create attack tree diagram
   - Identify mitigations (input validation, output filtering, monitoring)

**Audit Evidence**:
- Completed MAP controls from D1 checklists
- Risk register with risk owners and mitigations
- Threat model diagram

#### 4.3.2 Define Risk Acceptance Criteria

**ISO Requirement**: Clause 6.1 (Actions to Address Risks)

**Steps**:

1. **Establish Risk Matrix**
   - Define likelihood and impact scales (1-5)
   - Set risk acceptance thresholds (e.g., risks with score >12 require executive approval)

2. **Document in Governance Charter**
   - Who can accept which level of risk (e.g., CTO can accept medium risks, Board approval for critical)

**Audit Evidence**:
- Risk matrix diagram
- Risk acceptance records (for accepted risks)

### 4.4 Implement Measurement and Testing (ISO Clause 9.1, Annex A.1.3)

#### 4.4.1 Deploy Evaluation Harness (D2)

**ISO Requirement**: Clause 9.1 (Monitoring and Measurement), Annex A.1.3 (Testing and Validation)

**Starter Kit Artifacts**: D2 Evaluation Harness

**Steps**:

1. **Set Up D2 Harness**
   - Follow D2 setup instructions (see `/deliverables/02-eval-harness/README.md`)
   - Integrate scorers: PII detection, refusal-rate, bias/fairness, citation accuracy

2. **Execute D1 MEASURE Controls**
   - `RAG-MEAS-01`: Establish baseline metrics (accuracy, F1, latency)
   - `RAG-MEAS-02`: Deploy refusal-rate scorer (target: ≥98% on adversarial prompts)
   - `RAG-MEAS-03`: Deploy PII scorer (target: 0% leakage)
   - `RAG-MEAS-04`: Measure citation accuracy (target: ≥95%)

3. **Create Golden Evaluation Dataset**
   - Curate 100+ Q&A pairs representing real-world usage
   - Include edge cases (adversarial prompts, ambiguous queries, multilingual)

4. **Automate Testing in CI/CD**
   - Integrate D2 harness with D3 CI/CD workflows
   - Block deployment if acceptance criteria not met (e.g., PII leakage detected)

**Audit Evidence**:
- D2 eval reports (baseline + historical trends)
- Golden dataset documentation
- CI/CD logs showing automated testing

#### 4.4.2 Conduct Red Team Testing

**ISO Requirement**: Annex A.7.2 (Security Testing)

**Starter Kit Artifacts**: D1 `RAG-MEAS-05`, `FT-MEAS-06`, `CA-MEAS-06`

**Steps**:

1. **Execute D1 `RAG-MEAS-05`**
   - Hire internal security team or external red team specialists
   - Test ≥10 prompt injection techniques (see OWASP LLM Top 10)
   - Target: <10% success rate acceptable

2. **Document Findings**
   - Red team report with attack transcripts
   - Remediation plan for successful attacks

3. **Retest After Mitigations**
   - Verify mitigations effective (e.g., input validation blocks previous attacks)

**Audit Evidence**:
- Red team report
- Remediation plan and closure records
- Retest results

### 4.5 Implement Operational Controls (ISO Clause 8.1, Annex A.4)

#### 4.5.1 Deploy Monitoring and Logging

**ISO Requirement**: Annex A.4.1 (Performance Monitoring), A.4.3 (Logging)

**Starter Kit Artifacts**: D1 `RAG-MGT-06` (monitoring), `RAG-MGT-04` (logging)

**Steps**:

1. **Execute D1 `RAG-MGT-06`**
   - Deploy monitoring dashboard (e.g., Grafana, Datadog)
   - Track metrics: accuracy, latency, refusal rate, PII detections, error rate
   - Configure alerts (e.g., accuracy drops >10%, PII leak detected)

2. **Execute D1 `RAG-MGT-04`**
   - Enable centralized logging (e.g., ELK, Splunk)
   - Log all queries and responses with: timestamp, user_id, query text, response, model version
   - Configure tamper-evident logging (WORM storage or cryptographic signatures)
   - Set retention: 90 days minimum (adjust based on compliance requirements)

3. **Test Alerting**
   - Simulate drift (e.g., inject low-quality responses)
   - Verify alerts trigger and reach on-call team

**Audit Evidence**:
- Monitoring dashboard (screenshots or live access for auditor)
- Alert configuration and test results
- Log retention policy and sample logs

#### 4.5.2 Implement Incident Response

**ISO Requirement**: Clause 10.1 (Nonconformity and Corrective Action), Annex A.4.2 (Incident Management)

**Starter Kit Artifacts**: D1 `RAG-MGT-05`

**Steps**:

1. **Execute D1 `RAG-MGT-05`**
   - Create AI incident runbook covering:
     - PII leakage
     - Prompt injection / jailbreak
     - Model drift / performance degradation
     - Data poisoning
   - Define escalation paths and RACI
   - Target: <1 hour mean time to containment

2. **Conduct Tabletop Exercise**
   - Simulate incident (e.g., "User reports PII in RAG response")
   - Walk through runbook with cross-functional team
   - Document lessons learned and update runbook

3. **Integrate with Existing Incident Management**
   - If using ISO 27001, integrate AI incidents into information security incident process
   - Use same ticketing system (e.g., Jira, ServiceNow)

**Audit Evidence**:
- AI incident runbook
- Tabletop exercise report
- Incident logs (if real incidents occurred)

#### 4.5.3 Configure CI/CD Workflows (D3)

**ISO Requirement**: Clause 8.1 (Operational Planning), Annex A.7.3 (Supply Chain Security)

**Starter Kit Artifacts**: D3 SSDF for GenAI CI/CD

**Steps**:

1. **Deploy D3 Workflows**
   - Follow D3 setup instructions (see `/deliverables/03-ssdf-genai-ci/README.md`)
   - Configure workflows:
     - SBOM generation (SPDX + CycloneDX)
     - SLSA provenance attestation
     - OpenSSF Scorecard (weekly)
     - D2 eval harness integration

2. **Execute D1 `RAG-MGT-08`**
   - Vet third-party vendors (LLM provider, vector DB, embedding API)
   - Conduct vendor risk assessments
   - Include AI-specific SLAs in contracts (data deletion, audit rights, SBOM provision)

3. **Generate SBOMs for All Releases**
   - D3 workflows auto-generate SBOM on every release
   - Publish SBOMs to artifact registry or public repository

**Audit Evidence**:
- D3 workflow execution logs
- SBOMs (SPDX/CycloneDX files)
- SLSA provenance attestations
- Vendor risk assessment reports

### 4.6 Implement Transparency Controls (ISO Annex A.5)

#### 4.6.1 Complete Model Cards

**ISO Requirement**: Annex A.5.1 (Documentation for Users)

**Starter Kit Artifacts**: D1 Model Card Template

**Steps**:

1. **For Each AI System, Complete Model Card**
   - Use `/deliverables/01-gai-rmf-kit/templates/model-card.md`
   - Sections to complete:
     - Model Details
     - Intended Use (including out-of-scope uses)
     - Training Data (sources, licenses, limitations)
     - Evaluation (metrics, benchmarks, fairness)
     - Ethical Considerations (risks, mitigations)
     - Deployment (monitoring, update cadence)

2. **Publish Model Cards**
   - Internal: Company wiki or intranet
   - External (if customer-facing): Public documentation site

3. **Maintain Version History**
   - Update Model Card when system changes (retraining, new features)
   - Document changes in "Changelog" section

**Audit Evidence**:
- Completed Model Cards for all in-scope AI systems
- Publication records (wiki page history, website deployment logs)

#### 4.6.2 Apply C2PA Provenance (D4)

**ISO Requirement**: Annex A.5.1 (Transparency), Annex A.5.2 (Explainability)

**Starter Kit Artifacts**: D4 C2PA Provenance Demo

**Steps**:

1. **Deploy D4 C2PA Signing**
   - Follow D4 setup instructions (see `/deliverables/04-c2pa-provenance-demo/README.md`)
   - Sign AI-generated content with C2PA manifest
   - Include assertions:
     - `c2pa.ai_generative_training` (model name, version)
     - `c2pa.author` (your organization)
     - `c2pa.actions` (generation timestamp)

2. **Publish C2PA Verification Instructions**
   - Provide users with C2PA verification tool (e.g., D4 web viewer)
   - Include instructions in Model Card or user documentation

**Audit Evidence**:
- C2PA-signed content samples
- C2PA manifest JSON files
- User documentation with verification instructions

---

## 5. Phase 3: Validation and Audit Preparation

**Timeline**: 4-6 weeks

### 5.1 Conduct Internal Audit

**ISO Requirement**: Clause 9.2 (Internal Audit)

**Starter Kit Artifacts**: D5 Compliance Checklist

**Steps**:

1. **Use D5 Compliance Checklist**
   - Load `/deliverables/05-iso42001-bridge/compliance-checklist.yaml`
   - Assign internal auditor (should not audit their own work)

2. **Audit Scope**
   - Verify all ISO 42001 Clauses 4-10 and Annex A controls
   - Check that D1 checklist items are complete
   - Review documentation (Model Cards, risk registers, policies)

3. **Document Findings**
   - Record conformities and non-conformities
   - Assign corrective actions with owners and due dates

4. **Follow-Up Audit**
   - After corrective actions closed, re-audit to verify closure

**Audit Evidence**:
- Internal audit plan and schedule
- Internal audit report
- Corrective action register
- Follow-up audit report

### 5.2 Conduct Management Review

**ISO Requirement**: Clause 9.3 (Management Review)

**Starter Kit Artifacts**: D1 Governance Committee meetings

**Steps**:

1. **Schedule Executive Management Review**
   - Quarterly (minimum) per D1 `RAG-GOV-01`
   - Invite governance committee + executive leadership

2. **Review Agenda**
   - AIMS performance (D2 eval trends, incident metrics)
   - Internal audit results
   - External changes (new AI regulations, industry standards)
   - Resource needs (budget, headcount, tools)
   - Opportunities for improvement

3. **Document Outputs**
   - Meeting minutes with decisions, action items, and owners
   - Updated AI policy or objectives (if needed)

**Audit Evidence**:
- Management review meeting minutes (12+ months)
- Action item register with closure records

### 5.3 Prepare Audit Evidence Package

**Objective**: Assemble all documentation for certification audit.

**Checklist** (see detailed version in Section 6 below):

- [ ] **Governance**: Charter, AI policy, RACI matrix, meeting minutes
- [ ] **Planning**: Scope statement, risk register, gap analysis
- [ ] **Documentation**: Model Cards, SBOMs, SLSAs, C2PA manifests
- [ ] **Technical Evidence**: D2 eval reports, D3 workflow logs, monitoring dashboards
- [ ] **Performance**: Internal audit reports, management review minutes, corrective actions

**Action**: Create a shared folder (physical or digital) with all evidence indexed.

### 5.4 Select Certification Body

**Objective**: Engage an accredited certification body for ISO 42001 audit.

**Steps**:

1. **Find Accredited Auditors**
   - Check IAF (International Accreditation Forum) member list
   - Look for ISO 42001 scope (standard is new, so not all bodies may offer it yet)

2. **Request Proposals**
   - Provide scope statement, number of in-scope AI systems, locations
   - Compare cost, timeline, auditor expertise

3. **Schedule Stage 1 and Stage 2 Audits**
   - **Stage 1**: Documentation review (auditor reviews AIMS documentation remotely)
   - **Stage 2**: On-site/virtual audit (auditor interviews staff, observes processes, reviews evidence)

**Timeline**:
- Stage 1: 1-2 days
- Gap closure (if Stage 1 findings): 2-4 weeks
- Stage 2: 2-5 days (depends on organization size)
- Certificate issuance: 4-6 weeks post-Stage 2

---

## 6. Audit Preparation Checklist

Use this checklist to ensure you're ready for certification audit.

### 6.1 Document Repository

- [ ] **AI Management System Manual** (high-level AIMS description, scope, policy)
- [ ] **AI Policy** (published, communicated, acknowledged by users)
- [ ] **Governance Charter** (signed by executives, defines committee structure)
- [ ] **RACI Matrix** (populated with real names/teams)
- [ ] **Scope Statement** (defines in-scope AI systems, boundaries, standards)
- [ ] **Risk Register** (current, with risk owners and mitigations)
- [ ] **Model Cards** (one per AI system, complete, version-controlled)

### 6.2 Planning Evidence

- [ ] **Gap Analysis Report** (initial assessment showing compliance status)
- [ ] **Implementation Roadmap** (timeline with milestones)
- [ ] **AI Objectives** (documented in Model Cards or OKRs)

### 6.3 Technical Evidence

- [ ] **D1 Checklists** (all controls completed, acceptance criteria met)
- [ ] **D2 Evaluation Reports** (baseline + historical trends, covering all MEASURE controls)
- [ ] **D3 CI/CD Workflow Logs** (SBOM generation, SLSA attestations, Scorecard results)
- [ ] **D3 SBOMs** (SPDX/CycloneDX files for all releases)
- [ ] **D3 SLSA Attestations** (provenance for build artifacts)
- [ ] **D4 C2PA Manifests** (for AI-generated content)

### 6.4 Data Management Evidence

- [ ] **Data Lineage Diagrams** (source → processing → AI system)
- [ ] **PII Scan Reports** (automated + manual review)
- [ ] **Data Classification Labels** (public/internal/confidential/restricted)
- [ ] **Data Steward Appointment** (letter or RACI entry)
- [ ] **Data Quality SLA** (documented, reviewed quarterly)

### 6.5 Security Evidence

- [ ] **Threat Model** (attack surface, attack trees, mitigations)
- [ ] **Red Team Report** (adversarial testing, remediation plan)
- [ ] **Penetration Test Report** (if applicable, e.g., cross-tenant access testing)
- [ ] **Vendor Risk Assessments** (third-party LLM providers, vector DB, embedding API)

### 6.6 Operational Evidence

- [ ] **Monitoring Dashboard** (accessible to auditor, shows real-time metrics)
- [ ] **Alert Configuration** (rules, thresholds, escalation paths)
- [ ] **Audit Logs** (90+ days retention, tamper-evident)
- [ ] **Incident Response Runbook** (AI-specific incidents)
- [ ] **Tabletop Exercise Report** (incident response practice)

### 6.7 Performance Evaluation Evidence

- [ ] **Internal Audit Plan and Schedule** (annual minimum)
- [ ] **Internal Audit Reports** (with findings and corrective actions)
- [ ] **Corrective Action Register** (all non-conformities closed or with plan)
- [ ] **Management Review Meeting Minutes** (quarterly, 12+ months)
- [ ] **Action Item Register** (from management reviews, with closure records)

### 6.8 Human Resources Evidence

- [ ] **Training Records** (D6 one-pager distribution, AUP acknowledgments)
- [ ] **Competency Assessments** (for AI/ML roles)
- [ ] **Job Descriptions** (with AI-specific responsibilities)

### 6.9 Improvement Evidence

- [ ] **Model Card Changelogs** (version history showing improvements)
- [ ] **Retraining Logs** (drift-triggered retraining per D1 `RAG-MGT-06`)
- [ ] **A/B Test Results** (comparing model versions, demonstrating improvement)

---

## 7. Common Pitfalls

### 7.1 Incomplete Documentation

**Pitfall**: Model Cards or checklists partially completed; missing key sections.

**Solution**:
- Use D1 checklist `acceptance_criteria` fields to verify completion
- Assign document owners in RACI matrix
- Conduct peer review before submitting for audit

### 7.2 Governance Without Authority

**Pitfall**: Governance committee exists on paper but lacks decision-making power.

**Solution**:
- Ensure charter grants veto power over high-risk deployments
- Include C-level executives (CISO, CTO) as voting members
- Document decisions in meeting minutes (not just discussions)

### 7.3 Testing Without Action

**Pitfall**: Red team or eval harness finds issues, but no remediation occurs.

**Solution**:
- Track all findings in issue tracker (Jira, GitHub Issues)
- Block deployment on critical findings (use D3 CI/CD quality gates)
- Show auditor closed remediation tickets

### 7.4 Missing Traceability

**Pitfall**: Can't demonstrate which test covers which requirement.

**Solution**:
- Create traceability matrix: ISO requirement → D1 control → D2 test → audit evidence
- Example:
  - ISO A.8.1 (PII minimization) → D1 `RAG-MEAS-03` → D2 PII scorer → Test report showing 0% leakage

### 7.5 Siloed Implementation

**Pitfall**: ML team implements D1 controls but Security/Compliance teams unaware.

**Solution**:
- Use RACI matrix to enforce cross-functional collaboration
- Hold regular sync meetings (weekly during implementation)
- Include all stakeholders in internal audit

### 7.6 Static Documentation

**Pitfall**: Model Cards created once and never updated.

**Solution**:
- Set review cadence in Model Card "Next review" field (quarterly recommended)
- Trigger Model Card updates on: retraining, incident, regulatory change
- Version-control Model Cards in Git; show commit history to auditor

---

## 8. Integration Strategies

### 8.1 ISO 27001 (Information Security) Integration

If your organization has ISO 27001 certification:

**Shared Controls**:
- **ISO 27001 A.5.1 (Policies)** ↔ **ISO 42001 Clause 5.2 (AI Policy)**
  - Extend existing information security policy to include AI-specific clauses
- **ISO 27001 A.8.2 (Information Classification)** ↔ **ISO 42001 Clause 8.3 (Data Management)**
  - Use same classification scheme (public/internal/confidential)
- **ISO 27001 A.12.6 (Logging)** ↔ **ISO 42001 Annex A.4.3 (Logging)**
  - Extend SIEM to include AI system logs
- **ISO 27001 A.15.1 (Supplier Security)** ↔ **ISO 42001 Annex A.7.3 (Supply Chain)**
  - Add AI-specific vendor risk assessments to existing supplier process

**Benefits**:
- Single Statement of Applicability (SoA) for both standards
- Combined audits (some certification bodies offer joint ISO 27001 + 42001 audits)
- Reduced documentation overhead

### 8.2 ISO 9001 (Quality Management) Integration

If your organization has ISO 9001 certification:

**Shared Controls**:
- **ISO 9001 Clause 4.1 (Context)** ↔ **ISO 42001 Clause 4.1 (Context)**
- **ISO 9001 Clause 9.2 (Internal Audit)** ↔ **ISO 42001 Clause 9.2 (Internal Audit)**
  - Extend quality audit program to include AI systems
- **ISO 9001 Clause 10.2 (Nonconformity and Corrective Action)** ↔ **ISO 42001 Clause 10.1**
  - Use same corrective action process (CAPA system)

**Benefits**:
- Leverage existing quality management processes
- Unified audit schedule
- Common document control system

### 8.3 NIST AI RMF Integration

The Starter Kit is already built on NIST AI 600-1, so integration is natural:

**Mapping**:
- **D1 Checklists** directly implement NIST AI RMF Govern/Map/Measure/Manage functions
- Use NIST AI RMF as the "how-to" guide; ISO 42001 as the "what" requirements

**Benefit**: If you're already implementing NIST AI RMF (e.g., for U.S. federal procurement), the D1 checklists satisfy both NIST and ISO 42001.

### 8.4 AI Act (EU) Integration

If your organization is subject to the EU AI Act:

**High-Risk AI Systems** (AI Act Annex III):
- Map to ISO 42001 Annex A controls
- Use D1 checklists to satisfy AI Act transparency, human oversight, accuracy requirements
- Model Cards fulfill AI Act documentation obligations (Article 11)

**Conformity Assessment**:
- ISO 42001 certification may be accepted as harmonized standard for AI Act compliance (pending EU adoption)

---

## 9. Appendices

### Appendix A: Glossary

| Term | Definition |
|------|------------|
| **AIMS** | AI Management System (per ISO 42001) |
| **C2PA** | Coalition for Content Provenance and Authenticity (content watermarking standard) |
| **GAI** | Generative Artificial Intelligence |
| **PII** | Personally Identifiable Information |
| **RAG** | Retrieval-Augmented Generation (AI pattern combining vector search + LLM) |
| **RACI** | Responsible, Accountable, Consulted, Informed (role assignment matrix) |
| **SBOM** | Software Bill of Materials (inventory of software components) |
| **SLSA** | Supply-chain Levels for Software Artifacts (build provenance framework) |
| **SSDF** | Secure Software Development Framework (NIST SP 800-218) |

### Appendix B: Sample Timeline (Small Organization)

For organizations with 1-3 AI systems, 5-10 person team:

| Week | Phase | Activities |
|------|-------|------------|
| 1 | Planning | Gap analysis, scope definition |
| 2 | Planning | Team assembly, RACI matrix |
| 3-4 | Governance | Establish committee, draft AI policy |
| 5-8 | Data Management | Inventory data, classify PII, assign steward |
| 9-12 | Risk Assessment | Execute D1 MAP controls, threat modeling, risk register |
| 13-16 | Testing | Deploy D2 harness, red team, complete MEASURE controls |
| 17-20 | Operational | Deploy monitoring, logging, incident response, D3 CI/CD |
| 21-22 | Documentation | Complete Model Cards, apply C2PA |
| 23-24 | Internal Audit | Conduct internal audit, close findings |
| 25-26 | Certification | Stage 1 + Stage 2 audits |

### Appendix C: Sample Timeline (Large Organization)

For organizations with 10+ AI systems, 50+ person team:

| Month | Phase | Activities |
|-------|-------|------------|
| 1 | Planning | Gap analysis across all business units |
| 2 | Governance | Establish enterprise governance, policy |
| 3-4 | Pilot | Implement D1-D4 on 1-2 pilot AI systems |
| 5-6 | Rollout | Scale to remaining AI systems |
| 7-8 | Validation | Internal audits, management reviews |
| 9 | Certification | External audit |

### Appendix D: Key ISO 42001 Clauses Quick Reference

| Clause | Title | Key Requirement | Starter Kit Artifact |
|--------|-------|-----------------|----------------------|
| 4.1 | Context | Document external/internal issues | D1 Model Card, Risk Register |
| 4.2 | Stakeholders | Identify interested parties | D5 RACI Matrix |
| 5.1 | Leadership | Executive commitment | D1 `RAG-GOV-01` (Governance committee) |
| 5.2 | AI Policy | Establish AI policy | D1 `RAG-GOV-02` (AUP) |
| 6.1 | Risk Planning | Plan actions to address risks | D1 MAP controls, Risk Register |
| 6.2 | Objectives | Set measurable AI objectives | D1 MEASURE controls, D2 harness |
| 8.2 | Impact Assessment | Conduct AI impact assessment | D1 MAP controls |
| 8.3 | Data Management | Manage AI data lifecycle | D1 data controls, Model Card |
| 9.1 | Monitoring | Monitor and measure performance | D2 harness, D1 `RAG-MGT-06` |
| 9.2 | Internal Audit | Conduct internal audits | D5 Compliance Checklist |
| 9.3 | Management Review | Executive review of AIMS | D1 Governance meetings |
| A.7.3 | Supply Chain | SBOM, provenance, vendor vetting | D3 SBOM/SLSA, D1 `RAG-MGT-08` |
| A.8.1 | Data Privacy | PII minimization, detection, redaction | D1 `RAG-MAP-03`, `RAG-MEAS-03`, `RAG-MGT-02` |

---

## Support and Resources

**Questions?** Contact the Compliance Team at [compliance@yourorg.com]

**Additional Resources**:
- ISO 42001 Standard: https://www.iso.org/standard/81230.html
- NIST AI 600-1: https://doi.org/10.6028/NIST.AI.600-1
- Starter Kit Documentation: `/docs/refs.md`

---

**Version History**:

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2025-01-XX | Initial release |

---

**Document Owner**: Compliance Officer
**Next Review**: 2025-07-XX (6 months post-release)
**Maintained By**: DocsWriter Agent
