# dea:metric-model-lead-time-experiment-to-production

Candidate Performance Metric record for **Model Lead Time - Experiment to Production** (MLTEP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-lead-time-experiment-to-production`
- **Name:** Model Lead Time - Experiment to Production
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MLTEP

## 2. Definition

Model Lead Time - Experiment to Production (MLTEP) measures how efficiently resources are converted into outputs in the MLOps & Model Lifecycle Operations domain. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Days from Candidate Model to Production Deployment; the result is stated in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures elapsed time from experiment approval to production deployment. It is the responsiveness metric of the ML pipeline: in competitive model-driven products, the lead time determines whether a discovered insight still has market value by the time it ships. Lead time compression from skipped validation steps is speed purchased with risk. Read with deployment frequency (Deep Dive) and stage-by-stage bottleneck decomposition.

## Formula

```
Days from Candidate Model to Production Deployment
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2513 (batch 7)
