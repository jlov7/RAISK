# Deliverable 3: SSDF CI/CD Workflows for GenAI

Production-ready GitHub Actions workflows implementing **NIST SP 800-218A** (Secure Software Development Framework for Generative AI).

---

## Overview

This deliverable provides comprehensive CI/CD security workflows for Generative AI projects, implementing secure software development practices per NIST SSDF guidelines. All workflows are copy-paste ready, use pinned action versions (commit SHAs), and follow least-privilege permission models.

### Key Features

- **Security Scanning**: SAST (CodeQL), dependency checks (Trivy), secret detection (Gitleaks)
- **SBOM Generation**: SPDX and CycloneDX formats with cryptographic attestations
- **Build Provenance**: SLSA v1.0 compliant attestations with Sigstore signing
- **OpenSSF Scorecard**: Weekly security posture assessment with automated recommendations

---

## What's Included

```
03-ssdf-genai-ci/
├── workflows/
│   ├── security.yml        # SAST, dependency scanning, secret detection
│   ├── sbom.yml            # Software Bill of Materials generation
│   ├── provenance.yml      # Build provenance attestation (SLSA)
│   └── scorecard.yml       # OpenSSF Scorecard security assessment
├── .syft.yaml              # SBOM generation configuration
├── SSDF-mapping.md         # Detailed NIST SP 800-218A practice mappings
├── SETUP.md                # Comprehensive setup and configuration guide
├── validate-workflows.sh   # Workflow validation and compliance checker
└── README.md               # This file
```

---

## Quick Start

### 1. Copy workflows to your repository

```bash
# From your repository root
mkdir -p .github/workflows
cp deliverables/03-ssdf-genai-ci/workflows/*.yml .github/workflows/
cp deliverables/03-ssdf-genai-ci/.syft.yaml .
```

### 2. Enable GitHub Security Features

- Navigate to **Settings** → **Code security and analysis**
- Enable **CodeQL analysis**, **Secret scanning**, **Dependabot**

### 3. Configure Branch Protection

- **Settings** → **Branches** → Add rule for `main`
- Require PR reviews, status checks, conversation resolution

### 4. Validate and Deploy

```bash
# Validate workflows before committing
cd deliverables/03-ssdf-genai-ci
./validate-workflows.sh

# If validation passes (all mapped practices implemented):
git add .github/workflows/ .syft.yaml
git commit -m "Add SSDF-mapped CI/CD workflows (SP 800-218A)"
git push
```

---

## Workflow Details

### Security Scanning (`security.yml`)

**Triggers**: Push, PR, Weekly (Mondays 9 AM UTC)

**Capabilities**:
- CodeQL SAST for Python, JavaScript, Java, Go, C#, Ruby
- Dependency vulnerability scanning (Trivy, pip-audit, npm audit)
- Secret detection (Gitleaks + GenAI API key patterns)
- License compliance checking (pip-licenses, license-checker)

**SSDF Practices**: PS.1.1, PS.2.1, PW.4.1, PW.4.4, PW.6.1, PW.7.1

**Outputs**: SARIF results in Security tab, downloadable scan reports

---

### SBOM Generation (`sbom.yml`)

**Triggers**: Push to main, Release tags (`v*`), PR (dependency review)

**Capabilities**:
- SPDX-JSON and CycloneDX-JSON SBOM formats
- Python and Node.js ecosystem-specific SBOMs
- NTIA minimum elements validation
- Cryptographic signing with Sigstore Cosign
- GitHub native attestations (`actions/attest-sbom`)
- Vulnerability scanning of SBOM (Grype)
- Dependency review on PRs

**SSDF Practices**: PW.4.1, PW.4.2, PW.4.4, PS.3.1, PS.3.2

**Outputs**: SBOMs attached to releases, signed bundles, dependency review comments

---

### Build Provenance (`provenance.yml`)

**Triggers**: Release tags (`v*`), Published releases

**Capabilities**:
- SLSA v1.0 provenance generation
- GitHub native build attestations (`actions/attest-build-provenance`)
- Keyless signing with Sigstore Cosign (GitHub OIDC)
- Artifact SHA256 digests
- SBOM generation and attestation
- Automated signature verification

**SSDF Practices**: PS.3.1, PS.3.2, PW.1.3, PW.4.1

**SLSA Level**: L3 (signed provenance, hardened build platform)

**Outputs**: Signed provenance documents, attestation bundles, verification instructions

---

### OpenSSF Scorecard (`scorecard.yml`)

**Triggers**: Weekly (Mondays 10 AM UTC), Push to main

**Capabilities**:
- 18+ security checks (Branch-Protection, Pinned-Dependencies, SAST, etc.)
- SARIF integration for historical tracking
- Automated GitHub Issues for failed checks
- Badge generation for README display

**SSDF Practices**: PO.3.1, PO.3.2, PS.1.1, PW.1.1

**Outputs**: SARIF results, security recommendations, compliance badge

---

## SSDF Practice Coverage

This deliverable implements **20+ SSDF practices** across all four practice areas:

### Prepare the Organization (PO)
- **PO.3.1**: Establish security practices → Scorecard assessment
- **PO.3.2**: Provide security training → Automated recommendations

### Protect the Software (PS)
- **PS.1.1**: Store and secure code → Vulnerability scanning
- **PS.2.1**: Protect code integrity → Secret detection
- **PS.3.1**: Archive releases → Cryptographic signing
- **PS.3.2**: Make verification available → SBOM/provenance publishing

### Produce Well-Secured Software (PW)
- **PW.1.1**: Define secure builds → Scorecard validation
- **PW.1.3**: Secure build environment → SLSA L3 runners
- **PW.4.1**: Create SBOMs → Multi-format SBOM generation
- **PW.4.2**: Acquire secure components → Dependency review
- **PW.4.4**: Analyze vulnerabilities → Multi-tool scanning
- **PW.6.1**: Automated testing → SAST, dependency checks
- **PW.7.1**: Review results → SARIF centralization

### Respond to Vulnerabilities (RV)
- **RV.1.1**: Monitor vulnerabilities → Weekly scans
- **RV.2.1**: Analyze vulnerabilities → Severity filtering
- **RV.2.2**: Plan remediation → GitHub Issues

See **SSDF-mapping.md** for detailed mappings.

---

## GenAI-Specific Features

### 1. GenAI Credential Detection
Custom patterns for:
- OpenAI API keys (`sk-[A-Za-z0-9]{48}`)
- Anthropic keys (`sk-ant-[A-Za-z0-9-]{95,}`)
- HuggingFace tokens (`hf_[A-Za-z0-9]{32,}`)

### 2. ML Framework Support
- Automatic detection of TensorFlow, PyTorch, Transformers
- License checks for ML-specific packages
- Model file cataloging (.bin, .safetensors, .onnx)

### 3. Model Supply Chain
- SBOM metadata for model files
- Provenance for model lineage (base model → fine-tuned)
- Integration points for AI red-teaming (Deliverable 2)

---

## Validation and Testing

### Run Validation Script

```bash
cd deliverables/03-ssdf-genai-ci
./validate-workflows.sh
```

**Checks**:
- YAML syntax validity
- Action version pinning (commit SHAs)
- Least-privilege permissions
- SSDF practice annotations
- Security best practices (timeouts, no hardcoded secrets)
- Required workflow files
- Configuration file presence

**Output**: Compliance score (41 checks, 100% pass rate required)

### Test Workflows Locally

Use [act](https://github.com/nektos/act):

```bash
# Install act
brew install act

# Test security workflow
act push --workflows .github/workflows/security.yml

# Test SBOM generation
act push --workflows .github/workflows/sbom.yml
```

---

## Monitoring and Maintenance

### View Security Results

1. **Security Tab**: https://github.com/[org]/[repo]/security/code-scanning
   - CodeQL, Trivy, Scorecard results
2. **Dependabot**: https://github.com/[org]/[repo]/security/dependabot
   - Automated dependency updates
3. **Releases**: https://github.com/[org]/[repo]/releases
   - SBOMs and provenance documents

### Weekly Checklist

- [ ] Review OpenSSF Scorecard results (Mondays)
- [ ] Triage security alerts (Security tab)
- [ ] Update dependencies (Dependabot PRs)
- [ ] Verify SBOMs on recent releases
- [ ] Close resolved security issues

---

## Architecture Decisions

### Why Pinned Action Versions?

Per OpenSSF Scorecard requirements, all actions use **commit SHAs** (not tags):
- Prevents tag hijacking attacks
- Ensures reproducible builds
- Required for SLSA L2+ compliance

Example:
```yaml
uses: actions/checkout@eef61447b9ff4aafe5dcd4e0bbf5d482be7e7871  # v4.2.1
```

### Why Keyless Signing?

Workflows use **Sigstore Cosign** with GitHub OIDC tokens:
- No secret key management
- Identity bound to GitHub repository
- SLSA L2 compliant
- Automatic certificate transparency logs

### Why Multiple SBOM Formats?

- **SPDX**: ISO/IEC 5962:2021 standard (government/enterprise)
- **CycloneDX**: OWASP standard (security-focused, vulnerability data)

Both formats ensure broad tool compatibility.

---

## Troubleshooting

### "Resource not accessible by integration"

**Solution**: Add required permissions to workflow:
```yaml
permissions:
  contents: read
  security-events: write
  attestations: write
```

### CodeQL analysis fails

**Solution**: Explicitly specify languages:
```yaml
strategy:
  matrix:
    language: [python, javascript]
```

### Sigstore signing fails

**Solution**: Ensure `id-token: write` permission is set.

### SARIF upload blocked (private repos)

**Solution**: Enable GitHub Advanced Security (GHAS) or use artifacts instead.

See **SETUP.md** for detailed troubleshooting.

---

## Customization Examples

### Add Slack Notifications

```yaml
- name: Notify Slack
  if: failure()
  uses: slackapi/slack-github-action@70cd7be8e40a46e8b0eced40b0de447bdb42f68e
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK }}
```

### Add Docker Image Scanning

```yaml
- name: Scan Docker image
  uses: aquasecurity/trivy-action@5681af892cd0e5103d2a70678d27b314b7cef0c3
  with:
    image-ref: myapp:latest
    format: sarif
```

### Add Model File Scanning

```yaml
- name: Scan model files
  run: |
    pip install modelscan
    modelscan scan models/ --format json
```

---

## Integration with Other Deliverables

### Deliverable 1 (GAI RMF Kit)
- Use checklist to validate SSDF coverage
- Map workflows to AI RMF Govern practices

### Deliverable 2 (Evaluation Harness)
- Add GenAI safety evaluations to `security.yml`
- Run red-teaming tests on model deployments

### Deliverable 4 (C2PA Provenance)
- Sign model outputs with C2PA manifests
- Link C2PA metadata to SLSA provenance

### Deliverable 5 (ISO 42001)
- Map workflows to ISO 42001 operational controls
- Use SBOMs for AI system documentation

---

## Standards and Frameworks

### NIST Publications
- **NIST SP 800-218A**: SSDF for GenAI
- **NIST AI 600-1**: GenAI Risk Management Framework

### Supply Chain Standards
- **SLSA v1.0**: Supply-chain Levels for Software Artifacts
- **SPDX 2.3**: ISO/IEC 5962:2021 (SBOM standard)
- **CycloneDX 1.5**: OWASP SBOM standard
- **in-toto**: Supply chain security framework

### Tools
- **OpenSSF Scorecard**: Security posture assessment
- **Syft**: SBOM generation (Anchore)
- **Grype**: Vulnerability scanning (Anchore)
- **Cosign**: Artifact signing (Sigstore)
- **CodeQL**: SAST (GitHub)
- **Trivy**: Multi-scanner (Aqua Security)

---

## Compliance and Auditing

### Verification Commands

```bash
# Verify GitHub attestation
gh attestation verify release-v1.0.0.tar.gz --owner your-org

# Verify Cosign signature
cosign verify-blob \
  --bundle release-v1.0.0.tar.gz.bundle \
  --certificate-identity-regexp="^https://github.com/your-org/your-repo.*" \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  release-v1.0.0.tar.gz

# Inspect SLSA provenance
cat provenance.json | jq .predicate.buildDefinition

# Check OpenSSF Scorecard
curl https://api.securityscorecards.dev/projects/github.com/your-org/your-repo
```

### Audit Trail

All workflows create immutable audit records:
- **Workflow logs**: 90-day retention in Actions tab
- **SARIF results**: Permanent in Security tab
- **Attestations**: Permanent, signed, tamper-proof
- **SBOMs**: Attached to releases, 90-day artifact retention

---

## Contributing

To improve these workflows:

1. **Test locally**: Use `act` or validation script
2. **Update documentation**: Reflect changes in SSDF-mapping.md
3. **Pin actions**: Always use commit SHAs, not tags
4. **Add SSDF comments**: Document practice mappings

---

## License

Part of the Responsible GenAI Starter Kit.
Licensed under Apache 2.0 (see root LICENSE file).

---

## References

- **NIST SP 800-218A**: https://csrc.nist.gov/pubs/sp/800/218/a/final
- **OpenSSF Best Practices**: https://bestpractices.coreinfrastructure.org/
- **GitHub Actions Security**: https://docs.github.com/en/actions/security-guides
- **SLSA Framework**: https://slsa.dev/
- **Sigstore Documentation**: https://www.sigstore.dev/

---

**Version**: 1.0
**Last Updated**: 2025-01-XX
**Maintained By**: Responsible GenAI Starter Kit Project
