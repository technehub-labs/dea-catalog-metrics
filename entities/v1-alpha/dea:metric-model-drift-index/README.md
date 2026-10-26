# dea:metric-model-drift-index

Candidate Performance Metric record for **Model Drift Index** (MDI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-drift-index`
- **Name:** Model Drift Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MDI

## 2. Definition

Model Drift Index (MDI) addresses exposure to adverse outcomes and is a fixture of data management & analytics reporting. It is defined as Change in Feature or Prediction Distribution vs Training Baseline; the result is stated in index (0-100 or normalized). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the degree to which a production model's inputs or performance have shifted from training conditions. It matters because silent drift turns a good model into a confident wrong one. Teams can hide drift by retraining frequently enough to reset the metric while root data problems persist. Read with Model Prediction Accuracy trends and Data Completeness to distinguish genuine drift from data pipeline decay.

## Formula

```
Change in Feature or Prediction Distribution vs Training Baseline
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 346 (batch 1)
