# D5 — ISO/IEC 42001 Bridge

Translate the Responsible GenAI Starter Kit artifacts into ISO/IEC 42001:2023 AI Management System evidence. This deliverable packages mapping documents, RACI assignments, and tracking templates so you can accelerate certification without starting from scratch.

---

## Quick Reference

- **Primary users:** Compliance leads, risk officers, PMO teams, external auditors
- **Inputs:** Outputs from D1–D4 (checklists, evaluations, workflows, provenance)
- **Outputs:** Clause-by-clause mapping, populated RACI matrix, implementation playbook, compliance tracker
- **Licensing:** Documentation under CC-BY-4.0, structured data under Apache-2.0

---

## Contents

| Artifact | Purpose |
|----------|---------|
| [`ISO42001-MAPPING.md`](ISO42001-MAPPING.md) | Detailed mapping from Starter Kit deliverables to ISO 42001 clauses and Annex A controls. Includes gap analysis template and evidence suggestions. |
| [`RACI-MATRIX.csv`](RACI-MATRIX.csv) | Role assignment matrix (Responsible, Accountable, Consulted, Informed) covering governance, engineering, security, and compliance activities. |
| [`IMPLEMENTATION-GUIDE.md`](IMPLEMENTATION-GUIDE.md) | Phase-by-phase rollout plan (Plan → Implement → Validate) with timelines, integration guidance, and audit preparation checklist. |
| [`compliance-checklist.yaml`](compliance-checklist.yaml) | Machine-readable tracker for every ISO 42001 clause. Capture status, evidence links, responsible owners, and audit notes. |

---

## Getting Started

1. **Assess your baseline**  
   Read the gap analysis section in `ISO42001-MAPPING.md`. Mark controls that are already satisfied versus those requiring action.

2. **Assign ownership**  
   Populate `RACI-MATRIX.csv` with actual names/teams. Share with leadership to confirm accountability.

3. **Plan the rollout**  
   Follow the timeline in `IMPLEMENTATION-GUIDE.md`. Choose the small-org or large-org pathway that matches your scale.

4. **Track progress**  
   Update `compliance-checklist.yaml` as controls move from `not_started` to `implemented` to `verified`. Use the file during management reviews and internal audits.

5. **Collect evidence**  
   Link artifacts from other deliverables: D1 checklists, D2 evaluation reports, D3 SBOMs/SLSA attestations, D4 C2PA manifests.

---

## How the Pieces Fit

- **D1 Governance Controls → ISO Clauses 4, 5, 6, 7, 8**  
  Control IDs (e.g., `RAG-GOV-01`) appear throughout `ISO42001-MAPPING.md`. Update the risk register and model cards to satisfy transparency and context requirements.

- **D2 Evaluation Harness → Clause 9 (Performance Evaluation) & Annex A.1**  
  Provide evaluation reports and golden-run evidence as objective measurements.

- **D3 CI/CD Workflows → Annex A.7 (Cybersecurity) & Clause 8.1 (Operational Planning)**  
  Supply SBOMs, SLSA attestations, and Scorecard outputs as supply-chain evidence.

- **D4 C2PA Provenance → Annex A.5 (Transparency)**  
  Demonstrate content provenance controls for generated media.

- **D6 Education One-Pager → Clause 7.2/7.3 (Competence & Awareness)**  
  Attach training materials and attendance logs to the compliance checklist.

---

## Audit Preparation Checklist

Use the following as a pre-audit sanity check (full list in `IMPLEMENTATION-GUIDE.md` Section 6):

- [ ] AI policy and governance charter published and acknowledged
- [ ] RACI matrix approved and up to date
- [ ] Risk register with mitigation status per AI system
- [ ] Model cards completed for every production model
- [ ] Evaluation reports (baseline + latest run) archived
- [ ] SBOMs and SLSA attestations attached to releases
- [ ] C2PA manifests or alternative transparency mechanism documented
- [ ] Internal audit report and management review minutes from the last 12 months
- [ ] Incident response and corrective action logs current

---

## FAQ

**Can we achieve certification using only this deliverable?**  
This bridge accelerates the process, but certification still requires organizational commitment, evidence collection, and an accredited external audit. Treat the kit as your implementation backbone, not a turn-key guarantee.

**How does this interact with ISO/IEC 27001 or ISO 9001?**  
`IMPLEMENTATION-GUIDE.md` includes integration tips. Many controls overlap—reuse existing ISMS artifacts where possible and add AI-specific layers from the Starter Kit.

**What if we do not use C2PA?**  
Document an alternative transparency mechanism (e.g., disclosure banners, provenance metadata from another system) and note it in the compliance checklist. Auditors care about outcomes, not specific tooling.

**How frequently should we update the checklist?**  
Continuously. Treat it as a living artifact. Update after each sprint review, evaluation run, or incident response exercise.

---

## Next Steps

1. Schedule a kickoff meeting with governance, engineering, and compliance stakeholders.
2. Customize the mapping and RACI docs with your project names and references.
3. Align audit evidence storage (e.g., shared drive, GRC tool, version control).
4. Plan mock audits using the checklist to surface gaps early.

---

## Licensing

- Markdown documentation: CC-BY-4.0 (credit “Responsible GenAI Starter Kit – Jason Lovell”)
- Structured data (CSV/YAML): Apache-2.0

Feel free to remix and publish your tailored versions—just keep provenance intact.
