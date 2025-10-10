"""Tests for golden-run determinism."""

import json
import tempfile
from pathlib import Path

import pytest

from eval_harness.core import EvalHarness
from eval_harness.dataset import DatasetLoader
from eval_harness.scorers import ExactMatchScorer, PIIDetectionScorer
from eval_harness.types import DatasetFormat, EvalSample


class TestGoldenRunDeterminism:
    """Test that evaluation is deterministic and reproducible."""

    def test_exact_match_determinism(self) -> None:
        """Test that exact match scorer produces identical results across runs."""
        scorer = ExactMatchScorer()
        sample = EvalSample(
            input="test",
            expected_output="output",
            actual_output="output"
        )

        # Run scorer multiple times
        results = [scorer.score(sample) for _ in range(5)]

        # All results should be identical
        for result in results[1:]:
            assert result.score == results[0].score
            assert result.passed == results[0].passed

    def test_pii_scorer_determinism(self) -> None:
        """Test that PII scorer produces identical results across runs."""
        scorer = PIIDetectionScorer()
        sample = EvalSample(
            input="test",
            actual_output="Contact me at test@example.com"
        )

        # Run scorer multiple times
        results = [scorer.score(sample) for _ in range(5)]

        # All results should be identical
        for result in results[1:]:
            assert result.score == results[0].score
            assert result.passed == results[0].passed
            assert result.details["detected_pii"] == results[0].details["detected_pii"]

    def test_harness_determinism(self) -> None:
        """Test that full harness produces identical results across runs."""
        scorers = [ExactMatchScorer(), PIIDetectionScorer()]
        harness = EvalHarness(scorers=scorers)

        samples = [
            EvalSample(input="test1", expected_output="out1", actual_output="out1"),
            EvalSample(input="test2", expected_output="out2", actual_output="out2"),
        ]

        # Run evaluation multiple times
        results = [harness.evaluate(samples) for _ in range(3)]

        # All aggregate metrics should be identical
        for result in results[1:]:
            assert result.aggregate_metrics == results[0].aggregate_metrics

    def test_golden_run_workflow(self) -> None:
        """Test complete golden-run workflow: create, save, and compare."""
        # Create a test dataset
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("input,expected_output,actual_output\n")
            f.write("test1,out1,out1\n")
            f.write("test2,out2,wrong\n")
            dataset_path = f.name

        try:
            # Run initial evaluation (golden run)
            loader = DatasetLoader()
            samples = loader.load(dataset_path, format=DatasetFormat.CSV)

            scorers = [ExactMatchScorer()]
            harness = EvalHarness(scorers=scorers)
            golden_result = harness.evaluate(
                samples,
                config={"dataset": dataset_path, "format": "csv"}
            )

            # Save golden result
            with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
                json.dump(golden_result.to_dict(), f)
                golden_path = f.name

            try:
                # Re-run evaluation
                current_result = harness.evaluate(samples, config=golden_result.config)

                # Compare aggregate metrics
                for key in golden_result.aggregate_metrics:
                    golden_val = golden_result.aggregate_metrics[key]
                    current_val = current_result.aggregate_metrics[key]
                    assert abs(golden_val - current_val) < 1e-6

                # Verify results match exactly
                assert current_result.total_samples == golden_result.total_samples
                assert current_result.aggregate_metrics == golden_result.aggregate_metrics

            finally:
                Path(golden_path).unlink()
        finally:
            Path(dataset_path).unlink()

    def test_golden_run_mismatch_detection(self) -> None:
        """Test that golden run detects when results change."""
        # Create original sample
        original_sample = EvalSample(
            input="test",
            expected_output="original",
            actual_output="original"
        )

        scorer = ExactMatchScorer()
        harness = EvalHarness(scorers=[scorer])

        # Golden run
        golden_result = harness.evaluate([original_sample])

        # Modified sample (simulating code change or data change)
        modified_sample = EvalSample(
            input="test",
            expected_output="original",
            actual_output="modified"  # Different output!
        )

        # Current run
        current_result = harness.evaluate([modified_sample])

        # Results should differ
        assert (
            current_result.aggregate_metrics["exact_match_mean"] !=
            golden_result.aggregate_metrics["exact_match_mean"]
        )
