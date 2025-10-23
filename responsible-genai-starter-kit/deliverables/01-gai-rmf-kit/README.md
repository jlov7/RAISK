# D1 — GAI RMF Implementation Kit

Operational checklists, templates, and crosswalks for bringing NIST AI 600-1 controls to life. Built as part of a personal research project; battle-tested enough to serve as a production-quality reference.

---

## Quick Reference

- **Primary audience:** Product managers, risk officers, ML leads, compliance teams
- **Standards covered:** NIST AI 600-1, AI RMF Playbook, OWASP LLM Top 10 (mapped via threat model)
- **Artifacts:** YAML checklists, model card template, risk register CSV, crosswalk spreadsheets
- **Dependencies:** Python 3.10+, `pyyaml` for validation scripts
- **Related modules:** [D2 Evaluation Harness](../02-eval-harness/README.md), [D5 ISO Bridge](../05-iso42001-bridge/README.md)

---

## What's Inside

| File/Folder | Description |
|-------------|-------------|
| `checklists/rag.yaml` | RAG-specific controls tied to governance, data provenance, and evaluation |
| `checklists/fine-tune.yaml` | Controls for fine-tuning and LoRA workflows |
| `checklists/code-assistant.yaml` | Guardrails for shipping AI pair-programming tools safely |
| `templates/model-card.md` | NIST-informed model card skeleton |
| `templates/risk-register.csv` | Risk inventory with likelihood/impact placeholders |
| `crosswalk.csv` | Machine-generated mapping of control IDs to AI RMF functions and artifacts |
| `scripts/validate_checklists.py` | Linting for YAML schema, duplicates, references |
| `scripts/generate_crosswalk.py` | Rebuilds `crosswalk.csv` from YAML sources |

---

## Setup

```bash
cd deliverables/01-gai-rmf-kit
python -m pip install --upgrade pip pyyaml
```

Validation checks:

```bash
python scripts/validate_checklists.py
```

Regenerate crosswalk after editing any checklist:

```bash
python scripts/generate_crosswalk.py
```

> `validate_checklists.py` fails fast if required metadata is missing or `control_id` values collide. Fix issues before committing changes.

---

## How to Use the Checklists

1. **Pick your pattern.** Choose the YAML file that matches your deployment (RAG, fine-tuning, or code assistant).
2. **Assign owners.** Each control lists a suggested `owner_role`. Map these to actual humans in your organization.
3. **Review action lines.** Every control includes a concrete `action`, required evidence, and acceptance criteria.
4. **Track completion.** Copy items into your backlog or issue tracker. Example snippet:
   ```text
   - [ ] RAG-GOV-01: Establish AI governance committee (Owner: AI Program Lead)
   - [x] RAG-MAP-02: Inventory vector database sources (Owner: Data Engineer)
   - [ ] RAG-MEAS-03: Deploy automated PII detection (Owner: ML Engineer)
   ```
5. **Capture evidence.** Store links to artifacts (policies, dashboards, evaluation results) in the `required_artifacts` section of your risk register.
6. **Review regularly.** Treat “Govern” items as standing agenda topics for AI oversight meetings.

---

## Templates & Artifacts

- **Model Card (`templates/model-card.md`):** Mirrors AI 600-1 Appendix B. Fill in system context, training data, evaluation metrics, mitigation strategies, and contact points.
- **Risk Register (`templates/risk-register.csv`):** Capture likelihood, impact, mitigation owners, and linked checklist items. Pair this with the threat model in `docs/threat-model.md`.
- **Crosswalk (`crosswalk.csv`):** Use in executive briefings to demonstrate which AI RMF functions you have covered and where evidence lives.

Recommendation: Copy the templates into your project repository (or SharePoint/Notion space) and version them alongside code changes.

---

## Integration Points

- **Evaluation Harness (D2):** Many controls reference the refusal and PII scorers. Run `eval-harness` when closing out `Measure` actions.
- **CI/CD Workflows (D3):** Controls that mention SBOMs, provenance, or Scorecard map directly to the jobs defined in `03-ssdf-genai-ci`.
- **ISO/IEC 42001 Bridge (D5):** Control IDs are reused in the ISO mapping files—keep IDs stable when you extend the checklists.
- **Education One-Pager (D6):** Use the completed checklists to populate the teacher/parent communications about how AI systems are governed.

---

## Customization Tips

- **Add new controls:** Append entries to the relevant YAML file. Run the validator to ensure schema compliance.
- **Extend metadata:** Add `tags` or `risk_rating` fields if you need additional filters. Update validation scripts accordingly.
- **Localize language:** Translate action statements into your organization’s vocabulary, but keep control IDs stable to preserve crosswalk integrity.
- **Create variants:** Fork the checklists for regional regulations (e.g., EU AI Act) and maintain them under `checklists/<region>/`.

---

## FAQ

**Can I merge these controls into our existing GRC tooling?**  
Yes. Export YAML controls to CSV using `scripts/generate_crosswalk.py` or ingest directly via your GRC API.

**How do I prove coverage during an audit?**  
Use the risk register plus `crosswalk.csv` to show evidence links, and run `validate_checklists.py` to demonstrate internal quality checks.

**What if a control does not apply?**  
Document the exception in your risk register with a rationale and compensating controls. Flag it for review in governance meetings.

---

## Licensing

- **Code (scripts):** Apache-2.0
- **Documentation & checklists:** CC-BY-4.0 (credit “Responsible GenAI Starter Kit – Jason Lovell”)

---

## References

- NIST AI 600-1: https://doi.org/10.6028/NIST.AI.600-1
- AI RMF Playbook: https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook
- Related citations: [../../docs/refs.md](../../docs/refs.md)
