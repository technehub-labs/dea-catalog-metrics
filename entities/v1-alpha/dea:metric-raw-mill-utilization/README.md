# dea:metric-raw-mill-utilization

Candidate Performance Metric record for **Raw Mill Utilization** (RMU-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-raw-mill-utilization`
- **Name:** Raw Mill Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RMU-C

## 2. Definition

Raw Mill Utilization (RMU-C) addresses the utilization or availability of capacity and is a fixture of cement & building materials reporting. It is computed as Raw Mill Operating Time / Available Time, expressed in percent (%). Its use is concentrated in Manufacturing. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Raw Mill Operating Time / Available Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cement_building_materials
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1869 (batch 6)
