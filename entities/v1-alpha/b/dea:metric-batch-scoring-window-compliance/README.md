# dea:metric-batch-scoring-window-compliance

Candidate Performance Metric record for **Batch Scoring Window Compliance** (BSWC-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-batch-scoring-window-compliance`
- **Name:** Batch Scoring Window Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BSWC-M

## 2. Definition

Within MLOps & Model Lifecycle Operations, Batch Scoring Window Compliance (BSWC-M) is used to gauge conformance to standards, plans, or obligations. It is defined as Scoring Batches Completed in Window / Batches; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
BSWC-M = Scoring Batches Completed in Window / Batches
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** mlops_model_lifecycle_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2532 (batch 7)
