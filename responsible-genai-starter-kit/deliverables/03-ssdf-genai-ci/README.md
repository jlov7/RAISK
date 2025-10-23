# D3 — SSDF→CI/CD Workflows for GenAI

Hardened GitHub Actions workflows that operationalize NIST SP 800-218A and OpenSSF best practices for generative AI projects. Designed as part of the Responsible GenAI Starter Kit research effort; production-quality by default, but expect to tailor for your repositories.

---

## Module Snapshot

- **Workflows included:** `security.yml`, `sbom.yml`, `provenance.yml`, `scorecard.yml`
- **Practices covered:** Code scanning, dependency scanning, SBOM generation, provenance signing, OpenSSF Scorecard, license compliance, secret detection
- **Key attributes:** Pinned action SHAs, least-privilege permissions, scheduled jobs, manual triggers, attestation support
- **Supporting files:** `.syft.yaml`, `SETUP.md`, `SSDF-mapping.md`, `validate-workflows.sh`

---

## Quick Start

1. **Copy workflows into your repository:**
   ```bash
   mkdir -p .github/workflows
   cp deliverables/03-ssdf-genai-ci/workflows/*.yml .github/workflows/
   cp deliverables/03-ssdf-genai-ci/.syft.yaml .
   ```

2. **Review [SETUP.md](SETUP.md)** to enable GitHub security features, branch protection, and required permissions.

3. **Run the validator:**
   ```bash
   cd deliverables/03-ssdf-genai-ci
   ./validate-workflows.sh
   ```

4. **Commit and push:**
   ```bash
   git add .github/workflows .syft.yaml
   git commit -m "Add SSDF-aligned security workflows"
   git push
   ```

5. **Monitor runs** under GitHub Actions → Workflows. Address warnings surfaced in job summaries.

---

## Workflow Overview

| Workflow | Trigger Highlights | What it Does | SSDF Practices |
|----------|-------------------|--------------|----------------|
| `security.yml` | Push/PR to `main` & `develop`, weekly schedule, manual | CodeQL SAST, pip-audit, npm audit, Trivy, Gitleaks, GenAI secret scan, license reports | PS.1.1, PS.2.1, PW.4.1, PW.4.4, PW.6.1, PW.7.1 |
| `sbom.yml` | Push to `main`, release tags, published releases, manual | Generates SPDX & CycloneDX SBOMs, signs with Cosign, uploads artifacts, scans with Grype | PW.4.1, PW.4.2, PS.3.1, PS.3.2 |
| `provenance.yml` | Release tags, manual | Builds artifacts, records SLSA v1.0 Level 3 provenance, signs with Sigstore, uploads attestations | PS.3.1, PS.3.2, PW.1.3, PW.4.1 |
| `scorecard.yml` | Weekly schedule, push to `main`, manual | Runs OpenSSF Scorecard with SARIF output, publishes results | PO.3.1, PO.3.2, PS.1.1, PW.1.1 |

Each file includes inline SSDF practice comments for traceability.

---

## Validation Script (`validate-workflows.sh`)

Run this script before committing changes. It checks:

- YAML syntax (via `yq` or Python + PyYAML fallback)
- Action pinning (disallows `@vX` tags)
- Permissions blocks (warns on missing or overly broad scopes)
- Presence of SSDF references
- Timeouts, secret checks, cron triggers
- SBOM/provenance attestation wiring
- Required documentation files (`SETUP.md`, `SSDF-mapping.md`, `.syft.yaml`)

> Tip: Install `yq` (`brew install yq`) for faster validation runs. Otherwise the script falls back to Python.

---

## Customization Guide

1. **Languages:** Update CodeQL matrix in `security.yml` to match your codebase.
2. **Dependency managers:** Add or remove package scan steps (e.g., `poetry`, `gradle`, `cargo`).
3. **Severity thresholds:** Adjust `Trivy` and `Grype` severity filters to match risk appetite.
4. **SBOM formats:** Modify `.syft.yaml` or Syft action parameters to include XML or multi-layer scans.
5. **Artifact names:** Align output file names to your release conventions to simplify provenance verification.
6. **Notifications:** Integrate with Slack/Teams or issue trackers by adding final steps to workflows.

Keep action SHAs pinned—update them intentionally and document the change in `CHANGELOG.md`.

---

## Integration with Other Deliverables

- **D1 (GAI RMF Kit):** Several controls reference CodeQL, SBOMs, and provenance; link workflow runs as evidence.
- **D2 (Evaluation Harness):** Add an “evaluation” job or reuse the harness in `security.yml` to block unsafe responses.
- **D4 (C2PA Demo):** Publish signed content along with SBOMs for transparency.
- **D5 (ISO 42001 Bridge):** Use `SSDF-mapping.md` alongside the ISO crosswalk to demonstrate secure development coverage.

---

## Observability & Outputs

- SARIF results appear in the repository’s **Security** tab (CodeQL, Trivy, Scorecard).
- SBOMs (`sbom-spdx.json`, `sbom-cyclonedx.json`) and provenance bundles are uploaded as release assets.
- Workflow summaries include SSDF practice lists and job status tables for executive reporting.
- Attestation bundles can be verified with `gh attestation verify` and `slsa-verifier`.

---

## Frequently Asked Questions

**Do I need GitHub Advanced Security?**  
Required for private repositories to run CodeQL and secret scanning. Public repositories can run these workflows for free.

**Why are actions pinned to SHAs?**  
Mitigates supply-chain attacks via malicious updates. Update pins periodically and document approvals.

**Can I run these locally?**  
Yes—use [`act`](https://github.com/nektos/act) for local testing, or run individual commands (CodeQL, Syft, Cosign) manually following the steps in each job.

**How do I add evaluation gates?**  
Insert an additional job in `security.yml` that runs the D2 harness and add it to `needs` for the summary job.

---

## Licensing

- Workflow definitions and scripts: Apache-2.0
- Documentation (`SETUP.md`, `SSDF-mapping.md`): CC-BY-4.0

Attribution helps others trace the provenance of these best practices when you publish your own fork.
