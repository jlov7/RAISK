# DO THIS NEXT

**Focused checklist to finish and start using this work immediately.**

Last Updated: 2025-10-03 (post-crash rebuild + refinement)

---

## A. Cut Clean Public Release (v0.1.0)

### 1. Test eval gate with strict thresholds
```bash
# Clone to fresh directory
cd /tmp && git clone <your-repo> test-release && cd test-release

# Run eval harness
cd deliverables/02-eval-harness
pip install -e .
PYTHONHASHSEED=0 python -m eval_harness.cli run \
  --dataset examples/safety_dataset.jsonl \
  --scorers refusal,pii \
  --output results/safety_results.json

# Verify thresholds:
# - Refusal ≥ 98% (should pass)
# - PII leakage = 0 (should pass)

# To test that gate BLOCKS on failure, temporarily lower a threshold
# in .github/workflows/eval-gate.yml and confirm workflow fails
```

### 2. Create GitHub Release v0.1.0
```bash
cd <your-main-repo>

# Tag release
git tag -a v0.1.0 -m "Initial public release

- 6 deliverables (GAI RMF, Eval Harness, SSDF CI/CD, C2PA+CAWG, ISO 42001, Education)
- NIST AI 600-1, SP 800-218A, C2PA v2.2 + CAWG 1.1 aligned
- SLSA L3 provenance, dual SBOMs, OpenSSF Scorecard
- Evaluation quality gates operational
- CAWG training-mining assertions (DIF-ratified May 2025)
"

git push origin v0.1.0

# Create release
gh release create v0.1.0 \
  --title "v0.1.0 - Initial Public Release" \
  --notes-file CHANGELOG.md \
  --verify-tag
```

### 3. Verify attestations attach to release
```bash
# Wait for workflows to complete (~5-10 min)

# Check release page
gh release view v0.1.0

# Verify attestation
gh attestation verify <artifact>.tar.gz --owner <your-username>

# Verify SBOM artifacts present
gh api repos/<owner>/<repo>/releases/latest/assets | \
  jq -r '.[].name' | grep -E "(sbom|bom)"

# Expected: sbom-spdx.json, sbom-cyclonedx.json
```

**⚠️ Troubleshooting**: If attestations don't show:
- Check workflow has `id-token: write` and `attestations: write` at BOTH workflow and job level
- Review Actions logs for attestation API errors

### 4. Mint Zenodo DOI
```bash
# 1. Go to https://zenodo.org/ and sign in with GitHub
# 2. Navigate to Upload → GitHub
# 3. Enable sync for your repository
# 4. Create new version from v0.1.0 release
# 5. Copy DOI (format: 10.5281/zenodo.XXXXXXX)

# Update README.md badge
sed -i.bak 's/zenodo.XXXXXX/zenodo.<YOUR-DOI>/' README.md

# Update CITATION.cff
# (Edit DOI field manually)

# Commit
git add README.md CITATION.cff
git commit -m "docs: add Zenodo DOI for v0.1.0"
git push
```

---

## B. Lock Down Supply-Chain Settings (One-Time)

### 1. Verify Scorecard permissions
```bash
# Check .github/workflows/scorecard.yml has:
grep -A 5 "permissions:" .github/workflows/scorecard.yml

# Required when publish_results: true:
#   security-events: write
#   id-token: write
#   contents: read
#   actions: read
```

**Status**: ✅ Already correct in your workflows

### 2. Pin actions to commit SHAs
```bash
# Find any @vX.Y.Z pins
grep -r "@v[0-9]" .github/workflows/

# Replace with full commit SHAs per GitHub security guidance
# Example: actions/checkout@v4 → actions/checkout@eef61447b9ff4aafe5dcd4e0bbf5d482be7e7871
```

**Status**: ✅ Already pinned in your workflows

---

## C. Publish Starter Artifacts

### 1. Enable GitHub Pages
```bash
# Via GitHub UI:
# Settings → Pages → Source: Deploy from branch (main, /docs)

# Or via CLI:
gh api repos/<owner>/<repo>/pages -X POST \
  -f source[branch]=main -f source[path]=/docs

# Your public URL will be: https://<owner>.github.io/<repo>/
```

### 2. Add screenshots to docs/
```bash
mkdir -p docs/screenshots

# Add:
# - eval-gate-results.png (workflow summary with thresholds)
# - c2pa-verify-output.png (web viewer showing CAWG assertion)
# - attestation-release-page.png (GitHub release with attestation badge)

git add docs/screenshots/
git commit -m "docs: add screenshots for demos"
```

### 3. Verify canonical citations
```bash
# Check docs/refs.md includes:
grep -E "NIST AI 600-1|SP 800-218A|C2PA v2.2|CAWG" docs/refs.md
```

**Status**: ✅ Added CAWG 1.1 references (May 2025, DIF-ratified)

---

## D. Make It Visible (Low-Noise)

### 1. Write short OSF/SSRN preprint (6-10 pages)
**Title**: "Operationalizing NIST AI 600-1 for Enterprise GenAI Systems"

**Structure**:
1. **Abstract** (150 words): NIST AI 600-1 compliance challenge, your solution
2. **Introduction** (1 page): GenAI risks, regulatory landscape (NIST, EU AI Act)
3. **Methods** (2 pages): 6 deliverables, SSDF mapping, eval gates, SLSA provenance
4. **Results** (2 pages): Validation (37/37 tests, 41/41 workflow checks), CAWG assertion compliance
5. **Discussion** (1 page): Adoption pathway, UT/TACC use case, ISO 42001 bridge
6. **Conclusion** (0.5 page): GitHub link, DOI, contribution statement

**Upload to**:
- **SSRN**: https://www.ssrn.com/en/ (business/policy audience)
- **OSF Preprints**: https://osf.io/preprints/ (research audience)
- **arXiv** (if eligible): https://arxiv.org/

**Timeline**: Draft in 2-3 days, publish within 1 week

**Impact**: Single highest-leverage credibility boost for UT/TACC intros

### 2. Create impact.md tracking file
```bash
cat > docs/impact.md << 'EOF'
# Project Impact Tracking

*Evidence for O-1/NIW applications*

## Repository Metrics
- **Stars**: 0 (as of 2025-10-03)
- **Forks**: 0
- **Release DOI**: 10.5281/zenodo.XXXXXXX
- **GitHub Pages**: https://<owner>.github.io/<repo>/

## Citations & References
- [ ] SSRN preprint published (date: _____)
- [ ] OSF preprint published (date: _____)
- [ ] First external citation (date: _____)

## Presentations & Invites
- [ ] UT seminar (date: _____, title: _____)
- [ ] TACC training session (date: _____, title: _____)
- [ ] Conference presentation (name: _____, date: _____)

## Adoption Evidence
- [ ] First production deployment (org: _____, date: _____)
- [ ] GitHub Issue from external user (date: _____)
- [ ] External contribution PR (date: _____)

## Media & Recognition
- [ ] Blog post / article mention (source: _____, date: _____)
- [ ] LinkedIn post engagement (impressions: _____, date: _____)
- [ ] Newsletter feature (publication: _____, date: _____)

---
Last updated: 2025-10-03
EOF

git add docs/impact.md
git commit -m "docs: add impact tracking for O-1/NIW evidence"
```

---

## E. Flip UT/TACC On-Ramp Switch

### 1. Pick 2 events in next month
**Targets**:
- **1 seminar**: UT CS, TACC Friday Forum, Cockrell School AI seminar
- **1 training**: TACC Introduction to AI on HPC, UT Data Science Institute workshop

**Find events**:
```bash
# TACC calendar: https://www.tacc.utexas.edu/events
# UT CS seminars: https://www.cs.utexas.edu/events
```

### 2. Prepare 15-20 min mini-demo
**Structure**:
1. **Problem** (2 min): GenAI adoption without guardrails → NIST AI 600-1 complexity
2. **Solution** (3 min): 6 deliverables overview (show GitHub Pages)
3. **Demo 1** (5 min): Eval gate workflow blocking bad release (show GitHub Actions UI)
4. **Demo 2** (5 min): C2PA verify with CAWG training-mining assertion (show web viewer)
5. **Impact** (3 min): SLSA L3 provenance, ISO 42001 mapping, UT/TACC use case
6. **Q&A** (5 min)

**Key artifacts to show**:
- GitHub release page with attestations
- Eval gate workflow failure → fix → success
- C2PA web viewer showing `cawg.training-mining` assertion
- ISO 42001 mapping table

**Pitch-free approach**: "Here's what I built. Thought it might be useful for [HPC GenAI / research computing / compliance teams]."

### 3. Bring laptop + backup slides
- **Laptop**: Live demo from GitHub (Pages, Actions, Release page)
- **Backup**: PDF with screenshots in case wifi fails

---

## Summary Checklist

Before tagging yourself "done" with this phase:

- [ ] v0.1.0 release created with attestations attached
- [ ] Eval gate tested (passes with strict thresholds, blocks on failure)
- [ ] Zenodo DOI minted and badges updated
- [ ] GitHub Pages enabled
- [ ] Scorecard ran successfully (check Security tab)
- [ ] CAWG training-mining labels verified in D4 examples
- [ ] OSF/SSRN preprint drafted
- [ ] impact.md tracking file created
- [ ] 2 UT/TACC events identified and registered
- [ ] 15-min demo prepared and rehearsed

---

## Next Phase (After v0.1.0 Launch)

**Week 1-2**:
- Attend 1st event (seminar) with demo
- Publish preprint
- Monitor GitHub stars/forks

**Week 3-4**:
- Attend 2nd event (TACC training)
- Follow up with interested faculty/staff
- Update impact.md with engagement metrics

**Month 2**:
- First UT collaboration discussion
- External validation (user issue, PR, or citation)
- Consider next enhancements (Docker demo, advanced eval scorers, case study)

---

**Confidence Level**: After CAWG label fix + v0.1.0 release, you're good. Everything else is optional polish.

**Time Estimate**: A–C can be done in 1 focused day. D takes 3-5 days. E happens over 4 weeks.
