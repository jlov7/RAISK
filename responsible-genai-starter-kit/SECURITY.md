# Security Policy

## Reporting Security Vulnerabilities

We take security seriously. If you discover a security vulnerability in this project, please report it responsibly.

### Reporting Process

**DO NOT** open a public GitHub issue for security vulnerabilities.

Instead, please report security issues via:
- **Email**: security@yourdomain.com
- **GitHub Security Advisories**: Use the "Security" tab in this repository

### What to Include

Please provide:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

### Response Timeline

- **Initial response**: Within 48 hours
- **Status update**: Within 7 days
- **Fix timeline**: Depends on severity (critical issues prioritized)

---

## Scope

### In Scope

- Vulnerabilities in code, scripts, or workflows
- Supply chain security issues (dependencies, SBOM)
- CI/CD security misconfigurations
- Evaluation harness bypass or manipulation
- C2PA signature forgery or verification bypass

### Out of Scope

- Issues in third-party dependencies (report to upstream)
- Theoretical attacks without proof of concept
- Social engineering attacks
- Denial of service from rate limiting

---

## Security Practices

This project follows:
- **NIST SP 800-218A** (Secure Software Development Framework for GenAI)
- **OpenSSF Scorecard** best practices
- **SLSA Level 3** provenance for releases
- **Automated security scanning** (CodeQL, dependency updates)

---

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

---

Thank you for helping keep this project secure.
