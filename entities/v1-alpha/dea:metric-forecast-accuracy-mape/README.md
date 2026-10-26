# dea:metric-forecast-accuracy-mape

Candidate Performance Metric record for **Forecast Accuracy (MAPE)** (FA2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-forecast-accuracy-mape`
- **Name:** Forecast Accuracy (MAPE)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FA2

## 2. Definition

Within Supply Chain, Forecast Accuracy (MAPE) (FA2) is used to gauge the quality of outputs and outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Mean ABS(Actual - Forecast) / Actual, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures average absolute forecast error as a percentage of actuals. It matters because every planning decision inherits forecast error as cost. MAPE rewards under-forecasting volatile items and punishes exact forecasts on tiny volumes, so it can be optimized by hedging. Read with Forecast Bias and Mean Absolute Deviation to ensure high accuracy is not just conservative forecasting of easy items.

## Formula

```
Mean ABS(Actual - Forecast) / Actual
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 185 (batch 1)
