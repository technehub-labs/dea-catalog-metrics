"""CR-MET-020: the seeded subject-concept vocabulary.

The subject concept is the metamodel's own answer to a metric's identity:
it "distinguishes a Metric by what it measures rather than by its MECE label"
(dea-metamodel metric.json). The seed's metric ids name their subject
precisely, so the concept is derived from the id.

The vocabulary is SEEDED, not frozen (the Q16 ruling): it records what the
corpus uses, it is not a closed set, and it is reconciled to the metamodel's
concept entities when their home is settled (Q23, Q25).

Usage:
    python3 scripts/derive_subject_concepts.py
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402
from ingest_seed import subject_concept, subject_phrase  # noqa: E402

import yaml  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "classifications" / "subject-concepts.yaml"


def main() -> int:
    metrics = load_metrics()
    counts: Counter = Counter()
    names: dict[str, str] = {}
    for _, m in metrics:
        concept = m.get("subject_concept") or subject_concept(m["id"])
        counts[concept] += 1
        names.setdefault(concept, subject_phrase(m["id"]))

    rows = []
    for concept, count in sorted(counts.items()):
        rows.append({
            "concept": concept,
            "subject_phrase": names[concept],
            "records": count,
        })

    doc = {
        "version": "1.0.0",
        "authority": "CR-MET-020",
        "generated_by": "scripts/derive_subject_concepts.py",
        "ruling": (
            "Q26 (owner, 2026-10-26): extend the axis model so there is no "
            "collision. The extension is subject_concept in the MECE "
            "uniqueness key, which is what the metamodel says distinguishes a "
            "Metric from its MECE label."
        ),
        "status": (
            "Seeded, not frozen (Q16). The values are what the corpus uses. "
            "They are reconciled to the metamodel's concept entities when "
            "their home is settled (Q23, Q25); until then the vocabulary is "
            "advisory, and the gate checks the FORM of a concept reference, "
            "not its membership."
        ),
        "concepts": rows,
    }
    OUT.write_text(yaml.safe_dump(doc, sort_keys=False, width=100))
    print(f"concepts: {len(rows)} distinct, covering {sum(counts.values())} records")
    print(f"wrote {OUT.relative_to(BASE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
