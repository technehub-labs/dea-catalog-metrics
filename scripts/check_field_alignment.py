"""CR-MET-015 Gate 8: check_field_alignment.py.

Enforces the field-alias discipline and the coherence of the five field
dimensions added by CR-MET-015 (abbreviation, unit, domain, sector,
source_credit).

Checks:
  1. every alias in classifications/field-aliases.yaml resolves to a property
     the catalog schema declares (the registry cannot rot);
  2. no alias name is itself a canonical schema property (no ambiguity);
  3. no stored record uses an alias name (the catalogue stays canonical);
  4. no stored record carries both spellings of one field;
  5. abbreviation equals the left-hand variable of formula_definition.expression;
  6. unit is coherent with unit_ref: unit_ref is dea:unit-<unit> or
     dea:unit-ratio-<unit>;
  7. source_credit appears among the record's quality.measurement_evidence.

Checks 5 to 7 apply to admitted records. Candidates are held to the schema's
required fields only, matching how the other gates treat them.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402

import json

import yaml

BASE = Path(__file__).parent.parent
SCHEMA_PATH = BASE / "schemas" / "entity.schema.json"
ALIAS_FILE = BASE / "classifications" / "field-aliases.yaml"
ENTITIES_DIR = BASE / "entities"


def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


def _load_aliases() -> dict:
    data = yaml.safe_load(ALIAS_FILE.read_text()) or {}
    out = {}
    for alias, spec in (data.get("aliases") or {}).items():
        out[alias] = (spec or {}).get("canonical")
    return out


def _short_form(m: dict) -> str:
    expression = ((m.get("formula_definition") or {}).get("expression") or "")
    return expression.split("=")[0].strip()


def main() -> int:
    schema = _load_schema()
    declared = set(schema.get("properties", {}))
    aliases = _load_aliases()
    findings = []

    # 1. every alias resolves to a declared property
    for alias, canonical in sorted(aliases.items()):
        if not canonical:
            findings.append(f"alias registry: {alias!r} has no canonical target")
        elif canonical not in declared:
            findings.append(
                f"alias registry: {alias!r} points at {canonical!r}, "
                "which the catalog schema does not declare"
            )

    # 2. an alias must not collide with a canonical property name
    for alias in sorted(aliases):
        if alias in declared:
            findings.append(
                f"alias registry: {alias!r} is also a canonical schema property; "
                "the alias is ambiguous"
            )

    for mid, m in load_metrics():
        # 3. no stored record uses an alias name
        for alias in sorted(aliases):
            if alias in m:
                findings.append(
                    f"{mid}: uses alias field {alias!r}; stored records must use the "
                    f"canonical name {aliases[alias]!r}"
                )
        # 4. no record carries both spellings
        for alias, canonical in sorted(aliases.items()):
            if alias in m and canonical in m:
                findings.append(f"{mid}: carries both {alias!r} and {canonical!r}")

        if m.get("lifecycle_status") != "admitted":
            continue

        # 5. abbreviation equals the formula short form
        abbreviation = m.get("abbreviation")
        short = _short_form(m)
        if short:
            if not abbreviation:
                findings.append(f"{mid}: missing abbreviation")
            elif abbreviation != short:
                findings.append(
                    f"{mid}: abbreviation {abbreviation!r} does not equal the formula "
                    f"short form {short!r}"
                )

        # 6. unit is coherent with unit_ref
        unit = m.get("unit")
        unit_ref = m.get("unit_ref")
        if unit_ref:
            if not unit:
                findings.append(f"{mid}: missing unit")
            else:
                expected = {f"dea:unit-{unit}", f"dea:unit-ratio-{unit}"}
                if unit_ref not in expected:
                    findings.append(
                        f"{mid}: unit {unit!r} is not coherent with unit_ref "
                        f"{unit_ref!r}; expected one of {sorted(expected)}"
                    )

        # 7. source_credit appears among the measurement evidence
        credit = m.get("source_credit")
        if credit:
            evidence = (m.get("quality") or {}).get("measurement_evidence") or []
            if credit not in evidence:
                findings.append(
                    f"{mid}: source_credit {credit!r} is not among the record's "
                    "quality.measurement_evidence entries"
                )

    if findings:
        print("FAIL: check_field_alignment.py")
        for f in findings:
            print(f"  {f}")
        sys.exit(1)

    n = sum(1 for _, m in load_metrics() if m.get("lifecycle_status") == "admitted")
    print(f"PASS: check_field_alignment.py ({n} admitted metrics, 0 findings)")
    return 0


if __name__ == "__main__":
    main()
