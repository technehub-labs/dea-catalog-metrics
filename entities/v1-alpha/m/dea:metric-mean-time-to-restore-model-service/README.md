# dea:metric-mean-time-to-restore-model-service

Candidate Performance Metric record for **Mean Time to Restore Model Service** (MTRS-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-restore-model-service`
- **Name:** Mean Time to Restore Model Service
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MTRS-M

## 2. Definition

Within MLOps & Model Lifecycle Operations, Mean Time to Restore Model Service (MTRS-M) is used to gauge how efficiently resources are converted into outputs. The formula is Hours from Model Failure to Restored Service - reported in hours. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
MTRS-M = Hours from Model Failure to Restored Service
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2531 (batch 7)
