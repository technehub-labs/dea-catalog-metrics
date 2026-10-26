# CR-MET-020 -- The Axis Extension, the Seed as Evidence, and the Admission Tranches

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-26 |
| Depends on | CR-MET-016 (the candidate corpus); CR-MET-017 (canonical unit references); CR-MET-018 (the domain and sector reconciliation input); CR-MET-019 (the readiness assessment) |
| Blocks | the admission tranches |
| Cardinal authority | dea-catalog-metrics (the catalog); dea-metamodel (the controlled entity names) |
| Kanban | board 9, card #656 |

## 1. The rulings

The owner ruled on the three decision points CR-MET-019 raised (board card
#642, 2026-10-26):

- **Q26**: extend the axis model so there is no collision.
- **Q27**: the seed is admissible evidence.
- **Q28**: yes, to the tranche shape.

## 2. Q26, measured before it was implemented

The extension had to be chosen against the data, not asserted. Measured over
the 4428-record corpus, adding one axis to the 5-axis MECE signature:

| Axis added | Signatures | Records still colliding | Largest cluster |
|---|---|---|---|
| none (baseline) | 500 | 4303 | 100 |
| the domain (functional area) | 2303 | 3202 | 13 |
| the sector | 1339 | 3837 | 83 |
| domain + sector | 2309 | 3195 | 13 |
| the measurable entity kind | 938 | 4094 | 60 |
| **the subject concept** | **4402** | **26** | **3** |

No existing axis separates the corpus. The discriminator is what each metric
MEASURES, and that is exactly what the metamodel's `subject_concept` field is
for: it "distinguishes a Metric by what it measures rather than by its MECE
label" (dea-metamodel `metric.json`). The five classification axes are the
label; two metrics that share a label but measure different things are
different metrics, and Gate 3 was rejecting them.

**The extension is therefore `subject_concept` in the uniqueness key.** 4303
of the 4303 collisions disappear; 26 records in 25 clusters remain.

## 3. What the extension is made of

### D1: The uniqueness key gains `subject_concept`

`scripts/check_mece_coverage.py` keys on the five classification axes plus
the subject concept. The gate's own message names the key it enforces.

### D2: The subject concept is DERIVED from the seed's metric id, and the
### vocabulary is seeded, not frozen

The seed's ids name their subject precisely (`code-churn-rate` measures code
churn; the trailing measure noun says how it is expressed, not what it is
about). The derivation strips the topic-variant markers (`deep_dive`,
`standard_measures`) and the trailing measure nouns, and yields a concept
reference: `dea:subject-<phrase>`.

`classifications/subject-concepts.yaml` records the 4316 distinct concepts
the corpus uses. The vocabulary is seeded, not frozen (the Q16 ruling): it
records what the corpus uses, the gate checks the FORM of a concept
reference rather than its membership, and the values are reconciled to the
metamodel's concept entities when their home is settled (Q23, Q25).

### D3: `measurement_nature` is derived from the unit

Every seed metric measures a quantity, so the nature is `numeric` for all
4428 records, derived from the unit rather than authored per record.

### D4: The formula is BOUND to its short form

The seed publishes bare expressions (`Calls Abandoned / Calls Offered`). The
ingestion now binds them: `ABR-D = Calls Abandoned / Calls Offered`, so the
record's short form is its left-hand variable, Gate 8's rule (the
abbreviation equals the formula's left-hand variable) holds for every record,
and a consumer can evaluate the formula. The operands are read off the
right-hand side only: the left-hand side is the result, not an input.

A formula is already bound only if it carries a standalone `=`. A comparison
operator is not a binding: the seed publishes thresholds inside expressions
(`Milestones with SPI >= 0.95 / Milestones`), and reading their `=` as a
binding left one record unbound with a nonsense left-hand side.

### D5: Gate 7's unbound scan reads the right-hand side only

Gate 7 reports an expression that names a variable the record does not
declare as an input. With bound formulas, scanning the whole expression
reported the record's OWN short form as unbound, because a hyphen is not an
identifier character (`ABR-D` tokenises as `ABR` and `D`). The scan now
reads the right-hand side, which is where references to inputs live.

## 4. Q27: the seed is admissible evidence

A seed-derived record's evidence is the seed itself: the workbook, the
sheet, the row, and the credit the source carries. The ingestion writes

```
quality.measurement_evidence:
  - OpenDEAM candidate-metrics seed workbook (seeds/open-deam-candidate-metrics-seed.xlsx), sheet 'Candidate Metrics', row 412
  - <the source credit>
```

which satisfies Gate 4 (evidence is present) and Gate 8's rule 7 (the
source credit appears among the evidence). No independent reference is
required per record.

## 5. What is left: two judgement fields

After the derivation, every candidate carries everything mechanical. Two
fields remain, and they are judgements, so they are not derived:

| Field | Why it is not derived | Where it is authored |
|---|---|---|
| `orientation_classification` | leading / lagging / diagnostic / concurrent is a claim about the metric's place in time, not a property of its name or unit | once per topic pack |
| `measurement_nature_detail` | a human-readable description of the nature | per record, from its formula and unit, reviewed per pack |

## 6. Q28: the tranche plan

The corpus decomposes into the seed's own **276 topic packs** (the domain
packs of CR-MET-018), pack sizes 8 to 44 records, median 15. A pack is one
functional area's focused measure set, which makes it the natural unit for
the orientation judgement: a pack's measures share an orientation.

**One tranche per subject classification**, packs inside a tranche ordered
smallest first, so the mechanical packs land first and the large contested
ones land last:

| Tranche | Subject classification | Packs | Records |
|---|---|---|---|
| 1 | technology_architecture | 41 | 758 |
| 2 | product_or_service | 43 | 608 |
| 3 | financial | 33 | 535 |
| 4 | business_architecture | 36 | 529 |
| 5 | customer | 31 | 484 |
| 6 | organization | 23 | 386 |
| 7 | governance | 21 | 350 |
| 8 | risk | 11 | 197 |
| 9 | strategy | 11 | 166 |
| 10 | information_architecture | 9 | 152 |
| 11 | capability | 6 | 90 |
| 12 | sustainability | 6 | 84 |
| 13 | transformation | 3 | 44 |
| 14 | operations | 2 | 40 |

Each tranche: author one orientation per pack, generate each record's
`measurement_nature_detail` from its formula and unit, flip the pack's
records to `admitted` with their change-history entries, run the gates, and
land one PR.

**The residual curation set: 25 clusters, 26 records.** After the extension
these are the only collisions left, and they are the same metric published
twice, or one subject measured two ways:

- the base record and its `_deep_dive` variant (the commonest case),
- `lost-time-injury-rate` against `lost-time-injury-frequency-rate`,
- `market-share` against `market-share-growth`,
- `server-utilization` against `server-utilization-average`,
- `system-average-interruption-duration-index` against
  `system-average-interruption-frequency-index`.

Each needs a curation decision: admit the base and keep the variant a
candidate, admit both with an authored subject concept that keeps the
aspect, or deprecate one. The set is small enough to decide record by
record, and it is the last thing standing between the corpus and a
collision-free admission.

## 7. Definition of Done

- All eight gates exit 0 over the 4428-record corpus.
- The full test suite passes.
- The MECE uniqueness key carries `subject_concept`, and the corpus
  resolves to 4402 signatures with 26 records in 25 clusters.
- Every candidate carries a subject concept, a measurement nature, a bound
  formula and seed evidence; the readiness assessment reports only the two
  judgement fields outstanding.
- The seeded vocabulary is generated from the corpus and CI checks it.
- D-004, D-005 and the embargo denylist are clean on every touched file.

## 8. NOT-list

- No record is admitted in this CR. The admission is the tranches.
- No axis is added to the metamodel, and no concept entity is created (Q23).
- The subject-concept vocabulary is not frozen.
- No judgement field is derived by rule.

## 9. References

- Board cards #642 (the rulings), #655 (CR-MET-019), #656 (this card).
- CR-MET-001 (the metric entity), CR-MET-002 (the classification axes),
  CR-MET-016, CR-MET-017, CR-MET-018, CR-MET-019.
- dea-metamodel: `schemas/entities/metric.json` (subject_concept),
  `metamodel/vocabularies/classifications.yaml`.
