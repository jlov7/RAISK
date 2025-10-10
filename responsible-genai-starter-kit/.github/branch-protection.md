# Branch Protection Configuration

This document describes the recommended branch protection rules for this repository.

## Recommended Settings for `main` Branch

Navigate to: **Settings → Branches → Branch protection rules**

### Protect matching branches
- Branch name pattern: `main`

### Rule Settings

#### Require a pull request before merging
- ✅ Require approvals: **1**
- ✅ Dismiss stale pull request approvals when new commits are pushed
- ✅ Require review from Code Owners

#### Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- Required status checks:
  - `test` (from `.github/workflows/test.yml`)
  - `eval` (from `.github/workflows/eval.yml`)
  - `security` (from `.github/workflows/security.yml`)
  - `sbom` (from `.github/workflows/sbom.yml`)

#### Require conversation resolution before merging
- ✅ Enabled

#### Require signed commits
- ✅ Enabled (recommended for supply chain security)

#### Require linear history
- ✅ Enabled (enforces squash or rebase merges)

#### Do not allow bypassing the above settings
- ✅ Enabled
- Exception: Allow administrators to bypass (for emergency fixes only)

---

## Additional Recommendations

### Repository Settings

#### General
- ✅ Disable merge commits (use squash or rebase only)
- ✅ Automatically delete head branches after merge

#### Security
- ✅ Enable Dependabot alerts
- ✅ Enable Dependabot security updates
- ✅ Enable secret scanning
- ✅ Enable push protection for secrets

#### Actions
- ✅ Require approval for first-time contributors
- ✅ Restrict workflow permissions to read-only by default

---

## Enforcement

These settings help achieve:
- **NIST SP 800-218A** Task PW.1.2: Review code changes
- **OpenSSF Scorecard** Branch-Protection check
- **SLSA Level 3** requirements for source integrity
