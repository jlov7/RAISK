"""
Eval Harness: Minimal evaluation framework for LLM testing.

Part of the Responsible GenAI Starter Kit.

This package provides:
- Dataset loading (CSV, JSONL)
- Scoring plugins (exact-match, PII detection, length checks, refusal rate)
- LLM-judge interface (optional)
- Golden-run determinism testing

References:
- NIST AI 600-1: Section 3.3 (Measure function - GAI evaluation)
- NIST AI RMF Playbook: Measure 2.3 (Test AI system performance)
"""

__version__ = "0.1.0"

from eval_harness.core import EvalHarness, EvalResult
from eval_harness.dataset import DatasetLoader
from eval_harness.scorers import (
    ExactMatchScorer,
    PIIDetectionScorer,
    ResponseLengthScorer,
    RefusalRateScorer,
)

__all__ = [
    "EvalHarness",
    "EvalResult",
    "DatasetLoader",
    "ExactMatchScorer",
    "PIIDetectionScorer",
    "ResponseLengthScorer",
    "RefusalRateScorer",
]
