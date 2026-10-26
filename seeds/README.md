# Seed workbooks

Source datasets ingested into this catalog. A seed is a published, versioned
artifact; the catalog records derived from it carry provenance back to it, so
every ingested record can be traced to the row it came from.

## open-deam-candidate-metrics-seed.xlsx

| Property | Value |
|---|---|
| SHA-256 | `f037b8d3dfeb48538715e975492f4a864f56bfd58d66bed99afcad222a7af1c4` |
| Received | 2026-10-26 |
| Sheets | `Overview` (298 rows), `Candidate Metrics` (4428 data rows), `Field Guide` (24 rows) |
| Ingested by | CR-MET-016 |
| Records produced | 4423 candidate records |

The `Candidate Metrics` sheet carries a header row at row 6 and data rows 7 to
4434, so 4428 metric rows. The `Field Guide` sheet is the workbook's own
mapping table: it names, for each sheet field, the catalog artefact it is
meant to populate. That guide is the authority for the field mapping below,
and where the guide and this catalog's own field names differ, the guide
states which catalog artefact receives the value.

## Field mapping

| Sheet column | Field Guide name | Catalog field | Rule |
|---|---|---|---|
| `metric_id` | metric_id | `id` | `dea:metric-<slug>`; 2 ids begin with a digit, so the id pattern allows a leading digit (CR-MET-016) |
| `name` | name | `name` | verbatim |
| `abbr` | abbreviation | `abbreviation` | verbatim; 1362 short forms use characters the pilot pattern forbade (`%`, `/`, `:`, mixed case), so the pattern was widened |
| `description` | description | `description` | verbatim; the guide assigns it to the README definition section, and the catalog's `description` is that same text |
| `prose` | (not in the guide) | record README `Context` section | present on 2405 of 4428 rows; a hand-written narrative, complementary to the templated `description` |
| `formula` | formula | `formula_definition.expression` | plain-text expression, wrapped in the catalog's 8-field formula object |
| `unit_id` | unit_id | `unit_ref` | verbatim; the catalog's plain `unit` is derived from it |
| `unit` | unit | record README `Unit` line | human-readable unit label; the catalog's `unit` field is the slug derived from `unit_ref`, so the label is documentation |
| `reputability_tier` | reputability_tier | `reputability_tier` | verbatim; fixed at `industry_standard` for this seed |
| `subject_area` | subject_area | `subject_classification` | see the value mapping below |
| `domain` | domain | `domain` | slugified from the workbook's human title |
| `sector` | sector | `sector` | slugified; omitted where the workbook says `All industries`, which is not a sector |
| `scope` | scope | `scope_classification` | see the value mapping below |
| `entity_kind` | measurable_entity_kind | `measurable_entity_kind` | see the value mapping below |
| `purpose` | purpose | `purpose_classification` | see the value mapping below |
| `orientation` | orientation | `directionality` | the guide assigns this field to threshold semantics, which is the catalog's `directionality`; `higher-is-better`, `lower-is-better` and `target-band` map one to one |
| `significance` | significance | `management_significance` | see the value mapping below |
| `source_credit` | source_credit | `source_credit` | verbatim |
| `status` | status | `lifecycle_status` | verbatim; every seed row is `candidate` |
| `batch` | (not in the guide) | `metadata.seed.batch` | provenance: the workbook's batch number |

## Value mapping

Seed values that have no direct home in the catalog's controlled vocabularies
are mapped in
[`classifications/seed-value-maps.yaml`](../classifications/seed-value-maps.yaml),
which the ingestion script reads. A value is either carried through unchanged
(after hyphen to underscore normalisation), mapped to an existing catalog
value, or a new value added to the vocabulary. The three cases are kept
distinct in that file so a reader can see which is which.

## What the seed does not carry

The catalog's `subject_concept`, `measurement_nature`, `orientation_classification`
and `measurement_nature_detail` have no column in this workbook, and the
workbook's own field guide does not mention them. They are admission-time
fields: a candidate does not have to carry them, and CR-MET-016 makes the
schema's required set lifecycle-aware so that an `admitted` record must carry
the full set and a `candidate` record carries what the source provides.

## Id collisions with admitted records

Five of the workbook's 4428 rows carry the id of a record this catalog has
already admitted, and the two sources disagree about the unit:

| Metric | Workbook | Catalog |
|---|---|---|
| `dea:metric-mean-time-to-recovery` | `dea:unit-hours` | `dea:unit-minute` |
| `dea:metric-operating-margin` | `dea:unit-percent` | `dea:unit-ratio-percent` |
| `dea:metric-customer-retention-rate` | `dea:unit-percent` | `dea:unit-ratio-percent` |
| `dea:metric-data-completeness` | `dea:unit-percent` | `dea:unit-ratio-percent` |
| `dea:metric-control-effectiveness-rate` | `dea:unit-percent` | `dea:unit-ratio-percent` |

The admitted record wins: the ingestion skips those five rows rather than
overwriting a validated record with a candidate one. The disagreement is
recorded rather than silently resolved, and it is a live question for the
owner, because the two sources are both credible and they do not agree on
whether Mean Time to Recovery is measured in minutes or in hours.
