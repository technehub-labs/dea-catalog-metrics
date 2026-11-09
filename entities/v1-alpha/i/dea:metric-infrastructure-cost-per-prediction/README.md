# dea:metric-infrastructure-cost-per-prediction

Candidate Performance Metric record for **Infrastructure Cost per Prediction** (ICPP-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-infrastructure-cost-per-prediction`
- **Name:** Infrastructure Cost per Prediction
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ICPP-M

## 2. Definition

Within MLOps & Model Lifecycle Operations, Infrastructure Cost per Prediction (ICPP-M) is used to gauge how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Serving Infrastructure Cost / Predictions; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures compute and serving cost per inference call. It is the unit-economics metric of production ML, and it is where scaling ambitions meet reality: models with luxury serving costs destroy unit economics at volume, and generative models have made this metric a board conversation. Cost per prediction must be read against latency and quality, since the three trade directly. Read with utilization efficiency of serving infrastructure and model-distillation or routing optimization results.

## Formula

```
ICPP-M = Serving Infrastructure Cost / Predictions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2535 (batch 7)
