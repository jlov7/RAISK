# D2 — Evaluation Harness

Safety-focused evaluation framework for Large Language Model outputs. Part of the Responsible GenAI Starter Kit research project, engineered to production quality so you can plug it into CI/CD pipelines with minimal friction.

---

## At a Glance

- **Purpose:** Measure safety and accuracy risks (PII leakage, refusal behavior, regressions) before releases.
- **Language:** Python 3.10+, packaged as `eval-harness`.
- **Scorers included:** Exact match, regex PII detection, response length validation, refusal-rate detection, LLM judge hooks.
- **Key capabilities:** Golden-run determinism tests, JSON/CSV dataset loaders, CLI and Python API, CI-ready exit codes.
- **Integration:** Downstream in D3 workflows (quality gates) and referenced by D1 governance controls.

---

## Installation

```bash
cd deliverables/02-eval-harness
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

The editable install exposes the `eval-harness` CLI and pulls in test tooling (pytest, mypy, black, ruff). If you only need runtime dependencies, omit the `dev` extra.

---

## CLI Usage

### Run an Evaluation

```bash
eval-harness run \
  --dataset examples/qa_dataset.csv \
  --scorers exact_match,length,pii \
  --output results/qa_results.json \
  --fail-threshold 0.95
```

- **`--dataset`**: CSV or JSONL file containing `input`, `expected_output`, optional metadata.
- **`--scorers`**: Comma-separated list (`exact_match`, `pii`, `length`, `refusal`).
- **`--fail-threshold`**: Exit with status 1 if `overall_pass_rate` is below the threshold (ideal for CI).
- **`--output`**: Persist detailed JSON results for dashboards or artifact storage.

### Golden-Run Determinism

```bash
eval-harness golden-test \
  --dataset examples/qa_dataset.csv \
  --golden results/golden_run.json
```

Use this to ensure your scoring pipeline is deterministic between releases. Store golden files in version control and rerun after dependency upgrades.

---

## Python API

```python
from eval_harness import EvalHarness, DatasetLoader, ExactMatchScorer, PIIDetectionScorer
from eval_harness.types import DatasetFormat

loader = DatasetLoader()
samples = loader.load("examples/qa_dataset.csv", format=DatasetFormat.CSV)

scorers = [
    ExactMatchScorer(case_sensitive=False),
    PIIDetectionScorer(),
]

harness = EvalHarness(scorers=scorers)
result = harness.evaluate(samples, config={"dataset": "qa_dataset"})

print(result.aggregate_metrics["exact_match_pass_rate"])
print(result.to_dict())
```

API objects (`EvalSample`, `ScoreResult`, `EvalResult`) are simple dataclasses to keep serialization easy.

---

## Dataset Formats

### CSV

```
input,expected_output,actual_output,category
"What is 2+2?","4","4",math
"Explain photosynthesis.","Answer","Generated answer",science
```

Required column: `input`. Optional columns become metadata. `actual_output` can be pre-filled (offline evaluation) or empty if you plan to populate results programmatically.

### JSONL

```
{"input": "What is 2+2?", "expected_output": "4", "actual_output": "4", "metadata": {"category": "math"}}
{"input": "Capital of France?", "expected_output": "Paris"}
```

Each line is parsed independently. Provide `metadata` as nested JSON objects when needed.

---

## Extending Scorers

Create a custom scorer by subclassing `Scorer` in `eval_harness/scorers.py`:

```python
from eval_harness.scorers import Scorer
from eval_harness.types import EvalSample, ScoreResult

class ToxicityScorer(Scorer):
    name = "toxicity"

    def score(self, sample: EvalSample) -> ScoreResult:
        score = run_toxicity_model(sample.actual_output or "")
        passed = score < 0.2
        return ScoreResult(
            scorer_name=self.name,
            score=score,
            passed=passed,
            details={"threshold": 0.2},
        )
```

Register scorers in your own CLI wrapper or extend `get_scorer_by_name` for reuse.

---

## CI/CD Integration

- **D3 Workflow hook:** Call `eval-harness run ... --fail-threshold` in GitHub Actions to block merges when safety metrics degrade.
- **Artifacts:** Store JSON results for audit trails. Add `jq '.aggregate_metrics'` steps to emit summary tables.
- **Golden runs:** Keep `results/golden_run.json` under version control and run `golden-test` post-build.

Example GitHub Actions snippet:

```yaml
      - name: Run eval harness
        run: |
          eval-harness run \
            --dataset deliverables/02-eval-harness/examples/safety_dataset.jsonl \
            --scorers refusal,pii,length \
            --fail-threshold 0.98 \
            --output results/safety_results.json
```

---

## Quality & Testing

- `pytest` covers core scoring, dataset loaders, and deterministic behavior.
- `mypy` enforces type hints; `ruff` and `black` maintain style.
- The package avoids heavyweight dependencies beyond `numpy` and `pandas` for metrics and dataset handling.

Run everything with:

```bash
pytest
ruff check eval_harness
black --check .
mypy eval_harness
```

---

## Frequently Asked Questions

**Is this intended for production?**  
Yes—as a reference implementation. Review and harden it for your environment. Update dependencies regularly.

**Can I plug in LLM-as-a-judge?**  
Install the `llm-judge` extra (`pip install -e ".[llm-judge]"`) and integrate Anthropics/OpenAI scoring in a custom module.

**How does this relate to D1 and D3?**  
D1 checklists mandate automated evaluation; D3 workflows call this harness to enforce the controls.

---

## Licensing

- Code: Apache-2.0
- Documentation: CC-BY-4.0

Attribution appreciated when you extend or redistribute the package.
