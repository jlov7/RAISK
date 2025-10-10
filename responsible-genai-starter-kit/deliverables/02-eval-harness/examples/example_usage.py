#!/usr/bin/env python3
"""
Example usage of the Eval Harness framework.

This script demonstrates how to:
1. Load a dataset
2. Configure scorers
3. Run evaluation
4. Analyze results
"""

from eval_harness import (
    EvalHarness,
    DatasetLoader,
    ExactMatchScorer,
    PIIDetectionScorer,
    RefusalRateScorer,
    ResponseLengthScorer,
)
from eval_harness.types import DatasetFormat


def example_qa_evaluation() -> None:
    """Example: QA accuracy evaluation."""
    print("=" * 60)
    print("Example 1: QA Accuracy Evaluation")
    print("=" * 60)

    # Load QA dataset
    loader = DatasetLoader()
    samples = loader.load("examples/qa_dataset.csv", format=DatasetFormat.CSV)
    print(f"Loaded {len(samples)} QA samples")

    # Configure scorers
    scorers = [
        ExactMatchScorer(case_sensitive=False),
        ResponseLengthScorer(min_length=1, max_length=1000),
    ]

    # Run evaluation
    harness = EvalHarness(scorers=scorers)
    result = harness.evaluate(samples)

    # Print results
    print(f"\nTotal samples: {result.total_samples}")
    print(f"Overall pass rate: {result.aggregate_metrics['overall_pass_rate']:.2%}")
    print(f"Exact match pass rate: {result.aggregate_metrics['exact_match_pass_rate']:.2%}")
    print()


def example_safety_evaluation() -> None:
    """Example: Safety and refusal testing."""
    print("=" * 60)
    print("Example 2: Safety Evaluation")
    print("=" * 60)

    # Load safety dataset
    loader = DatasetLoader()
    samples = loader.load("examples/safety_dataset.jsonl", format=DatasetFormat.JSONL)
    print(f"Loaded {len(samples)} safety test samples")

    # Configure scorers for safety
    scorers = [
        RefusalRateScorer(),
        PIIDetectionScorer(),
    ]

    # Run evaluation
    harness = EvalHarness(scorers=scorers)
    result = harness.evaluate(samples)

    # Print results
    print(f"\nTotal samples: {result.total_samples}")
    print(f"Refusal rate: {result.aggregate_metrics['refusal_rate_mean']:.2%}")
    print(f"PII detection pass rate: {result.aggregate_metrics['pii_detection_pass_rate']:.2%}")

    # Detailed analysis
    print("\nPer-sample analysis:")
    for i, (sample, scores) in enumerate(zip(samples, result.sample_scores)):
        refusal_score = scores[0]  # RefusalRateScorer
        pii_score = scores[1]  # PIIDetectionScorer

        print(f"\nSample {i+1}:")
        print(f"  Category: {sample.metadata.get('category', 'N/A')}")
        print(f"  Refused: {refusal_score.passed}")
        print(f"  Contains PII: {not pii_score.passed}")
    print()


def example_pii_detection() -> None:
    """Example: PII leakage detection."""
    print("=" * 60)
    print("Example 3: PII Leakage Detection")
    print("=" * 60)

    # Load PII test dataset
    loader = DatasetLoader()
    samples = loader.load("examples/pii_test_dataset.csv", format=DatasetFormat.CSV)
    print(f"Loaded {len(samples)} PII test samples")

    # Configure PII scorer
    scorers = [PIIDetectionScorer()]

    # Run evaluation
    harness = EvalHarness(scorers=scorers)
    result = harness.evaluate(samples)

    # Print results
    print(f"\nTotal samples: {result.total_samples}")
    print(f"PII-free pass rate: {result.aggregate_metrics['pii_detection_pass_rate']:.2%}")

    # Show detected PII
    print("\nDetailed PII detection:")
    for i, (sample, scores) in enumerate(zip(samples, result.sample_scores)):
        pii_result = scores[0]
        detected = pii_result.details.get("detected_pii", {})

        print(f"\nSample {i+1}: {sample.input[:50]}...")
        if detected:
            print(f"  ALERT: PII detected!")
            for pii_type, matches in detected.items():
                print(f"    - {pii_type}: {matches}")
        else:
            print(f"  OK: No PII detected")
    print()


if __name__ == "__main__":
    try:
        example_qa_evaluation()
        example_safety_evaluation()
        example_pii_detection()

        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
