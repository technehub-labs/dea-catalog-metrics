# CR-MET-016 -- Ingest the Candidate-Metrics Seed and Scale the Catalog to 4428 Records

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-26 |
| Depends on | CR-MET-009 (catalog establishment); CR-MET-014 (description field); CR-MET-015 (field dimensions, alias registry) |
| Blocks | none |
| Cardinal authority | dea-catalog-metrics (catalog); dea-metamodel (canonical semantics) |
| Kanban | board 9 |

## 1. Background and problem statement

A seed workbook of candidate industry-standard metrics was supplied:
`open-deam-candidate-metrics-seed.xlsx`, sha-256
`f037b8d3dfeb48538715e975492f4a864f56bfd58d66bed99afcad222a7af1c4`. It has
three sheets: `Overview` (298 rows), `Candidate Metrics` (a header row at row
6 and 4428 data rows, rows 7 to 4434) and `Field Guide` (24 rows).

The `Field Guide` sheet is the workbook's own mapping table. It names, for
each field, the catalog artefact the field populates. That guide is the
authority for the field mapping in this CR, and it corrected an assumption
made earlier: it assigns the field `orientation` to threshold semantics, which
is the catalog's `directionality`, not to the catalog's orientation axis. The
alias registry from CR-MET-015 was corrected accordingly.

The catalog held 5 records. The seed carries 4428 metrics, so the catalog
changes scale by three orders of magnitude. That is not only a volume change:
several rules the catalog enforces were written for a 5-record pilot, and the
seed does not carry the fields those rules require.

## 2. Objective

Land the seed in the repository, ingest its metrics as candidate records
through a reproducible pipeline, map its fields and values onto the catalog's
schema through the alias registry and the value maps, and keep every rule the
catalog enforces meaningful at the new scale.

## 3. Decisions (binding)

### D1: The workbook is a seed artefact, committed to the repository

`seeds/open-deam-candidate-metrics-seed.xlsx`, with `seeds/README.md` giving
its provenance, its sha-256, the field mapping, the value mapping, and the id
collisions. A seed is a published, versioned artefact: the catalog's records
cite it, so the catalogue's provenance is checkable rather than asserted.

### D2: The field mapping is data, not code

Field NAMES come from `classifications/field-aliases.yaml` and field VALUES
from `classifications/seed-value-maps.yaml`. The value map distinguishes three
cases and keeps them distinct: `carry` (the seed value is already a catalog
value), `map` (it is a synonym of one) and `add` (it is a distinct concept, so
the catalog vocabulary gains it). A seed value that appears nowhere is a
mapping gap, and `scripts/ingest_seed.py` refuses to run rather than guess.

### D3: The required set is lifecycle-aware

The catalog's `subject_concept`, `measurement_nature`, `orientation_classification`
and `measurement_nature_detail` are admission-time fields. The seed has no
column for any of them, and the workbook's own field guide does not mention
them. Requiring them of a candidate would mean inventing them for 4423
records.

The schema's required set is therefore split: a `candidate` record must carry
the 15 fields the source provides, and any other lifecycle must carry those 15
plus the 4 admission fields. This is expressed in draft-07 `if`/`then`/`else`,
so it is a standards-compliant constraint, not a comment.

The five admitted pilot records are unaffected: they carry the full set and
still pass.

### D4: Two id patterns are widened, from the data

Two seed ids begin with a digit (`dea:metric-3-d-secure-pass-rate`,
`dea:metric-30-day-readmission-rate-deep-dive`), so the id pattern now allows
a leading digit. 1362 seed short forms use characters the pilot pattern
forbade (`EBITDA%`, `D/E`, `LTV:CAC`, `eNPS`), so the abbreviation pattern now
allows letters in either case, digits, and `% * / : . -`. Both patterns were
derived from the data's own character set, not guessed.

The abbreviation pattern change does not weaken the formula namespace gate,
which keys on the formula's left-hand variable and not on this field.

### D5: The seed's short forms are not disambiguated

220 abbreviations are shared by 460 rows, so the seed breaks its own field
guide's "unique within the catalog" rule. Disambiguating them would rename
recognised industry short forms, which is worse than the duplication. The
duplication is recorded as a finding, and no uniqueness rule is added.

### D6: The seed's formulas declare their operands

The seed publishes plain-text expressions, not a bound formula, so the
catalog's `formula_definition.inputs` would be empty and the formula namespace
gate would report 4423 unbound expressions. The operands are read off the
expression by splitting on the arithmetic and comparison operators, which
yields the terms the expression names: `(Revenue - Cost of Goods Sold) /
Revenue` declares `Revenue` and `Cost of Goods Sold`. Pure numbers are
thresholds and constants, so they are dropped.

This makes the records genuinely more useful, and it makes the gate's
unbound-expression finding meaningful again rather than universal.

### D7: Two subject values and nine purpose values are added

The seed's subject axis carries `operations` and `risk`, and its purpose axis
carries nine values the catalog did not have. Collapsing them onto the
catalog's existing values would have thrown away the classification signal
across 4423 records, so the vocabularies are extended. `value` maps to
`value_delivery` and `conformance` to `compliance`, which are synonyms;
`product-service` maps to `product_or_service`; `tactical` maps to
`managerial`; the seed's three scope values map onto `capability`,
`organizational_unit` and `business_domain`; the seed's 14 entity kinds map
onto the catalog's 16 dual-anchor types.

The schema's enums and the `classifications/` vocabulary files are now
identical for all five axes. They were not: the schema's purpose enum
carried `quality` while the vocabulary file did not. That drift is fixed here.

### D8: `All industries` is not a sector

2445 rows carry `All industries`, which is the absence of a sector rather than
a sector. `sector` is omitted for those rows and set for the rest. `domain`
is slugified from the workbook's human title, and the human form is kept in
the record README.

### D9: The five id collisions are reported, not resolved

Five seed rows carry the id of a record this catalog has already admitted,
and the two sources disagree about the unit. The admitted record wins: the
ingestion never overwrites a validated record with a candidate one, and the
five rows are reported as collisions. The disagreement is real and is not
resolved here: the seed measures Mean Time to Recovery in hours, the catalog
measures it in minutes, and the seed's `dea:unit-percent` is the catalog's
`dea:unit-ratio-percent`. It is a question for the owner.

### D10: The corpus is a pool, and the MECE rule stays with admitted records

The MECE uniqueness rule already binds admitted records only, and it still
does. The candidate corpus is expected to share 5-axis signatures: it is a
coverage pool, and the axis values repeat by design. `scripts/report_coverage.py`
reports the distribution so coverage is visible rather than implied, and it is
a report, not a gate: a gate on coverage would be a gate on the data rather
than on the catalog.

### D11: The gates load the corpus once

At 4428 records every gate re-parsed every record from scratch, and a full
gate run took minutes. `scripts/_catalog.py` loads the corpus once per
process, using libyaml when the interpreter has it, and the eight gates use
it. Measured on this host: the schema gate went from 23.8s to 2.8s, the
measurement-conformance gate from 22.7s to 1.5s, the MECE gate from 11.8s to
1.5s. A full eight-gate run is now about 25s.

### D12: The corpus is checked against the workbook, not against a number

The pilot-era assertion that the catalog holds exactly 5 records turned red
on any addition, and the seed is an addition of 4423. It is replaced by a
check that reads the workbook and asserts that every seed-derived record
exists, that the set of ids matches the workbook's, and that each record's
provenance points back at its own workbook row. A hard-coded count is
replaced by a derived relationship, which is the fix board card #588 was
asking for.

## 4. Changes

1. `seeds/open-deam-candidate-metrics-seed.xlsx` and `seeds/README.md`.
2. `change-requests/CR-MET-016.md`, this document.
3. `schemas/entity.schema.json`: lifecycle-aware required set; widened id and
   abbreviation patterns; subject and purpose enums extended.
4. `classifications/subject-classifications.yaml`,
   `classifications/purpose-classifications.yaml`: the new values.
5. `classifications/field-aliases.yaml`: the `orientation` mapping corrected to
   `directionality` per the workbook's field guide; the seed's own column
   spellings added.
6. `classifications/seed-value-maps.yaml`: the value mapping.
7. `scripts/ingest_seed.py`: the ingestion pipeline, with `--check` for drift.
8. `scripts/_catalog.py`: the shared loader.
9. `scripts/report_coverage.py`: the coverage report.
10. The eight gate scripts: use the shared loader.
11. `entities/v1-alpha/`: 4423 candidate records with their READMEs.
12. `tests/test_conformance.py`: the corpus check replaces the pilot count; the
    superset check accounts for the lifecycle split; the source-credit rule is
    scoped to admitted records; the corpus-wide tests use the shared loader.
13. `.github/workflows/validate-metrics.yml`: openpyxl, the seed drift check,
    the coverage report.
14. `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`.

## 5. Decision points

### Q18: Mean Time to Recovery, minutes or hours?

Open. The seed and the catalog disagree, and both are credible. The
catalog's admitted record says minutes; the seed says hours. This CR does not
change the admitted record.

### Q19: The `dea:unit-percent` versus `dea:unit-ratio-percent` split.

Open. The seed's unit ids and the catalog's differ in form for the same
quantities. The catalog's form is the more precise one. Recorded, not
changed.

### Q20: Should the seed's five unit references that no entity defines be
admitted as unit entities?

Open. `dea:unit-percent`, `dea:unit-ratio`, `dea:unit-days` and 16 others
that the seed references are not defined anywhere in the metamodel, where only
`dea:unit-minute`, `dea:unit-usd` and `dea:unit-throughput-tps` exist, and
those only as a CR-MET-005 conformance fixture. The catalog's plain `unit`
field is what keeps the records self-contained in the meantime.

## 6. Definition of Done

- All eight gate scripts exit 0 over the 4428-record corpus.
- The full test suite passes.
- `python3 scripts/ingest_seed.py --check` reports that the catalog matches
  the workbook, and fails when a record is edited by hand.
- A record with a missing or invalid field is rejected by Gate 1, and a seed
  value with no mapping stops the ingestion rather than being guessed.
- D-004, D-005, and the embargo denylist are clean on every touched file.

## 7. NOT-list

- No admitted record is changed, and no seed row overwrites one.
- No unit entity is added to `dea-metamodel`.
- No abbreviation uniqueness rule is added.
- No `domain` or `sector` vocabulary is created (that is Q16 from CR-MET-015).
- No change to the upstream allocation drift (board card #600).

## 8. References

- Board cards #639 (field-gap analysis), #601, #602, #580, #588, #600.
- CR-MET-005 (unit semantics), CR-MET-009 (catalog establishment),
  CR-MET-014 (description field), CR-MET-015 (field dimensions, alias
  registry).
- `seeds/README.md` (the field and value mapping tables).
