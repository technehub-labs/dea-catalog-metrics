# dea:metric-prediction-log-retention-compliance

Candidate Performance Metric record for **Prediction Log Retention Compliance** (PLRC-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-prediction-log-retention-compliance`
- **Name:** Prediction Log Retention Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PLRC-M

## 2. Definition

Prediction Log Retention Compliance (PLRC-M) addresses conformance to standards, plans, or obligations and is a fixture of mlops & model lifecycle operations reporting. It is computed as Serving Logs Retained per Policy / Logs, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
PLRC-M = Serving Logs Retained per Policy / Logs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2526 (batch 7)
