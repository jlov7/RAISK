# System Overview

Narrative view of how the Responsible GenAI Starter Kit fits together. Use this document to brief stakeholders on scope, architecture, and integration paths.

---

## Mission Statement

Build a research-grade, production-quality reference implementation that demonstrates how to implement responsible Generative AI practices aligned with:

- **NIST AI 600-1** (Generative AI Profile)
- **NIST AI RMF** (Govern, Map, Measure, Manage)
- **NIST SP 800-218A** (Secure Software Development Framework for GenAI)
- **C2PA v2.2** (Content provenance)
- **ISO/IEC 42001** (AI Management Systems)

The kit is designed as a *playbook* rather than a shrink-wrapped product. Every deliverable is modular so you can adopt pieces incrementally.

---

## High-Level Architecture

```
┌──────────────────────────┐
│  Governance & Controls   │  D1: Checklists, risk register, model card templates
└────────────┬─────────────┘
             │ feeds requirements
┌────────────▼─────────────┐
│   Evaluation Harness     │  D2: Scorers, datasets, golden runs
│   (Measure function)     │
└────────────┬─────────────┘
             │ gates releases
┌────────────▼─────────────┐
│   Secure CI/CD Workflows │  D3: SBOM, SLSA, Scorecard, secret scans
│   (Build & attest)       │
└────────────┬─────────────┘
             │ publishes artifacts
┌────────────▼─────────────┐
│  Content Provenance Demo │  D4: Sign & verify generated assets
│  (Transparency)          │
└────────────┬─────────────┘
             │ informs compliance
┌────────────▼─────────────┐
│  ISO/IEC 42001 Bridge    │  D5: Control mapping, RACI matrix
└────────────┬─────────────┘
             │ community education
┌────────────▼─────────────┐
│  Education One-Pager     │  D6: Classroom guardrails, comms templates
└──────────────────────────┘
```

Key flows:

1. **Governance artifacts (D1)** define what “responsible” means for your organization.
2. **Evaluation harness (D2)** operationalizes those controls as automated tests and scorers.
3. **CI/CD workflows (D3)** ensure builds are reproducible, attested, and monitored for regressions.
4. **Provenance tooling (D4)** provides user-facing transparency that content is AI-generated.
5. **Compliance mapping (D5)** lets you attest to standards bodies.
6. **Education materials (D6)** help downstream users and educators understand risks and guardrails.

---

## Storyline: A Day-in-the-Life

1. **Design Review**  
   Product, security, and compliance teams walk through the D1 checklist. They log risks in the provided templates and create Jira issues for open items.

2. **Model Development**  
   Engineers extend the evaluation harness with domain-specific datasets. They run `eval-harness` locally and in CI to measure refusal rates, PII leakage, and accuracy.

3. **Pipeline Hardening**  
   DevOps engineers adopt the D3 workflows, customize language matrices, and integrate SBOM signing. Scorecard scans run weekly; pull requests are blocked unless security gates pass.

4. **Release Prep**  
   CI publishes signed artifacts and SBOMs. The team runs `validate-workflows.sh` and documents the release using `docs/RELEASE-CHECKLIST.md`.

5. **User Transparency**  
   Communications teams sign generated assets with the C2PA demo before publishing. Viewer screenshots are embedded in educational materials from D6.

6. **Audit & Compliance**  
   Compliance teams map implemented controls to ISO/IEC 42001 using D5. Findings feed back into the risk register and evaluation backlog.

---

## Roles & Responsibilities

| Role | Responsibilities | Primary Deliverables |
|------|------------------|----------------------|
| Product Manager | Define use cases, document context, assign owners | D1 templates, D5 mappings |
| ML Engineer | Build datasets, extend scorers, interpret metrics | D2 evaluation harness |
| Security Engineer | Harden workflows, monitor SBOMs, triage findings | D3 CI/CD workflows |
| Compliance Lead | Track control coverage, prepare audits | D1, D5 |
| Educator / Stakeholder | Communicate AI guardrails to end-users | D6 materials |

---

## Alignment to AI RMF Functions

| AI RMF Function | Kit Coverage |
|-----------------|--------------|
| **Govern** | D1 checklists, ISO bridge (D5), RACI matrix |
| **Map** | System context templates, threat model |
| **Measure** | Evaluation harness (D2), scorecards |
| **Manage** | CI/CD workflows (D3), C2PA provenance (D4), release checklist |

---

## Extending the Kit

- **Custom Scorers:** Add new classes under `eval_harness/scorers.py` (e.g., toxicity models, policy compliance).
- **Additional Workflows:** Fork `03-ssdf-genai-ci/workflows` and add runtime-specific jobs (e.g., container scans, infrastructure-as-code scans).
- **Provenance Providers:** Swap out `c2pa-node` for native SDKs from your content pipeline.
- **Compliance Targets:** Extend D5 with sector-specific frameworks (e.g., EU AI Act, ISO/IEC 23894).
- **Datasets:** Create curated question sets for your domain, plug them into D2, and wire results into D3 as quality gates.

---

## Research Caveats

- **No managed hosting:** There is no API endpoint or turnkey SaaS. Treat everything as infrastructure-as-code.
- **Placeholder metadata:** Update contact info, DOIs, and domain names before sharing externally.
- **Dependencies evolve:** Monitor the dependency stack (Python, Node, GitHub Actions). The kit pins versions as of January 2025.
- **Community contributions:** If you extend the kit, document your changes and consider submitting a pull request to keep the reference implementation fresh.

---

## Related Documents

- `docs/GETTING-STARTED.md` — step-by-step setup
- `docs/threat-model.md` — STRIDE analysis for RAG systems
- `docs/RELEASE-CHECKLIST.md` — end-to-end release guide
- `deliverables/*/README.md` — detailed instructions per module

---

**Maintainer Note:** Contributions are welcome, but please respect that this is a personal research project. Prioritize clarity, reproducibility, and alignment with responsible AI standards. Provide context for any new artifacts so future readers understand how they fit into the story.
