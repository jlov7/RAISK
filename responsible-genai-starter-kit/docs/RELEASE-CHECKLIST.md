# Release Checklist

**Use this checklist before tagging and publishing any release.**

---

## Pre-Release Validation

### 1. Fresh Clone Build Test
```bash
# Clone to a clean directory
cd /tmp
git clone https://github.com/jlov7/responsible-genai-starter-kit.git test-release
cd test-release

# Test D2 eval harness
cd deliverables/02-eval-harness
pip install -e .
PYTHONHASHSEED=0 pytest tests/ -v
# Expected: 37/37 passed

# Test D4 C2PA demo
cd ../04-c2pa-provenance-demo
npm install
npm test
# Expected: All checks pass

cd ../..
```

### 2. Eval Gate Pass (Strict Thresholds)
```bash
# Trigger eval-gate workflow manually
gh workflow run eval-gate.yml

# Or test locally
cd deliverables/02-eval-harness
PYTHONHASHSEED=0 python -m eval_harness.cli run \
  --dataset examples/qa_dataset.csv \
  --scorers exact_match,length \
  --output results/qa_results.json

PYTHONHASHSEED=0 python -m eval_harness.cli run \
  --dataset examples/safety_dataset.jsonl \
  --scorers refusal,pii \
  --output results/safety_results.json

# Verify thresholds met:
# - Refusal rate ≥ 98%
# - PII leakage = 0
# - QA accuracy ≥ 95%
```

### 3. SBOMs Present
```bash
# Verify SBOM generation workflow exists
test -f .github/workflows/sbom.yml && echo "✓ SBOM workflow present"

# Check for dual formats in workflow
grep -q "spdx-json" .github/workflows/sbom.yml && echo "✓ SPDX format"
grep -q "cyclonedx" .github/workflows/sbom.yml && echo "✓ CycloneDX format"
```

### 4. Workflow Validation
```bash
cd deliverables/03-ssdf-genai-ci
./validate-workflows.sh
# Expected: 41/41 checks passed
```

---

## Release Process

### 5. Create GitHub Release (v0.1.0)

```bash
# Tag the release
git tag -a v0.1.0 -m "Initial public release

- 6 deliverables: GAI RMF Kit, Eval Harness, SSDF CI/CD, C2PA Demo, ISO 42001 Bridge, Education Guide
- NIST AI 600-1, SP 800-218A, C2PA v2.2 + CAWG 1.1 aligned
- SLSA L3 provenance, dual SBOMs, OpenSSF Scorecard
- Evaluation quality gates operational
"

git push origin v0.1.0

# Create release via GitHub UI or CLI
gh release create v0.1.0 \
  --title "v0.1.0 - Initial Public Release" \
  --notes-file CHANGELOG.md \
  --verify-tag
```

### 6. Verify Attestations Attach

After release workflow completes:

```bash
# Check release page for attestations
gh release view v0.1.0

# Verify attestation bundle present
gh attestation verify release-v0.1.0.tar.gz --owner jlov7

# Verify SBOM artifact
gh api repos/jlov7/responsible-genai-starter-kit/releases/latest/assets | \
  jq -r '.[].name' | grep -E "(sbom|bom)"
# Expected: sbom-spdx.json, sbom-cyclonedx.json
```

**Required workflow permissions for attestations:**
- Workflow level: `id-token: write`, `attestations: write`
- Job level: Same permissions (do not rely on workflow-level only)

---

## Post-Release

### 7. Mint Zenodo DOI

1. Go to https://zenodo.org/
2. Sign in (use GitHub OAuth)
3. Navigate to "Upload" → "GitHub"
4. Enable repository sync for `responsible-genai-starter-kit`
5. Create new version from v0.1.0 release
6. Copy DOI (format: `10.5281/zenodo.XXXXXXX`)

### 8. Update Repository with DOI

```bash
# Update README.md badge
sed -i.bak 's/zenodo.XXXXXX/zenodo.XXXXXXX/' README.md

# Update CITATION.cff
# Edit the DOI field manually in CITATION.cff

# Commit DOI updates
git add README.md CITATION.cff
git commit -m "docs: add Zenodo DOI for v0.1.0"
git push
```

### 9. Enable GitHub Pages

```bash
# Via GitHub UI: Settings → Pages
# Source: Deploy from branch (main, /docs or root)
# Or via CLI:
gh api repos/jlov7/responsible-genai-starter-kit/pages \
  -X POST \
  -f source[branch]=main \
  -f source[path]=/docs
```

### 10. Scorecard Verification

```bash
# Trigger Scorecard workflow manually
gh workflow run scorecard.yml

# Wait for completion, then check score
gh api repos/jlov7/responsible-genai-starter-kit/code-scanning/alerts \
  --jq '.[] | select(.tool.name == "OpenSSF Scorecard") | .most_recent_instance.state'

# Or check public API (if publish_results: true)
curl https://api.securityscorecards.dev/projects/github.com/jlov7/responsible-genai-starter-kit
```

---

## Release Quality Gates

All of the following must be ✅ before release:

- [ ] Fresh clone builds successfully (D2 + D4)
- [ ] Eval gate passes with strict thresholds
- [ ] SSDF workflow validation: 41/41 checks
- [ ] GitHub Release created with tag v0.1.0
- [ ] Attestations visible on release page
- [ ] SBOMs attached to release (SPDX + CycloneDX)
- [ ] Zenodo DOI minted and badge added
- [ ] CITATION.cff updated with DOI
- [ ] GitHub Pages enabled
- [ ] OpenSSF Scorecard ran successfully

---

## Troubleshooting

### Attestations Not Showing
- Verify workflow has `id-token: write` and `attestations: write` at **both** workflow and job level
- Check Actions logs for attestation API errors
- Ensure `actions/attest-sbom` and `actions/attest-build-provenance` ran

### Eval Gate Failing
- Check `PYTHONHASHSEED=0` is set in workflow
- Verify example datasets exist and are valid
- Confirm threshold values are achievable (may need adjustment for initial release)

### Scorecard Score Low
- Review failed checks in Security tab
- Common issues: branch protection not enabled, dependencies not pinned to SHAs
- Fix issues and re-run workflow

---

**Last Updated**: 2025-10-03
**Version**: v0.1.0 preparation
