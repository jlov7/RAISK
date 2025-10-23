# Contributing to Responsible GenAI Starter Kit

Thank you for your interest in contributing! This document provides guidelines for development setup, testing, and contribution workflows.

---

## 🛠️ Development Setup

### Prerequisites

- **Python 3.11+** (for eval harness)
- **Node.js 18+** (for C2PA demo)
- **Git** with commit signing recommended
- **Docker** (optional, for isolated testing)

### Initial Setup

```bash
# Clone and enter the repository
git clone https://github.com/jlov7/responsible-genai-starter-kit.git
cd responsible-genai-starter-kit

# Install Python dependencies (eval harness)
cd deliverables/02-eval-harness
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install Node.js dependencies (C2PA demo)
cd ../04-c2pa-provenance-demo
npm install

# Return to root
cd ../..
```

---

## 🧪 Running Tests

### All Tests

```bash
# From repository root
./scripts/run_all_tests.sh
```

### Per-Deliverable Tests

```bash
# D1: Validate YAML schemas and references
cd deliverables/01-gai-rmf-kit
python scripts/validate_checklists.py

# D2: Run eval harness unit tests
cd ../02-eval-harness
PYTHONHASHSEED=0 pytest tests/

# D2: Run golden eval (determinism check)
# Note: PYTHONHASHSEED=0 ensures deterministic hash ordering for reproducible golden runs
PYTHONHASHSEED=0 python -m eval_harness run --task rag_qa --model local_dummy --limit 50
python scripts/check_thresholds.py --refusal-min 0.98 --pii-max 0

# D4: Test C2PA signing and verification
cd ../04-c2pa-provenance-demo
npm test
```

---

## 🔄 Regenerating Documentation

### Eval Reports

```bash
cd deliverables/02-eval-harness
python -m eval_harness run --task rag_qa --model local_dummy --limit 100
python -m eval_harness report --last-run --format html
# Output: reports/eval_report.html
```

### SBOM Generation (Local)

```bash
# SPDX via Syft
syft dir:. -o spdx-json > sbom-spdx.json

# CycloneDX via cdxgen
cdxgen -t python -o sbom-cyclonedx.json .
```

### Provenance (requires GitHub Actions)

Provenance attestations are generated automatically on release via `.github/workflows/provenance.yml`.

---

## 📝 Contribution Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/d2-add-toxicity-scorer
```

### 2. Make Changes

- Follow existing code style (Black for Python, Prettier for JS/TS)
- Add unit tests for new functionality
- Update relevant documentation

### 3. Run Pre-Commit Checks

```bash
# Python: format and lint
black deliverables/02-eval-harness
ruff check deliverables/02-eval-harness

# Node.js: format and lint
cd deliverables/04-c2pa-provenance-demo
npm run lint
npm run format
```

### 4. Commit with Conventional Commits

```bash
git add .
git commit -m "feat(d2): add toxicity scorer plugin"
```

**Commit prefix conventions:**
- `feat(d1)`: New feature in deliverable 1
- `fix(d3)`: Bug fix in deliverable 3
- `docs`: Documentation updates
- `test`: Test additions or fixes
- `ci`: CI/CD workflow changes
- `chore`: Maintenance tasks

### 5. Push and Create Pull Request

```bash
git push origin feature/d2-add-toxicity-scorer
```

Open a PR on GitHub with:
- **Title**: Clear, concise description
- **Description**: What changed, why, and how to test
- **Linked issues**: Reference any related issues

---

## 🧑‍💻 Code Review Process

1. **Automated checks** must pass (tests, linting, Scorecard)
2. **At least one maintainer approval** required
3. **Squash and merge** preferred for feature branches
4. **Release notes** updated for user-facing changes

---

## 🔒 Security Policy

- Do **not** commit secrets, API keys, or credentials
- Report vulnerabilities via [SECURITY.md](SECURITY.md)
- Use `.env.example` for environment variable templates

---

## 🎯 Quality Standards

All contributions must meet:
- **Test coverage**: New code requires accompanying tests
- **Documentation**: Public APIs and workflows documented
- **Linting**: Pass Black (Python) and Prettier (JS/TS)
- **Eval thresholds**: D2 changes must not regress safety scores

---

## 🌍 Community Guidelines

- Follow the [Code of Conduct](CODE_OF_CONDUCT.md)
- Be respectful and inclusive
- Provide constructive feedback
- Celebrate contributions of all sizes

---

## 📧 Questions?

- Open a [GitHub Discussion](https://github.com/jlov7/responsible-genai-starter-kit/discussions)
- Tag maintainers in issues or PRs
- Check existing [documentation](docs/)

---

Thank you for helping build responsible AI systems! 🙏
