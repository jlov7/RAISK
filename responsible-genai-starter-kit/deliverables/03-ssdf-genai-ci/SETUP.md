# Setup Guide: SSDF CI/CD Workflows for GenAI

This guide explains how to enable and configure the NIST SSDF-compliant GitHub Actions workflows in your GenAI repository.

---

## Prerequisites

- **GitHub Repository**: Public or private repository with Actions enabled
- **Admin Access**: Required for enabling Security features and branch protection
- **GitHub CLI**: Optional but recommended for attestation verification

---

## Quick Start

### 1. Copy Workflows to Your Repository

Copy the workflow files to your repository's `.github/workflows/` directory:

```bash
# From the root of your repository
mkdir -p .github/workflows

# Copy all workflow files
cp deliverables/03-ssdf-genai-ci/workflows/*.yml .github/workflows/

# Copy SBOM configuration
cp deliverables/03-ssdf-genai-ci/.syft.yaml .
```

### 2. Commit and Push

```bash
git add .github/workflows/ .syft.yaml
git commit -m "Add SSDF-compliant CI/CD workflows"
git push origin main
```

The workflows will automatically trigger based on their defined events (push, pull request, schedule, etc.).

---

## Repository Configuration

### Enable Security Features

#### 1. Enable Code Scanning (Required for SARIF uploads)

1. Navigate to **Settings** → **Code security and analysis**
2. Enable **CodeQL analysis**
3. Enable **Secret scanning**
4. Enable **Dependency graph**
5. Enable **Dependabot alerts**

#### 2. Enable GitHub Advanced Security (Private Repos)

For private repositories, you need GitHub Advanced Security:
- Contact your GitHub organization admin
- Enable GHAS for your repository
- This unlocks CodeQL, secret scanning, and dependency review

#### 3. Configure Branch Protection

Protect your `main` branch per OpenSSF Scorecard requirements:

1. Go to **Settings** → **Branches** → **Branch protection rules**
2. Add rule for `main`:
   - ✅ Require pull request before merging
   - ✅ Require status checks to pass (select: `Security Scanning`, `SBOM Generation`)
   - ✅ Require conversation resolution before merging
   - ✅ Require signed commits (optional but recommended)
   - ✅ Include administrators (enforce for all)

---

## Workflow-Specific Configuration

### Security Scanning (`security.yml`)

**No additional configuration required.** Runs automatically on:
- Push to `main` or `develop`
- Pull requests
- Weekly schedule (Mondays at 9 AM UTC)

**Optional: Customize Language Matrix**

If your project uses languages other than Python/JavaScript, edit `security.yml`:

```yaml
strategy:
  matrix:
    language: [python, javascript, java, go, csharp]
```

**Optional: Custom CodeQL Queries**

Create `.github/codeql/codeql-config.yml`:

```yaml
name: "Custom CodeQL Config"
queries:
  - uses: security-extended
  - uses: security-and-quality

# Add custom queries for GenAI-specific checks
query-filters:
  - exclude:
      id: py/clear-text-storage-sensitive-data  # If intentional for demos
```

---

### SBOM Generation (`sbom.yml`)

**Required Permissions:**
- `contents: write` (for uploading to releases)
- `id-token: write` (for Sigstore signing)
- `attestations: write` (for GitHub attestations)

**Configuration:**

1. **Customize `.syft.yaml`** (optional):
   - Add exclusions for test directories
   - Configure license detection preferences
   - Enable/disable specific package catalogers

2. **License Policy** (optional):
   Edit `sbom.yml` to customize denied licenses:
   ```yaml
   deny-licenses: GPL-2.0, GPL-3.0, AGPL-3.0, SSPL-1.0, CC-BY-NC-4.0
   ```

3. **Trigger on Releases**:
   - SBOM is automatically generated on tags matching `v*` (e.g., `v1.0.0`)
   - To generate manually: **Actions** → **SBOM Generation** → **Run workflow**

---

### Build Provenance (`provenance.yml`)

**Required Permissions:**
- `id-token: write` (for keyless Sigstore signing)
- `attestations: write` (for GitHub attestations)
- `contents: read`

**Configuration:**

1. **Customize Build Steps**:
   Edit the `Build application` step to match your build process:

   ```yaml
   - name: Build application
     run: |
       # Python example
       pip install build
       python -m build

       # Node.js example
       npm ci
       npm run build

       # Go example
       go build -o myapp

       # Docker example
       docker build -t myimage:latest .
   ```

2. **Artifact Naming**:
   Update the `artifact_name` output to match your build artifacts.

3. **Verification**:
   After release, verify attestations:
   ```bash
   gh attestation verify release-v1.0.0.tar.gz --owner your-org
   ```

---

### OpenSSF Scorecard (`scorecard.yml`)

**Required Permissions:**
- `security-events: write`
- `contents: read`
- `actions: read`

**Configuration:**

1. **Publishing to OpenSSF API** (Public Repos):
   Edit `scorecard.yml`:
   ```yaml
   with:
     publish_results: true  # Change to true for public repos
   ```

2. **Badge Generation**:
   Add to your README.md:
   ```markdown
   [![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/your-org/your-repo/badge)](https://api.securityscorecards.dev/projects/github.com/your-org/your-repo)
   ```

3. **Issue Creation**:
   The workflow automatically creates GitHub Issues for failed checks.
   - Label: `security`, `openssf-scorecard`
   - Assignees: Configure in `scorecard.yml` if desired

---

## Required Secrets

### No Secrets Required!

All workflows use **keyless signing** with GitHub OIDC tokens. You do not need to:
- Generate GPG keys
- Store signing keys in secrets
- Manage key rotation

The workflows authenticate using GitHub's built-in identity system.

### Optional Secrets

If integrating with external services:

- **SLACK_WEBHOOK**: For security scan notifications
- **PAGERDUTY_TOKEN**: For critical vulnerability alerts
- **SONARCLOUD_TOKEN**: For additional SAST integration

Add these in **Settings** → **Secrets and variables** → **Actions**.

---

## Validation and Testing

### 1. Validate Workflow Syntax

Run the included validation script:

```bash
cd deliverables/03-ssdf-genai-ci
./validate-workflows.sh
```

This checks:
- YAML syntax validity
- Action version pinning
- Required permissions
- SSDF practice annotations

### 2. Test Workflows Locally

Use [act](https://github.com/nektos/act) to test workflows locally:

```bash
# Install act
brew install act  # macOS
# or: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Test security workflow
act push --workflows .github/workflows/security.yml

# Test SBOM generation
act push --workflows .github/workflows/sbom.yml --eventpath test-event.json
```

### 3. Trigger Test Runs

1. Go to **Actions** tab in GitHub
2. Select a workflow (e.g., "Security Scanning")
3. Click **Run workflow**
4. Monitor execution and review results

---

## Monitoring and Maintenance

### Viewing Security Results

1. **Security Tab**:
   - Navigate to **Security** → **Code scanning**
   - View all SARIF results (CodeQL, Trivy, Scorecard)
   - Filter by severity, tool, date range

2. **Dependency Graph**:
   - Navigate to **Insights** → **Dependency graph**
   - Review Dependabot alerts
   - View SBOMs attached to releases

3. **Actions Logs**:
   - Navigate to **Actions** tab
   - Click on workflow runs to view detailed logs
   - Download artifacts (scan reports, SBOMs, attestations)

### Weekly Review Checklist

- [ ] Review OpenSSF Scorecard results (Mondays)
- [ ] Triage new security alerts (Security tab)
- [ ] Update dependencies flagged by Dependabot
- [ ] Close resolved security issues
- [ ] Verify SBOMs attached to recent releases

---

## Troubleshooting

### Common Issues

#### 1. "Resource not accessible by integration"

**Cause**: Insufficient workflow permissions

**Solution**: Add required permissions to workflow file:
```yaml
permissions:
  contents: read
  security-events: write
  attestations: write
```

#### 2. CodeQL analysis fails with "language not found"

**Cause**: Language detection failed

**Solution**: Explicitly specify languages in workflow:
```yaml
strategy:
  matrix:
    language: [python]  # Explicitly list your languages
```

#### 3. Sigstore signing fails

**Cause**: `id-token: write` permission missing

**Solution**: Ensure workflow has:
```yaml
permissions:
  id-token: write
```

#### 4. SARIF upload blocked

**Cause**: Code scanning not enabled (private repos without GHAS)

**Solution**:
- Enable GitHub Advanced Security (if available)
- Or: Remove `upload-sarif` steps and use artifacts instead

#### 5. OpenSSF Scorecard score is low

**Cause**: Missing security best practices

**Solution**: Address issues listed in workflow summary:
- Enable branch protection
- Pin all action versions to commit SHAs
- Add SECURITY.md file
- Enable Dependabot
- Require code review for PRs

---

## Customization Examples

### Add Slack Notifications

Add this step to `security.yml`:

```yaml
- name: Notify Slack on failures
  if: failure()
  uses: slackapi/slack-github-action@70cd7be8e40a46e8b0eced40b0de447bdb42f68e  # v1.26.0
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK }}
    payload: |
      {
        "text": "Security scan failed in ${{ github.repository }}"
      }
```

### Add Docker Image Scanning

Add to `security.yml`:

```yaml
- name: Build Docker image
  run: docker build -t myapp:latest .

- name: Scan Docker image with Trivy
  uses: aquasecurity/trivy-action@5681af892cd0e5103d2a70678d27b314b7cef0c3
  with:
    image-ref: myapp:latest
    format: sarif
    output: trivy-docker-results.sarif

- name: Upload Docker scan results
  uses: github/codeql-action/upload-sarif@f09c1c0a94de965c15400f5634aa42fac8fb8f88
  with:
    sarif_file: trivy-docker-results.sarif
```

### Add Model File Scanning

For GenAI projects with model files:

```yaml
- name: Scan model files for malware
  run: |
    # Use ClamAV or ModelScan
    pip install modelscan
    modelscan scan models/ --format json --output model-scan.json

- name: Upload model scan results
  uses: actions/upload-artifact@b4b15b8c7c6ac21ea08fcf65892d2ee8f75cf882
  with:
    name: model-scan-results
    path: model-scan.json
```

---

## Integration with Deliverable 2 (Evaluation Harness)

To integrate with the AI Red-Teaming evaluation harness:

```yaml
# Add to security.yml
- name: Run GenAI safety evaluations
  run: |
    python -m eval_harness.run_evals \
      --model ${{ env.MODEL_PATH }} \
      --tests toxicity,fairness,privacy \
      --output eval-results.json

- name: Upload evaluation results
  uses: actions/upload-artifact@b4b15b8c7c6ac21ea08fcf65892d2ee8f75cf882
  with:
    name: genai-eval-results
    path: eval-results.json
```

---

## Compliance Checklist

Use this checklist to verify SSDF compliance:

### Prepare the Organization (PO)
- [ ] Security policies documented (SECURITY.md)
- [ ] OpenSSF Scorecard enabled
- [ ] Team trained on workflow usage

### Protect the Software (PS)
- [ ] Branch protection enabled
- [ ] Secret scanning enabled
- [ ] SBOMs generated for all releases
- [ ] Provenance attestations signed

### Produce Well-Secured Software (PW)
- [ ] SAST enabled (CodeQL)
- [ ] Dependency scanning enabled (Trivy, pip-audit)
- [ ] SBOMs include all components
- [ ] Build environment hardened (GitHub-hosted runners)

### Respond to Vulnerabilities (RV)
- [ ] Weekly vulnerability scans scheduled
- [ ] Security alerts monitored
- [ ] Remediation tracked via GitHub Issues

---

## Additional Resources

### Documentation
- [GitHub Actions Security Hardening](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [Using Artifact Attestations](https://docs.github.com/en/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds)
- [NIST SSDF Implementation Guide](https://csrc.nist.gov/pubs/sp/800/218/a/final)

### Tools
- [GitHub CLI](https://cli.github.com/): Verify attestations
- [Syft](https://github.com/anchore/syft): SBOM generation
- [Cosign](https://github.com/sigstore/cosign): Signature verification
- [act](https://github.com/nektos/act): Local workflow testing

### Community
- [OpenSSF Best Practices Badge](https://bestpractices.coreinfrastructure.org/)
- [SLSA Community](https://slsa.dev/)
- [Sigstore Project](https://www.sigstore.dev/)

---

## Support

If you encounter issues or have questions:

1. **Check Workflow Logs**: Actions tab → Select run → View logs
2. **Review SSDF-mapping.md**: Detailed practice implementation notes
3. **Open GitHub Issue**: Tag with `ci-cd`, `ssdf`, `security`
4. **Consult NIST SP 800-218A**: https://csrc.nist.gov/pubs/sp/800/218/a/final

---

**Version**: 1.0
**Last Updated**: 2025-01-XX
**Maintained By**: Responsible GenAI Starter Kit Project
