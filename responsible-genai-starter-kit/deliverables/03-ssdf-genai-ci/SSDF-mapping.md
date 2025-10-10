# SSDF Practice Mapping: CI/CD Workflows for GenAI

This document maps the GitHub Actions workflows in this deliverable to specific practices from **NIST SP 800-218A: Secure Software Development Framework (SSDF) Version 1.1 - Community Profile for Generative AI and Dual-Use Foundation Models**.

**Citation:**
> Souppaya, M., Scarfone, K., & Dodson, D. (2024). *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities – A Community Profile for Generative AI and Dual-Use Foundation Models* (NIST SP 800-218A). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-218A

---

## Overview

The SSDF defines four practice areas for secure software development:

1. **PO (Prepare the Organization)**: Governance, training, and process establishment
2. **PS (Protect the Software)**: Secure storage, integrity, and access control
3. **PW (Produce Well-Secured Software)**: Development, testing, and vulnerability management
4. **RV (Respond to Vulnerabilities)**: Detection, response, and remediation

This deliverable implements **automated CI/CD workflows** that address practices in PS and PW, with supporting mechanisms for PO and RV.

---

## Practice Mappings by Workflow

### 1. Security Scanning Workflow (`security.yml`)

| SSDF Practice | Description | Implementation |
|--------------|-------------|----------------|
| **PS.1.1** | Store and secure all forms of code (including source, executable, configuration, etc.) in a repository | Regular vulnerability scanning of repository contents (weekly schedule + push triggers) |
| **PS.2.1** | Protect the integrity of the software that the organization works on | Secret scanning with Gitleaks prevents credential leakage; GenAI-specific API key detection |
| **PW.4.1** | Identify and document all software components | Dependency scanning identifies all third-party components (Python, Node.js, etc.) |
| **PW.4.4** | Analyze identified software components for known vulnerabilities | Trivy, pip-audit, npm audit check components against CVE/OSV databases |
| **PW.6.1** | Use automated processes to perform testing | CodeQL SAST for static analysis; automated on every push/PR |
| **PW.7.1** | Review and analyze scan results | Results uploaded to GitHub Security tab (SARIF format) for centralized review |
| **PS.3.1** | Archive and protect each software release | Scan reports retained for 90 days per retention policy |

**Key Features:**
- **CodeQL SAST**: Multi-language static analysis (Python, JavaScript, Java, Go, etc.)
- **Dependency Scanning**: Trivy for comprehensive vulnerability detection across package managers
- **Secret Detection**: Gitleaks + custom GenAI API key patterns (OpenAI, Anthropic, HuggingFace)
- **License Compliance**: pip-licenses and license-checker for open-source license validation

**GenAI Extensions:**
- Custom regex patterns for GenAI service credentials
- License checks for ML frameworks (TensorFlow, PyTorch use Apache 2.0)
- Integration with SARIF for consistent reporting

---

### 2. SBOM Generation Workflow (`sbom.yml`)

| SSDF Practice | Description | Implementation |
|--------------|-------------|----------------|
| **PW.4.1** | Obtain and maintain well-formed SBOMs | Syft generates SPDX-JSON and CycloneDX-JSON SBOMs per ISO/IEC 5962:2021 |
| **PW.4.2** | Acquire and maintain well-secured software components | Dependency review on PRs; automated checks for new dependencies |
| **PW.4.4** | Analyze identified software components for known vulnerabilities | Grype scans SBOM for CVEs; results uploaded to Security tab |
| **PS.3.1** | Archive and protect each software release | SBOMs cryptographically signed with Sigstore Cosign (keyless signing) |
| **PS.3.2** | Make software integrity verification information available to software acquirers | SBOMs published to GitHub Releases; attestations linked via GitHub API |

**Key Features:**
- **Dual-Format SBOMs**: SPDX (ISO standard) + CycloneDX (OWASP standard)
- **Ecosystem-Specific**: Python (cyclonedx-py), Node.js (cyclonedx-npm) tooling
- **NTIA Validation**: Checks SBOM contains NTIA minimum elements (supplier, component, dependencies)
- **Cryptographic Signing**: Sigstore Cosign with OIDC (GitHub identity binding)
- **Attestation**: GitHub native attestations (`actions/attest-sbom`) for verifiable provenance
- **Dependency Review**: PR-based review prevents problematic licenses (GPL, AGPL, SSPL)

**GenAI Extensions:**
- `.syft.yaml` config excludes test files, includes ML framework detection
- Custom metadata for model files (.bin, .safetensors, .onnx)
- License checks for AI/ML-specific packages

---

### 3. Build Provenance Workflow (`provenance.yml`)

| SSDF Practice | Description | Implementation |
|--------------|-------------|----------------|
| **PS.3.1** | Archive and protect each software release | Build artifacts cryptographically signed with Cosign; SLSA provenance generated |
| **PS.3.2** | Make software integrity verification information available | Provenance documents published to releases; verification instructions in release notes |
| **PW.1.3** | Establish and maintain a secure build environment | GitHub-hosted runners (SLSA L3 compliant); ephemeral, isolated builds |
| **PW.4.1** | Create Software Bill of Materials (SBOM) for each release | SBOM generated and attested alongside provenance |

**Key Features:**
- **SLSA v1.0 Provenance**: Structured metadata per SLSA specification
- **GitHub Attestations**: Native `actions/attest-build-provenance` for tamper-proof linking
- **Keyless Signing**: Sigstore Cosign with GitHub OIDC (no key management burden)
- **Automated Verification**: Second job verifies all signatures immediately after generation
- **SHA256 Digests**: Artifact integrity checksums included in attestations

**SLSA Level Compliance:**
- **SLSA L1**: Provenance exists (JSON document)
- **SLSA L2**: Signed provenance (Cosign + OIDC)
- **SLSA L3**: Hardened build platform (GitHub-hosted runners)

**GenAI Extensions:**
- Provenance includes dataset/model lineage metadata (if applicable)
- Verification instructions demonstrate reproducibility
- Integration with SBOM for complete supply chain transparency

---

### 4. OpenSSF Scorecard Workflow (`scorecard.yml`)

| SSDF Practice | Description | Implementation |
|--------------|-------------|----------------|
| **PO.3.1** | Establish and maintain security practices | Weekly assessment of 18+ security best practices |
| **PO.3.2** | Provide role-based training | Automated recommendations via GitHub Issues (actionable guidance) |
| **PS.1.1** | Store and secure all forms of code | Checks for branch protection, signed commits, dangerous workflows |
| **PW.1.1** | Define and maintain secure build processes | Validates pinned dependencies, SAST enablement, CI testing |

**Key Features:**
- **18+ Security Checks**: Branch-Protection, Pinned-Dependencies, Token-Permissions, SAST, Vulnerabilities, etc.
- **Weekly Automation**: Scheduled runs every Monday at 10 AM UTC
- **SARIF Integration**: Results uploaded to Security tab for historical tracking
- **Actionable Issues**: Creates GitHub Issues for failed checks with remediation guidance

**Scorecard Checks Mapped to SSDF:**
- **Branch-Protection** → PS.1.1 (secure code storage)
- **Pinned-Dependencies** → PW.1.1 (reproducible builds)
- **Token-Permissions** → PS.2.1 (least privilege)
- **SAST** → PW.6.1 (automated testing)
- **Signed-Releases** → PS.3.1 (artifact integrity)
- **Dependency-Update-Tool** → PW.4.4 (vulnerability management)

**GenAI Extensions:**
- Evaluates ML pipeline security practices
- Checks for model signing and versioning
- Identifies gaps in data provenance documentation

---

## SSDF Practice Coverage Matrix

### Prepare the Organization (PO)

| Practice | Task | Workflow | Implementation |
|----------|------|----------|----------------|
| PO.3.1 | Establish and maintain security practices | `scorecard.yml` | Weekly OpenSSF Scorecard assessment |
| PO.3.2 | Provide security training | `scorecard.yml` | Automated recommendations via GitHub Issues |

### Protect the Software (PS)

| Practice | Task | Workflow | Implementation |
|----------|------|----------|----------------|
| PS.1.1 | Store and secure code | `security.yml`, `scorecard.yml` | Vulnerability scanning, branch protection checks |
| PS.2.1 | Protect code integrity | `security.yml` | Secret scanning, token permissions validation |
| PS.3.1 | Archive and protect releases | `sbom.yml`, `provenance.yml` | Cryptographic signing, attestations |
| PS.3.2 | Make verification info available | `sbom.yml`, `provenance.yml` | SBOMs and provenance published to releases |

### Produce Well-Secured Software (PW)

| Practice | Task | Workflow | Implementation |
|----------|------|----------|----------------|
| PW.1.1 | Define secure build processes | `scorecard.yml` | Validate pinned dependencies, reproducibility |
| PW.1.3 | Secure build environment | `provenance.yml` | GitHub-hosted runners (SLSA L3) |
| PW.4.1 | Create and maintain SBOM | `sbom.yml`, `provenance.yml` | SPDX/CycloneDX SBOMs with attestations |
| PW.4.2 | Acquire well-secured components | `sbom.yml` | Dependency review on PRs |
| PW.4.4 | Analyze components for vulnerabilities | `security.yml`, `sbom.yml` | Trivy, Grype, pip-audit, npm audit |
| PW.6.1 | Use automated testing | `security.yml` | CodeQL SAST, automated scans on push/PR |
| PW.7.1 | Review and analyze results | `security.yml` | SARIF upload to Security tab, centralized tracking |

### Respond to Vulnerabilities (RV)

| Practice | Task | Workflow | Implementation |
|----------|------|----------|----------------|
| RV.1.1 | Monitor for vulnerabilities | `security.yml` | Weekly scheduled scans, CVE database checks |
| RV.2.1 | Analyze vulnerabilities | `security.yml` | Trivy severity filtering (CRITICAL, HIGH, MEDIUM) |
| RV.2.2 | Plan and implement remediation | `scorecard.yml` | GitHub Issues for tracking remediation |

---

## GenAI-Specific SSDF Enhancements

NIST SP 800-218A extends the SSDF with GenAI-specific considerations. These workflows implement:

### 1. Model Supply Chain Security
- **SBOM for Models**: `.syft.yaml` includes ML framework detection (TensorFlow, PyTorch, Transformers)
- **Provenance for Models**: Placeholder for model lineage tracking (base model → fine-tuning → deployment)
- **License Compliance**: Checks for AI model licenses (CreativeML, BigScience RAIL, etc.)

### 2. Credential Protection
- **GenAI API Keys**: Custom regex patterns in `security.yml` detect OpenAI, Anthropic, HuggingFace tokens
- **Secret Scanning**: Prevents accidental commit of LLM service credentials

### 3. Dependency Risks
- **ML Framework Vulnerabilities**: Trivy includes ML-specific CVE databases (e.g., TensorFlow CVEs)
- **Transitive Dependencies**: SBOM captures nested dependencies common in ML stacks

### 4. Evaluation and Testing
- **Automated Testing**: Integration points for AI red-teaming and evaluation harness (see Deliverable 2)
- **Scorecard Extensions**: Future checks for model card presence, dataset documentation

---

## Implementation Notes

### Permissions Strategy
All workflows follow **least-privilege principles**:
- `contents: read` (default)
- `security-events: write` (SARIF uploads)
- `id-token: write` (keyless signing)
- `attestations: write` (GitHub attestations)

### Pinned Actions
All GitHub Actions use **commit SHAs** (not tags) per OpenSSF Scorecard best practices:
- `actions/checkout@eef61447b9ff4aafe5dcd4e0bbf5d482be7e7871` (v4.2.1)
- `github/codeql-action/analyze@f09c1c0a94de965c15400f5634aa42fac8fb8f88` (v3.27.5)

### Retention Policies
- **Security Scan Reports**: 90 days (compliance requirement)
- **SBOMs**: 90 days + permanent release attachment
- **Attestations**: Permanent (GitHub-hosted, immutable)

### Triggering Strategy
- **On Push**: `security.yml` (immediate feedback)
- **On PR**: `security.yml`, `sbom.yml` (dependency review)
- **On Release/Tag**: `sbom.yml`, `provenance.yml` (release artifacts)
- **Weekly Schedule**: `security.yml`, `scorecard.yml` (continuous monitoring)

---

## Compliance Verification

### Auditing SSDF Implementation
To verify SSDF compliance:

1. **Check Security Tab**: https://github.com/[org]/[repo]/security/code-scanning
   - View all SARIF uploads (CodeQL, Trivy, Scorecard)
2. **Review Releases**: https://github.com/[org]/[repo]/releases
   - Confirm SBOMs and provenance documents attached
3. **Inspect Attestations**:
   ```bash
   gh attestation verify [artifact] --owner [org]
   ```
4. **OpenSSF Scorecard Badge**:
   ```bash
   curl https://api.securityscorecards.dev/projects/github.com/[org]/[repo]
   ```

### Gap Analysis
Practices **not fully automated** (require organizational processes):
- **PO.1**: Define security requirements (manual governance)
- **PO.2**: Implement secure development training (requires LMS)
- **RV.3**: Release vulnerability information (requires disclosure process)

---

## References

### NIST Publications
- **NIST SP 800-218A**: https://csrc.nist.gov/pubs/sp/800/218/a/final
- **NIST AI 600-1** (GenAI Profile): https://doi.org/10.6028/NIST.AI.600-1

### Standards
- **SPDX 2.3** (ISO/IEC 5962:2021): https://spdx.dev/specifications/
- **CycloneDX 1.5**: https://cyclonedx.org/specification/overview/
- **SLSA v1.0**: https://slsa.dev/spec/v1.0/

### Tools
- **OpenSSF Scorecard**: https://github.com/ossf/scorecard
- **Syft**: https://github.com/anchore/syft
- **Sigstore Cosign**: https://github.com/sigstore/cosign
- **GitHub Attestations**: https://docs.github.com/en/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds

---

**Document Version**: 1.0
**Last Updated**: 2025-01-XX
**Maintained By**: Responsible GenAI Starter Kit Project
