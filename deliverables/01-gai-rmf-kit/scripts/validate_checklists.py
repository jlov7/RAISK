#!/usr/bin/env python3
"""Validate Responsible GenAI checklists for schema compliance and duplicates."""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable, List

try:
    import yaml
except ImportError as exc:  # pragma: no cover - dependency missing only
    sys.stderr.write(
        "ERROR: PyYAML is required. Install it with:\n"
        "  python -m pip install pyyaml\n"
    )
    raise SystemExit(2) from exc


REQUIRED_METADATA_FIELDS = {"pattern", "version", "last_updated", "description"}
REQUIRED_CONTROL_FIELDS = {
    "control_id",
    "function",
    "ref",
    "action",
    "required_artifacts",
    "owner_role",
    "lifecycle_stage",
    "acceptance_criteria",
}
ALLOWED_FUNCTIONS = {"Govern", "Map", "Measure", "Manage"}
ALLOWED_LIFECYCLE = {"design", "development", "deploy", "monitor"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate all checklist YAML files.")
    parser.add_argument(
        "--checklist-dir",
        default=None,
        help="Optional checklist directory (defaults to ../checklists)",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate_metadata(metadata: dict, path: Path, errors: List[str]) -> None:
    missing = REQUIRED_METADATA_FIELDS.difference(metadata.keys())
    if missing:
        errors.append(
            f"{path.name}: missing metadata fields: {', '.join(sorted(missing))}"
        )


def validate_control(control: dict, path: Path, errors: List[str]) -> None:
    missing = REQUIRED_CONTROL_FIELDS.difference(control.keys())
    if missing:
        errors.append(
            f"{path.name}::{control.get('control_id', '<unknown>')}: "
            f"missing keys: {', '.join(sorted(missing))}"
        )
        return

    if control["function"] not in ALLOWED_FUNCTIONS:
        errors.append(
            f"{path.name}::{control['control_id']}: invalid function '{control['function']}'"
        )

    if control["lifecycle_stage"] not in ALLOWED_LIFECYCLE:
        errors.append(
            f"{path.name}::{control['control_id']}: invalid lifecycle_stage '{control['lifecycle_stage']}'"
        )

    ref_val = control.get("ref", "")
    if ref_val and not ref_val.startswith("AI 600-1 Section"):
        errors.append(
            f"{path.name}::{control['control_id']}: ref should start with 'AI 600-1 Section ...'"
        )

    artifacts = control.get("required_artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append(
            f"{path.name}::{control['control_id']}: required_artifacts must be a non-empty list"
        )


def iter_checklists(base: Path) -> Iterable[Path]:
    return sorted(base.glob("*.yaml"))


def main() -> int:
    args = parse_args()
    deliverable_root = Path(__file__).resolve().parent.parent
    checklists_dir = Path(args.checklist_dir) if args.checklist_dir else deliverable_root / "checklists"

    if not checklists_dir.exists():
        sys.stderr.write(f"ERROR: Checklist directory not found: {checklists_dir}\n")
        return 1

    errors: List[str] = []
    control_ids: List[str] = []

    for checklist in iter_checklists(checklists_dir):
        data = load_yaml(checklist)
        metadata = data.get("checklist_metadata", {})
        validate_metadata(metadata, checklist, errors)

        controls = data.get("controls")
        if not isinstance(controls, list) or not controls:
            errors.append(f"{checklist.name}: controls section must be a non-empty list")
            continue

        for control in controls:
            validate_control(control, checklist, errors)
            if "control_id" in control:
                control_ids.append(control["control_id"])

    duplicate_ids = [cid for cid, count in Counter(control_ids).items() if count > 1]
    if duplicate_ids:
        errors.append(
            "Duplicate control_id values found: " + ", ".join(sorted(duplicate_ids))
        )

    if errors:
        sys.stderr.write("✗ Checklist validation failed:\n")
        for err in errors:
            sys.stderr.write(f"  - {err}\n")
        return 1

    print("✓ All checklist files validated successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
