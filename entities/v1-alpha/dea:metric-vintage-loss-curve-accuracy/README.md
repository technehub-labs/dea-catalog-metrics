# dea:metric-vintage-loss-curve-accuracy

Candidate Performance Metric record for **Vintage Loss Curve Accuracy** (VLCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vintage-loss-curve-accuracy`
- **Name:** Vintage Loss Curve Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** VLCA

## 2. Definition

Vintage Loss Curve Accuracy (VLCA) measures the quality of outputs and outcomes in the Banking Retail Lending (Deep Dive) domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Actual Vintage Losses vs Forecast / Forecast, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Banking practice.

## 3. Context

Measures how realized losses on origination cohorts track the loss curves assumed in pricing and provisioning. The accuracy of vintage curves is the actuarial backbone of consumer credit: pricing, capital, and provisioning all inherit its errors, and systematic under-prediction in early buckets is the classic warning sign. Track by product and channel, since curves diverge by originator behavior. Read with early payment default - 3 Month and reserve development patterns.

## Formula

```
VLCA = Actual Vintage Losses vs Forecast / Forecast
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** banking_retail_lending_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2077 (batch 6)
