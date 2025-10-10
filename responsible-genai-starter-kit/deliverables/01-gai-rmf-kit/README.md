# D1: GAI-RMF Implementation Kit

Production-ready checklists and templates for implementing NIST AI 600-1 (Generative AI Profile) controls.

---

## Contents

### Checklists
1. [**RAG Applications**](checklists/rag.yaml) – Retrieval-Augmented Generation systems
2. [**Fine-Tuning & LoRA**](checklists/fine-tune.yaml) – Custom model training workflows
3. [**Code Assistants**](checklists/code-assistant.yaml) – AI-powered development tools in enterprise environments

### Templates
- [**Model Card**](templates/model-card.md) – Structured documentation for AI models
- [**Risk Register**](templates/risk-register.csv) – Track and prioritize AI risks

### Cross-Reference
- [**Crosswalk**](crosswalk.csv) – Map AI RMF functions to concrete actions and artifacts

---

## Usage

### 1. Select Your Pattern

Choose the checklist matching your use case:
- Building a Q&A bot with retrieval? → `rag.yaml`
- Fine-tuning a model on proprietary data? → `fine-tune.yaml`
- Deploying GitHub Copilot in your org? → `code-assistant.yaml`

### 2. Review Checklist Items

Each checklist contains:
- **control_id**: Unique identifier (e.g., `RAG-GOV-01`)
- **function**: AI RMF function (Govern, Map, Measure, Manage)
- **ref**: NIST AI 600-1 section reference
- **action**: Concrete task to perform
- **required_artifacts**: Evidence of completion
- **owner_role**: Responsible party (e.g., ML Engineer, CISO)
- **lifecycle_stage**: When to perform (design, dev, deploy, monitor)
- **acceptance_criteria**: How to verify completion

### 3. Track Progress

Use the checklists in your sprint planning:
```bash
# Example: Mark items complete in your issue tracker
- [ ] RAG-GOV-01: Establish AI governance committee
- [x] RAG-MAP-02: Inventory vector database data sources
- [ ] RAG-MEAS-03: Deploy PII detection scorer
```

### 4. Generate Artifacts

Fill out templates:
```bash
cp templates/model-card.md ../my-project/docs/model-card.md
# Edit with your model's details
```

---

## Validation

Install the lightweight tooling dependency (PyYAML) and run the validation script to ensure all checklist references are correct:

```bash
cd deliverables/01-gai-rmf-kit
python -m pip install --upgrade pip pyyaml  # first run only
python scripts/validate_checklists.py
```

This checks:
- ✅ YAML schema compliance
- ✅ All `ref` fields point to valid NIST AI 600-1 sections
- ✅ No duplicate `control_id` values
- ✅ `required_artifacts` lists are populated for every control

Need to regenerate the crosswalk after editing any checklist? Run:

```bash
cd deliverables/01-gai-rmf-kit
python scripts/generate_crosswalk.py
```

This produces an updated [`crosswalk.csv`](crosswalk.csv) with mappings of every control to its function, artifacts, and NIST reference.

---

## Mapping to NIST AI 600-1

| AI RMF Function | Controls in Kit | Key Risks Addressed |
|-----------------|-----------------|---------------------|
| **Govern** | 15 items across 3 checklists | Governance gaps, accountability |
| **Map** | 18 items | Context definition, risk identification |
| **Measure** | 22 items | Evaluation gaps, metric blindness |
| **Manage** | 20 items | Incident response, continuous monitoring |

See [crosswalk.csv](crosswalk.csv) for full mapping.

---

## Examples

### RAG Checklist Excerpt

```yaml
- control_id: RAG-MEAS-03
  function: Measure
  ref: "AI 600-1 Section 3.3"
  action: "Deploy automated PII detection on RAG outputs"
  required_artifacts:
    - "PII scorer integrated in eval pipeline (see D2)"
    - "Test report showing 0% PII leakage on golden dataset"
  owner_role: "ML Engineer"
  lifecycle_stage: "development"
  acceptance_criteria: "PII scorer runs on every release candidate; blocks deployment if >0 leaks detected"
```

### Model Card Template

See [templates/model-card.md](templates/model-card.md) for a complete example following the format recommended in NIST AI 600-1 Appendix B.

---

## Integration with Other Deliverables

- **D2 (Eval Harness)**: Checklist items reference specific scorers (PII, refusal-rate)
- **D3 (CI/CD)**: Lifecycle stages map to GitHub Actions workflows
- **D5 (ISO 42001)**: Control IDs cross-referenced in ISO bridge document

---

## License

- **Code** (validation scripts): Apache-2.0
- **Documentation** (checklists, templates): CC-BY-4.0

---

## References

- NIST AI 600-1: https://doi.org/10.6028/NIST.AI.600-1
- AI RMF Playbook: https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook
- Full citations: [/docs/refs.md](../../docs/refs.md)
