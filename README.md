# Performance Metrics Catalog

> Catalog for Performance Metric (PM) entities in the OpenDEAM framework.

[![Status: Live](https://img.shields.io/badge/Status-Live-22c55e?style=flat-square)](./)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](LICENSE)

## Overview

Canonical catalog for Performance Metric (PM) entities in the OpenDEAM framework.
Aligns with `dea:PerformanceMetric` in [dea-metamodel](https://github.com/technehub-labs/dea-metamodel)
(CR-MET-001 binding).

The catalog publishes reusable Metric definitions across 13 subject areas:
strategy, organization, customer, product/service, business architecture, value architecture,
information architecture, technology architecture, governance, transformation,
sustainability, capability, financial.

## Status (CR-MET-009, 2026-10-18)

- **5-Metric pilot admitted**: Customer Retention Rate, Mean Time to Recovery, Operating Margin, Data Completeness, Control Effectiveness Rate.
- **6 validation gates**: schema, measurement-conformance, MECE coverage, evidence anchors, threshold semantics, dual-anchor.
- **5 classification axes**: subject, purpose, orientation, scope, management significance (CR-MET-002 binding).
- **Dual-anchor model**: measurable-entity kind (16 CR-MET-007 types) + reputability tier (5-value enum).

See [docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md) for the canonical scope, classification, dual-anchor model, MECE coverage target, and pilot composition.

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
|-- metamodel-pointer.yaml           # points to dea:PerformanceMetric
|
|-- entities/v1-alpha/               # admitted + candidate Metric records
|
|-- schemas/                         # entity.schema.json mirror of metric.json
|-- classifications/                 # 5-axis classification vocabularies
|-- contexts/v1-alpha/               # Baseline/Target/Threshold/Interpretation contexts
|
|-- validation/conformance/          # the 6 validation gates
|-- scripts/                         # gate scripts + regenerator
|-- tests/                           # gate tests
|
|-- docs/FOUNDATIONS.md              # scope, classification, dual-anchor, MECE, pilot
|
|-- change-requests/
|   `-- CR-MET-009.md
|
`-- .github/workflows/
    |-- validate-allocation.yml      # existing reusable validator (dea-architecture-framework)
    `-- validate-metrics.yml         # NEW: runs all 6 gates
```

## How to contribute

See [CONTRIBUTING.md](./CONTRIBUTING.md). Each Metric requires:

1. A `entities/v1-alpha/dea:metric-<slug>/dea:metric-<slug>.yaml` machine-readable definition.
2. A `README.md` covering 19 documentation sections (see FOUNDATIONS.md).
3. Both dual anchors (measurable-entity kind + reputability tier).
4. At least one `quality.measurement_evidence` reference.
5. A `metadata.established_by` CR reference.

The 6 validation gates will fail the PR if any requirement is missing.

## License

Apache 2.0 - see [LICENSE](./LICENSE).