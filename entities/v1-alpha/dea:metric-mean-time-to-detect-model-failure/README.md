# dea:metric-mean-time-to-detect-model-failure

Candidate Performance Metric record for **Mean Time to Detect Model Failure** (MTTD-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-detect-model-failure`
- **Name:** Mean Time to Detect Model Failure
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTTD-M

## 2. Definition

Mean Time to Detect Model Failure (MTTD-M) measures the quality of outputs and outcomes in the MLOps & Model Lifecycle Operations domain. The formula is Hours from Model Failure to Detection - reported in hours. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Hours from Model Failure to Detection
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2530 (batch 7)
