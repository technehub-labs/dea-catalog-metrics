"""CR-MET-009 Gate 5: check_threshold_semantics.py.

Directionality binding consistency:
- higher_is_better: Metric declares applicability positive
- lower_is_better: Metric declares applicability negative
- target_band: Metric declares bounded optimum
- categorical: Metric declares categorical scale_type

CR-MET-005 / CR-MET-006 binding. The directionality is declared on Metric;
the catalog-side check verifies it is one of the 4 binding values.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

BASE = Path(__file__).parent.parent
ENTITIES_DIR = BASE / "entities"

ALLOWED = {"higher_is_better", "lower_is_better", "target_band", "categorical"}


def _load_metrics():
    metrics = []
    for path in sorted(ENTITIES_DIR.glob("v1-alpha/*/*.yaml")):
        if path.parent.name.startswith("dea:metric-"):
            metrics.append((path.parent.name, yaml.safe_load(path.read_text())))
    return metrics


def main():
    findings = []
    for mid, m in _load_metrics():
        d = m.get("directionality")
        if d not in ALLOWED:
            findings.append(f"{mid}: directionality {d!r} not in {sorted(ALLOWED)}")
    if findings:
        print("FAIL: check_threshold_semantics.py")
        for f in findings:
            print(f"  {f}")
        sys.exit(1)
    n = len(_load_metrics())
    print(f"PASS: check_threshold_semantics.py ({n} metrics, 0 directionality findings)")


if __name__ == "__main__":
    main()