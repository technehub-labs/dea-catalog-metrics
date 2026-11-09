# dea:metric-container-crane-utilization-deep-dive

Candidate Performance Metric record for **Container Crane Utilization (Deep Dive)** (CCU-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-container-crane-utilization-deep-dive`
- **Name:** Container Crane Utilization (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CCU-D

## 2. Definition

Container Crane Utilization (Deep Dive) (CCU-D) addresses the utilization or availability of capacity and is a fixture of maritime shipping (deep dive) reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Crane Working Time / Available Time, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Maritime practice.

## Formula

```
CCU-D = Crane Working Time / Available Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2433 (batch 6)
