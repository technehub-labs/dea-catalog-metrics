# dea:metric-model-precision-positive-predictive-value

Candidate Performance Metric record for **Model Precision (Positive Predictive Value)** (MPPPV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-precision-positive-predictive-value`
- **Name:** Model Precision (Positive Predictive Value)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MPPPV

## 2. Definition

Model Precision (Positive Predictive Value) (MPPPV) addresses the quality of outputs and outcomes and is a fixture of statistical model performance diagnostics reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is True Positives / (True Positives + False Positives), measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Software practice.

## Formula

```
True Positives / (True Positives + False Positives)
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4056 (batch 9)
