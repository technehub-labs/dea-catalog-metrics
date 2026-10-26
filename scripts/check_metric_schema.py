"""CR-MET-009 Gate 1: check_metric_schema.py.

Validates each catalog Metric against the entity.schema.json schema.
CR-MET-009 binding: this gate is the entry-point conformance check.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402

import json

from jsonschema import Draft7Validator

BASE = Path(__file__).parent.parent
SCHEMA_PATH = BASE / "schemas" / "entity.schema.json"
ENTITIES_DIR = BASE / "entities"


def _load_schema():
    return json.loads(SCHEMA_PATH.read_text())


def main():
    schema = _load_schema()
    validator = Draft7Validator(schema)
    findings = []
    for mid, metric in load_metrics():
        for err in validator.iter_errors(metric):
            findings.append(f"{mid}: {err.message}")
    if findings:
        print("FAIL: check_metric_schema.py")
        for f in findings:
            print(f"  {f}")
        sys.exit(1)
    print(f"PASS: check_metric_schema.py ({len(load_metrics())} metrics, 0 findings)")


if __name__ == "__main__":
    main()