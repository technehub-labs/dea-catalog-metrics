"""CR-MET-009 Gate 2: check_measurement_conformance.py.

Metric-Measurement conformance binding (CR-MET-003):
- Every Metric with measurement_nature declared carries a formula_definition
  OR a calculation_definition (human-readable summary).
- The formula_definition.unit_semantics.output_unit is present.
- The formula_definition.expression is present.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

BASE = Path(__file__).parent.parent
ENTITIES_DIR = BASE / "entities"


def _load_metrics():
    metrics = []
    for path in sorted(ENTITIES_DIR.glob("v1-alpha/*/*.yaml")):
        if path.parent.name.startswith("dea:metric-"):
            metrics.append((path.parent.name, yaml.safe_load(path.read_text())))
    return metrics


def main():
    findings = []
    for mid, m in _load_metrics():
        if m.get("lifecycle_status") != "admitted":
            continue
        fd = m.get("formula_definition") or {}
        if not fd.get("expression"):
            findings.append(f"{mid}: missing formula_definition.expression")
        us = fd.get("unit_semantics") or {}
        if not us.get("output_unit"):
            findings.append(f"{mid}: missing formula_definition.unit_semantics.output_unit")
        if not m.get("calculation_definition"):
            findings.append(f"{mid}: missing calculation_definition (human-readable summary)")
    if findings:
        print("FAIL: check_measurement_conformance.py")
        for f in findings:
            print(f"  {f}")
        sys.exit(1)
    n = sum(1 for _, m in _load_metrics() if m.get("lifecycle_status") == "admitted")
    print(f"PASS: check_measurement_conformance.py ({n} admitted metrics, 0 findings)")


if __name__ == "__main__":
    main()