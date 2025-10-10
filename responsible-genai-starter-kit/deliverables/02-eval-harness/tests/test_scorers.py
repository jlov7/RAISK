"""Tests for scoring plugins."""

import pytest

from eval_harness.scorers import (
    ExactMatchScorer,
    PIIDetectionScorer,
    RefusalRateScorer,
    ResponseLengthScorer,
)
from eval_harness.types import EvalSample


class TestExactMatchScorer:
    """Test exact match scorer."""

    def test_exact_match_success(self) -> None:
        """Test exact match when outputs are identical."""
        scorer = ExactMatchScorer()
        sample = EvalSample(
            input="test",
            expected_output="correct answer",
            actual_output="correct answer"
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is True

    def test_exact_match_failure(self) -> None:
        """Test exact match when outputs differ."""
        scorer = ExactMatchScorer()
        sample = EvalSample(
            input="test",
            expected_output="correct answer",
            actual_output="wrong answer"
        )

        result = scorer.score(sample)

        assert result.score == 0.0
        assert result.passed is False

    def test_exact_match_case_insensitive(self) -> None:
        """Test case-insensitive matching."""
        scorer = ExactMatchScorer(case_sensitive=False)
        sample = EvalSample(
            input="test",
            expected_output="CORRECT ANSWER",
            actual_output="correct answer"
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is True

    def test_exact_match_missing_expected(self) -> None:
        """Test when expected_output is missing."""
        scorer = ExactMatchScorer()
        sample = EvalSample(
            input="test",
            actual_output="some output"
        )

        result = scorer.score(sample)

        assert result.score == 0.0
        assert result.passed is False
        assert "error" in result.details


class TestPIIDetectionScorer:
    """Test PII detection scorer."""

    def test_pii_ssn_detection(self) -> None:
        """Test detection of SSN."""
        scorer = PIIDetectionScorer()
        sample = EvalSample(
            input="test",
            actual_output="The SSN is 123-45-6789"
        )

        result = scorer.score(sample)

        assert result.score == 1.0  # PII detected (bad)
        assert result.passed is False
        assert "ssn" in result.details["detected_pii"]

    def test_pii_email_detection(self) -> None:
        """Test detection of email."""
        scorer = PIIDetectionScorer()
        sample = EvalSample(
            input="test",
            actual_output="Contact us at test@example.com"
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is False
        assert "email" in result.details["detected_pii"]

    def test_pii_phone_detection(self) -> None:
        """Test detection of phone number."""
        scorer = PIIDetectionScorer()
        sample = EvalSample(
            input="test",
            actual_output="Call me at 555-123-4567"
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is False
        assert "phone_us" in result.details["detected_pii"]

    def test_pii_no_detection(self) -> None:
        """Test when no PII is present."""
        scorer = PIIDetectionScorer()
        sample = EvalSample(
            input="test",
            actual_output="This is a clean response with no sensitive data"
        )

        result = scorer.score(sample)

        assert result.score == 0.0  # No PII (good)
        assert result.passed is True
        assert len(result.details["detected_pii"]) == 0

    def test_pii_custom_pattern(self) -> None:
        """Test custom PII pattern."""
        scorer = PIIDetectionScorer(
            custom_patterns={"employee_id": r"EMP-\d{6}"}
        )
        sample = EvalSample(
            input="test",
            actual_output="Employee ID: EMP-123456"
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is False
        assert "employee_id" in result.details["detected_pii"]


class TestResponseLengthScorer:
    """Test response length scorer."""

    def test_length_within_bounds(self) -> None:
        """Test when length is within bounds."""
        scorer = ResponseLengthScorer(min_length=5, max_length=50)
        sample = EvalSample(
            input="test",
            actual_output="This is a valid response"
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is True

    def test_length_too_short(self) -> None:
        """Test when length is below minimum."""
        scorer = ResponseLengthScorer(min_length=20, max_length=100)
        sample = EvalSample(
            input="test",
            actual_output="Short"  # 5 chars
        )

        result = scorer.score(sample)

        assert result.score < 1.0
        assert result.passed is False

    def test_length_too_long(self) -> None:
        """Test when length exceeds maximum."""
        scorer = ResponseLengthScorer(min_length=5, max_length=20)
        sample = EvalSample(
            input="test",
            actual_output="This is a very long response that exceeds the maximum allowed length"
        )

        result = scorer.score(sample)

        assert result.score < 1.0
        assert result.passed is False

    def test_length_token_unit(self) -> None:
        """Test token-based length measurement."""
        scorer = ResponseLengthScorer(min_length=3, max_length=10, unit="tokens")
        sample = EvalSample(
            input="test",
            actual_output="This is five tokens"  # 4 tokens by simple split
        )

        result = scorer.score(sample)

        assert result.passed is True


class TestRefusalRateScorer:
    """Test refusal rate scorer."""

    def test_refusal_detected_cannot(self) -> None:
        """Test detection of 'I cannot' refusal."""
        scorer = RefusalRateScorer()
        sample = EvalSample(
            input="harmful request",
            actual_output="I cannot help with that request as it violates guidelines"
        )

        result = scorer.score(sample)

        assert result.score == 1.0  # Refused (good)
        assert result.passed is True
        assert len(result.details["matched_patterns"]) > 0

    def test_refusal_detected_sorry(self) -> None:
        """Test detection of 'I'm sorry' refusal."""
        scorer = RefusalRateScorer()
        sample = EvalSample(
            input="harmful request",
            actual_output="I'm sorry, but I can't assist with that"
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is True

    def test_refusal_not_detected(self) -> None:
        """Test when model complies (no refusal)."""
        scorer = RefusalRateScorer()
        sample = EvalSample(
            input="benign request",
            actual_output="Here is the information you requested"
        )

        result = scorer.score(sample)

        assert result.score == 0.0  # Did not refuse
        assert result.passed is False

    def test_refusal_custom_pattern(self) -> None:
        """Test custom refusal pattern."""
        scorer = RefusalRateScorer(
            custom_refusal_patterns=["Access denied"]
        )
        sample = EvalSample(
            input="test",
            actual_output="Access denied: insufficient permissions"
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is True

    def test_refusal_case_insensitive(self) -> None:
        """Test case-insensitive refusal detection."""
        scorer = RefusalRateScorer()
        sample = EvalSample(
            input="test",
            actual_output="i cannot help with that"  # lowercase
        )

        result = scorer.score(sample)

        assert result.score == 1.0
        assert result.passed is True
