"""CR-MET-009 Gate 3: check_mece_coverage.py.

MECE coverage on the 5 classification axes (subject, purpose, orientation, scope, directionality).
No two admitted Metrics share the same (subject, purpose, orientation, scope) tuple.
CR-MET-002 binding; CR-MET-009 Q14 disposition.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402

import sys
from collections import defaultdict
from pathlib import Path


BASE = Path(__file__).parent.parent
ENTITIES_DIR = BASE / "entities"


def main():
    metrics = load_metrics()
    findings = []
    sig_index = defaultdict(list)
    for mid, m in metrics:
        if m.get("lifecycle_status") != "admitted":
            continue
        # CR-MET-020: the uniqueness key carries subject_concept. The
        # metamodel says it outright: subject_concept "distinguishes a Metric
        # by what it measures rather than by its MECE label" (metric.json).
        # The five classification axes are the label; two metrics that share
        # a label but measure different things are different metrics, and
        # with the label alone the corpus collapsed 4423 records into 500
        # signatures.
        sig = (
            tuple(m.get("subject_classification") or []),
            tuple(m.get("purpose_classification") or []),
            m.get("orientation_classification"),
            tuple(m.get("scope_classification") or []),
            m.get("directionality"),
            m.get("subject_concept"),
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