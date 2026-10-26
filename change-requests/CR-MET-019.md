# CR-MET-019 -- The Admission Programme: Readiness Assessment and Tranche Shape

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-26 |
| Depends on | CR-MET-016 (the 4423-record candidate corpus); CR-MET-017 (canonical unit references); CR-MET-018 (the domain and sector reconciliation input) |
| Blocks | the admission tranches that follow |
| Cardinal authority | dea-catalog-metrics (the catalog); dea-metamodel (the controlled entity names) |
| Kanban | board 9, card #655 |

## 1. Background and problem statement

CR-MET-016 landed 4423 candidate records alongside the 5 admitted pilot. The
catalog's gates bind admission: an `admitted` record must carry four
admission-time fields, a bound formula with unit semantics, measurement
evidence, and a MECE signature no other admitted record holds.

Nothing yet says how many of the 4423 can be admitted, what each one needs,
or in what order. This CR answers those questions from the corpus and fixes
the shape of the admission programme.

## 2. What admission requires, per record

`scripts/admission_readiness.py` scores every candidate against exactly the
requirements the gates enforce. It imports `MEASURABLE_KINDS` and
`REPUTABILITY_TIERS` from `check_dual_anchor.py`, so the assessment cannot
drift from what the gates enforce.

| Requirement | Source | Candidates failing it |
|---|---|---|
| `subject_concept` | schema admission branch | 4423 |
| `measurement_nature` | schema admission branch | 4423 |
| `orientation_classification` | schema admission branch | 4423 |
| `measurement_nature_detail` | schema admission branch | 4423 |
| `quality.measurement_evidence` | Gate 4 | 4423 |
| `source_credit` among the evidence | Gate 8 check 7 | 4423 |
| formula left-hand variable | Gate 8 check 5 | 4422 |
| abbreviation equals the formula LHS | Gate 8 check 5 | 1 |
| unit coherent with `unit_ref` | Gate 8 check 6 | 0 |
| `measurable_entity_kind` admissible | Gate 6 | 0 |
| `reputability_tier` admissible | Gate 6 | 0 |

**No candidate is admission-ready, and none is close in the mechanical sense.**
Every one needs authoring work: the four admission fields are judgements
about what the metric measures, and the evidence list is a citation set that
has to name real sources. The seed supplies a description, a formula, and a
credit; it does not supply a subject concept or a measurement nature.

One candidate already carries a formula with a left-hand variable, and that
variable differs from its abbreviation. It is the only candidate whose
abbreviation rule can be fixed by editing one field rather than authoring
one.

## 3. The structural constraint: MECE

Gate 3 forbids two admitted records from sharing a 5-axis signature. Over the
whole corpus:

| Measure | Value |
|---|---|
| distinct signatures | 500 |
| already held by an admitted record | 5 |
| **signatures with room for one more record** | **495** |
| of those, a singleton (no choice to make) | 120 |
| of those, contested (a representative must be chosen) | 375 |
| largest contested cluster | 100 candidates |

Cluster sizes run from 1 to 100. The distribution is the shape of the
decision: 495 signatures have room, and each of the 375 contested ones needs
a curation call about which record is the canonical representative.

This is the number that decides the programme. Enriching the 4423 records
does not change it; only the axis model can. Three shapes follow:

1. **Curate to the signatures.** Admit at most 495 more records, one per
   signature, and leave the rest as candidates. Rule-compliant, and it
   discards most of the pool.
2. **Extend the axis model** so that legitimately distinct metrics stop
   colliding. The 100-record clusters are the evidence that the current five
   axes do not separate what the seed considers separate. This is a
   metamodel-level change (CR-MET-002 territory) and a bigger decision.
3. **Admit in tranches by signature cluster**, curating as you go, and let the
   cluster sizes tell you where the axis model needs work.

## 4. Decisions (binding)

### D1: The assessment is generated, and CI checks it

`scripts/admission_readiness.py --write` produces
`classifications/admission-readiness.yaml`: one row per signature, with every
candidate member and its blockers. CI regenerates it and diffs it, so the
working set cannot drift from the corpus.

### D2: The assessment imports the gates' own constant sets

A second copy of the 16-type set and the 5-value enum would be a second
source of truth that drifts. The script imports them from
`check_dual_anchor.py`.

### D3: The MECE ceiling is reported as a ceiling, not as a plan

The assessment reports how many signatures have room. It does not decide
which record represents a contested signature: that is a curation decision,
taken per cluster, and it belongs to the owner and to the admission tranche
that carries the cluster.

### D4: No record changes in this CR

The assessment is read-only over the corpus. No candidate is enriched, no
signature is altered, and no record is admitted.

## 5. Decision points

### Q26: curate to the signatures, or extend the axis model?

Open, and it is the programme's central decision. It is the owner's call,
and the assessment supplies the evidence: 495 signatures with room, 375 of
them contested, largest cluster 100 candidates.

### Q27: what is the evidence standard for a seed-derived record?

Open. The admitted pilot cites named references (the ITIL 4 incident
management practice, the SRE workbook). A seed-derived record's own source is
the seed. Whether the seed itself is admissible evidence, or whether
admission requires an independent reference per record, decides the size of
the authoring work per record by an order of magnitude.

### Q28: tranche shape and order?

Open, pending Q26 and Q27. If the answer is curation, the natural tranches
are by signature cluster, smallest first (the 120 singletons are mechanical),
with the 100-record clusters last and on their own.

## 6. Definition of Done

- The assessment runs over the whole corpus and reports the blockers, the
  MECE ceiling and the cluster distribution.
- The committed assessment artefact matches the corpus (CI proves it).
- The script imports the gates' constant sets rather than copying them.
- No record changes.

## 7. NOT-list

- No candidate is admitted, enriched, or renamed.
- No signature is altered.
- No axis is added, and the metamodel is not changed.
- The curation decisions are not taken here.

## 8. References

- Board cards #642 (the rulings), #655 (this card), #649 (Q16 enrichment),
  #650 (Q20 unit entities), #651 (CR-MET-017).
- CR-MET-002 (the classification axes), CR-MET-006 (contexts, thresholds),
  CR-MET-009 (the pilot admission), CR-MET-016, CR-MET-017, CR-MET-018.
