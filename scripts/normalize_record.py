"""CR-MET-015: canonicalise a Metric record's field names for ingestion.

The catalog keeps its canonical field names. A Metric contribution authored
against an external vocabulary may use an alias instead (for example
`subject_area` for `subject_classification`). This script rewrites those alias
names to their canonical names, so the record can be validated against
`schemas/entity.schema.json` afterwards.

Rules:
- A record carrying both spellings of one field is ACCEPTED only when the
  values are equal, and REJECTED otherwise. Two spellings with different
  values is a contradiction the tool must not silently resolve.
- The script is idempotent: canonicalising a canonical record changes
  nothing.

Usage:
    python3 scripts/normalize_record.py <record.yaml> [-o <output.yaml>]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).parent.parent
ALIAS_FILE = BASE / "classifications" / "field-aliases.yaml"


def load_aliases() -> dict:
    """Map alias name -> canonical name."""
    data = yaml.safe_load(ALIAS_FILE.read_text()) or {}
    out = {}
    for alias, spec in (data.get("aliases") or {}).items():
        canonical = (spec or {}).get("canonical")
        if not canonical:
            raise SystemExit(f"normalize_record.py: alias {alias!r} has no canonical target")
        out[alias] = canonical
    return out


def canonicalize(record: dict, aliases: dict) -> tuple:
    """Return (canonical_record, changes, conflicts)."""
    out = {}
    changes = []
    conflicts = []
    for key, value in record.items():
        if key not in aliases:
            out[key] = value
            continue
        canonical = aliases[key]
        if canonical in record:
            if record[canonical] == value:
                changes.append((key, canonical, "duplicate-with-equal-value"))
                continue
            conflicts.append((key, canonical))
            continue
        out[canonical] = value
        changes.append((key, canonical, "renamed"))
    return out, changes, conflicts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("record", type=Path, help="record YAML to canonicalise")
    ap.add_argument("-o", "--output", type=Path, help="write the canonical record here")
    args = ap.parse_args()

    if not args.record.exists():
        print(f"normalize_record.py: {args.record} not found")
        return 1

    aliases = load_aliases()
    record = yaml.safe_load(args.record.read_text())
    if not isinstance(record, dict):
        print(f"normalize_record.py: {args.record} is not a mapping")
        return 1

    canonical, changes, conflicts = canonicalize(record, aliases)

    if conflicts:
        print(f"FAIL: normalize_record.py ({args.record.name})")
        for alias, canonical_name in conflicts:
            print(f"  {alias!r} and {canonical_name!r} both present with different values")
        return 1

    for alias, canonical_name, kind in changes:
        print(f"  {alias!r} -> {canonical_name!r} ({kind})")

    text = yaml.dump(canonical, sort_keys=False)
    if args.output:
        args.output.write_text(text)
        print(f"PASS: normalize_record.py wrote {args.output} ({len(changes)} change(s))")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
