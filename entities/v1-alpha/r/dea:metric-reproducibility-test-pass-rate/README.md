# dea:metric-reproducibility-test-pass-rate

Candidate Performance Metric record for **Reproducibility Test Pass Rate** (RTPR-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reproducibility-test-pass-rate`
- **Name:** Reproducibility Test Pass Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RTPR-M

## 2. Definition

Within MLOps & Model Lifecycle Operations, Reproducibility Test Pass Rate (RTPR-M) is used to gauge the quality of outputs and outcomes. The formula is Experiment Runs Reproduced within Tolerance / Sampled - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether model training and inference can be deterministically reproduced from versioned code, data, and configuration. Reproducibility is the scientific floor of ML operations: without it, no result can be verified, no incident fully diagnosed, and no audit fully answered. Pass rates must test the full stack (seeds, environments, data snapshots), since partial reproducibility is theater at the moment it matters. Read with environment-versioning compliance and incident reconstruction success.

## Formula

```
RTPR-M = Experiment Runs Reproduced within Tolerance / Sampled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2522 (batch 7)
