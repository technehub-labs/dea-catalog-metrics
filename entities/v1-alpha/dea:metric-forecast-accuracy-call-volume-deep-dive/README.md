# dea:metric-forecast-accuracy-call-volume-deep-dive

Candidate Performance Metric record for **Forecast Accuracy - Call Volume (Deep Dive)** (FACV-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-forecast-accuracy-call-volume-deep-dive`
- **Name:** Forecast Accuracy - Call Volume (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FACV-D

## 2. Definition

A Contact Center Operations (Deep Dive) indicator, Forecast Accuracy - Call Volume (Deep Dive) (FACV-D) quantifies the quality of outputs and outcomes. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as 1 - Absolute Forecast Error / Actual; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
FACV-D = 1 - Absolute Forecast Error / Actual
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2480 (batch 6)
