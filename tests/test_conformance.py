"""Conformance tests for the dea-catalog-metrics 6 validation gates.

These tests run each gate against the live catalog and assert 0 findings.
If a gate fails, the test fails with the gate's findings.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

BASE = Path(__file__).parent.parent
SCRIPTS = BASE / "scripts"
sys.path.insert(0, str(SCRIPTS))
from _catalog import load_metrics, load_metric_paths  # noqa: E402

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


def test_corpus_matches_the_seed_workbook():
    """CR-MET-016: the corpus must match the seed workbook exactly.

    The seed carries 4428 metric rows. Five of them are records this catalog
    admitted by another route, so those rows are reported as collisions rather
    than ingested. Every other row must be present as a candidate record whose
    provenance points back at the workbook row it came from.

    This replaces the pilot-era assertion that the catalog holds exactly 5
    records, which turned red on any addition (board card #588).
    """
    from conftest import BASE  # type: ignore
    import yaml
    try:
        import openpyxl
    except ImportError:
        pytest.skip("openpyxl not available; seed corpus check skipped")

    seed = BASE / "seeds" / "open-deam-candidate-metrics-seed.xlsx"
    if not seed.exists():
        pytest.skip("seed workbook not present; seed corpus check skipped")
    wb = openpyxl.load_workbook(seed, read_only=True, data_only=True)
    ws = wb["Candidate Metrics"]
    rows = ws.iter_rows(min_row=6, values_only=True)
    header = [str(h).strip() if h is not None else "" for h in next(rows)]
    data = [dict(zip(header, r)) for r in rows
            if any(v is not None and str(v).strip() for v in r)]
    wb.close()

    expected = {str(r["metric_id"]).strip(): r for r in data}
    records = {}
    for p in sorted((BASE / "entities" / "v1-alpha").glob("dea:metric-*/*.yaml")):
        records[p.parent.name] = yaml.safe_load(p.read_text())

    seed_derived = {
        mid: r for mid, r in records.items()
        if (r.get("metadata") or {}).get("seed")
    }
    assert set(seed_derived) == set(expected) - {
        mid for mid in expected
        if mid in records and not (records[mid].get("metadata") or {}).get("seed")
    }, "the seed-derived records do not match the workbook's metric ids"

    # provenance: every record must point back at its own workbook row
    for mid, r in seed_derived.items():
        seed_meta = r["metadata"]["seed"]
        assert seed_meta["workbook"] == "seeds/open-deam-candidate-metrics-seed.xlsx"
        assert seed_meta["sheet"] == "Candidate Metrics"
        row_number = seed_meta["row"]
        source = expected[mid]
        assert str(source["name"]).strip() == r["name"], (
            f"{mid}: record name does not match the workbook row"
        )
        assert row_number >= 7, f"{mid}: provenance row {row_number} is inside the header block"


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
    for field in ["id", "name", "type", "description", "abbreviation", "unit", "version", "lifecycle_status",
                  "subject_classification", "purpose_classification",
                  "scope_classification",
                  "directionality", "management_significance"]:
        assert field in required, \
            f"entity.schema.json required fields must include {field!r} (got {sorted(required)})"

    # CR-MET-016: the admission-time fields are required of every record that
    # is not a candidate. They live in the schema's allOf/else branch, so the
    # base required set alone no longer proves them.
    admitted_extra = set()
    for clause in catalog.get("allOf", []):
        admitted_extra |= set((clause.get("else") or {}).get("required", []))
    for field in ["subject_concept", "measurement_nature",
                  "orientation_classification", "measurement_nature_detail"]:
        assert field in admitted_extra, (
            f"entity.schema.json must require {field!r} for non-candidate records "
            f"(got {sorted(admitted_extra)})"
        )

    upstream = _norm_metamodel_required()
    if upstream is None:
        pytest.skip("dea-metamodel checkout not available; upstream superset check skipped")
    # CR-MET-016: the schema's required set is lifecycle-aware. An admitted
    # record must carry the base fields AND the admission-time fields, so the
    # set the catalog guarantees for an admitted record is the union.
    missing = sorted(upstream - (required | admitted_extra))
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
    for p, m in load_metric_paths():
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


def _alias_map():
    import yaml
    data = yaml.safe_load((BASE / "classifications" / "field-aliases.yaml").read_text())
    return {a: (s or {}).get("canonical") for a, s in (data.get("aliases") or {}).items()}


def test_alias_registry_resolves_to_schema_properties():
    """CR-MET-015 D8.1/D8.2: every alias resolves to a declared schema property
    and no alias collides with a canonical property name."""
    import json
    declared = set(json.loads((BASE / "schemas" / "entity.schema.json").read_text())["properties"])
    for alias, canonical in _alias_map().items():
        assert canonical, f"alias {alias!r} has no canonical target"
        assert canonical in declared, f"alias {alias!r} points at {canonical!r}, not declared by the schema"
        assert alias not in declared, f"alias {alias!r} is also a canonical schema property"


def test_stored_records_use_canonical_names_only():
    """CR-MET-015 D8.3/D8.4: no stored record uses an alias name, and none
    carries both spellings of one field."""
    import yaml
    aliases = _alias_map()
    for _mid, m in load_metrics():
        for alias, canonical in aliases.items():
            assert alias not in m, f"{m['id']}: stored record uses alias {alias!r} instead of {canonical!r}"
            assert not (alias in m and canonical in m), f"{m['id']}: carries both {alias!r} and {canonical!r}"


def test_abbreviation_matches_formula_short_form():
    """CR-MET-015 D2: abbreviation equals the left-hand variable of the formula."""
    import yaml
    for _mid, m in load_metrics():
        if m.get("lifecycle_status") != "admitted":
            continue
        expression = ((m.get("formula_definition") or {}).get("expression") or "")
        short = expression.split("=")[0].strip()
        assert m.get("abbreviation"), f"{m['id']}: missing abbreviation"
        assert m["abbreviation"] == short, (
            f"{m['id']}: abbreviation {m['abbreviation']!r} does not equal the "
            f"formula short form {short!r}"
        )


def test_unit_is_coherent_with_unit_ref():
    """CR-MET-015 D3: unit_ref is dea:unit-<unit> or dea:unit-ratio-<unit>."""
    import yaml
    for _mid, m in load_metrics():
        if m.get("lifecycle_status") != "admitted":
            continue
        unit_ref, unit = m.get("unit_ref"), m.get("unit")
        if not unit_ref:
            continue
        assert unit, f"{m['id']}: missing unit"
        assert unit_ref in {f"dea:unit-{unit}", f"dea:unit-ratio-{unit}"}, (
            f"{m['id']}: unit {unit!r} is not coherent with unit_ref {unit_ref!r}"
        )


def test_source_credit_is_among_measurement_evidence():
    """CR-MET-015 D5: a credit that is not evidence is rejected.

    CR-MET-016: the rule binds admitted records. A candidate carries the
    credit its source published, and the evidence that backs it is a
    requirement of admission, not of candidacy.
    """
    import yaml
    for _mid, m in load_metrics():
        if m.get("lifecycle_status") != "admitted":
            continue
        credit = m.get("source_credit")
        if not credit:
            continue
        evidence = (m.get("quality") or {}).get("measurement_evidence") or []
        assert credit in evidence, (
            f"{m['id']}: source_credit {credit!r} is not among the measurement evidence"
        )


def test_normalizer_canonicalises_aliases_and_is_idempotent():
    """CR-MET-015 D7: the ingestion normaliser rewrites alias names, refuses a
    record carrying both spellings with different values, and is idempotent."""
    import sys
    import yaml
    sys.path.insert(0, str(SCRIPTS))
    from normalize_record import canonicalize  # type: ignore

    aliases = _alias_map()
    external = {
        "id": "dea:metric-example",
        "metric id": "dea:metric-example",
        "name": "Example",
        "description": "An example.",
        "abbreviation": "EX",
        "unit": "percent",
        "subject_area": ["technology_architecture"],
        "status": "candidate",
    }
    canonical, changes, conflicts = canonicalize(external, aliases)
    assert not conflicts, f"unexpected conflicts: {conflicts}"
    assert canonical["id"] == "dea:metric-example"
    assert "metric id" not in canonical
    assert canonical["subject_classification"] == ["technology_architecture"]
    assert canonical["lifecycle_status"] == "candidate"
    assert changes, "normaliser reported no changes for an alias-spelled record"

    # idempotent: canonicalising a canonical record changes nothing
    again, changes2, conflicts2 = canonicalize(canonical, aliases)
    assert again == canonical
    assert not changes2
    assert not conflicts2

    # a record carrying both spellings with different values is a conflict
    both = {"subject_area": ["a"], "subject_classification": ["b"]}
    _, _, conflicts3 = canonicalize(both, aliases)
    assert conflicts3, "normaliser accepted both spellings with different values"

    # a record carrying both spellings with equal values is accepted
    same = {"subject_area": ["a"], "subject_classification": ["a"]}
    out, _, conflicts4 = canonicalize(same, aliases)
    assert not conflicts4
    assert out["subject_classification"] == ["a"]
    assert "subject_area" not in out