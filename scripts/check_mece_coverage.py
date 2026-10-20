"""CR-MET-009 Gate 3: check_mece_coverage.py.

MECE coverage on the 5 classification axes (subject, purpose, orientation, scope, directionality).
No two admitted Metrics share the same (subject, purpose, orientation, scope) tuple.
CR-MET-002 binding; CR-MET-009 Q14 disposition.
"""
from __future__ import annotations

import sys
from collections import defaultdict
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
    metrics = _load_metrics()
    findings = []
    sig_index = defaultdict(list)
    for mid, m in metrics:
        if m.get("lifecycle_status") != "admitted":
            continue
        sig = (
            tuple(m.get("subject_classification") or []),
            tuple(m.get("purpose_classification") or []),
            m.get("orientation_classification"),
            tuple(m.get("scope_classification") or []),
            m.get("directionality"),
        )
        sig_index[sig].append(mid)
    for sig, ids in sig_index.items():
        if len(ids) > 1:
            findings.append(f"MECE conflict: {ids} share {sig}")
    if findings:
        print("FAIL: check_mece_coverage.py")
        for f in findings:
            print(f"  {f}")
        sys.exit(1)
    print(f"PASS: check_mece_coverage.py ({len(metrics)} metrics, 0 MECE conflicts)")


if __name__ == "__main__":
    main()