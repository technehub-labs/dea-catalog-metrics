# dea:metric-false-positive-rate-model

Candidate Performance Metric record for **False Positive Rate (Model)** (FPRM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-false-positive-rate-model`
- **Name:** False Positive Rate (Model)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FPRM

## 2. Definition

A Statistical Model Performance Diagnostics indicator, False Positive Rate (Model) (FPRM) quantifies exposure to adverse outcomes. It is computed as False Positives / Actual Negatives, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
FPRM = False Positives / Actual Negatives
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4061 (batch 9)
