# dea:metric-internal-fraud-detection-share

Candidate Performance Metric record for **Internal Fraud Detection Share** (IFDS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-internal-fraud-detection-share`
- **Name:** Internal Fraud Detection Share
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IFDS

## 2. Definition

A Enterprise Fraud & Financial Crime Management indicator, Internal Fraud Detection Share (IFDS) quantifies exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Frauds Detected via Internal Controls / All Detected Frauds, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how much detected fraud originates internally (employees, collusion). Internal fraud is a governance and culture signal as much as a financial one. Detection dominated by tip lines rather than analytics shows where capability sits. Read with control override detection rate and fraud model coverage.

## Formula

```
IFDS = Frauds Detected via Internal Controls / All Detected Frauds
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3762 (batch 8)
