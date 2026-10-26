# dea:metric-payment-fraud-block-rate

Candidate Performance Metric record for **Payment Fraud Block Rate** (PFBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payment-fraud-block-rate`
- **Name:** Payment Fraud Block Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PFBR

## 2. Definition

Payment Fraud Block Rate (PFBR) addresses exposure to adverse outcomes and is a fixture of enterprise fraud & financial crime management reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Fraudulent Payment Attempts Blocked / Attempts Detected, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Fraudulent Payment Attempts Blocked / Attempts Detected
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** enterprise_fraud_financial_crime_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3766 (batch 8)
