"""CR-MET-016: report the catalog's classification coverage.

The candidate-metrics seed turns the catalog from a 5-record pilot into a
corpus of 4428 metrics. This script reports how that corpus is distributed
across the classification axes, the domains and the sectors, so coverage is
visible rather than implied.

It is a report, not a gate: it prints and exits 0. A gate that fails on
coverage would be a gate on the data rather than on the catalog, and the
owner decides what coverage should be.

Usage:
    python3 scripts/report_coverage.py
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402


def _axis(record: dict, key: str) -> list:
    value = record.get(key)
    if value is None:
        return []
    return [value] if isinstance(value, str) else list(value)


def main() -> int:
    metrics = load_metrics()
    admitted = [m for _, m in metrics if m.get("lifecycle_status") == "admitted"]
    candidates = [m for _, m in metrics if m.get("lifecycle_status") == "candidate"]

    print("=" * 72)
    print("Catalog coverage")
    print("=" * 72)
    print(f"  records total          : {len(metrics)}")
    print(f"  admitted               : {len(admitted)}")
    print(f"  candidate              : {len(candidates)}")
    print()

    for axis in [
        "subject_classification",
        "purpose_classification",
        "scope_classification",
        "management_significance",
        "directionality",
        "measurable_entity_kind",
        "reputability_tier",
    ]:
        counter = Counter()
        for _, m in metrics:
            for value in _axis(m, axis):
                counter[value] += 1
        print(f"  {axis:28s} {len(counter):>3} values, {sum(counter.values()):>5} assignments")
        for value, count in counter.most_common(8):
            print(f"      {value:34s} {count:>5}")
        if len(counter) > 8:
            print(f"      ... and {len(counter) - 8} more")
        print()

    for field in ["domain", "sector"]:
        counter = Counter(m[field] for _, m in metrics if m.get(field))
        print(f"  {field:28s} {len(counter):>3} values")
        for value, count in counter.most_common(6):
            print(f"      {value:34s} {count:>5}")
        if len(counter) > 6:
            print(f"      ... and {len(counter) - 6} more")
        print()

    # the MECE signature the admission gate uses
    signatures = Counter()
    for _, m in metrics:
        signature = (
            tuple(sorted(_axis(m, "subject_classification"))),
            tuple(sorted(_axis(m, "purpose_classification"))),
            tuple(sorted(_axis(m, "orientation_classification"))),
            tuple(sorted(_axis(m, "scope_classification"))),
        )
        signatures[signature] += 1
    print(f"  MECE signatures (subject, purpose, orientation, scope)")
    print(f"      distinct signatures : {len(signatures)}")
    print(f"      records sharing a signature with another: "
          f"{sum(c for c in signatures.values() if c > 1)}")
    print(f"      largest cluster     : {max(signatures.values()) if signatures else 0}")
    print()
    print("  The MECE uniqueness rule binds ADMITTED records only. The candidate")
    print("  corpus is expected to share signatures: it is a coverage pool, and")
    print("  the axis values repeat by design.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
