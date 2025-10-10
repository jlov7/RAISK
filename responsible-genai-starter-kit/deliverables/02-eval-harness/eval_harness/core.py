"""
Core evaluation harness implementation.

References:
- NIST AI 600-1 Section 3.3: Measure function
- NIST AI RMF Playbook: Measure 2.3 (Test AI system performance)
"""

from typing import List

from eval_harness.scorers import Scorer
from eval_harness.types import EvalResult, EvalSample, ScoreResult


class EvalHarness:
    """Main evaluation harness for running scorers on datasets.

    Example:
        >>> harness = EvalHarness(scorers=[ExactMatchScorer(), PIIDetectionScorer()])
        >>> samples = [EvalSample(input="test", actual_output="test")]
        >>> result = harness.evaluate(samples)
        >>> print(result.aggregate_metrics)
    """

    def __init__(self, scorers: List[Scorer]):
        """Initialize evaluation harness.

        Args:
            scorers: List of scorer instances to run
        """
        if not scorers:
            raise ValueError("At least one scorer is required")
        self.scorers = scorers

    def evaluate(self, samples: List[EvalSample], config: dict = None) -> EvalResult:
        """Run evaluation on a list of samples.

        Args:
            samples: List of evaluation samples
            config: Optional configuration metadata

        Returns:
            EvalResult with aggregated scores and per-sample details
        """
        if not samples:
            raise ValueError("No samples to evaluate")

        sample_scores: List[List[ScoreResult]] = []

        # Score each sample with all scorers
        for sample in samples:
            sample_result = []
            for scorer in self.scorers:
                score_result = scorer.score(sample)
                sample_result.append(score_result)
            sample_scores.append(sample_result)

        # Compute aggregate metrics
        aggregate_metrics = self._compute_aggregates(sample_scores)

        return EvalResult(
            total_samples=len(samples),
            sample_scores=sample_scores,
            aggregate_metrics=aggregate_metrics,
            config=config or {},
        )

    def _compute_aggregates(self, sample_scores: List[List[ScoreResult]]) -> dict:
        """Compute aggregate metrics across all samples.

        Returns dict with:
        - {scorer_name}_mean: Mean score for each scorer
        - {scorer_name}_pass_rate: Percentage of samples that passed
        - overall_pass_rate: Percentage of samples that passed all scorers
        """
        metrics = {}

        # Get unique scorer names
        scorer_names = [sr.scorer_name for sr in sample_scores[0]]

        for i, scorer_name in enumerate(scorer_names):
            # Extract scores for this scorer across all samples
            scores = [sample[i].score for sample in sample_scores]
            passed = [sample[i].passed for sample in sample_scores]

            # Compute metrics
            metrics[f"{scorer_name}_mean"] = sum(scores) / len(scores)
            metrics[f"{scorer_name}_pass_rate"] = sum(passed) / len(passed)

        # Overall pass rate (all scorers must pass)
        all_passed = sum(1 for sample in sample_scores if all(sr.passed for sr in sample))
        metrics["overall_pass_rate"] = all_passed / len(sample_scores)

        return metrics
