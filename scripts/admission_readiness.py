"""Step 1 of the admission programme: what does admission actually require?

The catalog holds 4428 records: 5 admitted and 4423 candidates. Admission is
not a status flip. A candidate must gain four admission-time fields, a
formula with unit semantics and a left-hand variable, measurement evidence,
and a MECE signature that no other admitted record holds.

This script scores every candidate against exactly those requirements, and
reports the shape of the work: how many blockers each candidate carries, how
many are otherwise ready, and how the MECE signature clusters constrain how
many records can be admitted at all.

It imports the gate's own constant sets, so the assessment cannot drift from
what the gates enforce.

Usage:
    python3 scripts/admission_readiness.py            # the report
    python3 scripts/admission_readiness.py --write    # also write the per-signature YAML
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402
from check_dual_anchor import MEASURABLE_KINDS, REPUTABILITY_TIERS  # noqa: E402

import yaml  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "classifications" / "admission-readiness.yaml"

# The four fields the schema's admission branch requires (CR-MET-016 D3).
ADMISSION_FIELDS = (
    "subject_concept",
    "measurement_nature",
    "orientation_classification",
    "measurement_nature_detail",
)

# The unit coherence rule (Gate 8 check 6).
def unit_coherent(unit, unit_ref):
    if not unit_ref:
        return True
    if not unit:
        return False
    return unit_ref in (f"dea:unit-{unit}", f"dea:unit-ratio-{unit}")


def formula_lhs(expression: str | None):
    """The left-hand variable of a bound formula, or None."""
    if not expression or "=" not in expression:
        return None
    return expression.split("=", 1)[0].strip()


def blockers(metric: dict) -> list:
    """The requirements this record does not yet meet for admission."""
    out = []
    for field in ADMISSION_FIELDS:
        value = metric.get(field)
        if not (isinstance(value, str) and value.strip()):
            out.append(f"missing_{field}")

    formula = metric.get("formula_definition") or {}
    if not (formula.get("expression") or "").strip():
        out.append("missing_formula_expression")
    if not ((formula.get("unit_semantics") or {}).get("output_unit") or "").strip():
        out.append("missing_formula_output_unit")
    if not (metric.get("calculation_definition") or "").strip():
        out.append("missing_calculation_definition")

    quality = metric.get("quality") or {}
    if not (quality.get("measurement_evidence") or []):
        out.append("missing_measurement_evidence")

    metadata = metric.get("metadata") or {}
    if not metadata.get("established_by"):
        out.append("missing_established_by")

    kind = metric.get("measurable_entity_kind")
    if kind not in MEASURABLE_KINDS:
        out.append("measurable_entity_kind_not_admissible")
    if metric.get("reputability_tier") not in REPUTABILITY_TIERS:
        out.append("reputability_tier_not_admissible")

    abbreviation = metric.get("abbreviation")
    lhs = formula_lhs(formula.get("expression"))
    if not lhs:
        out.append("formula_has_no_left_hand_variable")
    elif lhs != abbreviation:
        out.append("abbreviation_differs_from_formula_lhs")

    if not unit_coherent(metric.get("unit"), metric.get("unit_ref")):
        out.append("unit_not_coherent_with_unit_ref")

    credit = metric.get("source_credit")
    if credit and credit not in (quality.get("measurement_evidence") or []):
        out.append("source_credit_not_in_measurement_evidence")
    return out


def signature(metric: dict):
    """The MECE uniqueness key (Gate 3).

    CR-MET-020 extended it with subject_concept: the metamodel says the
    concept "distinguishes a Metric by what it measures rather than by its
    MECE label", and with the label alone the corpus collapsed 4423 records
    into 500 signatures.
    """
    return (
        tuple(sorted(metric.get("subject_classification") or [])),
        tuple(sorted(metric.get("purpose_classification") or [])),
        metric.get("orientation_classification"),
        tuple(sorted(metric.get("scope_classification") or [])),
        metric.get("directionality"),
        metric.get("subject_concept"),
    )


def main() -> int:
    metrics = load_metrics()
    admitted = {mid: m for mid, m in metrics if m.get("lifecycle_status") == "admitted"}
    candidates = [(mid, m) for mid, m in metrics if m.get("lifecycle_status") != "admitted"]

    per_record = {}
    for mid, m in candidates:
        per_record[mid] = blockers(m)

    # MECE clusters over the whole corpus, admitted included.
    clusters = defaultdict(list)
    for mid, m in metrics:
        clusters[signature(m)].append(mid)

    admitted_sig = {signature(m) for m in admitted.values()}
    # A candidate whose signature is already held by an admitted record can
    # never be admitted without changing the axis values.
    blocked_by_admitted = {
        mid for mid, m in candidates if signature(m) in admitted_sig
    }

    blocker_counts = Counter()
    for mid, _ in candidates:
        for b in per_record[mid]:
            blocker_counts[b] += 1
    ready = [mid for mid, _ in candidates if not per_record[mid]]

    print("=" * 72)
    print("Admission readiness")
    print("=" * 72)
    print(f"  records in the corpus      : {len(metrics)}")
    print(f"  admitted                   : {len(admitted)}")
    print(f"  candidates                 : {len(candidates)}")
    print()
    print(f"  candidates with NO blocker : {len(ready)}")
    print(f"  candidates with >=1 blocker: {len(candidates) - len(ready)}")
    print()
    print("  BLOCKERS, by requirement")
    for name, count in blocker_counts.most_common():
        print(f"      {name:44s} {count:>5}")
    print()
    print("  MECE CONSTRAINT (Gate 3: an admitted signature is unique)")
    print(f"      distinct signatures in the corpus : {len(clusters)}")
    print(f"      signatures already held by admitted: {len(admitted_sig)}")
    print(f"      candidates whose signature is already admitted: {len(blocked_by_admitted)}")
    cluster_sizes = Counter(len(v) for v in clusters.values())
    print(f"      cluster size distribution          : "
          f"{dict(sorted(cluster_sizes.items()))}")
    print(f"      largest cluster                     : {max(len(v) for v in clusters.values())}")
    print()
    # The ceiling under the current axis model: one admitted record per
    # signature, and a signature already held by an admitted record cannot be
    # held again. The curation question is therefore how many signatures
    # still have room, and how big the choice is inside each.
    open_signatures = [s for s in clusters if s not in admitted_sig]
    singletons = [s for s in open_signatures if len(clusters[s]) == 1]
    contested = [s for s in open_signatures if len(clusters[s]) > 1]
    biggest = max((len(clusters[s]) for s in contested), default=0)
    print("  ADMISSIBLE SET UNDER THE CURRENT AXIS MODEL")
    print(f"      signatures in the corpus                       : {len(clusters)}")
    print(f"      already held by an admitted record             : {len(admitted_sig)}")
    print(f"      signatures with room for one more record       : {len(open_signatures)}")
    print(f"      of those, a singleton (no choice to make)      : {len(singletons)}")
    print(f"      of those, contested (choose one representative): {len(contested)}")
    print(f"      largest contested cluster                      : {biggest} candidates")
    print(f"      so at most {len(open_signatures)} further records can be admitted under")
    print("      the current axis model, and each contested signature")
    print("      needs a curation decision about which record is the")
    print("      canonical one. Enriching the records does not change")
    print("      this number; only the axis model can.")
    print()
    print("  Every candidate needs the four admission fields and a bound")
    print("  formula; those are authoring work, not derivations. The MECE")
    print("  ceiling is the structural constraint, and it is the one that")
    print("  decides how the programme is shaped.")

    if "--write" in sys.argv:
        rows = []
        for sig, ids in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
            members = []
            for mid in sorted(ids):
                if mid in per_record:
                    members.append({
                        "id": mid,
                        "blockers": per_record[mid],
                    })
            rows.append({
                "signature": {
                    "subject_classification": list(sig[0]),
                    "purpose_classification": list(sig[1]),
                    "orientation_classification": sig[2],
                    "scope_classification": list(sig[3]),
                    "directionality": sig[4],
                },
                "members": len(ids),
                "candidates": len(members),
                "held_by_admitted": sig in admitted_sig,
                "ready_candidates": sum(1 for x in members if not x["blockers"]),
                "records": members,
            })
        doc = {
            "version": "1.0.0",
            "authority": "CR-MET-019",
            "generated_by": "scripts/admission_readiness.py",
            "admitted": len(admitted),
            "candidates": len(candidates),
            "blocker_free_candidates": len(ready),
            "distinct_signatures": len(clusters),
            "open_signatures": len(open_signatures),
            "singleton_signatures": len(singletons),
            "contested_signatures": len(contested),
            "largest_contested_cluster": biggest,
            "signatures": rows,
        }
        OUT.write_text(yaml.safe_dump(doc, sort_keys=False, width=100))
        print(f"  wrote {OUT.relative_to(BASE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
