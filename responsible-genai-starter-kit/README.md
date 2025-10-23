# Responsible GenAI Starter Kit

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/jlov7/responsible-genai-starter-kit/actions)
[![OpenSSF Scorecard](https://img.shields.io/badge/scorecard-passing-brightgreen)](https://securityscorecards.dev/)
[![SLSA Provenance](https://img.shields.io/badge/SLSA-L3-green)](https://slsa.dev/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Docs: CC-BY-4.0](https://img.shields.io/badge/Docs-CC--BY--4.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.XXXXXX-blue)](https://zenodo.org/badge/latestdoi/XXXXXX)

**A personal research passion project that delivers a production-quality reference implementation for responsible Generative AI.**

---

> ⚠️ **Important:** This repository is *not* a commercial product. It is a public research artifact built to demonstrate responsible AI practices end-to-end. Everything is open source, reproducible, and hardened, but you own the risk when adopting it in production.

---

## Contents

- [Project Snapshot](#project-snapshot)
- [What This Is / Is Not](#what-this-is--is-not)
- [Story & Motivation](#story--motivation)
- [How to Use the Kit](#how-to-use-the-kit)
- [Modules at a Glance](#modules-at-a-glance)
- [Architecture & Flow](#architecture--flow)
- [Quality Gates & Security](#quality-gates--security)
- [Compliance & Governance](#compliance--governance)
- [Repository Layout](#repository-layout)
- [Community & Contributions](#community--contributions)
- [Citation & Licensing](#citation--licensing)

---

## Project Snapshot

- **Purpose:** Provide a turnkey blueprint for teams who need to operationalize responsible GenAI practices aligned with U.S. federal guidance.
- **Scope:** Six deliverables spanning governance, evaluation, secure DevSecOps, content provenance, compliance mapping, and education.
- **Standards Alignment:** NIST AI 600-1, NIST AI RMF Playbook, NIST SP 800-218A, C2PA v2.2, ISO/IEC 42001.
- **Audience:** Builders, security engineers, compliance leads, and educators who want a high-quality reference implementation.

Supporting documents:
- [Getting Started Guide](docs/GETTING-STARTED.md)
- [System Overview Narrative](docs/SYSTEM-OVERVIEW.md)
- [Threat Model (STRIDE)](docs/threat-model.md)
- [Release Checklist](docs/RELEASE-CHECKLIST.md)

---

## What This Is / Is Not

| This *is* | This is *not* |
|-----------|----------------|
| A rigorously documented **research reference** that shows how to build responsible GenAI systems | A managed service, SaaS platform, or supported commercial product |
| Production-grade code, workflows, and templates you can fork and harden for your organization | A “one size fits all” solution; expect to customize datasets, workflows, and policies |
| A storytelling vehicle for how governance, safety, and provenance fit together | Legal advice or compliance certification |
| Dual-licensed (Apache-2.0 for code, CC-BY-4.0 for docs) so you can remix and extend | A guarantee of zero risk—always perform your own security and compliance review |

---

## Story & Motivation

Generative AI is racing ahead faster than the controls designed to keep it safe. This kit emerged from the practical needs of shipping RAG systems and AI-powered assistants within regulated environments:

1. **Governance first.** Start with tangible checklists and risk registers that map to NIST AI RMF.
2. **Measure continuously.** Automate evaluations for PII leakage, refusal behavior, accuracy, and determinism.
3. **Secure the pipeline.** Treat CI/CD, SBOMs, and attestations as first-class citizens.
4. **Ship with provenance.** Sign AI content so downstream users know what they are looking at.
5. **Educate stakeholders.** Provide plain-language guardrails for classrooms and policy briefings.

Every artifact is crafted to tell that story end-to-end, from design to release.

---

## How to Use the Kit

1. **Clone the repository and review the [Getting Started guide](docs/GETTING-STARTED.md).**
2. **Work through the governance artifacts (D1)** to understand roles, controls, and risks.
3. **Run the evaluation harness (D2)** locally and in CI to set quality gates.
4. **Adopt the SSDF-aligned workflows (D3)** to harden your supply chain.
5. **Sign generated content with the C2PA demo (D4)** for transparency.
6. **Map controls to ISO/IEC 42001 (D5)** and brief stakeholders with the education pack (D6).
7. **Update placeholders** (GitHub handle, contact info, DOI) before publishing publicly.

---

## Modules at a Glance

| Deliverable | Summary | Quick Start |
|-------------|---------|-------------|
| **D1 – GAI RMF Implementation Kit** | Checklists, model cards, and risk registers for RAG, fine-tuning, and code assistants. | `deliverables/01-gai-rmf-kit/README.md` |
| **D2 – Evaluation Harness** | Python package with exact-match, PII, length, and refusal scorers; golden-run determinism tests. | `deliverables/02-eval-harness/README.md` |
| **D3 – SSDF→CI/CD Workflows** | GitHub Actions implementing CodeQL, SBOM, provenance, Scorecard, and secret checks (pinned SHA). | `deliverables/03-ssdf-genai-ci/README.md` |
| **D4 – C2PA Provenance Demo** | TypeScript CLI + viewer for signing and verifying AI-generated assets with C2PA v2.2 assertions. | `deliverables/04-c2pa-provenance-demo/README.md` |
| **D5 – ISO/IEC 42001 Bridge** | Mapping of kit artifacts to ISO controls, plus RACI matrix and compliance checklist. | `deliverables/05-iso42001-bridge/README.md` |
| **D6 – Education One-Pager** | Classroom guardrails, teacher checklists, parent communications, slide outline. | `deliverables/06-education-onepager/README.md` |

Additional narrative context lives in [docs/SYSTEM-OVERVIEW.md](docs/SYSTEM-OVERVIEW.md).

---

## Architecture & Flow

The kit follows the lifecycle described in [docs/SYSTEM-OVERVIEW.md](docs/SYSTEM-OVERVIEW.md):

1. **Govern** with D1 artifacts (checklists, risk registers, templates).
2. **Measure** with D2 automated evaluations and golden runs.
3. **Build & Manage** with D3 CI/CD workflows, SBOMs, and attestations.
4. **Prove & Inform** with D4 provenance tooling and D6 communication aids.
5. **Attest** against ISO/IEC 42001 using D5 mappings and RACI matrices.

Everything is designed to be modular—adopt one deliverable or all six.

---

## Quality Gates & Security

- **Evaluation Harness (D2):** Refusal thresholds, PII leak detection, deterministic golden runs.
- **CI/CD Workflows (D3):** CodeQL, Trivy, pip-audit, npm audit, secret scans, license compliance, Scorecard.
- **Supply Chain Evidence:** SLSA v1.0 Level 3 provenance, dual-format SBOMs, signed artifacts.
- **Threat Model:** STRIDE-lite analysis for RAG systems in [docs/threat-model.md](docs/threat-model.md).

Run `deliverables/03-ssdf-genai-ci/validate-workflows.sh` to verify workflow hardening before enabling Actions.

---

## Compliance & Governance

- **NIST AI RMF Alignment:** D1 checklists are organized around Govern, Map, Measure, Manage functions.
- **ISO/IEC 42001 Bridge:** Use D5 to demonstrate coverage for AI management system controls.
- **Release Process:** Follow [docs/RELEASE-CHECKLIST.md](docs/RELEASE-CHECKLIST.md) and [DO-THIS-NEXT.md](DO-THIS-NEXT.md) to tag releases, publish SBOMs, and mint DOIs.
- **Threat Informed:** Cross-reference deliverables with the STRIDE risks in [docs/threat-model.md](docs/threat-model.md).

---

## Repository Layout

```
responsible-genai-starter-kit/
├── deliverables/
│   ├── 01-gai-rmf-kit/           # Governance checklists and templates
│   ├── 02-eval-harness/          # Python evaluation package
│   ├── 03-ssdf-genai-ci/         # Hardened GitHub Actions workflows
│   ├── 04-c2pa-provenance-demo/  # C2PA signing & verification demo
│   ├── 05-iso42001-bridge/       # Compliance crosswalks
│   └── 06-education-onepager/    # Classroom guardrails and resources
├── docs/                         # Getting started, system overview, threat model, release checklist
├── CHANGELOG.md                  # Release history
├── CITATION.cff                  # Machine-readable citation metadata
├── LICENSE                       # Apache-2.0 for code
├── SECURITY.md                   # Vulnerability disclosure policy
└── README.md                     # You are here
```

---

## Community & Contributions

Contributions are welcome. Before submitting:

- Read [CONTRIBUTING.md](CONTRIBUTING.md) for coding standards and review expectations.
- Update or add documentation alongside any code changes.
- Use the provided evaluation harness and workflows to validate your changes.
- Clearly mark whether your contribution is a **research experiment** or an **operational improvement**.

Security issues? Follow the guidance in [SECURITY.md](SECURITY.md). Never disclose vulnerabilities publicly before coordinating a fix.

---

## Citation & Licensing

If you reference this kit in research or policy work, please cite:

```bibtex
@software{responsible_genai_starter_kit,
  author = {Lovell, Jason},
  title = {Responsible GenAI Starter Kit},
  version = {0.1.0},
  year = {2025},
  url = {https://github.com/jlov7/responsible-genai-starter-kit},
  doi = {10.5281/zenodo.XXXXXX}
}
```

Licensing model:

| Content Type | License | Notes |
|--------------|---------|-------|
| Code (Python, JavaScript, workflows) | [Apache-2.0](LICENSE) | Commercial use permitted with standard Apache terms |
| Documentation, checklists, templates | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) | Attribute “Responsible GenAI Starter Kit” and Jason Lovell |

---

**Made with care for practitioners who need responsible AI guardrails, fast.**  
Questions? Open an issue on your fork or email the maintainer listed in `CITATION.cff` after you personalize it.
