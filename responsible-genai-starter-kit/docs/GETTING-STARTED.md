# Getting Started

Step-by-step guide for spinning up the Responsible GenAI Starter Kit as a research-focused, production-grade reference implementation.

> **Reminder:** This repository is a personal research passion project. The code and workflows strive for production quality, but the project is **not** a supported commercial product. Clone, adapt, and extend at your own risk.

---

## 1. Prerequisites

Install the tools you need before cloning the repo.

- Git 2.40+
- Python 3.10 or later
- Node.js 18+ (bundled npm)
- OpenSSL (for demo certificates)
- Bash-compatible shell (macOS and Linux tested)
- Optional: GitHub CLI (`gh`) for release and attestation flows

Verify versions:

```bash
python --version
node --version
openssl version
gh --version   # optional
```

---

## 2. Clone the Repository

```bash
git clone https://github.com/jlov7/responsible-genai-starter-kit.git
cd responsible-genai-starter-kit
```

> Forking? Swap in your own GitHub handle when cloning so badges and links resolve to your repository.

---

## 3. Explore the Deliverables

Each deliverable is a self-contained package under `deliverables/`:

| ID | Name | Purpose |
|----|------|---------|
| D1 | `01-gai-rmf-kit` | NIST AI 600-1 aligned checklists, templates, and validation scripts |
| D2 | `02-eval-harness` | Python package for automated model evaluation with safety-focused scorers |
| D3 | `03-ssdf-genai-ci` | GitHub Actions workflows mapped to NIST SP 800-218A |
| D4 | `04-c2pa-provenance-demo` | Node.js CLI + viewer for C2PA content signing and verification |
| D5 | `05-iso42001-bridge` | Crosswalk to ISO/IEC 42001 AI Management System controls |
| D6 | `06-education-onepager` | Plain-language guardrails and classroom resources |

Skim each README after this quick-start to understand artifacts in detail.

---

## 4. Run the Evaluation Harness (D2)

1. Create and activate a virtual environment:
   ```bash
   cd deliverables/02-eval-harness
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies (includes dev extras for tests and linting):
   ```bash
   pip install -e ".[dev]"
   ```

3. Run the test suite:
   ```bash
   pytest
   ```

4. Execute an example evaluation:
   ```bash
   eval-harness run \
     --dataset examples/qa_dataset.csv \
     --scorers exact_match,length \
     --output results/qa_results.json
   ```

   Expected output:
   - Metrics summary printed to the console
   - JSON report written to `results/qa_results.json`

5. Inspect aggregated metrics:
   ```bash
   jq '.aggregate_metrics' results/qa_results.json
   ```

> See `deliverables/02-eval-harness/README.md` for scorer configuration, dataset schemas, and CI integration patterns.

---

## 5. Validate Governance Checklists (D1)

1. Install checker dependencies:
   ```bash
   cd ../01-gai-rmf-kit
   python -m pip install --upgrade pip pyyaml
   ```

2. Run the checklist validator:
   ```bash
   python scripts/validate_checklists.py
   ```

3. Regenerate the crosswalk if you modify any controls:
   ```bash
   python scripts/generate_crosswalk.py
   ```

Artifacts:
- YAML checklists for RAG, fine-tuning, and code assistants
- Model card and risk register templates
- `crosswalk.csv` mapping control IDs to NIST AI RMF functions

---

## 6. Exercise the Supply Chain Workflows (D3)

1. Inspect workflows under `deliverables/03-ssdf-genai-ci/workflows/`.

2. Run the validation script (requires either `yq` or `PyYAML`):
   ```bash
   cd ../03-ssdf-genai-ci
   ./validate-workflows.sh
   ```

3. Copy workflows into your repo to test end-to-end:
   ```bash
   mkdir -p ../../.github/workflows
   cp workflows/*.yml ../../.github/workflows/
   ```

4. Review the setup guide (`SETUP.md`) to enable required GitHub permissions, SBOM config, and attestation flows.

> These pipelines are hardened for open-source release but expect you to wire them into an actual project. Customize job matrices, language targets, and artifact names as needed.

---

## 7. Try the C2PA Provenance Demo (D4)

1. Install Node dependencies:
   ```bash
   cd ../04-c2pa-provenance-demo
   npm install
   ```

2. Build the TypeScript sources:
   ```bash
   npm run build
   ```

3. Generate dev certificates (demo only):
   ```bash
   bash examples/generate-dev-certs.sh
   ```

4. Sign an example image:
   ```bash
   npm run sign -- \
     -i examples/images/photo.jpg \
     -o examples/images/photo-signed.jpg \
     -c examples/certs/dev-certificate.pem \
     -k examples/certs/dev-private-key.pem \
     --title "Demo Image" \
     --ai-generated
   ```

5. Verify the signature:
   ```bash
   npm run verify -- \
     -i examples/images/photo-signed.jpg \
     --detailed
   ```

6. Launch the viewer (optional):
   ```bash
   npm run viewer
   # Open http://localhost:8080 in a browser
   ```

> The CLI and viewer warn loudly that the bundled certificates are for development only. Replace them with production-grade credentials before signing real content.

---

## 8. Map to ISO/IEC 42001 (D5)

- `deliverables/05-iso42001-bridge/README.md` summarizes how kit artifacts align with AI Management System controls.
- `ISO42001-MAPPING.md` provides detailed mappings.
- `compliance-checklist.yaml` gives a starting point for control attestations.

Use this deliverable to brief compliance or risk teams on how your implementation satisfies AI governance requirements.

---

## 9. Share Classroom Guardrails (D6)

- `deliverables/06-education-onepager/` contains teacher checklists, parent notes, and a slide-deck outline.
- Adapt the language to your community; the documents are licensed CC-BY-4.0 so they can be remixed with attribution.

---

## 10. Next Steps

1. Personalize metadata:
   - Update README badges with your GitHub username and release URLs.
   - Set real contact info in `SECURITY.md` and `CITATION.cff`.
2. Automate releases:
   - Tag a version.
   - Publish SBOMs and attestations.
   - Sync to Zenodo for long-term archival.
3. Extend evaluations:
   - Add custom scorers for your domain.
   - Integrate red-team datasets.
4. Operationalize governance:
   - Track checklist items in your issue tracker.
   - Connect risk register entries to evaluation gates.

---

## Frequently Asked Questions

**Is this a product?**  
No. It is a public research reference that demonstrates how to operationalize responsible AI guardrails. There is no support contract, SLA, or roadmap guarantee.

**Can I use this in production?**  
Yes, but do so with a full review. Treat this repository as a high-quality starting point. You must own the security posture, dependency updates, and compliance obligations.

**Where should I file issues?**  
Use your fork’s issue tracker. If you find a bug in the reference implementation, open an issue with detailed reproduction steps and clearly mark whether it is security-sensitive.

---

**Last updated:** 2025-01-XX  
Maintainer: Jason Lovell (personal research initiative)
