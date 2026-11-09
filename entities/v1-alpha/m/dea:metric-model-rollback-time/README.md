# dea:metric-model-rollback-time

Candidate Performance Metric record for **Model Rollback Time** (MRBT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-rollback-time`
- **Name:** Model Rollback Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MRBT

## 2. Definition

Model Rollback Time (MRBT) captures how efficiently resources are converted into outputs for organizations tracking mlops & model lifecycle operations. It is computed as Minutes to Roll Back to Prior Model Version, expressed in minutes. It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
MRBT = Minutes to Roll Back to Prior Model Version
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2521 (batch 7)
