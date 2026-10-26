# dea:metric-planned-maintenance-window-compliance

Candidate Performance Metric record for **Planned Maintenance Window Compliance** (PMWC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-planned-maintenance-window-compliance`
- **Name:** Planned Maintenance Window Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PMWC

## 2. Definition

A Telecom Network Operations (Deep Dive) indicator, Planned Maintenance Window Compliance (PMWC) quantifies conformance to standards, plans, or obligations. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Maintenance Completed in Window / Scheduled, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Telecommunications.

## Formula

```
Maintenance Completed in Window / Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2132 (batch 6)
