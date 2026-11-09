# dea:metric-forecast-accuracy-mape-deep-dive

Candidate Performance Metric record for **Forecast Accuracy MAPE (Deep Dive)** (MAPEDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-forecast-accuracy-mape-deep-dive`
- **Name:** Forecast Accuracy MAPE (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MAPEDD

## 2. Definition

Forecast Accuracy MAPE (Deep Dive) (MAPEDD) measures the quality of outputs and outcomes in the Supply Chain Standard Measures (Deep Dive) domain. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Mean Absolute Percent Error of Demand Forecast; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
MAPEDD = Mean Absolute Percent Error of Demand Forecast
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4259 (batch 10)
