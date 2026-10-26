# dea:metric-route-efficiency-index

Candidate Performance Metric record for **Route Efficiency Index** (REI-F) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-route-efficiency-index`
- **Name:** Route Efficiency Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** REI-F

## 2. Definition

Route Efficiency Index (REI-F) captures how efficiently resources are converted into outputs for organizations tracking field service & asset performance. It is computed as Effective Travel Time / Total Travel Time, expressed in index (0-100 or normalized). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Effective Travel Time / Total Travel Time
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3391 (batch 7)
