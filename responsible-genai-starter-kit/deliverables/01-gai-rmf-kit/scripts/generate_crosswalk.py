#!/usr/bin/env python3
"""Generate crosswalk.csv from checklist YAML files."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import List

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "ERROR: PyYAML is required. Install it with 'python -m pip install pyyaml'."
    ) from exc


def load_controls(checklist: Path) -> List[dict]:
    with checklist.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    metadata = data.get("checklist_metadata", {})
    pattern = metadata.get("pattern", checklist.stem)

    controls: List[dict] = []
    for control in data.get("controls", []):
        controls.append(
            {
                "control_id": control.get("control_id", ""),
                "pattern": pattern,
                "function": control.get("function", ""),
                "nist_reference": control.get("ref", ""),
                "action": control.get("action", ""),
                "lifecycle_stage": control.get("lifecycle_stage", ""),
                "owner_role": control.get("owner_role", ""),
                "required_artifacts": "; ".join(control.get("required_artifacts", [])),
            }
        )
    return controls


def main() -> int:
    deliverable_root = Path(__file__).resolve().parent.parent
    checklists_dir = deliverable_root / "checklists"
    output_path = deliverable_root / "crosswalk.csv"

    if not checklists_dir.exists():
        raise SystemExit(f"Checklist directory not found: {checklists_dir}")

    controls: List[dict] = []
    for checklist in sorted(checklists_dir.glob("*.yaml")):
        controls.extend(load_controls(checklist))

    controls.sort(key=lambda row: row["control_id"])

    fieldnames = [
        "control_id",
        "pattern",
        "function",
        "nist_reference",
        "action",
        "lifecycle_stage",
        "owner_role",
        "required_artifacts",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in controls:
            writer.writerow(row)

    print(f"✓ Generated {output_path.relative_to(deliverable_root)} with {len(controls)} entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
