# dea:metric-data-drift-detection-coverage

Candidate Performance Metric record for **Data Drift Detection Coverage** (DDDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-drift-detection-coverage`
- **Name:** Data Drift Detection Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DDDC

## 2. Definition

Data Drift Detection Coverage (DDDC) measures exposure to adverse outcomes in the MLOps & Model Lifecycle Operations domain. It is defined as Monitored Features with Drift Checks / Features; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of production models with automated input-data drift monitoring. Drift is the silent killer of model quality: populations, behaviors, and upstream systems change, and models degrade without failing loudly - coverage determines whether degradation is detected before decisions suffer. Monitoring must extend to feature-level drift, not just aggregate inputs, since drift concentrates in specific signals. Read with model performance monitoring cadence and retraining triggers.

## Formula

```
DDDC = Monitored Features with Drift Checks / Features
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2525 (batch 7)
