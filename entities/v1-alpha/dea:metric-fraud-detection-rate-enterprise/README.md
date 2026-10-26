# dea:metric-fraud-detection-rate-enterprise

Candidate Performance Metric record for **Fraud Detection Rate (Enterprise)** (FDER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fraud-detection-rate-enterprise`
- **Name:** Fraud Detection Rate (Enterprise)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FDER

## 2. Definition

A Enterprise Fraud & Financial Crime Management indicator, Fraud Detection Rate (Enterprise) (FDER) quantifies exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Fraud Detected before Loss Fully Incurred / Confirmed Fraud, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of fraud (by value or volume) detected before loss or by control rather than by external report. Self-detection is the difference between managing fraud and discovering it. Rates computed against detected-only populations are circular. Read with fraud loss ratio and internal fraud detection share.

## Formula

```
Fraud Detected before Loss Fully Incurred / Confirmed Fraud
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** enterprise_fraud_financial_crime_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3756 (batch 8)
