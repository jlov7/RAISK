"""Tests for core evaluation harness."""

import pytest

from eval_harness.core import EvalHarness
from eval_harness.scorers import ExactMatchScorer, PIIDetectionScorer
from eval_harness.types import EvalSample


class TestEvalHarness:
    """Test main evaluation harness."""

    def test_evaluate_basic(self) -> None:
        """Test basic evaluation with single scorer."""
        scorers = [ExactMatchScorer()]
        harness = EvalHarness(scorers=scorers)

        samples = [
            EvalSample(input="test1", expected_output="out1", actual_output="out1"),
            EvalSample(input="test2", expected_output="out2", actual_output="out2"),
        ]

        result = harness.evaluate(samples)

        assert result.total_samples == 2
        assert result.aggregate_metrics["exact_match_mean"] == 1.0
        assert result.aggregate_metrics["exact_match_pass_rate"] == 1.0
        assert result.aggregate_metrics["overall_pass_rate"] == 1.0

    def test_evaluate_multiple_scorers(self) -> None:
        """Test evaluation with multiple scorers."""
        scorers = [ExactMatchScorer(), PIIDetectionScorer()]
        harness = EvalHarness(scorers=scorers)

        samples = [
            EvalSample(
                input="test",
                expected_output="safe output",
                actual_output="safe output"
            ),
        ]

        result = harness.evaluate(samples)

        assert result.total_samples == 1
        assert "exact_match_mean" in result.aggregate_metrics
        assert "pii_detection_mean" in result.aggregate_metrics
        assert "overall_pass_rate" in result.aggregate_metrics

    def test_evaluate_mixed_results(self) -> None:
        """Test evaluation with mixed pass/fail results."""
        scorers = [ExactMatchScorer()]
        harness = EvalHarness(scorers=scorers)

        samples = [
            EvalSample(input="test1", expected_output="out1", actual_output="out1"),  # pass
            EvalSample(input="test2", expected_output="out2", actual_output="wrong"),  # fail
        ]

        result = harness.evaluate(samples)

        assert result.total_samples == 2
        assert result.aggregate_metrics["exact_match_mean"] == 0.5
        assert result.aggregate_metrics["exact_match_pass_rate"] == 0.5
        assert result.aggregate_metrics["overall_pass_rate"] == 0.5

    def test_evaluate_with_config(self) -> None:
        """Test evaluation with config metadata."""
        scorers = [ExactMatchScorer()]
        harness = EvalHarness(scorers=scorers)

        samples = [
            EvalSample(input="test", expected_output="out", actual_output="out"),
        ]

        config = {"dataset": "test.csv", "version": "1.0"}
        result = harness.evaluate(samples, config=config)

        assert result.config == config

    def test_evaluate_no_scorers(self) -> None:
        """Test that initialization with no scorers raises error."""
        with pytest.raises(ValueError, match="At least one scorer is required"):
            EvalHarness(scorers=[])

    def test_evaluate_no_samples(self) -> None:
        """Test that evaluation with no samples raises error."""
        scorers = [ExactMatchScorer()]
        harness = EvalHarness(scorers=scorers)

        with pytest.raises(ValueError, match="No samples to evaluate"):
            harness.evaluate([])

    def test_result_to_dict(self) -> None:
        """Test EvalResult serialization to dict."""
        scorers = [ExactMatchScorer()]
        harness = EvalHarness(scorers=scorers)

        samples = [
            EvalSample(input="test", expected_output="out", actual_output="out"),
        ]

        result = harness.evaluate(samples)
        result_dict = result.to_dict()

        assert "total_samples" in result_dict
        assert "aggregate_metrics" in result_dict
        assert "sample_scores" in result_dict
        assert "config" in result_dict
