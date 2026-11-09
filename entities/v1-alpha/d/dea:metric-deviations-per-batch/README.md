# dea:metric-deviations-per-batch

Candidate Performance Metric record for **Deviations per Batch** (DPB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deviations-per-batch`
- **Name:** Deviations per Batch
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DPB

## 2. Definition

Within Pharmaceuticals & Life Sciences, Deviations per Batch (DPB) is used to gauge the quality of outputs and outcomes. Its calculation is Quality Deviations / Batches Produced, measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Pharmaceuticals practice.

## Formula

```
DPB = Quality Deviations / Batches Produced
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmaceuticals_life_sciences
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 481 (batch 1)
