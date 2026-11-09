# dea:metric-model-serving-availability

Candidate Performance Metric record for **Model Serving Availability** (MSAV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-serving-availability`
- **Name:** Model Serving Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MSAV

## 2. Definition

Model Serving Availability (MSAV) measures the utilization or availability of capacity in the MLOps & Model Lifecycle Operations domain. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Serving Endpoint Uptime / Required Time, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
MSAV = Serving Endpoint Uptime / Required Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2519 (batch 7)
