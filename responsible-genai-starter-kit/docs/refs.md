# References & Citations

This document provides canonical citations for all standards, frameworks, and specifications referenced in the Responsible GenAI Starter Kit.

---

## NIST AI Guidance

### NIST AI 600-1: Generative AI Profile (July 2024)

**Full Title**: Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

**Citation**:
> National Institute of Standards and Technology (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.600-1

**PDF**: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

**Key Sections**:
- Section 2: GAI Risk Categories (CBRN, bias, data privacy, environmental, human-AI configuration, information integrity, dangerous content, value chain)
- Section 3: GAI-specific updates to AI RMF functions (Govern, Map, Measure, Manage)
- Appendix A: Mapping to AI RMF Core

**Used In**: D1 (checklist control_id references), D2 (eval categories), D5 (ISO 42001 mapping)

---

### NIST AI RMF Playbook

**Full Title**: AI Risk Management Framework Playbook

**URL**: https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook

**Description**: Practical implementation guide with "suggested actions" for each AI RMF outcome. Non-normative companion to the AI RMF Core.

**Key Resources**:
- Suggested Actions by Function (Govern, Map, Measure, Manage)
- Cross-sectoral use case examples
- Links to tooling and measurement techniques

**Used In**: D1 (crosswalk CSV, checklist actions), D6 (educator guidance)

---

### NIST SP 800-218A: SSDF for GenAI (July 2024)

**Full Title**: Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities – A Community Profile for Generative AI and Dual-Use Foundation Models

**Citation**:
> Souppaya, M., Scarfone, K., & Dodson, D. (2024). *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities – A Community Profile for Generative AI and Dual-Use Foundation Models* (NIST SP 800-218A). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-218A

**PDF**: https://csrc.nist.gov/pubs/sp/800/218/a/final

**Key Practices** (SSDF task IDs):
- **PO**: Prepare the Organization (governance, training)
- **PS**: Protect the Software (secure design, SBOM)
- **PW**: Produce Well-Secured Software (code review, testing)
- **RV**: Respond to Vulnerabilities (incident response, patching)

**Used In**: D3 (SSDF-218A-mapping.md, CI workflow justifications)

---

## Content Provenance & Authenticity

### C2PA Technical Specification v2.2 (May 2025)

**Full Title**: Coalition for Content Provenance and Authenticity (C2PA) Technical Specification Version 2.2

**URL**: https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html

**PDF**: https://spec.c2pa.org/specifications/specifications/2.2/specs/_attachments/C2PA_Specification.pdf

**Key Concepts**:
- **Manifest**: Cryptographically signed metadata describing content history
- **Assertions**: Claims about content (e.g., authorship, edits)
- **Hard Bindings**: Manifests embedded in file formats (JPEG, PNG, PDF, MP4)

**Important**: C2PA v2.2 removed the Training & Data Mining assertion from core spec. See CAWG 1.1 below for replacement.

**Used In**: D4 (C2PA sign/verify CLI, web viewer)

---

### CAWG Training & Data Mining Assertion 1.1 (May 16, 2025)

**Full Title**: Creator Assertions Working Group (CAWG) Training and Data Mining Assertion Specification v1.1

**Status**: DIF-ratified (Decentralized Identity Foundation)

**Assertion Label**: `cawg.training-mining`

**Entry Keys**:
- `cawg.ai_generative_training` - Generative AI training permissions (`allowed` | `notAllowed` | `constrained`)
- `cawg.ai_training` - General AI model training permissions
- `cawg.data_mining` - Data mining permissions
- `cawg.ai_inference` - AI inference permissions

**Context**: Replaces the C2PA v1.x core training/mining assertion. As of C2PA v2.2 (May 2025), AI training restrictions are defined by CAWG, not C2PA core spec.

**References**:
- C2PA v2.2 Specification (notes removal of training/mining from core)
- C2PA v1.3 Explainer (historical context): https://c2pa.org/specifications/specifications/1.3/explainer/Explainer.html
- CAWG Working Group: https://creator-assertions.github.io/

**Used In**: D4 (AI-generated content metadata examples, documentation)

---

### Content Authenticity Initiative (CAI) JavaScript SDK

**URL**: https://opensource.contentauthenticity.org/docs/js-sdk/getting-started/overview/

**GitHub**: https://github.com/contentauth/c2pa-js

**Description**: Open-source tools for reading and displaying C2PA manifests in web applications.

**Used In**: D4 (in-browser manifest viewer)

---

## Supply Chain Security

### OpenSSF Scorecard

**GitHub**: https://github.com/ossf/scorecard

**Action**: https://github.com/ossf/scorecard-action

**Docs**: https://github.com/ossf/scorecard-action#publishing-results

**Description**: Automated security assessment of open-source projects across 18 checks (Branch-Protection, Signed-Releases, Dependency-Update-Tool, etc.).

**Required Permissions** (v2.x when `publish_results: true`):
```yaml
permissions:
  security-events: write
  id-token: write
  contents: read
  actions: read
```

**Used In**: D3 (weekly Scorecard workflow), quality gates

---

### SLSA Framework

**URL**: https://slsa.dev/

**GitHub Generator**: https://github.com/slsa-framework/slsa-github-generator

**Description**: Supply-chain Levels for Software Artifacts. Framework for preventing tampering and ensuring build integrity.

**Levels**:
- **L1**: Provenance exists
- **L2**: Signed provenance
- **L3**: Hardened build platform (GitHub-hosted runners qualify)

**Used In**: D3 (provenance.yml workflow)

---

### GitHub Artifact Attestations

**Docs**: https://docs.github.com/en/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds

**Action**: `actions/attest-build-provenance@v1`, `actions/attest-sbom@v1`

**Security Guide**: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#using-secrets

**Description**: Native GitHub feature for attaching signed SLSA provenance to release artifacts.

**Required Permissions** (at workflow AND job level):
```yaml
permissions:
  contents: read
  id-token: write      # Required for keyless signing with OIDC
  attestations: write  # Required for attestation API
```

**Action Pinning**: GitHub recommends pinning actions to full commit SHAs (not tags) for security.

**Used In**: D3 (provenance.yml, sbom.yml workflows)

---

### SBOM Tools

#### Syft (Anchore)
- **GitHub**: https://github.com/anchore/syft
- **Action**: https://github.com/anchore/sbom-action
- **Format**: SPDX-JSON, SPDX-XML, CycloneDX-JSON
- **Used In**: D3 (sbom.yml → SPDX generation)

#### cdxgen (CycloneDX)
- **GitHub**: https://github.com/CycloneDX/cdxgen
- **Action**: https://github.com/CycloneDX/gh-node-module-generatebom
- **Format**: CycloneDX-JSON
- **Used In**: D3 (sbom.yml → CycloneDX generation)

---

## ISO Standards

### ISO/IEC 42001:2023

**Full Title**: Information technology — Artificial intelligence — Management system

**Description**: International standard specifying requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System (AIMS).

**Key Sections**:
- Clause 4: Context of the organization
- Clause 5: Leadership
- Clause 6: Planning (risk assessment, objectives)
- Clause 7: Support (resources, competence, documentation)
- Clause 8: Operation (AI system lifecycle)
- Clause 9: Performance evaluation
- Clause 10: Improvement

**Used In**: D5 (ISO 42001 bridge note, RACI matrix)

---

## Development Tools

### Claude Code

**Docs**: https://docs.claude.com/en/docs/claude-code/

**VS Code Extension**: https://docs.claude.com/en/docs/claude-code/ide-integrations

**Sub-Agents**: Specialized agents for parallel task execution (PolicyMapper, EvalHarnessEngineer, CIEngineer, C2PAEngineer, DocsWriter, Educator)

**Used In**: AGENTS.md (workflow documentation)

---

## Additional Resources

### NIST AI Safety Institute
- **URL**: https://www.nist.gov/aisi
- Resources for red-teaming, evaluation, and measurement science

### OWASP LLM Top 10
- **URL**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Common vulnerabilities in LLM applications (prompt injection, data leakage, etc.)

### MLCommons AI Safety Benchmark
- **URL**: https://mlcommons.org/benchmarks/ai-safety/
- Standardized hazard taxonomies and evaluation datasets

---

## Citation Format

When citing this toolkit in academic or professional work:

**APA**:
> Lovell, J. (2025). *Responsible GenAI Starter Kit* (Version 0.1.0) [Computer software]. https://github.com/yourusername/responsible-genai-starter-kit

**BibTeX**:
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

See [CITATION.cff](../CITATION.cff) for machine-readable metadata.

---

**Last Updated**: 2025-01-XX
