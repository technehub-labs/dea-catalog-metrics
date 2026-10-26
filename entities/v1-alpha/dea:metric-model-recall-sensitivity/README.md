# dea:metric-model-recall-sensitivity

Candidate Performance Metric record for **Model Recall (Sensitivity)** (MREC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-recall-sensitivity`
- **Name:** Model Recall (Sensitivity)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MREC

## 2. Definition

Within Statistical Model Performance Diagnostics, Model Recall (Sensitivity) (MREC) is used to gauge the quality of outputs and outcomes. It is computed as True Positives / (True Positives + False Negatives), expressed in percent (%). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
True Positives / (True Positives + False Negatives)
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4057 (batch 9)
