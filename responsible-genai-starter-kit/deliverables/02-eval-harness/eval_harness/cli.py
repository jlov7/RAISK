"""
Command-line interface for eval harness.

Usage:
    eval-harness run --dataset data.csv --scorers exact_match,pii --output results.json
    eval-harness golden-test --dataset data.csv --golden golden.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

from eval_harness.core import EvalHarness
from eval_harness.dataset import DatasetLoader
from eval_harness.scorers import (
    ExactMatchScorer,
    PIIDetectionScorer,
    RefusalRateScorer,
    ResponseLengthScorer,
    Scorer,
)
from eval_harness.types import DatasetFormat


def get_scorer_by_name(name: str) -> Optional[Scorer]:
    """Get scorer instance by name.

    Available scorers:
    - exact_match: Exact string matching
    - pii: PII detection (SSN, email, phone, etc.)
    - length: Response length validation
    - refusal: Refusal rate calculation
    """
    scorers = {
        "exact_match": lambda: ExactMatchScorer(),
        "pii": lambda: PIIDetectionScorer(),
        "length": lambda: ResponseLengthScorer(),
        "refusal": lambda: RefusalRateScorer(),
    }
    return scorers.get(name, lambda: None)()


def cmd_run(args: argparse.Namespace) -> int:
    """Run evaluation on dataset."""
    print(f"[eval-harness] Loading dataset: {args.dataset}")

    # Detect format from extension if not specified
    dataset_path = Path(args.dataset)
    if args.format:
        format = DatasetFormat(args.format)
    elif dataset_path.suffix == ".csv":
        format = DatasetFormat.CSV
    elif dataset_path.suffix == ".jsonl":
        format = DatasetFormat.JSONL
    else:
        print(f"ERROR: Could not detect format for {dataset_path}", file=sys.stderr)
        print("Specify --format csv or --format jsonl", file=sys.stderr)
        return 1

    # Load dataset
    try:
        loader = DatasetLoader()
        samples = loader.load(dataset_path, format=format)
        print(f"[eval-harness] Loaded {len(samples)} samples")
    except Exception as e:
        print(f"ERROR: Failed to load dataset: {e}", file=sys.stderr)
        return 1

    # Initialize scorers
    scorer_names = [s.strip() for s in args.scorers.split(",")]
    scorers = []
    for name in scorer_names:
        scorer = get_scorer_by_name(name)
        if scorer is None:
            print(f"ERROR: Unknown scorer '{name}'", file=sys.stderr)
            print("Available: exact_match, pii, length, refusal", file=sys.stderr)
            return 1
        scorers.append(scorer)

    print(f"[eval-harness] Using scorers: {', '.join(scorer_names)}")

    # Run evaluation
    try:
        harness = EvalHarness(scorers=scorers)
        result = harness.evaluate(
            samples,
            config={
                "dataset": str(dataset_path),
                "format": format.value,
                "scorers": scorer_names,
            },
        )
    except Exception as e:
        print(f"ERROR: Evaluation failed: {e}", file=sys.stderr)
        return 1

    # Print summary
    print("\n[eval-harness] Evaluation Results")
    print("=" * 60)
    print(f"Total samples: {result.total_samples}")
    print(f"Overall pass rate: {result.aggregate_metrics['overall_pass_rate']:.2%}")
    print("\nPer-scorer metrics:")
    for key, value in sorted(result.aggregate_metrics.items()):
        if key != "overall_pass_rate":
            print(f"  {key}: {value:.4f}")

    # Save results if output specified
    if args.output:
        output_path = Path(args.output)
        print(f"\n[eval-harness] Saving results to: {output_path}")
        try:
            with open(output_path, "w") as f:
                json.dump(result.to_dict(), f, indent=2)
            print(f"[eval-harness] Results saved successfully")
        except Exception as e:
            print(f"ERROR: Failed to save results: {e}", file=sys.stderr)
            return 1

    # Exit with error if overall pass rate is below threshold
    if args.fail_threshold:
        if result.aggregate_metrics["overall_pass_rate"] < args.fail_threshold:
            print(
                f"\n[eval-harness] FAILED: Pass rate {result.aggregate_metrics['overall_pass_rate']:.2%} "
                f"< threshold {args.fail_threshold:.2%}",
                file=sys.stderr,
            )
            return 1

    return 0


def cmd_golden_test(args: argparse.Namespace) -> int:
    """Run golden-run determinism test.

    Compares current evaluation results against a saved golden result.
    """
    print(f"[eval-harness] Running golden-run test")
    print(f"  Dataset: {args.dataset}")
    print(f"  Golden file: {args.golden}")

    # Load golden results
    golden_path = Path(args.golden)
    if not golden_path.exists():
        print(f"ERROR: Golden file not found: {golden_path}", file=sys.stderr)
        print("Run evaluation first and save with --output to create golden file", file=sys.stderr)
        return 1

    try:
        with open(golden_path, "r") as f:
            golden_data = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to load golden file: {e}", file=sys.stderr)
        return 1

    # Re-run evaluation with same config
    dataset_path = Path(args.dataset)
    format = DatasetFormat(golden_data["config"]["format"])
    scorer_names = golden_data["config"]["scorers"]

    try:
        loader = DatasetLoader()
        samples = loader.load(dataset_path, format=format)

        scorers = [get_scorer_by_name(name) for name in scorer_names]
        harness = EvalHarness(scorers=scorers)
        result = harness.evaluate(samples, config=golden_data["config"])
    except Exception as e:
        print(f"ERROR: Evaluation failed: {e}", file=sys.stderr)
        return 1

    # Compare results
    print("\n[eval-harness] Comparing results...")
    mismatches = []

    for key in golden_data["aggregate_metrics"]:
        golden_val = golden_data["aggregate_metrics"][key]
        current_val = result.aggregate_metrics[key]

        # Use small epsilon for float comparison
        if abs(golden_val - current_val) > 1e-6:
            mismatches.append(
                f"  {key}: golden={golden_val:.4f}, current={current_val:.4f}"
            )

    if mismatches:
        print("\nFAILED: Results differ from golden run!", file=sys.stderr)
        for mismatch in mismatches:
            print(mismatch, file=sys.stderr)
        return 1
    else:
        print("\nPASS: Results match golden run (deterministic)")
        return 0


def main() -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Eval Harness: Minimal evaluation framework for LLM testing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Run command
    run_parser = subparsers.add_parser("run", help="Run evaluation on dataset")
    run_parser.add_argument(
        "--dataset", required=True, help="Path to dataset file (CSV or JSONL)"
    )
    run_parser.add_argument(
        "--format", choices=["csv", "jsonl"], help="Dataset format (auto-detected if not specified)"
    )
    run_parser.add_argument(
        "--scorers",
        required=True,
        help="Comma-separated list of scorers: exact_match,pii,length,refusal",
    )
    run_parser.add_argument("--output", help="Path to save results JSON")
    run_parser.add_argument(
        "--fail-threshold",
        type=float,
        help="Exit with error if overall pass rate < threshold (0.0-1.0)",
    )

    # Golden-test command
    golden_parser = subparsers.add_parser(
        "golden-test", help="Run golden-run determinism test"
    )
    golden_parser.add_argument("--dataset", required=True, help="Path to dataset file")
    golden_parser.add_argument(
        "--golden", required=True, help="Path to golden results JSON"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    if args.command == "run":
        return cmd_run(args)
    elif args.command == "golden-test":
        return cmd_golden_test(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
