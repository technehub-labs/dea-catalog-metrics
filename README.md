# Performance Metrics Catalog

> Canonical catalog of Performance Metric records for the OpenDEAM metamodel.

**Dimension:** `measurement-dimension` · **Entity:** `dea:PerformanceMetric` · **Alias:** `MTR` · **Metamodel:** [v0.2.1](https://github.com/technehub-labs/dea-metamodel)

[![View in Metamodel Explorer](https://img.shields.io/badge/Metamodel%20Explorer-View%20Entity-2C3E50?style=shield)](https://technehub-labs.github.io/metamodel/?entity=MTR)
[![Status: Live](https://img.shields.io/badge/Status-Live-22c55e?style=flat-square)](./)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](LICENSE)

## Overview

This catalog publishes **Metric records**: reusable, reusable-semantic
specifications of what is measurable and how its value is to be read and
interpreted. A record binds to the normative entity `dea:PerformanceMetric`,
defined in [dea-metamodel](https://github.com/technehub-labs/dea-metamodel)
(CR-MET-001 binding, metamodel `v0.2.1`).

The metamodel definition of the bound entity is:

> A formally defined, reusable semantic specification that describes a
> measurable property, characteristic, condition, quantity, rate, ratio, index,
> or other observable aspect of a subject, including the semantic rules
> necessary to determine and interpret its value.

`dea:PerformanceMetric` is a **normative, existing** entity in the
`measurement-dimension`, with class alias `MTR`. It is one of 163 metamodel
entities and the only one bound to this catalog.

### What this catalog does not do

- It **MUST NOT redefine** the normative Metric entity. `dea:PerformanceMetric`
  is defined once, in `dea-metamodel`. This catalog publishes *records of use*,
  not definitions of the entity.
- It is **not** an assessment catalog. The metamodel does define
  `dea:Assessment` and a 33-entity `dea:assessment` profile, but none of those
  is bound to a catalog, and no assessment catalog repository exists. Assessment
  semantics live in the metamodel and in `docs/FOUNDATIONS.md` as *related
  vocabulary*, not as content published here.
- It does not define maturity models. `dea:MaturityModel` and related entities
  are unbound metamodel concepts.

### Relationship to the wider framework

| Role | Where it lives |
|---|---|
| Normative Metric entity | `dea-metamodel` → `dea:PerformanceMetric` |
| Root model and allocation | `dea-architecture-framework` (`v0.2.1`, ADR-0002) |
| Metric records | **this repo** |
| Viewer | [Metamodel Explorer](https://technehub-labs.github.io/metamodel/?entity=MTR) |

The binding is declared in [`metamodel-pointer.yaml`](./metamodel-pointer.yaml)
and is validated in CI by the reusable allocation validator
(`dea-architecture-framework/.github/workflows/validate-against-model.yml`).

## Scope

The catalog publishes Metric records across 13 subject areas:
strategy, organization, customer, product/service, business architecture,
value architecture, information architecture, technology architecture,
governance, transformation, sustainability, capability, financial.

Records are classified on 5 axes plus a directionality axis:

| Axis | Cardinality | Source |
|---|---|---|
| subject | 1..* | `classifications/subject-classifications.yaml` |
| purpose | 1..* | `classifications/purpose-classifications.yaml` |
| orientation | 1 | `classifications/orientation-classifications.yaml` |
| scope | 1..* | `classifications/scope-classifications.yaml` |
| management significance | 1..* | `classifications/management-significance-classifications.yaml` |
| directionality | 1 | `higher_is_better` / `lower_is_better` / `target_band` / `categorical` |

Because these axes jointly define a Metric's identity, two records may not share
the same axis signature. The `check_mece_coverage` gate is the arbiter.

## Status (CR-MET-009, 2026-10-20)

- **5 Metric records admitted**, all at version 1.2.0: Customer Retention Rate,
  Mean Time to Recovery, Operating Margin, Data Completeness, Control
  Effectiveness Rate. These are the pilot cohort; they are not a complete set.
- **8 validation gates run in CI**: schema, measurement-conformance, MECE
  coverage, evidence anchors, threshold semantics, dual-anchor, formula
  namespace, and field alignment, plus a pytest run. See
  [CONTRIBUTING.md](./CONTRIBUTING.md) for the gate table.
- **5 classification axes** plus directionality (CR-MET-002 binding).
- **Dual-anchor model**: measurable-entity kind (16 CR-MET-007 types) plus
  reputability tier (5-value enum). Both are required for an `admitted` record.
- **Field dimensions** (CR-MET-015): `abbreviation` (the short form, equal to
  the formula's left-hand variable), `unit` (the plain unit label), plus the
  optional `domain`, `sector`, and `source_credit`. A field-alias registry
  maps an external vocabulary onto the catalog's canonical names, for
  ingesting Metric contributions.

See [docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md) for the canonical scope,
classification model, dual-anchor model, MECE coverage target, and pilot
composition.

## Layout

```text
dea-catalog-metrics/
|-- README.md
|-- CONTRIBUTING.md
|-- CHANGELOG.md
|-- CITATION.cff
|-- LICENSE
|-- NOTICE
|-- CATALOG.yaml                     # registry of admitted catalog records
|-- TEMPLATE_VERSION
|-- metamodel-pointer.yaml           # binds to dea:PerformanceMetric (v0.2.1)
|
|-- entities/v1-alpha/               # Metric records (admitted + candidate)
|
|-- schemas/entity.schema.json       # SUPERSET of dea-metamodel metric.json
|-- classifications/                 # 5-axis vocabularies + field-alias registry
|
|-- scripts/                         # gate scripts + catalog regenerator
|-- tests/                           # gate tests
|
|-- docs/FOUNDATIONS.md              # scope, classification, dual-anchor, MECE, pilot
|
|-- 00_inbox/                        # CR-MET-000..012 programme drafts
|-- change-requests/
|   `-- CR-MET-009.md
|
`-- .github/workflows/
    |-- validate-allocation.yml      # reusable validator (dea-architecture-framework)
    `-- validate-metrics.yml         # runs the wired gates + pytest
```

Every path above exists in the repository. `contexts/v1-alpha/` and
`validation/conformance/`, both shown in earlier revisions of this file, do not
exist; the gate scripts live in `scripts/` and Baseline/Target/Threshold/
Interpretation contexts (CR-MET-006) are **not yet published**.

## How to contribute

See [CONTRIBUTING.md](./CONTRIBUTING.md). Each Metric record requires:

1. `entities/v1-alpha/dea:metric-<slug>/dea:metric-<slug>`, a
   schema-compliant YAML definition. Since CR-MET-014 that includes a required
   `description`: the canonical human-readable definition of the record, which
   must match the record README's Definition section verbatim (a conformance
   test compares them).
2. A record `README.md` following the structure in
   [CONTRIBUTING.md](./CONTRIBUTING.md).
3. Both dual anchors (measurable-entity kind and reputability tier).
4. An `abbreviation` equal to the formula's short form, and a `unit` coherent
   with `unit_ref` (CR-MET-015).
5. At least one `quality.measurement_evidence` reference.
6. A `metadata.established_by` CR reference.

Three constraints are easy to miss and are enforced in CI, not by review:

- **MECE uniqueness.** The 5-axis signature must not collide with an existing
  record. Copying an existing record and renaming it fails
  `check_mece_coverage`.
- **The pilot-count assertion.** `tests/test_conformance.py` asserts the record
  count is 5 ("CR-MET-009: pilot must have 5 metrics"). Adding a record makes
  that test red until the same PR updates the count. This is a pilot-era
  assertion and is tracked for removal.
- **Registry freshness.** `CATALOG.yaml` is generated. Edit a record, then run
  `python3 scripts/regenerate_catalog.py` and commit the result in the same
  change. Since CR-MET-014 the generator is idempotent, so CI fails a PR whose
  registry does not match the records.

## License

Apache 2.0 - see [LICENSE](./LICENSE).