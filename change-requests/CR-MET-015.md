# CR-MET-015 -- Extend the Catalog Metric Schema with Five Field Dimensions and an Ingestion Alias Registry

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-25 |
| Depends on | CR-MET-009 (catalog establishment); CR-MET-014 (description field, PR #6) |
| Blocks | none |
| Cardinal authority | dea-catalog-metrics (catalog); dea-metamodel (canonical semantics) |
| Kanban | board 9 |

## 1. Background and problem statement

A Metric field list supplied from outside this organisation names 18 fields.
Reconciled against the catalog schema (board card #639): 13 have an
equivalent, 5 have no catalog field at all.

| Field | Status in the catalog schema |
|---|---|
| abbreviation | absent |
| unit | absent (present in the normative `metric.json` only) |
| domain | absent |
| sector | absent |
| source_credit | absent |

Ten further fields exist in the catalog under a different name (`metric id` to
`id`, `formula` to `formula_definition`, `unit id` to `unit_ref`,
`subject_area` to `subject_classification`, `scope` to `scope_classification`,
`purpose` to `purpose_classification`, `orientation` to
`orientation_classification`, `significance` to `management_significance`,
`status` to `lifecycle_status`).

The purpose of the catalog is to be the canonical home for Metric records, and
the stated purpose of these five fields is to make the catalog able to receive
Metric contributions authored against that external vocabulary. That requires
two separate things, and this CR does both:

1. the five absent fields must be expressible, so an ingested record is not
   silently lossy;
2. the renamed fields must be receivable under their external names, so an
   ingested record is not rejected for spelling.

The owner's direction on the second point: do **not** rename the catalog's
`subject_classification` to `subject_area`. Treat the external names as
**synonyms / aliases**, used when ingesting contributions, while the catalog
keeps its canonical names.

## 2. Objective

Add the five missing field dimensions to the catalog schema with definitions
and coherence rules, and add a registry that maps the external vocabulary onto
the canonical one so an ingested record can be canonicalised before it is
validated.

## 3. Decisions (binding)

### D1: Field definitions

| Field | Type | Required | Definition |
|---|---|---|---|
| `abbreviation` | string, `^[A-Z][A-Z0-9]{1,9}$` | yes | The Metric's short form. Must equal the left-hand variable of `formula_definition.expression` for admitted records. |
| `unit` | string, `^[a-z][a-z0-9_]*$` | yes | The plain unit label the value is expressed in. |
| `domain` | string, `^[a-z][a-z0-9_]*$` | no | The business domain the Metric characterises. |
| `sector` | string, `^[a-z][a-z0-9_]*$` | no | The industry sector the Metric applies to. |
| `source_credit` | string | no | The attribution for the Metric's definition (who may be credited as its source). |

`abbreviation` and `unit` are required because they are intrinsic to a
Metric's identity: every record in the pilot has a short form and a unit, and
both are already implied by fields the gates enforce. `domain`, `sector`, and
`source_credit` are optional because they are contextual and not every Metric
has an attributable sector or a creditable source.

### D2: `abbreviation` is the formula short form, not a second naming system

`formula_definition.expression` already carries the short form on its
left-hand side, and Gate 7 (`check_formula_namespace.py`) already guards the
namespace of that form: `MTTR` is reserved for Mean Time to Recovery, and
binding a reserved form to a different quantity is a blocking finding.
Declaring `abbreviation` as a separate field would create a second place to
state the same fact. It is therefore required to **equal** that short form, and
Gate 8 checks the equality. A record that wants a different short form changes
the formula's left-hand side, which Gate 7 then namespaces as it should.

### D3: `unit` is coherent with `unit_ref` by a mechanical rule, not a vocabulary

The catalog's `unit_ref` points at a `dea:unit-*` id. Those ids are not
canonical metamodel entities: `dea:unit-minute`, `dea:unit-usd`, and
`dea:unit-throughput-tps` are defined only in the metamodel's CR-MET-005
conformance fixture, and `dea:unit-ratio-percent`, which four of the five
pilot records reference, is **referenced in six places and defined in none**.
The unit-reference target set is therefore not something a catalog gate can
resolve today, and the `unit` string is what makes a record self-contained.

The coherence rule is mechanical and needs no vocabulary:
`unit_ref` must be `dea:unit-<unit>` or `dea:unit-ratio-<unit>`. So
`dea:unit-minute` pairs with `minute`, and `dea:unit-ratio-percent` pairs with
`percent`.

### D4: `domain` and `sector` are free slugs, with a recorded gap

The metamodel has domain vocabularies, but they belong to other entity types:
`Blueprint.domain` carries `integration, data, application, infrastructure,
security, business, technology`, which is an architecture blueprint taxonomy,
not a business domain. `BusinessObject.ecf_domain` and `Guardrail.domain` are
the same shape. Reusing the Blueprint values for a Metric would be a category
error, so `domain` is a free slug.

There is no industry-sector axis anywhere in the metamodel, the normative
schema, or the catalog, so `sector` is a free slug too. Both are recorded as
Q16: a controlled vocabulary for each would be better, and that is a separate
decision with a separate CR.

### D5: `source_credit` is coherent with the evidence already required

Gate 4 already requires at least one `quality.measurement_evidence` reference
for every admitted record. `source_credit` names the attribution for the
Metric's definition, so Gate 8 requires it to appear among the record's
measurement evidence. The two fields cannot disagree, and a credit that is not
evidence is rejected.

### D6: The catalog keeps its canonical names; the external names are aliases

`subject_classification` is **not** renamed. The catalog's axis names are
deliberate: they say which axis a value belongs to, where the external
vocabulary says only "area" or "purpose" or "scope". Renaming them would
break every record, every gate, and the CR-MET-002 binding, in exchange for
spelling that is less precise.

Instead, `classifications/field-aliases.yaml` is a registry mapping the
external names onto the canonical ones:

| Alias | Canonical |
|---|---|
| metric id | id |
| formula | formula_definition |
| unit id | unit_ref |
| subject_area | subject_classification |
| scope | scope_classification |
| purpose | purpose_classification |
| orientation | orientation_classification |
| significance | management_significance |
| status | lifecycle_status |

### D7: Ingestion canonicalises before it validates

`scripts/normalize_record.py` reads a record, rewrites alias names to
canonical names, and refuses when a record carries both spellings of one field
with different values. It is idempotent, and it is the step an ingestion path
runs before Gate 1.

The catalog schema declares only canonical names. A record that arrives with
`subject_area` is not valid against the schema, and is not meant to be: it is
canonicalised first. That keeps the catalogue itself unambiguous, which is the
point of the registry, and it is why the alias names are not added to
`schemas/entity.schema.json`.

### D8: Gate 8 enforces alias discipline and the new fields' coherence

`scripts/check_field_alignment.py` is a new gate, wired into CI as Gate 8. It
checks:

1. every alias in the registry resolves to a property the schema declares
   (the registry cannot rot);
2. no alias name is itself a canonical schema property (no ambiguity);
3. no live catalog record uses an alias name (the catalogue stays canonical);
4. no live record carries both spellings of one field;
5. `abbreviation` equals the formula short form;
6. `unit` is coherent with `unit_ref` under the D3 rule;
7. `source_credit` appears in `quality.measurement_evidence`.

### D9: The pilot records are populated only where the value is derivable

`abbreviation` and `unit` are derived from each record's existing content
(`MTTR`, `CRR`, `OM`, `DC`, `CER`; `minute`, `percent`). `source_credit` is
derived from the record's own first `quality.measurement_evidence` entry, so
it is a credit the record already carries rather than a new assertion.

`domain` and `sector` are **left absent** on all five records. There is no
vocabulary to draw them from, and inventing a sector for a pilot Metric would
be a fabricated provenance claim, not a schema exercise.

Records are bumped 1.0.1 to 1.2.0. The catalog's versioning rule gives a patch
bump for an additive change and a minor bump for a substantive one; two newly
required fields on the record contract is substantive.

## 4. Changes

1. `schemas/entity.schema.json`: add the five properties; add `abbreviation`
   and `unit` to `required`.
2. `classifications/field-aliases.yaml`: the alias registry.
3. `scripts/normalize_record.py`: alias canonicalisation for ingestion.
4. `scripts/check_field_alignment.py`: Gate 8.
5. `entities/v1-alpha/*`: populate `abbreviation`, `unit`, `source_credit`;
   bump to 1.2.0; append a change-history entry.
6. `tests/test_conformance.py`: registry integrity, alias-free catalogue,
   abbreviation and unit coherence, source-credit coherence, normaliser
   idempotence.
7. `.github/workflows/validate-metrics.yml`: wire Gate 8.
8. `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`: the new fields, the alias
   registry, and the ingestion path.

## 5. Decision points

### Q16: Controlled vocabularies for `domain` and `sector`

Open. Both are free slugs because no suitable vocabulary exists in this
organisation: the metamodel's domain vocabularies belong to Blueprint,
BusinessObject, Guardrail, and OrganizationalUnit, and there is no sector axis
at all. A metric-domain vocabulary and a sector vocabulary would make both
fields MECE-checkable, the way the five classification axes are.

### Q17: Should `source_credit` be plural?

Open. It is a single string here. A Metric with several attributable sources
would need a repeated credit, which `quality.measurement_evidence` already
covers as an array. Making `source_credit` an array is a one-line change if
the owner prefers it.

## 6. Definition of Done

- Gate 1 fails a record that omits `abbreviation` or `unit`, or sets either
  to an empty string (proven by mutation in a throwaway clone).
- Gate 8 fails a record whose `abbreviation` disagrees with its formula short
  form, whose `unit` disagrees with its `unit_ref`, whose `source_credit` is
  not among its evidence, or that uses an alias name (each proven by
  mutation).
- `normalize_record.py` canonicalises an alias-spelled record to the canonical
  names, refuses a record that carries both spellings with different values,
  and is idempotent on a canonical record (each proven by test).
- All nine gate scripts exit 0 and the full test suite passes.
- D-004, D-005, and the embargo denylist are clean on every touched file.

## 7. NOT-list

- No renaming of any existing catalog field. `subject_classification` stays.
- No alias names in `schemas/entity.schema.json` (see D7).
- No `domain` or `sector` values invented for the pilot records (see D9).
- No change to the upstream allocation drift (board card #600).
- No unit entity definitions added to `dea-metamodel`; the undefined
  `dea:unit-ratio-percent` reference is recorded as a finding, not fixed here.

## 8. References

- Board cards #639 (field-gap analysis), #601, #602, #580.
- CR-MET-005 (unit semantics, metamodel fixture), CR-MET-009 (catalog
  establishment), CR-MET-014 (description field).
- `dea-metamodel/schemas/entities/metric.json` (normative `unit`).
