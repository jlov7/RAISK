"""
Type definitions for the eval harness.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class DatasetFormat(Enum):
    """Supported dataset formats."""

    CSV = "csv"
    JSONL = "jsonl"


@dataclass
class EvalSample:
    """A single evaluation sample.

    Attributes:
        input: The input prompt/question
        expected_output: The expected/reference output (optional)
        actual_output: The actual model output (to be filled during evaluation)
        metadata: Additional metadata (e.g., category, difficulty)
    """

    input: str
    expected_output: Optional[str] = None
    actual_output: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ScoreResult:
    """Result from a single scorer.

    Attributes:
        scorer_name: Name of the scorer
        score: Numeric score (0.0 to 1.0 for normalized scores, or raw metric)
        passed: Whether the sample passed the scorer's criteria
        details: Additional details (e.g., detected PII patterns, error messages)
    """

    scorer_name: str
    score: float
    passed: bool
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EvalResult:
    """Complete evaluation result for a dataset.

    Attributes:
        total_samples: Total number of samples evaluated
        sample_scores: List of score results per sample
        aggregate_metrics: Aggregate metrics across all samples
        config: Configuration used for evaluation
    """

    total_samples: int
    sample_scores: List[List[ScoreResult]]  # List of scorer results per sample
    aggregate_metrics: Dict[str, float]
    config: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "total_samples": self.total_samples,
            "aggregate_metrics": self.aggregate_metrics,
            "config": self.config,
            "sample_scores": [
                [
                    {
                        "scorer_name": sr.scorer_name,
                        "score": sr.score,
                        "passed": sr.passed,
                        "details": sr.details,
                    }
                    for sr in sample_score_list
                ]
                for sample_score_list in self.sample_scores
            ],
        }
