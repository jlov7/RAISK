"""
Dataset loading utilities.

Supports CSV and JSONL formats for evaluation datasets.
"""

import csv
import json
from pathlib import Path
from typing import List, Union

from eval_harness.types import DatasetFormat, EvalSample


class DatasetLoader:
    """Loads evaluation datasets from CSV or JSONL files.

    CSV format expects columns: input, expected_output (optional), and any metadata columns.
    JSONL format expects one JSON object per line with keys: input, expected_output (optional), metadata (optional).

    Examples:
        >>> loader = DatasetLoader()
        >>> samples = loader.load("data.csv", format=DatasetFormat.CSV)
        >>> samples = loader.load("data.jsonl", format=DatasetFormat.JSONL)
    """

    def load(
        self, file_path: Union[str, Path], format: DatasetFormat = DatasetFormat.CSV
    ) -> List[EvalSample]:
        """Load dataset from file.

        Args:
            file_path: Path to the dataset file
            format: Format of the dataset (CSV or JSONL)

        Returns:
            List of EvalSample objects

        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If format is unsupported or file is malformed
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Dataset file not found: {file_path}")

        if format == DatasetFormat.CSV:
            return self._load_csv(file_path)
        elif format == DatasetFormat.JSONL:
            return self._load_jsonl(file_path)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def _load_csv(self, file_path: Path) -> List[EvalSample]:
        """Load CSV dataset.

        CSV must have at minimum an 'input' column.
        Optional columns: 'expected_output', 'actual_output', and any metadata columns.
        """
        samples = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if "input" not in reader.fieldnames:
                    raise ValueError("CSV must have an 'input' column")

                for row in reader:
                    # Extract core fields
                    input_text = row.pop("input")
                    expected_output = row.pop("expected_output", None)
                    actual_output = row.pop("actual_output", None)

                    # Remaining fields become metadata
                    metadata = {k: v for k, v in row.items() if v}

                    samples.append(
                        EvalSample(
                            input=input_text,
                            expected_output=expected_output if expected_output else None,
                            actual_output=actual_output if actual_output else None,
                            metadata=metadata,
                        )
                    )
        except Exception as e:
            raise ValueError(f"Error loading CSV file: {e}")

        if not samples:
            raise ValueError(f"No samples loaded from {file_path}")

        return samples

    def _load_jsonl(self, file_path: Path) -> List[EvalSample]:
        """Load JSONL dataset.

        Each line must be valid JSON with at minimum an 'input' field.
        Optional fields: 'expected_output', 'actual_output', 'metadata'.
        """
        samples = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        data = json.loads(line)
                    except json.JSONDecodeError as e:
                        raise ValueError(f"Invalid JSON on line {line_num}: {e}")

                    if "input" not in data:
                        raise ValueError(f"Line {line_num} missing 'input' field")

                    input_text = data["input"]
                    expected_output = data.get("expected_output")
                    actual_output = data.get("actual_output")
                    metadata = data.get("metadata", {})

                    samples.append(
                        EvalSample(
                            input=input_text,
                            expected_output=expected_output,
                            actual_output=actual_output,
                            metadata=metadata,
                        )
                    )
        except Exception as e:
            raise ValueError(f"Error loading JSONL file: {e}")

        if not samples:
            raise ValueError(f"No samples loaded from {file_path}")

        return samples
