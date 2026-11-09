"""Regenerate CATALOG.yaml from the sharded entity tree (CR-MET-024).

Each Metric becomes an entry in the catalog entities list. Since the
CR-MET-024 shard level the tree is `entities/v1-alpha/<shard>/<id>/`, so
discovery is a recursive walk and each entry's `path` is derived from the
record id (entity-storage-layout.md §5), not from where the file sits —
a misplaced record produces a stale path that `tests/test_layout.py`
catches.

CR-MET-014: each entry projects the record's required `description`, and
`last_modified` is derived from the record's own provenance (the latest
metadata.change_history date, falling back to metadata.established_at) instead
of the run date, so two consecutive runs on an unchanged tree produce
byte-identical output.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import iter_record_yaml_paths, record_relpath  # noqa: E402

import yaml

BASE = Path(__file__).parent.parent
CATALOG_PATH = BASE / "CATALOG.yaml"


def _last_modified(m: dict) -> str:
    """Latest provenance date on the record (CR-MM-04 R1 requires both fields)."""
    meta = m.get("metadata") or {}
    dates = [c.get("date") for c in (meta.get("change_history") or []) if c.get("date")]
    if meta.get("established_at"):
        dates.append(meta["established_at"])
    if not dates:
        raise SystemExit(f"regenerate_catalog.py: {m.get('id')} has no provenance dates")
    return str(max(dates))


def main():
    metrics = []
    for path in iter_record_yaml_paths():
        if path.parent.name.startswith("dea:metric-"):
            m = yaml.safe_load(path.read_text())
            metrics.append({
                "id": m["id"],
                "name": m["name"],
                "description": m.get("description"),
                "abbreviation": m.get("abbreviation"),
                "unit": m.get("unit"),
                "lifecycle_status": m.get("lifecycle_status"),
                "subject_classification": m.get("subject_classification"),
                "directionality": m.get("directionality"),
                "path": record_relpath(m["id"]),
                "last_modified": _last_modified(m),
            })
    catalog = {
        "catalog": {
            "abbreviation": "PM",
            "counts": {
                "total": len(metrics),
                "admitted": sum(1 for m in metrics if m["lifecycle_status"] == "admitted"),
                "candidate": sum(1 for m in metrics if m["lifecycle_status"] == "candidate"),
            },
            "description": (
                "Reference catalog for Performance Metric (PM) entities. Authority: "
                "CR-MET-009 (catalog-establishment). Aligns with dea:PerformanceMetric "
                "in dea-metamodel (CR-MET-001 binding)."
            ),
            "entities": metrics,
            "cross_cutting": {
                "change_requests": "change-requests/",
                "classifications": "classifications/",
                "schemas": "schemas/",
                "validators": "scripts/",
            },
        }
    }
    CATALOG_PATH.write_text(yaml.dump(catalog, sort_keys=False))
    print(f"PASS: regenerate_catalog.py ({len(metrics)} metrics written)")


if __name__ == "__main__":
    main()