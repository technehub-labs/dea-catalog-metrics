"""Conformance tests for the dea-catalog-metrics 6 validation gates.

These tests run each gate against the live catalog and assert 0 findings.
If a gate fails, the test fails with the gate's findings.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

BASE = Path(__file__).parent.parent
SCRIPTS = BASE / "scripts"

GATES = [
    "check_metric_schema.py",
    "check_measurement_conformance.py",
    "check_mece_coverage.py",
    "check_evidence_anchors.py",
    "check_threshold_semantics.py",
    "check_dual_anchor.py",
]


@pytest.mark.parametrize("gate", GATES)
def test_gate_passes(gate):
    result = subprocess.run(
        ["python3", str(SCRIPTS / gate)],
        capture_output=True, text=True, cwd=str(BASE),
    )
    assert result.returncode == 0, (
        f"{gate} FAILED\nstdout: {result.stdout}\nstderr: {result.stderr}"
    )
    assert "PASS" in result.stdout
    assert "0 findings" in result.stdout or "0 MECE" in result.stdout or "0 directionality" in result.stdout or "0 dual-anchor" in result.stdout


def test_pilot_has_5_metrics():
    from conftest import BASE  # type: ignore
    n = sum(1 for _ in (BASE / "entities" / "v1-alpha").glob("*") if _.is_dir())
    assert n == 5, f"CR-MET-009: pilot must have 5 metrics (got {n})"


def test_metamodel_pointer_migrated_to_performance_metric():
    import yaml
    pointer = yaml.safe_load((BASE / "metamodel-pointer.yaml").read_text())
    assert pointer["metamodel"]["entity_id"] == "dea:PerformanceMetric", \
        f"metamodel-pointer.entity_id must be dea:PerformanceMetric (got {pointer['metamodel']['entity_id']})"
    assert "dea:entity-metric" in (pointer["metamodel"].get("legacy_ids") or []), \
        "metamodel-pointer must preserve legacy_id dea:entity-metric"


def test_dual_anchor_required_for_admitted():
    """CR-MET-009 §9 Q14: dual anchors required for admitted records."""
    import yaml
    for p in (BASE / "entities" / "v1-alpha").glob("dea:metric-*/*.yaml"):
        m = yaml.safe_load(p.read_text())
        if m.get("lifecycle_status") != "admitted":
            continue
        assert m.get("measurable_entity_kind"), \
            f"{m['id']} must declare measurable_entity_kind (CR-MET-009 §9 dual anchor 1)"
        assert m.get("reputability_tier"), \
            f"{m['id']} must declare reputability_tier (CR-MET-009 §9 dual anchor 2)"


def _norm_metamodel_required():
    """Read the normative schema's required fields from the upstream checkout.

    Returns None when the upstream repo is not available (CI fetches only the
    allocation validator, not a metamodel checkout), so the caller can skip the
    upstream assertion rather than fail on an environment that never had it.
    """
    import json
    import os
    candidates = [
        os.environ.get("DEA_METAMODEL_ROOT"),
        BASE.parent / "dea-metamodel",
        BASE / ".metamodel",
    ]
    for root in candidates:
        if not root:
            continue
        p = Path(root) / "schemas" / "entities" / "metric.json"
        if p.exists():
            return set(json.loads(p.read_text()).get("required", []))
    return None


def test_schema_supersets_dea_metamodel_metric_json():
    """CR-MET-009 Section 4: schemas/entity.schema.json is a SUPERSET of the
    normative dea-metamodel/schemas/entities/metric.json.

    The catalog adds the classification axes and the dual anchors that the
    normative entity does not carry, so the catalog's required set must CONTAIN
    the upstream one. Containment, not equality, is the correct relationship; an
    earlier revision of this test checked a hardcoded field list and never
    opened the upstream file, so an upstream schema change could not fail it.
    """
    import json
    catalog = json.loads((BASE / "schemas" / "entity.schema.json").read_text())
    required = set(catalog.get("required", []))
    for field in ["id", "name", "type", "description", "version", "lifecycle_status",
                  "subject_concept", "measurement_nature",
                  "subject_classification", "purpose_classification",
                  "orientation_classification", "scope_classification",
                  "directionality", "management_significance"]:
        assert field in required, \
            f"entity.schema.json required fields must include {field!r} (got {sorted(required)})"

    upstream = _norm_metamodel_required()
    if upstream is None:
        pytest.skip("dea-metamodel checkout not available; upstream superset check skipped")
    missing = sorted(upstream - required)
    assert not missing, (
        "schemas/entity.schema.json no longer covers the normative fields "
        f"{missing}; dea-metamodel/schemas/entities/metric.json now requires "
        "them. Re-sync the catalog schema."
    )


def test_5_classification_axes_present():
    """CR-MET-002 binding: 5 classification axis files must be present."""
    classifications = BASE / "classifications"
    for name in ["subject-classifications", "purpose-classifications",
                 "orientation-classifications", "scope-classifications",
                 "management-significance-classifications"]:
        assert (classifications / f"{name}.yaml").exists(), \
            f"classifications/{name}.yaml missing (CR-MET-002 binding)"


def test_catalog_yaml_regenerated():
    """CR-MET-009 §7: CATALOG.yaml MUST be regenerated by regenerate_catalog.py."""
    import yaml
    catalog = yaml.safe_load((BASE / "CATALOG.yaml").read_text())
    assert "catalog" in catalog
    assert catalog["catalog"]["abbreviation"] == "PM"
    assert catalog["catalog"]["counts"]["total"] >= 5


def test_foundations_doc_present():
    """CR-MET-009 Section 11: docs/FOUNDATIONS.md MUST be present (parked card #427)."""
    foundations = BASE / "docs" / "FOUNDATIONS.md"
    assert foundations.exists(), "docs/FOUNDATIONS.md missing (CR-MET-009 Section 11)"
    text = foundations.read_text()
    for section in ["Scope", "Classification model", "Dual-anchor model", "MECE coverage target", "Pilot composition"]:
        assert section in text, f"FOUNDATIONS.md must cover '{section}'"


def _norm_ws(s: str) -> str:
    return " ".join(s.split())


def test_readme_definition_matches_description():
    """CR-MET-014 D3: the record README 'Definition' section must match the
    record's YAML description verbatim (whitespace-normalised), so the two
    prose surfaces cannot diverge silently (board card #602)."""
    import re
    import yaml
    for p in sorted((BASE / "entities" / "v1-alpha").glob("dea:metric-*/*.yaml")):
        m = yaml.safe_load(p.read_text())
        desc = m.get("description")
        assert desc, f"{m['id']}: missing required description (CR-MET-014)"
        readme = (p.parent / "README.md").read_text()
        match = re.search(r"##\s*\d+\.\s*Definition\s*\n+(.*?)(?=\n##|\Z)", readme, re.S)
        assert match, f"{m['id']}: README has no 'Definition' section"
        assert _norm_ws(match.group(1)) == _norm_ws(desc), (
            f"{m['id']}: README Definition and YAML description diverge; "
            "edit both together (CR-MET-014 D3)"
        )


def test_catalog_regeneration_is_idempotent():
    """CR-MET-014 D6: regenerate_catalog.py must produce byte-identical output
    on consecutive runs (board card #580). last_modified is derived from record
    provenance, not the run date."""
    before = (BASE / "CATALOG.yaml").read_bytes()
    for _ in range(2):
        result = subprocess.run(
            ["python3", str(SCRIPTS / "regenerate_catalog.py")],
            capture_output=True, text=True, cwd=str(BASE),
        )
        assert result.returncode == 0, f"regenerate_catalog.py failed: {result.stderr}"
    after = (BASE / "CATALOG.yaml").read_bytes()
    assert after == before, "CATALOG.yaml changed across regeneration runs (not idempotent)"