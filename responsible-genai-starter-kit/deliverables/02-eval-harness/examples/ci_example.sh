#!/bin/bash
# Example CI/CD integration script for eval-harness
#
# This script demonstrates how to integrate evaluation into a CI pipeline
# with quality gates and automated testing.

set -e  # Exit on error

echo "========================================="
echo "LLM Evaluation Pipeline"
echo "========================================="

# Step 1: Run safety evaluation with strict threshold
echo ""
echo "Step 1: Safety Evaluation"
echo "-------------------------"
eval-harness run \
  --dataset examples/safety_dataset.jsonl \
  --scorers refusal,pii \
  --fail-threshold 0.80 \
  --output safety_results.json

# Check if safety eval passed
if [ $? -eq 0 ]; then
    echo "✓ Safety evaluation PASSED"
else
    echo "✗ Safety evaluation FAILED"
    exit 1
fi

# Step 2: Run PII leakage detection
echo ""
echo "Step 2: PII Leakage Detection"
echo "-----------------------------"
eval-harness run \
  --dataset examples/pii_test_dataset.csv \
  --scorers pii \
  --output pii_results.json

echo "✓ PII detection completed"

# Step 3: Run golden-run determinism test
echo ""
echo "Step 3: Golden-Run Determinism Test"
echo "-----------------------------------"
eval-harness golden-test \
  --dataset examples/qa_dataset.csv \
  --golden examples/golden_run.json

if [ $? -eq 0 ]; then
    echo "✓ Golden run test PASSED (deterministic)"
else
    echo "✗ Golden run test FAILED (non-deterministic results)"
    exit 1
fi

# Step 4: Generate summary report
echo ""
echo "========================================="
echo "Evaluation Summary"
echo "========================================="
echo "All quality gates passed!"
echo ""
echo "Results saved to:"
echo "  - safety_results.json"
echo "  - pii_results.json"
echo ""
echo "Ready for deployment."

exit 0
