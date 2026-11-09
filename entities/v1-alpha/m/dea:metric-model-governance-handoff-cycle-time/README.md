# dea:metric-model-governance-handoff-cycle-time

Candidate Performance Metric record for **Model Governance Handoff Cycle Time** (MGHCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-model-governance-handoff-cycle-time`
- **Name:** Model Governance Handoff Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MGHCT

## 2. Definition

Within MLOps & Model Lifecycle Operations, Model Governance Handoff Cycle Time (MGHCT) is used to gauge how efficiently resources are converted into outputs. It is computed as Days from Model Sign-off to Deployment Readiness, expressed in days. It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
MGHCT = Days from Model Sign-off to Deployment Readiness
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2536 (batch 7)
