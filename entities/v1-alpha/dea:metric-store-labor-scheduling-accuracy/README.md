# dea:metric-store-labor-scheduling-accuracy

Candidate Performance Metric record for **Store Labor Scheduling Accuracy** (SLSA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-store-labor-scheduling-accuracy`
- **Name:** Store Labor Scheduling Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SLSA

## 2. Definition

Within Retail Standard Measures, Store Labor Scheduling Accuracy (SLSA) is used to gauge how efficiently resources are converted into outputs. It is computed as Scheduled Hours Matching Traffic Model / Scheduled, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Retail & E-commerce.

## Formula

```
SLSA = Scheduled Hours Matching Traffic Model / Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** retail_standard_measures
- **Sector:** retail_e_commerce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4314 (batch 10)
