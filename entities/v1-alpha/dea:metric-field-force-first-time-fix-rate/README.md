# dea:metric-field-force-first-time-fix-rate

Candidate Performance Metric record for **Field Force First-Time Fix Rate** (FTFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-field-force-first-time-fix-rate`
- **Name:** Field Force First-Time Fix Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FTFR

## 2. Definition

Field Force First-Time Fix Rate (FTFR) addresses how efficiently resources are converted into outputs and is a fixture of telecom network operations reporting. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Faults Resolved on First Visit / Faults Dispatched, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Telecommunications.

## Formula

```
Faults Resolved on First Visit / Faults Dispatched
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 869 (batch 3)
