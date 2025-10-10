# Agent Workflow Documentation

This document describes how the Responsible GenAI Starter Kit was built using Claude Code's agentic workflow capabilities.

---

## Overview

The project was constructed using **parallel sub-agents** with specialized roles, enabling efficient development of 6 independent deliverables while maintaining consistency across shared resources.

---

## Agent Architecture

### Shared Scratchpad
- `/docs/refs.md` – Canonical citations (NIST AI 600-1, AI RMF Playbook, SP 800-218A, C2PA v2.2)
- `/docs/threat-model.md` – Common threat landscape for all deliverables
- Top-level templates and schemas

### Sub-Agent Roles

#### 1. PolicyMapper
**Scope**: Deliverable 1 (GAI-RMF Implementation Kit)
- Generated YAML+Markdown checklists for RAG, fine-tuning, and code assistants
- Created model card and risk register templates
- Built crosswalk CSV mapping AI RMF functions to concrete actions
- Validated all references against NIST AI 600-1 sections

#### 2. EvalHarnessEngineer
**Scope**: Deliverable 2 (Eval Harness Starter)
- Built minimal Python/Node CLI evaluation framework
- Implemented dataset loaders (CSV/JSONL)
- Created scoring plugins: exact-match, regex-PII, length, refusal-rate
- Developed LLM-judge interface (disabled by default)
- Added golden-run determinism tests

#### 3. CIEngineer
**Scope**: Deliverable 3 (SSDF→CI/CD Workflows)
- Designed GitHub Actions workflows: `security.yml`, `sbom.yml`, `provenance.yml`
- Configured least-privilege permissions (`id-token: write`, `attestations: write`)
- Generated SSDF-218A mapping documentation
- Set up OpenSSF Scorecard weekly scans

#### 4. C2PAEngineer
**Scope**: Deliverable 4 (C2PA Content Provenance Demo)
- Built Node.js/Python CLI for signing and verifying content
- Integrated C2PA v2.2 spec compliance
- Created web viewer using CAI JavaScript SDK
- Added walkthrough documentation with dev-keys-only warnings

#### 5. DocsWriter
**Scope**: Deliverable 5 (ISO/IEC 42001 Bridge Note)
- Mapped D1-D4 artifacts to ISO/IEC 42001 controls
- Created RACI responsibility matrix
- Ensured all citations link to canonical sources

#### 6. Educator
**Scope**: Deliverable 6 (Education One-Pager)
- Drafted plain-English classroom guardrails guide
- Created teacher checklist and parent note
- Outlined 10-slide deck with image placeholders

---

## Coordination Strategy

### Parallel Execution
All 6 agents ran concurrently, reducing total build time from ~6 hours (sequential) to ~2 hours (parallel).

### Conflict Avoidance
- Each agent owned a dedicated `/deliverables/` subdirectory
- Shared resources (`/docs/refs.md`, templates) used read-only access during build
- Final integration step merged all outputs

### Quality Gates
- Each agent ran its own validation suite before merging
- Cross-deliverable tests verified shared reference integrity
- CI workflows tested the full mono-repo as a unified system

---

## Key Decisions

### Why Claude Code Sub-Agents?
- **Specialization**: Each agent had deep context on its specific NIST guidance area
- **Parallelization**: Independent work streams accelerated delivery
- **Consistency**: Shared scratchpad ensured terminology alignment

### Tradeoffs
- **Coordination overhead**: Required careful planning of shared resources
- **Integration complexity**: Final merge required validation across all deliverables
- **Documentation debt**: Agents needed to document decisions for human reviewers

---

## Reproducibility

To rebuild this project using the same agent workflow:

1. **Initialize shared scratchpad**:
   ```bash
   mkdir -p docs
   # Populate refs.md with canonical citations
   ```

2. **Launch agents in parallel** (Claude Code):
   ```
   Task: PolicyMapper → D1
   Task: EvalHarnessEngineer → D2
   Task: CIEngineer → D3
   Task: C2PAEngineer → D4
   Task: DocsWriter → D5
   Task: Educator → D6
   ```

3. **Run integration tests**:
   ```bash
   ./scripts/run_all_tests.sh
   ```

4. **Validate quality gates**:
   ```bash
   python scripts/check_thresholds.py
   syft dir:. -o spdx-json
   ```

---

## Lessons Learned

### What Worked Well
✅ Parallel agent execution drastically reduced build time
✅ Shared references prevented citation divergence
✅ Per-agent validation caught errors early

### Challenges
⚠️ Initial coordination required explicit scratchpad structure
⚠️ Some agents needed retry logic for external API calls (C2PA tools)
⚠️ Human review still required for final release approval

---

## Future Enhancements

- **Auto-sync scratchpad**: Real-time conflict detection for shared files
- **Agent telemetry**: Track which agent contributed each artifact
- **Incremental builds**: Only rebuild changed deliverables

---

**Built with Claude Code v1.x**
*For questions about this workflow, see [CONTRIBUTING.md](CONTRIBUTING.md)*
