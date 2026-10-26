# dea:metric-model-deployment-frequency

Candidate Performance Metric record for **Model Deployment Frequency** (MDF-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-deployment-frequency`
- **Name:** Model Deployment Frequency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MDF-M

## 2. Definition

Within MLOps & Model Lifecycle Operations, Model Deployment Frequency (MDF-M) is used to gauge how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Production Model Deployments per Period; the result is stated in times per period. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how often model changes reach production. In modern ML operations, deployment frequency is the metabolic indicator: models decay, and frequent, low-risk updates beat rare, risky re-releases. Frequency without quality gates is chaos, so read alongside deployment success and rollback rates. Read with model lead time - experiment to production (Deep Dive) and validation currency under the faster cadence.

## Formula

```
Production Model Deployments per Period
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2512 (batch 7)
