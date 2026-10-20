"""CR-MET-009 Gate 4: check_evidence_anchors.py.

Each admitted Metric MUST carry:
- metadata.established_by (CR reference)
- at least one quality.measurement_evidence reference
CR-MM-04 R1 binding.
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
        meta = m.get("metadata") or {}
        if not meta.get("established_by"):
            findings.append(f"{mid}: missing metadata.established_by")
        q = m.get("quality") or {}
        ev = q.get("measurement_evidence") or []
        if not ev:
            findings.append(f"{mid}: missing quality.measurement_evidence")
    if findings:
        print("FAIL: check_evidence_anchors.py")
        for f in findings:
            print(f"  {f}")
        sys.exit(1)
    n = sum(1 for _, m in _load_metrics() if m.get("lifecycle_status") == "admitted")
    print(f"PASS: check_evidence_anchors.py ({n} admitted metrics, 0 findings)")


if __name__ == "__main__":
    main()