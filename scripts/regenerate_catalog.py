"""Regenerate CATALOG.yaml from entities/v1-alpha/*/*.yaml.

Each Metric becomes an entry in the catalog entities list.
"""
from __future__ import annotations

import sys
from pathlib import Path
from datetime import date

import yaml

BASE = Path(__file__).parent.parent
ENTITIES_DIR = BASE / "entities"
CATALOG_PATH = BASE / "CATALOG.yaml"


def main():
    metrics = []
    for path in sorted(ENTITIES_DIR.glob("v1-alpha/*/*.yaml")):
        if path.parent.name.startswith("dea:metric-"):
            m = yaml.safe_load(path.read_text())
            metrics.append({
                "id": m["id"],
                "name": m["name"],
                "lifecycle_status": m.get("lifecycle_status"),
                "subject_classification": m.get("subject_classification"),
                "directionality": m.get("directionality"),
                "path": f"entities/v1-alpha/{path.parent.name}/{path.name}",
                "last_modified": str(date.today()),
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