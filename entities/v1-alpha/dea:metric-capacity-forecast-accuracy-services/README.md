# dea:metric-capacity-forecast-accuracy-services

Candidate Performance Metric record for **Capacity Forecast Accuracy - Services** (CFAS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-forecast-accuracy-services`
- **Name:** Capacity Forecast Accuracy - Services
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CFAS

## 2. Definition

Capacity Forecast Accuracy - Services (CFAS) addresses the quality of outputs and outcomes and is a fixture of observability & site reliability engineering reporting. Its calculation is 1 - Absolute Forecast Error / Actual, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how closely demand forecasts predict actual service resource consumption. Accurate forecasts prevent both provisioned waste and saturation outages. Forecasts that err systematically low get corrected by incidents, which is the expensive way. Read with capacity utilization trends and SLO attainment.

## Formula

```
1 - Absolute Forecast Error / Actual
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2879 (batch 7)
