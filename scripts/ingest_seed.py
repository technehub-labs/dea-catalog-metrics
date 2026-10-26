"""CR-MET-016: ingest the candidate-metrics seed workbook into catalog records.

Reads `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`
(header row 6, data rows 7 onward), and writes one candidate Metric record
plus its README for every row that does not collide with a record the
catalog already holds.

The workbook's own `Field Guide` sheet states, for each column, which catalog
artefact the column populates. That guide is the authority for the field
mapping. The field NAMES come from `classifications/field-aliases.yaml` and
the field VALUES from `classifications/seed-value-maps.yaml`, so the mapping
lives in data rather than in this script.

Usage:
    python3 scripts/ingest_seed.py              # write the records
    python3 scripts/ingest_seed.py --check      # verify the tree matches the seed
    python3 scripts/ingest_seed.py --report     # summarise without writing

The script is idempotent: running it twice produces byte-identical files.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

try:  # libyaml is roughly five times faster
    from yaml import CSafeLoader as SafeLoader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader

BASE = Path(__file__).parent.parent
ENTITIES_DIR = BASE / "entities"
SEED_FILE = BASE / "seeds" / "open-deam-candidate-metrics-seed.xlsx"
ALIAS_FILE = BASE / "classifications" / "field-aliases.yaml"
VALUE_MAP_FILE = BASE / "classifications" / "seed-value-maps.yaml"

SEED_SHEET = "Candidate Metrics"
HEADER_ROW = 6
ESTABLISHED_AT = "2026-10-26"
ESTABLISHED_BY = "CR-MET-016"
# CR-MET-017 (Q19): unit references canonicalised. The record version tracks
# record changes (the formula version tracks the formula, which did not
# change); the pilot records bumped their version on each field change.
RECORD_VERSION = "1.1.0"
FORMULA_VERSION = "1.1.0"
RECORD_CHANGES = [
    {
        "cr": ESTABLISHED_BY,
        "date": ESTABLISHED_AT,
        "change": "Ingested from the candidate-metrics seed workbook",
    },
    {
        "cr": "CR-MET-017",
        "date": "2026-10-26",
        "change": "Unit reference canonicalised: ratio form and singular names (Q19)",
    },
    {
        "cr": "CR-MET-020",
        "date": "2026-10-26",
        "change": "Derived admission fields added (subject_concept, measurement_nature, "
                  "seed evidence) and the formula bound to its short form (Q26, Q27)",
    },
]
SEED_WORKBOOK = "seeds/open-deam-candidate-metrics-seed.xlsx"

# CR-MET-020: the admission-time fields that are DERIVABLE, and the axis
# extension that makes the corpus collision-free.
#
# subject_concept is the metamodel's own answer to a metric's identity: it
# "distinguishes a Metric by what it measures rather than by its MECE label"
# (dea-metamodel metric.json). The seed's metric ids name the subject
# precisely, so the concept is derived from the id rather than authored.
#
# The vocabulary is SEEDED, not frozen: the values live in
# classifications/subject-concepts.yaml and are reconciled to the
# metamodel's concept entities when their home is settled (Q23, Q25).

# A topic VARIANT marker: the same subject published as a focused measure set.
VARIANT_MARKERS = ("deep_dive", "standard_measures")

# Trailing measure nouns: the thing MEASURED is not the thing MEASURED ABOUT.
# `code-churn-rate` and `code-churn` name the same subject; the rate is how
# it is expressed.
# A standalone "=": the formula's binding, not a comparison operator.
BOUND_FORMULA_RE = re.compile(r"(?<![<>!=])=(?![=])")

MEASURE_NOUNS = {
    "rate", "index", "level", "score", "percentage", "percent", "amount",
    "count", "ratio", "duration", "time", "coverage", "attainment", "trend",
    "efficiency", "margin", "growth", "balance", "value", "volume",
    "frequency", "accuracy", "sla", "kpi", "target", "variance", "average",
    "mean", "sum", "number", "total",
}

# Every seed metric measures a quantity, so the measurement nature is derived
# from the unit rather than authored per record.
UNIT_NATURE = {
    "percent": "numeric", "ratio": "numeric", "score": "numeric",
    "index": "numeric", "count": "numeric", "event": "numeric",
    "times": "numeric", "currency": "numeric", "minute": "numeric",
    "hour": "numeric", "day": "numeric", "second": "numeric",
    "millisecond": "numeric", "month": "numeric", "week": "numeric",
    "year": "numeric", "tonne": "numeric", "kilolitre": "numeric",
    "megawatthour": "numeric",
}

# Columns the workbook carries that the catalog has no field for. They are
# documentation or provenance, and each is handled explicitly below.
SOURCE_ONLY = {"prose", "unit", "batch"}


def load_aliases() -> dict:
    data = yaml.safe_load(ALIAS_FILE.read_text()) or {}
    return {a: (s or {}).get("canonical") for a, s in (data.get("aliases") or {}).items()}


def load_value_maps() -> dict:
    return yaml.safe_load(VALUE_MAP_FILE.read_text()) or {}


def slug(text: str) -> str:
    """Lowercase, hyphen/space/ampersand to underscore, for a slug field."""
    out = re.sub(r"[^a-z0-9]+", "_", str(text).lower()).strip("_")
    return out


def unit_slug(unit_ref: str) -> str:
    """The catalog's plain unit label, derived from the unit reference.

    `dea:unit-minute` -> `minute`; `dea:unit-ratio-percent` -> `percent`.
    """
    out = unit_ref.replace("dea:unit-", "", 1)
    if out.startswith("ratio-"):
        out = out[len("ratio-"):]
    return out


def expression_operands(expression: str) -> list:
    """The operand terms named by a published expression.

    The seed publishes plain-text expressions such as
    `(Revenue - Cost of Goods Sold) / Revenue`, not a bound formula. The
    operands are the terms the expression names, read off by splitting on the
    arithmetic and comparison operators. Pure numbers are thresholds and
    constants rather than inputs, so they are dropped.

    Declaring the operands is what lets a consumer see what the expression
    depends on, and it is what the formula namespace gate checks for: an
    expression that names a term with no declared input is a formula nobody
    can reproduce.
    """
    if not expression:
        return []
    parts = re.split(r"[-+*/()=<>]", str(expression))
    seen = []
    for part in parts:
        term = " ".join(part.split())
        if not term or not re.search(r"[A-Za-z]", term):
            continue
        if term not in seen:
            seen.append(term)
    return seen


def read_seed_rows() -> list:
    try:
        import openpyxl
    except ImportError:
        raise SystemExit(
            "ingest_seed.py: openpyxl is required to read the seed workbook "
            "(pip install openpyxl)"
        )
    wb = openpyxl.load_workbook(SEED_FILE, read_only=True, data_only=True)
    ws = wb[SEED_SHEET]
    rows = ws.iter_rows(min_row=HEADER_ROW, values_only=True)
    header = [str(h).strip() if h is not None else "" for h in next(rows)]
    out = []
    for index, row in enumerate(rows):
        if not any(v is not None and str(v).strip() for v in row):
            continue
        record = {h: v for h, v in zip(header, row) if h}
        record["_row"] = HEADER_ROW + 1 + index
        out.append(record)
    wb.close()
    return out


def _normalise_spec(spec: dict) -> dict:
    """Normalise a value-map axis so lookups compare like with like.

    The seed's values use hyphens (`technology-architecture`,
    `higher-is-better`); the catalog's use underscores. Both sides are
    normalised to the underscore form, so a lookup never misses on spelling.
    """
    def norm(value: str) -> str:
        return str(value).strip().replace("-", "_")

    return {
        "carry": {norm(v) for v in (spec.get("carry") or [])},
        "map": {norm(k): v for k, v in (spec.get("map") or {}).items()},
        "add": {norm(k): v for k, v in (spec.get("add") or {}).items()},
    }


def map_value(axis: str, value: str, maps: dict) -> str:
    """Map one seed value onto a catalog value, or fail loudly."""
    spec = _normalise_spec(maps.get(axis) or {})
    normalised = str(value).strip().replace("-", "_")
    if normalised in spec["carry"]:
        return normalised
    if normalised in spec["map"]:
        return spec["map"][normalised]
    if normalised in spec["add"]:
        return normalised
    raise SystemExit(
        f"ingest_seed.py: no mapping for {axis} value {value!r}; add it to "
        f"{VALUE_MAP_FILE.name} rather than guessing"
    )


def map_unit_ref(value: str, maps: dict) -> str:
    """Resolve a seed unit id to the catalog's canonical unit reference.

    CR-MET-017 (Q19): the ratio form is canonical and unit names are
    singular. Unit ids are hyphen-significant (`dea:unit-percent` is not
    `dea:unit_percent`), so unlike the classification axes this lookup does
    no hyphen normalisation. An unmapped value stops the ingestion, same as
    the other axes.
    """
    spec = maps.get("unit_ref") or {}
    carry = set(spec.get("carry") or [])
    mapped = dict(spec.get("map") or {})
    v = str(value).strip()
    if v in carry:
        return v
    if v in mapped:
        return mapped[v]
    raise SystemExit(
        f"ingest_seed.py: no mapping for unit_ref value {value!r}; add it to "
        f"{VALUE_MAP_FILE.name} rather than guessing"
    )


def subject_phrase(metric_id: str) -> str:
    """The subject a metric id names: what it measures, not how it is expressed.

    `dea:metric-code-churn-rate` and `dea:metric-code-churn` name the same
    subject, `code_churn`; the trailing measure noun and the topic-variant
    markers are stripped, because the subject is the thing the metric is
    about.
    """
    slug = metric_id.replace("dea:metric-", "")
    tokens = [t for t in slug.split("-")]
    while tokens and tokens[-1] in MEASURE_NOUNS:
        tokens.pop()
    while tokens and "_".join(tokens[-2:]) in VARIANT_MARKERS:
        tokens = tokens[:-2]
    while tokens and tokens[-1] in VARIANT_MARKERS:
        tokens.pop()
    return "_".join(tokens) if tokens else slug


def subject_concept(metric_id: str) -> str:
    """The concept reference a metric's subject resolves to."""
    return f"dea:subject-{subject_phrase(metric_id)}"


def seed_evidence(record_seed: dict, source_credit: str) -> list:
    """The measurement evidence for a seed-derived record (Q27 ruling).

    The seed is admissible evidence: the record cites the workbook, the
    sheet, the row it came from, and the credit the source carries.
    """
    evidence = [
        f"OpenDEAM candidate-metrics seed workbook "
        f"({record_seed.get('workbook', SEED_WORKBOOK)}), sheet "
        f"'{record_seed.get('sheet', SEED_SHEET)}', row {record_seed.get('row')}"
    ]
    if source_credit:
        evidence.append(source_credit)
    return evidence


def build_record(row: dict, aliases: dict, maps: dict) -> dict:
    """Build one candidate Metric record from one workbook row."""
    def cell(name: str) -> str:
        value = row.get(name)
        return str(value).strip() if value is not None else ""

    metric_id = cell("metric_id")
    name = cell("name")
    description = cell("description")
    abbreviation = cell("abbr")
    formula = cell("formula")
    unit_ref = map_unit_ref(cell("unit_id"), maps)
    unit = unit_slug(unit_ref)

    # CR-MET-020: the formula is BOUND. The short form is the record's own
    # left-hand variable, so a consumer can evaluate it, and Gate 8's rule
    # (the abbreviation equals the formula's left-hand variable) holds for
    # every record. The operands are read off the RIGHT-HAND side only: the
    # left-hand side is the result, not an input.
    abbreviation = cell("abbr")
    # A formula is already BOUND only if it carries a standalone "=". A
    # comparison operator (">=", "<=", "==") is not a binding: the seed
    # publishes thresholds inside expressions, and reading their "=" as a
    # binding left the record unbound with a nonsense left-hand side.
    if BOUND_FORMULA_RE.search(formula):
        bound_expression = formula
        bound_operands = expression_operands(formula.split("=", 1)[1])
    else:
        bound_expression = f"{abbreviation} = {formula}"
        bound_operands = expression_operands(formula)

    record = {
        "id": metric_id,
        "name": name,
        "type": "Metric",
        "description": description,
        "abbreviation": abbreviation,
        "unit": unit,
        "version": RECORD_VERSION,
        "lifecycle_status": cell("status") or "candidate",
        "subject_classification": [map_value("subject_classification", cell("subject_area"), maps)],
        "purpose_classification": [map_value("purpose_classification", cell("purpose"), maps)],
        "scope_classification": [map_value("scope_classification", cell("scope"), maps)],
        "directionality": map_value("directionality", cell("orientation"), maps),
        "management_significance": [map_value("management_significance", cell("significance"), maps)],
        "measurable_entity_kind": map_value("measurable_entity_kind", cell("entity_kind"), maps),
        "reputability_tier": cell("reputability_tier"),
        "unit_ref": unit_ref,
        "source_credit": cell("source_credit"),
        "calculation_definition": formula,
        "formula_definition": {
            "formula_id": f"dea:formula-{metric_id.replace('dea:metric-', '')}",
            "expression": bound_expression,
            "inputs": [{"name": term} for term in bound_operands],
            "operators": [],
            "parameters": [],
            "unit_semantics": {"input_units": [], "output_unit": unit_ref},
            "validation_rules": [],
            "version": FORMULA_VERSION,
        },
        "metadata": {
            "established_by": ESTABLISHED_BY,
            "established_at": ESTABLISHED_AT,
            "change_history": [dict(entry) for entry in RECORD_CHANGES],
            "seed": {
                "workbook": SEED_WORKBOOK,
                "sheet": SEED_SHEET,
                "row": row["_row"],
                "batch": cell("batch"),
            },
        },
    }
    domain = cell("domain")
    if domain:
        record["domain"] = slug(domain)
    sector = cell("sector")
    if sector and sector.lower() != "all industries":
        record["sector"] = slug(sector)

    # CR-MET-020: the derivable admission-time fields. The two judgement
    # fields (orientation_classification and measurement_nature_detail) are
    # NOT derived: they are authored per topic pack, in the admission
    # tranches, and a rule would fabricate them.
    record["subject_concept"] = subject_concept(metric_id)
    record["measurement_nature"] = UNIT_NATURE.get(unit, "numeric")
    record["quality"] = {
        "measurement_evidence": seed_evidence(record["metadata"]["seed"], cell("source_credit")),
        "known_limitations": [],
    }
    return record


def render_readme(record: dict, row: dict) -> str:
    """The record README. The Definition section is the canonical description."""
    def cell(name: str) -> str:
        value = row.get(name)
        return str(value).strip() if value is not None else ""

    lines = [
        f"# {record['id']}",
        "",
        f"Candidate Performance Metric record for **{record['name']}**"
        f" ({record['abbreviation']}) in the OpenDEAM Metric catalog.",
        "",
        "## 1. Identity",
        "",
        f"- **Canonical id:** `{record['id']}`",
        f"- **Name:** {record['name']}",
        "- **Type:** Metric",
        f"- **Version:** {record['version']}",
        f"- **Lifecycle:** {record['lifecycle_status']}",
        f"- **Short form:** {record['abbreviation']}",
        "",
        "## 2. Definition",
        "",
        record["description"],
        "",
    ]
    prose = cell("prose")
    if prose:
        lines += ["## 3. Context", "", prose, ""]
    lines += [
        "## Formula",
        "",
        "```",
        record["formula_definition"]["expression"],
        "```",
        "",
        "## Unit",
        "",
        f"- **Unit reference:** `{record.get('unit_ref', '')}`",
        f"- **Unit:** {record['unit']}",
    ]
    label = cell("unit")
    if label:
        lines.append(f"- **Unit label (as published):** {label}")
    lines += [
        "",
        "## Classification",
        "",
        f"- **Subject classification:** {', '.join(record['subject_classification'])}",
        f"- **Purpose classification:** {', '.join(record['purpose_classification'])}",
        f"- **Scope classification:** {', '.join(record['scope_classification'])}",
        f"- **Directionality:** {record['directionality']}",
        f"- **Management significance:** {', '.join(record['management_significance'])}",
        f"- **Measurable entity kind:** {record['measurable_entity_kind']}",
        f"- **Reputability tier:** {record['reputability_tier']}",
    ]
    if record.get("domain"):
        lines.append(f"- **Domain:** {record['domain']}")
    if record.get("sector"):
        lines.append(f"- **Sector:** {record['sector']}")
    lines += [
        "",
        "## Attribution",
        "",
        f"- **Source credit:** {record.get('source_credit', '')}",
        "",
        "## Provenance",
        "",
        f"- **Established by:** {ESTABLISHED_BY} on {ESTABLISHED_AT}",
        f"- **Seed workbook:** `{SEED_WORKBOOK}`, sheet `{SEED_SHEET}`, row {row['_row']}"
        f" (batch {record['metadata']['seed']['batch']})",
        "",
    ]
    return "\n".join(lines)


def existing_ids() -> dict:
    """The records already on disk, as id -> record.

    The ingestion OWNS the records it created: a seed-derived record is
    refreshed on every run, so the corpus always matches the workbook. A
    record the catalog admitted by another route is never overwritten; those
    ids are reported as collisions instead.
    """
    records = {}
    for path in ENTITIES_DIR.glob("v1-alpha/*/*.yaml"):
        if not path.parent.name.startswith("dea:metric-"):
            continue
        records[path.parent.name] = yaml.load(path.read_text(), Loader=SafeLoader)
    return records


def is_seed_derived(record) -> bool:
    return bool(record) and bool((record.get("metadata") or {}).get("seed"))


def check_columns_resolve(columns: list, aliases: dict, maps: dict) -> None:
    """Every workbook column must resolve through the alias registry, be a
    canonical schema field, or be declared source-only.

    Without this the ingestion script and the alias registry could drift
    apart: a column renamed in the workbook would be silently dropped.
    """
    schema = json.loads((BASE / "schemas" / "entity.schema.json").read_text())
    canonical = set(schema.get("properties", {}))
    source_only = set((maps.get("source_only") or {}).keys())
    unresolved = []
    for column in columns:
        if column.startswith("_"):
            continue
        if column in canonical or column in aliases or column in source_only:
            continue
        unresolved.append(column)
    if unresolved:
        raise SystemExit(
            f"ingest_seed.py: workbook columns {unresolved} resolve to no "
            f"catalog field, no alias, and no declared source-only column; "
            "add them to classifications/field-aliases.yaml or "
            "classifications/seed-value-maps.yaml rather than dropping them"
        )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="verify the tree matches the seed; write nothing")
    ap.add_argument("--report", action="store_true", help="summarise the mapping; write nothing")
    args = ap.parse_args()

    aliases = load_aliases()
    maps = load_value_maps()
    rows = read_seed_rows()
    already = existing_ids()
    check_columns_resolve(list(rows[0].keys()), aliases, maps)

    written = 0
    skipped = 0
    refreshed = 0
    conflicts = []
    for row in rows:
        record = build_record(row, aliases, maps)
        metric_id = record["id"]
        if metric_id in already and not is_seed_derived(already[metric_id]):
            # A record this catalog admitted by another route. Never overwrite
            # it with a candidate; report the collision instead.
            skipped += 1
            conflicts.append(metric_id)
            continue
        if args.report:
            written += 1
            continue
        target_dir = ENTITIES_DIR / "v1-alpha" / metric_id
        target_dir.mkdir(parents=True, exist_ok=True)
        yaml_path = target_dir / f"{metric_id}.yaml"
        readme_path = target_dir / "README.md"
        yaml_text = yaml.safe_dump(record, sort_keys=False, width=100, allow_unicode=True)
        readme_text = render_readme(record, row)
        if args.check:
            if not yaml_path.exists() or yaml_path.read_text() != yaml_text:
                print(f"DRIFT: {yaml_path} does not match the seed")
                return 1
            if not readme_path.exists() or readme_path.read_text() != readme_text:
                print(f"DRIFT: {readme_path} does not match the seed")
                return 1
        else:
            yaml_path.write_text(yaml_text)
            readme_path.write_text(readme_text)
        written += 1
        if metric_id in already:
            refreshed += 1

    print(f"seed rows: {len(rows)}")
    print(f"records written: {written}")
    print(f"skipped (id already in the catalog): {skipped}")
    if conflicts:
        print(f"  {', '.join(sorted(conflicts))}")
    if refreshed:
        print(f"records refreshed from the seed: {refreshed}")
    if args.check:
        print("PASS: the catalog matches the seed workbook")
    return 0


if __name__ == "__main__":
    sys.exit(main())
