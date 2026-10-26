# CR-MET-017 -- Canonical Unit References at Ingestion

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-26 |
| Depends on | CR-MET-015 (field dimensions, alias registry); CR-MET-016 (seed ingestion) |
| Blocks | the unit-entity slice in dea-metamodel (Q20), which admits the canonical names |
| Cardinal authority | dea-catalog-metrics (catalog); dea-metamodel (canonical semantics) |
| Kanban | board 9, card #651 |

## 1. Background and problem statement

CR-MET-016 ingested the candidate-metrics seed workbook, whose `unit_id`
column carried the source's own spellings. The catalog's unit-reference form
(CR-MET-015) is `dea:unit-<unit>`, with the more precise
`dea:unit-ratio-<unit>` where the unit is a ratio, and singular names
(`dea:unit-minute`, not `dea:unit-minutes`). The seed's spellings disagreed on
both counts: `dea:unit-percent` rather than `dea:unit-ratio-percent`, and
plural names for 13 further units.

CR-MET-016 recorded this as its Q19 decision point and carried the seed's
spellings verbatim. The owner has now ruled on Q19 (board card #642,
2026-10-26): **the ratio form is canonical**, and singular names with it. The
seed's spellings are ingestion-time aliases of the canonical references.

The scale of the change: 21 distinct unit references across the corpus, of
which 13 map to a canonical form. Roughly 3,400 candidate records change their
`unit_ref`. The 5 admitted pilot records already carry canonical references
and do not change.

## 2. Objective

Make the canonical unit reference the only form the catalog stores, by mapping
the seed's spellings at ingestion, exactly as the classification axes already
map theirs.

## 3. Decisions (binding)

### D1: The mapping is data, not code, and it lives with the other mappings

`classifications/seed-value-maps.yaml` gains a `unit_ref` section. `carry`
lists the 8 seed spellings that are already canonical; `map` lists the 13
that resolve to a canonical form. A seed unit id that appears in neither stops
the ingestion with a message naming the value, exactly as an unmapped
classification value does.

### D2: Unit ids resolve by exact match

`map_value` normalises hyphens to underscores because the classification axes
are underscore-spelled and the seed is not. Unit ids are hyphen-significant:
`dea:unit-percent` and `dea:unit_percent` are not the same reference. The
unit resolver therefore does no hyphen normalisation; the map's keys are the
seed's spellings verbatim.

### D3: The plain `unit` label follows the canonical reference

`unit` derives from the canonical `unit_ref` (`dea:unit-ratio-percent` gives
`percent`; `dea:unit-minute` gives `minute`), so Gate 8's coherence rule
holds for every record without exception handling.

### D4: The refreshed records bump their version

Every refreshed candidate record goes 1.0.0 to 1.0.1 and gains a
change-history entry naming this CR, matching the pilot's versioning
convention (the record version tracks record changes; the formula version
tracks the formula, which did not change and stays 1.0.0).

### D5: `dea:unit-times` carries as-is

The seed distinguishes `times` (occurrences) from `count` (a tally). Singular
`time` would read as a duration, which it is not. `dea:unit-times` is the
canonical name for the occurrence-count unit and is recorded as such.

## 4. Changes

1. `classifications/seed-value-maps.yaml`: the `unit_ref` section.
2. `scripts/ingest_seed.py`: `map_unit_ref` (exact-match resolver), the
   version constant, and the change-history entry.
3. `entities/v1-alpha/`: 4423 candidate records refreshed.
4. `CATALOG.yaml`: regenerated.
5. `CHANGELOG.md`.
6. `change-requests/CR-MET-017.md`, this document.

## 5. Definition of Done

- All eight gate scripts exit 0 over the 4428-record corpus.
- The full test suite passes.
- `python3 scripts/ingest_seed.py --check` reports that the catalog matches
  the workbook, and the ingestion is idempotent (a second run changes
  nothing).
- A seed unit id with no mapping stops the ingestion, proven by injection in
  a throwaway clone.
- No record carries a flat or plural unit reference after the refresh.
- D-004, D-005, and the embargo denylist are clean on every touched file.

## 6. NOT-list

- No admitted record changes.
- No unit entity is created here; that is the dea-metamodel slice ruled under
  Q20 (card #650), which admits the canonical names this CR establishes.
- No change to the domain/sector free-text values (Q16 is seeded, not
  frozen; the reconciliation slice is card #649).

## 7. References

- Board cards #642 (the Q19 ruling), #650 (Q20 unit-entity slice), #649
  (Q16 reconciliation), #651 (this CR).
- CR-MET-005 (unit semantics), CR-MET-015 (field dimensions), CR-MET-016
  (seed ingestion).
- `seeds/README.md` (the field and value mapping tables).
