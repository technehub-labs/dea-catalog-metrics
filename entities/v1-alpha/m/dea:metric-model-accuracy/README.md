# dea:metric-model-accuracy

Candidate Performance Metric record for **Model Accuracy** (MACC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-accuracy`
- **Name:** Model Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MACC

## 2. Definition

Within Statistical Model Performance Diagnostics, Model Accuracy (MACC) is used to gauge the quality of outputs and outcomes. It is a working-level control: thresholds trigger immediate operational response. It is defined as Correct Predictions / Total Predictions; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
MACC = Correct Predictions / Total Predictions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** statistical_model_performance_diagnostics
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4055 (batch 9)
