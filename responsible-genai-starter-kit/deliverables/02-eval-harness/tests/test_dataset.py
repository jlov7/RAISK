"""Tests for dataset loading."""

import json
import tempfile
from pathlib import Path

import pytest

from eval_harness.dataset import DatasetLoader
from eval_harness.types import DatasetFormat, EvalSample


class TestDatasetLoader:
    """Test dataset loading functionality."""

    def test_load_csv_basic(self) -> None:
        """Test loading basic CSV dataset."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("input,expected_output,actual_output\n")
            f.write('test input,test expected,test actual\n')
            f.write('another,output2,actual2\n')
            temp_path = f.name

        try:
            loader = DatasetLoader()
            samples = loader.load(temp_path, format=DatasetFormat.CSV)

            assert len(samples) == 2
            assert samples[0].input == "test input"
            assert samples[0].expected_output == "test expected"
            assert samples[0].actual_output == "test actual"
        finally:
            Path(temp_path).unlink()

    def test_load_csv_with_metadata(self) -> None:
        """Test loading CSV with metadata columns."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("input,expected_output,actual_output,category,difficulty\n")
            f.write('test,expected,actual,math,easy\n')
            temp_path = f.name

        try:
            loader = DatasetLoader()
            samples = loader.load(temp_path, format=DatasetFormat.CSV)

            assert len(samples) == 1
            assert samples[0].metadata["category"] == "math"
            assert samples[0].metadata["difficulty"] == "easy"
        finally:
            Path(temp_path).unlink()

    def test_load_csv_missing_input_column(self) -> None:
        """Test that loading CSV without 'input' column raises error."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("output,expected\n")
            f.write("test,expected\n")
            temp_path = f.name

        try:
            loader = DatasetLoader()
            with pytest.raises(ValueError, match="must have an 'input' column"):
                loader.load(temp_path, format=DatasetFormat.CSV)
        finally:
            Path(temp_path).unlink()

    def test_load_jsonl_basic(self) -> None:
        """Test loading basic JSONL dataset."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
            f.write(json.dumps({"input": "test1", "expected_output": "out1", "actual_output": "act1"}) + "\n")
            f.write(json.dumps({"input": "test2", "actual_output": "act2"}) + "\n")
            temp_path = f.name

        try:
            loader = DatasetLoader()
            samples = loader.load(temp_path, format=DatasetFormat.JSONL)

            assert len(samples) == 2
            assert samples[0].input == "test1"
            assert samples[0].expected_output == "out1"
            assert samples[1].expected_output is None
        finally:
            Path(temp_path).unlink()

    def test_load_jsonl_with_metadata(self) -> None:
        """Test loading JSONL with metadata."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
            data = {
                "input": "test",
                "actual_output": "output",
                "metadata": {"category": "test", "score": 0.95}
            }
            f.write(json.dumps(data) + "\n")
            temp_path = f.name

        try:
            loader = DatasetLoader()
            samples = loader.load(temp_path, format=DatasetFormat.JSONL)

            assert len(samples) == 1
            assert samples[0].metadata["category"] == "test"
            assert samples[0].metadata["score"] == 0.95
        finally:
            Path(temp_path).unlink()

    def test_load_jsonl_invalid_json(self) -> None:
        """Test that invalid JSON raises error."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
            f.write('{"input": "test"}\n')
            f.write('invalid json here\n')
            temp_path = f.name

        try:
            loader = DatasetLoader()
            with pytest.raises(ValueError, match="Invalid JSON"):
                loader.load(temp_path, format=DatasetFormat.JSONL)
        finally:
            Path(temp_path).unlink()

    def test_load_nonexistent_file(self) -> None:
        """Test that loading non-existent file raises error."""
        loader = DatasetLoader()
        with pytest.raises(FileNotFoundError):
            loader.load("/nonexistent/file.csv", format=DatasetFormat.CSV)
