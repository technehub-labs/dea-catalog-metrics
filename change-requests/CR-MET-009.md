# CR-MET-009 -- Establish the Canonical DEA Metric Catalog and Reusable Metric Definition Repository

| Field | Value |
|---|---|
| Status | Proposed (this document) |
| Target repository | `technehub-labs/dea-catalog-metrics` |
| Author | Emmanuel A. Otchere |
| Date | 2026-10-18 |
| Depends on | CR-MET-001 (merged 2c445e4); CR-MET-002 (merged 84f10f4); CR-MET-005 (merged 9fdf356); CR-MET-007 (merged c319ea5); CR-MET-008 (merged 1fa04ef) |
| Blocks | CR-MET-010 (governance on Metric/Measurement); CR-MET-011 (calculation lineage on the catalog); CR-MET-012 (analytics on the catalog); CR-MET-013 (programme closure) |
| Cardinal authority | dea-catalog-metrics (catalog); dea-metamodel (canonical semantics); dea-governance (identity / lifecycle / conformance / change control) |
| Kanban | T-MET umbrella #429; this CR is card #439; parked card #427 re-scopes here |
| Stream | Stream B (Enterprise interpretation and governance); fourth Stream B item. First CATALOG-side slice (CR-MET-001..008 were metamodel-side). |

## 1. Background and problem statement

The metamodel defines what a Metric is. It does not provide the complete collection of reusable Metric definitions required across enterprise architecture domains.

OpenDEAM needs a dedicated catalog for publishing, discovering, referencing, and reusing governed Metric definitions. The catalog must become a semantic resource, not merely a list of KPIs.

It should support Metrics across strategy, organization, customers, business architecture, technology, data, risk, governance, sustainability, and transformation.

The current `dea-catalog-metrics` repo is a scaffold (4 files: LICENSE, NOTICE, README.md, metamodel-pointer.yaml). The previous round-2 CR-METRIC-01 proposal is superseded by this CR.

## 2. Objective

Establish a canonical Metric catalog repository aligned with the OpenDEAM metamodel, identity architecture, repository conventions, documentation standards, and CI/CD pipeline.

## 3. Repository positioning (binding)

The catalog repository:

- Consumes the canonical entity definitions from `dea-metamodel` (binding: the metamodel is the source of truth; the catalog publishes reusable definitions; the catalog MUST NOT redefine the normative Metric entity).
- Publishes reusable Metric definitions (catalog-internal `type: Metric` records with full attribute sets).
- Supports controlled Metric classifications (CR-MET-002 binding 6 axes).
- Maintains canonical entity identifiers (CR-3P binding; entity id = `dea:metric-<slug>`).
- Documents calculation methods (CR-MET-005 binding formula_definition; CR-MET-003 binding Measurement).
- Establishes relationships to relevant enterprise concepts (CR-MET-007 cross-domain extensions).
- Supports versioning and lifecycle management (CR-MM-04 R1 binding).
- Provides machine-readable (`<id>.yaml`) and human-readable (`README.md`) representations per record.
- Integrates with existing DEA registry + validation tooling (`dea-architecture-framework`).
- Supports contributions from multiple enterprise domains.

## 4. Repository structure (binding; per dea-catalog-processes proven pattern)

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
|-- metamodel-pointer.yaml           # points to dea:PerformanceMetric (CR-MET-001)
|
|-- entities/
|   `-- v1-alpha/
|       |-- dea:metric-mean-time-to-recovery/
|       |   |-- dea:metric-mean-time-to-recovery.yaml
|       |   |-- README.md
|       |   `-- research/
|       |       `-- ...
|       |-- dea:metric-customer-retention-rate/
|       |-- dea:metric-system-availability/
|       |-- dea:metric-operating-margin/
|       |-- dea:metric-data-completeness/
|       `-- dea:metric-control-effectiveness-rate/
|
|-- schemas/
|   |-- entity.schema.json           # CR-MET-009 catalog schema mirror of dea-metamodel metric.json
|   |-- indicator-designation.schema.json  # CR-MET-008 binding
|   `-- baseline.schema.json         # CR-MET-006 binding
|
|-- classifications/                 # CR-MET-002 binding; 6-axis classification files
|   |-- subject-classifications.yaml
|   |-- purpose-classifications.yaml
|   |-- orientation-classifications.yaml
|   |-- scope-classifications.yaml
|   `-- management-significance-classifications.yaml
|
|-- contexts/                        # CR-MET-006 binding; Baseline / Target / Threshold / Interpretation contexts
|   `-- v1-alpha/
|       `-- ...
|
|-- validation/
|   `-- conformance/
|       `-- README.md
|
|-- scripts/                         # the 6 validation gates (CR-MM-04 R1 binding)
|   |-- check_metric_schema.py
|   |-- check_measurement_conformance.py
|   |-- check_mece_coverage.py
|   |-- check_evidence_anchors.py
|   |-- check_threshold_semantics.py
|   |-- check_dual_anchor.py
|   `-- regenerate_catalog.py
|
|-- tests/                           # gate tests
|   `-- test_conformance.py
|
|-- docs/
|   |-- FOUNDATIONS.md               # scope, classification, dual-anchor model, MECE coverage
|   `-- examples/
|
|-- examples/
|
|-- change-requests/
|   `-- CR-MET-009.md (this document)
|
`-- .github/
    `-- workflows/
        |-- validate-allocation.yml  # existing reusable validator
        `-- validate-metrics.yml     # NEW: the 6 validation gates
```

The structure reuses the proven `dea-catalog-processes` layout (entity-folder per record; `<id>.yaml` + `README.md`; `CATALOG.yaml`; `schemas/`; `classifications/`; `contexts/`; `validation/`; `scripts/`; `tests/`).

## 5. Metric entity documentation standard (19 sections; per user-supplied §5)

Every Metric has a machine-readable definition (`dea:metric-<id>.yaml`) and a human-readable README. The README template covers 19 sections:

1. Identity (canonical id + name)
2. Definition (formal semantic)
3. Purpose (intended use)
4. Classification (CR-MET-002 binding: subject, purpose, orientation, scope, management_significance, nature)
5. Measurement subject (what is measured)
6. Unit or scale (CR-MET-005 binding unit/scale references)
7. Formula (CR-MET-005 binding formula_definition)
8. Inputs (required data and input definitions)
9. Source (authoritative data source)
10. Frequency (measurement frequency)
11. Directionality (CR-MET-002 binding; higher_is_better / lower_is_better / etc.)
12. Applicability (organizational contexts; CR-MET-007 cross-domain applicability)
13. Relationships (CR-MET-007 cross-domain; CR-MET-008 designation; CR-MET-006 baseline/target/threshold)
14. Quality (validation requirements; CR-MET-005 precision/rounding)
15. Governance (CR-MET-010 owner / steward; binding deferred to CR-MET-010)
16. Examples (illustrative calculation; CR-MET-005 binding)
17. Limitations (known exclusions)
18. Version (version and lifecycle status)
19. References (supporting standards; CR-MM-04 R1 binding)

## 6. Initial catalog content: 5-Metric pilot (binding)

The 5-Metric pilot composition (per Section 9 Q12a/b disposition) demonstrates cross-domain coverage and exercises every dimension of the metamodel:

| # | Domain | Metric | Demonstrates |
|---|--------|--------|--------------|
| 1 | Customer | Customer Retention Rate | CR-MET-001/002/005/006/008 (KPI Lagging + KRI Leading designations; target band; bounded_optimum threshold; formula_definition; composite_definition; cross-domain applicability to BusinessCapability/BusinessProcess/Outcome) |
| 2 | Technology | Mean Time to Recovery | CR-MET-005 lifecycle + CR-MET-004 measurement execution modes (formula: arithmetic mean; Lifecycle: completed/failed/cancelled/superseded) |
| 3 | Financial | Operating Margin | CR-MET-005 WEIGHTED_MEAN aggregation with weight_basis=numerator_denominator (the binding aggregation semantic for financial ratios; ratio dimensionality) |
| 4 | Data | Data Completeness | CR-MET-007 cross-domain applicability to DataEntity (the canonical data-quality Metric) |
| 5 | Governance | Control Effectiveness Rate | CR-MET-008 KCI designation (control effectiveness; control objective reference; threshold_reference for warning/critical) |

The remaining 7 reference Metrics from the user-supplied §6 (Strategic Objective Attainment, Employee Engagement Score, Process Cycle Time, Risk Exposure Index, Benefits Realization Rate, Energy Consumption Intensity, Capability Performance Score) land in a follow-on slice (per Q12a recommendation; the pilot proves the slice anchor model).

## 7. Catalog governance (binding; per CR-MM-04 R1)

The repository establishes:

- Metric contribution process (CONTRIBUTING.md).
- Definition review and approval (gate: `check_measurement_conformance.py`).
- Canonical identifier assignment (gate: `check_metric_schema.py`).
- Semantic duplicate detection (gate: `check_mece_coverage.py`).
- Classification consistency (gate: `check_classification_consistency.py`; CR-MET-002 binding).
- Versioning (CR-MM-04 R1; minor bump on additive change; major bump on breaking change).
- Deprecation (lifecycle_status: "retired" preserves historical record).
- Cross-repository references (CR-MM-04 R2; cross-repo-consumer tests in dea-metamodel).
- Domain stewardship (CONTRIBUTING.md; CR-MET-010 governance deferred).
- Provenance and source attribution (per-record `metadata.established_by: CR-MET-009`).

Catalog contributions MUST NOT redefine the normative Metric entity. The metamodel is the source of truth.

## 8. CI/CD integration (binding; the 6 validation gates)

The catalog pipeline runs 6 validation gates on every push and PR. Each gate emits 0 findings for the catalog to pass:

| Gate | File | Purpose |
|---|---|---|
| 1 | `check_metric_schema.py` | Schema compliance against `schemas/entity.schema.json` (mirror of dea-metamodel metric.json). Validates required fields, id pattern, version semver, classification axes. |
| 2 | `check_measurement_conformance.py` | Metric-measurement conformance. Validates that each Metric with `measurement_method` references an existing Measurement schema; each Measurement references a real Metric. (CR-MET-003 binding.) |
| 3 | `check_mece_coverage.py` | MECE coverage on the 5 classification axes (subject, purpose, orientation, scope, management_significance). No two Metrics share the same (subject, purpose, orientation, scope) tuple. (CR-MET-002 binding.) |
| 4 | `check_evidence_anchors.py` | Provenance. Each record carries `metadata.established_by` (CR reference) and at least one `references` link to a standard or empirical source. (CR-MM-04 R1 binding.) |
| 5 | `check_threshold_semantics.py` | Threshold semantics. Each Metric with `direction: lower_is_better` declares thresholds in the correct order (warning > critical); each Metric with `direction: higher_is_better` declares thresholds in the reverse order. Each Metric with `direction: bounded_optimum` declares `{min, max}`. (CR-MET-006 binding.) |
| 6 | `check_dual_anchor.py` | Dual-anchor requirement. Each record declares BOTH (a) a measurable-entity kind (the 16 cross-domain subject types from CR-MET-007) AND (b) a reputability tier (one of: industry_standard, framework_derived, sectoral_standard, internal_custom, emerging). (CR-MET-009 §9 Q13/14 binding.) |

## 9. Decision points (binding disposition)

### Q12; Initial catalog composition (binding)

- (a) **12 reference Metrics one per domain** (user-supplied §6).
- (b) **5-KPI pilot then 7 follow-on** (the round-2 proposal).
- (c) **3 named in §4 then grow** (minimal viable).

**Recommended: (a) for the canonical catalog-establishment slice, with (b) as the immediate-pilot sub-slice.** The catalog's first PR is method + schemas + templates + the 5-Metric pilot (Section 6 above); the remaining 7 land in a follow-on PR after the pilot proves the slice anchor model.

### Q13; Reputability tier model (binding)

- **(a) 5-value enum: industry_standard | framework_derived | sectoral_standard | internal_custom | emerging.** RECOMMENDED. Matches the round-2 dual-anchor proposal and CR-MET-001 direction.

### Q14; Dual-anchor requirement strength (binding)

- **(a) Both anchors required for ADMIT-CANONICAL; informational-only on `lifecycle_status: candidate` records.** RECOMMENDED. Matches the round-2 dual-anchor proposal.

## 10. metamodel-pointer.yaml migration (binding)

The current `metamodel-pointer.yaml` declares `entity_id: dea:entity-metric`. CR-MET-001 re-membershiped the canonical Metric to `dea:PerformanceMetric` (kind: core / profile: null). The pointer MUST migrate to:

```yaml
metamodel:
  version: v0.2.1
  entity_id: dea:PerformanceMetric
  class_alias: MTR
  dimension: measurement-dimension
  scope_layers: [L1, L2, L3, L4, L5]
  viewer_url: "https://technehub-labs.github.io/metamodel/?entity=dea:PerformanceMetric"
  legacy_ids:
  - dea:entity-metric
  - Metric
```

The `legacy_ids` preserves the dea-architecture-framework cross-reference so the existing allocation validator does not fail.

## 11. Definition of Done

- Repository structure matches Section 4.
- `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `CITATION.cff`, `CATALOG.yaml`, `schemas/entity.schema.json`, `classifications/` (5 files), `templates/`, `examples/`, `validation/conformance/`, `scripts/` (6 gates + 1 regenerator), `tests/`, `docs/FOUNDATIONS.md`, `change-requests/CR-MET-009.md` are all present.
- The 5-Metric pilot records (Section 6) are landed with full `<id>.yaml` + `README.md` per the documentation standard.
- The 6 validation gates pass with 0 findings on the pilot.
- The metamodel-pointer.yaml is migrated (Section 10).
- D-004 / D-005 / embargo / author-denylist scans pass on all new files.
- The parked card #427 (FOUNDATIONS.md sub-card) re-scopes here; `docs/FOUNDATIONS.md` documents scope, classification, dual-anchor, MECE, pilot composition.

## 12. NOT-list

- This CR does NOT redefine the normative Metric entity. The metamodel is the source of truth.
- This CR does NOT include operational measurement history or observations. The catalog is a definitions repository.
- This CR does NOT publish hundreds of Metrics in the first slice. The 5-Metric pilot is the conservative starting point.

## 13. References

- CR-MET-001 (merged; commit 2c445e4) (Metric canonical entity; `dea:PerformanceMetric` re-membershiped).
- CR-MET-002 (merged; commit 84f10f4) (classification axes).
- CR-MET-003 (merged; commit 5f7cddf) (Measurement / Observation entities; `dea:measures-subject`).
- CR-MET-005 (merged; commit 9fdf356) (units, dimensions, formulas, aggregation).
- CR-MET-006 (merged; commit 8a8185a) (Baseline / Target / Threshold / PerformanceInterpretation).
- CR-MET-007 (merged; commit c319ea5) (cross-domain `dea:measured-by` widening).
- CR-MET-008 (merged; commit 1fa04ef) (IndicatorDesignation).
- Existing dea-catalog-processes pattern (proven catalog layout; reused).
- Existing dea-architecture-framework reusable allocation validator (CR-MM-04 R1 binding).
- User-supplied CR-MET-009: `/home/hermes/dea-work/dea-catalog-metrics/00_inbox/CR-MET-006-012.md` (lines 808..1036).
- User-supplied §4 escape clause (per CR-MET-008): where a designation introduces materially different lifecycle / identity / governance requirements, a specialized construct may be justified through an ADR.
- CR-MM-04 R1 (versioning + citation conventions).
- CR-MM-04 R2 (cross-repo-consumer tests).
- EGV-004 (identity continuity).
- ADR-013 (Core non-accumulation).