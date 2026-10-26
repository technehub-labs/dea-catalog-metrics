# dea:metric-backlog-health-ratio

Candidate Performance Metric record for **Backlog Health Ratio** (BHR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backlog-health-ratio`
- **Name:** Backlog Health Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BHR-S

## 2. Definition

Backlog Health Ratio (BHR-S) measures how efficiently resources are converted into outputs in the Software Product Operations (Deep Dive) domain. It is computed as Active Items Completed per Sprint / Committed, expressed in percent (%). Its use is concentrated in Technology. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Active Items Completed per Sprint / Committed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** software_product_operations_deep_dive
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2167 (batch 6)
