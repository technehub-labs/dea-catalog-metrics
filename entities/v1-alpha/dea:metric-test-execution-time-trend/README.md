# dea:metric-test-execution-time-trend

Candidate Performance Metric record for **Test Execution Time Trend** (TETT-CI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-test-execution-time-trend`
- **Name:** Test Execution Time Trend
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TETT-CI

## 2. Definition

Test Execution Time Trend (TETT-CI) measures how efficiently resources are converted into outputs in the Continuous Integration domain. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Change in Median Test Suite Duration per Quarter; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Change in Median Test Suite Duration per Quarter
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2680 (batch 7)
