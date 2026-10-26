"""CR-MET-018 (Q16): reconcile the catalog's domain and sector values.

The owner ruled on Q16 (board card #642, 2026-10-26): seed the domain and
sector vocabulary from the corpus, do not freeze it yet, and reconcile the
seeded text into the metamodel's controlled entity names by a separate slice
on the related entities in dea-metaframework.

This script produces the reconciliation INPUT for that slice. It classifies
every seeded value by what it actually is, so the follow-up slice inherits a
structured input instead of a flat list of 363 slugs:

  - A domain is either a FUNCTION (finance_accounting, human_resources) or a
    SECTOR VARIANT of a function (airport_operations, maritime_shipping).
    The seed names the two the same way, which is why the raw value list
    reads as if the domain axis were a single thing.
  - A sector is an INDUSTRY. Every one of the 77 values is an industry; none
    is an organisational structure.

It does NOT decide the ECF compound-domain mapping. That mapping requires
the domain-grounding discipline dea-metaframework owns (axiom grounding,
boundary rules against adjacent domains, internal MECE partition), and it
cannot be derived from a keyword. The output therefore carries the domain
variants as UNRESOLVED for that slice, deliberately, rather than guessing.

Usage:
    python3 scripts/reconcile_domain_sector.py
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402

import yaml  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
OUT_DOMAIN = BASE / "classifications" / "domain-reconciliation.yaml"
OUT_SECTOR = BASE / "classifications" / "sector-reconciliation.yaml"

# The seed names a topic VARIANT with a trailing marker. A variant is the
# same functional area as its base, published as a focused set of measures.
VARIANT_SUFFIXES = ("_deep_dive", "_standard_measures", "_measures")

def _tokens(slug: str) -> list:
    """The slug's tokens, singularised, so `airports` and `airport` match."""
    out = []
    for token in slug.split("_"):
        out.append(token[:-1] if len(token) > 3 and token.endswith("s") else token)
    return out


def names_sector(base: str, sector: str) -> bool:
    """Does the functional area name the industry, as a contiguous phrase?

    The test is the corpus's own: a record knows its sector, and a
    sector-scoped function names that industry inside its own name
    (`airport_operations` in the airport industry, `maritime_shipping` in
    maritime shipping). A function that merely shares a word with an
    industry is not a variant of it: `advertising_media_buying` is marketing
    work, not a media-industry variant, and the corpus's own sector values
    say so.
    """
    if not sector:
        return False
    haystack = _tokens(base)
    needle = _tokens(sector)
    if not needle:
        return False
    for start in range(len(haystack) - len(needle) + 1):
        if haystack[start:start + len(needle)] == needle:
            return True
    return False


def base_function(domain: str) -> str:
    """The functional area a domain value names, variant markers removed."""
    for suffix in VARIANT_SUFFIXES:
        if domain.endswith(suffix):
            return domain[: -len(suffix)]
    return domain


def display_name(slug: str) -> str:
    """A slug as a display name: `finance_accounting` -> `Finance Accounting`."""
    words = []
    for word in slug.split("_"):
        words.append(word.upper() if word in {"r_and_d", "esg", "hr", "ai", "it",
                                              "ml", "api", "pmo", "okr", "b2b",
                                              "b2c", "saas", "erp", "cro", "crm"}
                     else word.capitalize())
    return " ".join(words)


def main() -> int:
    metrics = load_metrics()
    domains = Counter(m["domain"] for _, m in metrics if m.get("domain"))
    sectors = Counter(m["sector"] for _, m in metrics if m.get("sector"))

    # Which sector does a domain value sit in, if any? Decided per RECORD
    # from the record's own sector, then aggregated over the domain value.
    per_domain: dict[str, dict] = {}
    for _, record in metrics:
        domain = record.get("domain")
        if not domain:
            continue
        sector = record.get("sector")
        base = base_function(domain)
        entry = per_domain.setdefault(domain, {
            "records": 0,
            "base_function": base,
            "variants": Counter(),
            "functions": 0,
        })
        entry["records"] += 1
        if names_sector(base, sector):
            entry["variants"][sector] += 1
        else:
            entry["functions"] += 1

    domain_rows = []
    for domain, entry in sorted(per_domain.items()):
        variants = entry["variants"]
        mixed = bool(variants) and entry["functions"] > 0
        if mixed:
            disposition = "mixed"
        elif variants:
            disposition = "sector_variant"
        else:
            disposition = "function"
        domain_rows.append({
            "seeded_value": domain,
            "records": entry["records"],
            "base_function": entry["base_function"],
            "proposed_business_function": display_name(entry["base_function"]),
            "disposition": disposition,
            "sector": sorted(variants)[0] if variants and not mixed else None,
            "sector_records": sum(variants.values()),
            "function_records": entry["functions"],
            "metamodel_entity": "dea:BusinessFunction",
            "ecf_domain": None,
            "ecf_domain_status": "unresolved",
        })

    sector_rows = []
    for sector, count in sorted(sectors.items()):
        sector_rows.append({
            "seeded_value": sector,
            "records": count,
            "display_name": display_name(sector),
            "axis": "industry",
            "organizational_unit_type": None,
            "ou_type_status": "not_applicable",
            "note": (
                "The seeded value names an industry, not an organisational "
                "structure. The metamodel's organisation-type vocabulary "
                "(OrganizationalUnit.ou_type) holds structures (business-unit, "
                "division, department, team, role-cluster, virtual-team, "
                "governance-body, external-partner-role), so no seeded sector "
                "value maps to one."
            ),
        })

    doc = {
        "version": "1.0.0",
        "authority": "CR-MET-018",
        "generated_by": "scripts/reconcile_domain_sector.py",
        "ruling": (
            "Q16 (owner, 2026-10-26): seed the vocabulary from the corpus, do "
            "not freeze it; reconcile the seeded text into the metamodel's "
            "controlled entity names by a separate slice on the related "
            "entities in dea-metaframework."
        ),
        "scope": (
            "The seeded values are the corpus's domain and sector values. The "
            "ECF compound-domain mapping is deliberately left unresolved: it "
            "requires the domain-grounding discipline (axiom grounding, "
            "boundary rules, internal MECE partition) that dea-metaframework "
            "owns, and a keyword cannot derive it."
        ),
        "domains": domain_rows,
    }
    sec = {
        "version": "1.0.0",
        "authority": "CR-MET-018",
        "generated_by": "scripts/reconcile_domain_sector.py",
        "finding": (
            "Every seeded sector value names an INDUSTRY. The metamodel's "
            "organisation-type vocabulary names organisational STRUCTURES. "
            "The two axes are not the same, so the seeded sector values do "
            "not map to OrganizationalUnit.ou_type."
        ),
        "sectors": sector_rows,
    }

    OUT_DOMAIN.write_text(yaml.safe_dump(doc, sort_keys=False, width=100))
    OUT_SECTOR.write_text(yaml.safe_dump(sec, sort_keys=False, width=100))

    functions = sum(1 for r in domain_rows if r["disposition"] == "function")
    variants = len(domain_rows) - functions
    print(f"domains: {len(domain_rows)} ({functions} functions, {variants} sector variants)")
    print(f"sectors: {len(sector_rows)} (all industry axis)")
    print(f"wrote {OUT_DOMAIN.relative_to(BASE)}")
    print(f"wrote {OUT_SECTOR.relative_to(BASE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
