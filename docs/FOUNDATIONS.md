# FOUNDATIONS -- Performance Metric Catalog

> Canonical scope, classification, dual-anchor model, MECE coverage target, and pilot composition for the OpenDEAM Performance Metric catalog.

Lives at `docs/FOUNDATIONS.md` per CR-MET-009 Section 11 (parked card #427 re-scopes here). Lands as part of CR-MET-009 (catalog-establishment).

## 1. Scope

The catalog publishes reusable Metric definitions across the OpenDEAM framework.
It does NOT redefine the normative Metric entity; the canonical Metric is
`dea:PerformanceMetric` in [dea-metamodel](https://github.com/technehub-labs/dea-metamodel)
(CR-MET-001 binding; kind: core; profile: null).

The catalog publishes:

- **Metric records**: `entities/v1-alpha/dea:metric-<slug>/dea:metric-<slug>.yaml` + `README.md`.
- **Classification vocabularies**: `classifications/` (CR-MET-002 binding).
- **Context records**: `contexts/v1-alpha/` (Baseline / Target / Threshold / Interpretation contexts; CR-MET-006 binding).
- **Schema mirror**: `schemas/entity.schema.json` (mirror of `dea-metamodel/schemas/entities/metric.json`).

## 2. Classification model (CR-MET-002 binding)

5-axis classification:

| Axis | Cardinality | Values | Source |
|---|---|---|---|
| subject | 1..* | strategy, organization, customer, product_or_service, business_architecture, value_architecture, information_architecture, technology_architecture, governance, transformation, sustainability, capability, financial | `classifications/subject-classifications.yaml` |
| purpose | 1..* | performance, health, risk, compliance, adoption, maturity, satisfaction, efficiency, effectiveness, value_delivery | `classifications/purpose-classifications.yaml` |
| orientation | 1 | leading, lagging, diagnostic, concurrent | `classifications/orientation-classifications.yaml` |
| scope | 1..* | enterprise, business_domain, business_unit, organizational_unit, value_stream, capability, process, product_or_service, system_or_component, individual_subject | `classifications/scope-classifications.yaml` |
| management_significance | 1..* | operational, managerial, strategic, regulatory, external_disclosure, executive | `classifications/management-significance-classifications.yaml` |

A 6th axis, `directionality` (higher_is_better / lower_is_better / target_band / categorical), captures how the value is read (CR-MET-002 disposition).

## 3. Dual-anchor model (CR-MET-009 §9)

Every admitted Metric MUST carry both anchors.

### Anchor 1: measurable_entity_kind

The Metric's primary measurable-entity kind, drawn from the 16 CR-MET-007 cross-domain subject types:

```
dea:BusinessCapability, dea:BusinessProcess, dea:BusinessService, dea:Outcome,
dea:StrategicObjective, dea:ValueStream, dea:OrganizationalUnit, dea:DataEntity,
dea:Service, dea:ApplicationComponent, dea:AssessmentDimension, dea:Control,
dea:Policy, dea:Risk, dea:MaturityModel, dea:AIMLModel
```

For candidate records this anchor is informational.

### Anchor 2: reputability_tier

| Tier | Description |
|---|---|
| `industry_standard` | The Metric is recognized by an industry body (e.g., ITIL, ISO, NIST) |
| `framework_derived` | The Metric is derived from a recognized framework (e.g., Balanced Scorecard, COSO, DAMA-DMBOK) |
| `sectoral_standard` | The Metric is a recognized standard in a particular sector |
| `internal_custom` | The Metric is defined for a particular organization |
| `emerging` | The Metric is newly proposed and not yet widely adopted |

## 4. MECE coverage target

Per CR-MET-009 Gate 3 (`check_mece_coverage.py`):

- No two admitted Metrics share the same (subject, purpose, orientation, scope, directionality) signature.
- This ensures that every Metric record covers a distinct measurement concern.

The 5-Metric pilot covers:

| Metric | Subject | Purpose | Orientation | Scope | Directionality |
|---|---|---|---|---|---|
| Customer Retention Rate | customer | performance, satisfaction | lagging | business_unit, business_domain | higher_is_better |
| Mean Time to Recovery | technology_architecture | performance, health | lagging | system_or_component, service | lower_is_better |
| Operating Margin | financial | performance, value_delivery | lagging | enterprise, business_unit | higher_is_better |
| Data Completeness | information_architecture | quality, compliance | diagnostic | enterprise, business_domain | higher_is_better |
| Control Effectiveness Rate | governance | compliance, effectiveness | lagging | enterprise, process | higher_is_better |

## 5. Pilot composition

The 5-Metric pilot (CR-MET-009 Section 6) demonstrates cross-domain coverage and exercises every dimension of the metamodel:

1. **Customer Retention Rate** -- demonstrates KPI Lagging + KRI Leading designations (CR-MET-008), bounded_optimum threshold (CR-MET-006), composite_definition + formula_definition (CR-MET-005), cross-domain applicability to BusinessCapability / BusinessProcess / Outcome (CR-MET-007).
2. **Mean Time to Recovery** -- demonstrates formula_definition for arithmetic mean (CR-MET-005), lifecycle semantics (CR-MET-004), and SLI applicability.
3. **Operating Margin** -- demonstrates WEIGHTED_MEAN aggregation with weight_basis=numerator_denominator (the binding ratio-aggregation pattern; CR-MET-005 §3.3), and external_disclosure management significance.
4. **Data Completeness** -- demonstrates cross-domain applicability to DataEntity (CR-MET-007 extension), diagnostic orientation, framework_derived tier (DAMA-DMBOK).
5. **Control Effectiveness Rate** -- demonstrates KCI designation (CR-MET-008 §5.3), applicability to Control + Policy, regulatory management significance.

The remaining 7 reference Metrics from the user-supplied §6 (Strategic Objective Attainment, Employee Engagement Score, Process Cycle Time, Risk Exposure Index, Benefits Realization Rate, Energy Consumption Intensity, Capability Performance Score) land in a follow-on slice.

## 6. Cross-references

- [dea-metamodel](https://github.com/technehub-labs/dea-metamodel) -- canonical source for `dea:PerformanceMetric`, `dea:Measurement`, `dea:MeasurementObservation`, `dea:Baseline`, `dea:PerformanceTarget`, `dea:Threshold`, `dea:PerformanceInterpretation`, `dea:IndicatorDesignation`.
- [dea-architecture-framework](https://github.com/technehub-labs/dea-architecture-framework) -- reusable allocation validator.
- [dea-catalog-processes](https://github.com/technehub-labs/dea-catalog-processes) -- proven catalog layout (entity-folder per record; `<id>.yaml` + `README.md`; `CATALOG.yaml`; `schemas/`; `classifications/`; `contexts/`; `validation/`; `scripts/`; `tests/`).
- CR-MET-001 through CR-MET-008 (metamodel-side slices).
- CR-MM-04 R1 (versioning + citation conventions).
- CR-MM-04 R2 (cross-repo-consumer tests).