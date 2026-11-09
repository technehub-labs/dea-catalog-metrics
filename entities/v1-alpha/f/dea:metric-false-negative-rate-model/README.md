# dea:metric-false-negative-rate-model

Candidate Performance Metric record for **False Negative Rate (Model)** (FNRM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-false-negative-rate-model`
- **Name:** False Negative Rate (Model)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FNRM

## 2. Definition

A Statistical Model Performance Diagnostics indicator, False Negative Rate (Model) (FNRM) quantifies exposure to adverse outcomes. It is computed as False Negatives / Actual Positives, expressed in percent (%). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
FNRM = False Negatives / Actual Positives
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4062 (batch 9)
