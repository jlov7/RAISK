# Responsible GenAI Starter Kit

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/yourusername/responsible-genai-starter-kit/actions)
[![OpenSSF Scorecard](https://img.shields.io/badge/scorecard-passing-brightgreen)](https://securityscorecards.dev/)
[![SLSA Provenance](https://img.shields.io/badge/SLSA-L3-green)](https://slsa.dev/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Docs: CC-BY-4.0](https://img.shields.io/badge/Docs-CC--BY--4.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.XXXXXX-blue)](https://zenodo.org/badge/latestdoi/XXXXXX)

**Production-ready toolkit for building responsible generative AI systems aligned to U.S. federal guidance.**

This open-source starter kit provides checklists, evaluation harnesses, CI/CD workflows, and educational resources grounded in:
- **NIST AI 600-1** (Generative AI Profile, July 2024)
- **NIST AI RMF Playbook** (AI Risk Management Framework implementation)
- **NIST SP 800-218A** (Secure Software Development Framework for GenAI & dual-use foundation models)
- **C2PA v2.2** (Content Provenance and Authenticity)

---

## 🎯 What's Inside

### Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| **D1** | [GAI-RMF Implementation Kit](deliverables/01-gai-rmf-kit/) | Risk management checklists for RAG, fine-tuning, and code assistants; model card and risk register templates |
| **D2** | [Eval Harness Starter](deliverables/02-eval-harness/) | Minimal evaluation framework with PII detection, refusal-rate scoring, and pluggable LLM judges |
| **D3** | [SSDF→CI/CD Workflows](deliverables/03-ssdf-genai-ci/) | Security workflows (CodeQL, Scorecard, SBOM, SLSA provenance) mapped to NIST SP 800-218A |
| **D4** | [C2PA Provenance Demo](deliverables/04-c2pa-provenance-demo/) | CLI and web viewer for signing and verifying content credentials |
| **D5** | [ISO/IEC 42001 Bridge](deliverables/05-iso42001-bridge/) | Mapping of kit artifacts to ISO/IEC 42001 AI management system controls |
| **D6** | [Education One-Pager](deliverables/06-education-onepager/) | Plain-English classroom guardrails guide with teacher checklist and parent note |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/responsible-genai-starter-kit.git
cd responsible-genai-starter-kit

# Install dependencies (Python example)
cd deliverables/02-eval-harness
pip install -e .

# Run sample evaluation
eval-harness run \
  --dataset examples/qa_dataset.csv \
  --scorers exact_match,length

# Sign content with C2PA
cd ../04-c2pa-provenance-demo
npm install
npm run build
npm run sign -- -i examples/images/photo.jpg -o examples/images/photo-signed.jpg -c examples/certs/dev-certificate.pem -k examples/certs/dev-private-key.pem --title "Demo" --ai-generated
npm run verify -- -i examples/images/photo-signed.jpg --detailed
```

---

## 📋 Licensing

This project uses **dual licensing** to maximize open access:

| Content Type | License | Scope |
|--------------|---------|-------|
| **Code** | [Apache License 2.0](LICENSE) | Python/JavaScript/TypeScript source, CI workflows, scripts |
| **Documentation** | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) | Markdown files, checklists, templates, diagrams |

**What this means:**
- Software components can be used commercially, modified, and distributed under Apache 2.0 terms
- Educational materials can be freely adapted and redistributed with attribution under CC-BY-4.0
- Educators, researchers, and practitioners may use all content without fees or permission requests

---

## 🛡️ Security & Supply Chain

All releases include:
- **SBOMs** (SPDX and CycloneDX formats) via Syft and cdxgen
- **SLSA v1.0 L3 provenance** via slsa-github-generator + GitHub Artifact Attestations
- **OpenSSF Scorecard** weekly scans
- **CodeQL** static analysis
- **Evaluation quality gates** blocking releases unless thresholds met (NIST AI RMF MEASURE/MANAGE)

**Supply chain verification:**
```bash
# Verify SLSA provenance (requires slsa-verifier)
slsa-verifier verify-artifact release.tar.gz \
  --provenance-path provenance.jsonl \
  --source-uri github.com/yourusername/responsible-genai-starter-kit
```

See [SECURITY.md](SECURITY.md) for vulnerability reporting.

---

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Test commands
- Code review process
- Commit and PR guidelines

---

## 📚 Documentation

- [References & Citations](docs/refs.md) – Canonical NIST and C2PA sources
- [Threat Model](docs/threat-model.md) – STRIDE-lite analysis for RAG systems
- [Agents Workflow](AGENTS.md) – How this kit was built with Claude Code sub-agents

---

## 📖 Citation

If you use this kit in research or practice, please cite:

```bibtex
@software{responsible_genai_starter_kit,
  author = {Lovell, Jason},
  title = {Responsible GenAI Starter Kit},
  version = {0.1.0},
  year = {2025},
  url = {https://github.com/yourusername/responsible-genai-starter-kit},
  doi = {10.5281/zenodo.XXXXXX}
}
```

See [CITATION.cff](CITATION.cff) for machine-readable metadata.

---

## 📜 Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

---

## 📄 Release Notes

See [CHANGELOG.md](CHANGELOG.md) for version history and [RELEASE_NOTES.md](RELEASE_NOTES.md) for the latest release summary.

---

## 🙏 Acknowledgments

Built with guidance from:
- NIST AI Safety Institute
- OpenSSF Best Practices Working Group
- Content Authenticity Initiative (CAI)
- Claude Code agentic workflows

---

**Made with ❤️ for responsible AI development**
