# dea:metric-load-forecast-accuracy-grid

Candidate Performance Metric record for **Load Forecast Accuracy (Grid)** (LFA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-load-forecast-accuracy-grid`
- **Name:** Load Forecast Accuracy (Grid)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LFA

## 2. Definition

Load Forecast Accuracy (Grid) (LFA) captures the quality of outputs and outcomes for organizations tracking utilities field operations & grid. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is 1 - Absolute Forecast Error / Actual Load - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Utilities sector.

## 3. Context

Measures deviation between forecast and actual demand at system and nodal levels. Forecast accuracy drives capacity investment, procurement, and reliability: over-forecasting strands capital in unneeded plant, under-forecasting produces emergency procurement at punitive prices. Read accuracy at the granularity of decisions (peak, weather-normalized, DER-adjusted), not blended averages. Read with procurement cost variances and capacity margin trends.

## Formula

```
1 - Absolute Forecast Error / Actual Load
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
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1896 (batch 6)
