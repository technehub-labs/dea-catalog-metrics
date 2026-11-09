# dea:metric-hospital-standardized-mortality-ratio

Candidate Performance Metric record for **Hospital Standardized Mortality Ratio** (HSMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hospital-standardized-mortality-ratio`
- **Name:** Hospital Standardized Mortality Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HSMR

## 2. Definition

A Healthcare Quality & Patient Safety Standard Measures indicator, Hospital Standardized Mortality Ratio (HSMR) quantifies the quality of outputs and outcomes. Its calculation is Observed Deaths / Risk-Adjusted Expected Deaths, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. It originates from and is most used in Healthcare practice.

## 3. Context

Measures observed deaths relative to the expected rate for case-mix. HSMR is the most scrutinized outcome measure in hospital quality. Risk models lag, so coding intensity shifts the ratio without care changes. Read with risk-adjusted complication rate and clinical coding accuracy.

## Formula

```
HSMR = Observed Deaths / Risk-Adjusted Expected Deaths
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4236 (batch 10)
