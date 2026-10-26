# dea:metric-model-detection-rate-aml

Candidate Performance Metric record for **Model Detection Rate - AML** (MDRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-detection-rate-aml`
- **Name:** Model Detection Rate - AML
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MDRA

## 2. Definition

Model Detection Rate - AML (MDRA) captures capability maturity or development for organizations tracking insurance fraud & financial crime. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Suspicious Activity Confirmed / Model Flagged - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Financial Services sector.

## 3. Context

Measures the share of genuinely suspicious activity the AML transaction-monitoring system surfaces. Detection rate is the recall metric of AML: missed suspicious activity is both regulatory exposure and undetected crime, and it trades against alert volume (false positives), which overwhelms investigation capacity. Ground-truth measurement is genuinely hard, so benchmarking through red-team synthetic scenarios hardens the estimate. Read with SAR filing quality and alert-to-investigation conversion rates.

## Formula

```
MDRA = Suspicious Activity Confirmed / Model Flagged
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_fraud_financial_crime
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2471 (batch 6)
