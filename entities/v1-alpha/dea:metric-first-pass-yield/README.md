# dea:metric-first-pass-yield

Candidate Performance Metric record for **First Pass Yield** (FPY) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-pass-yield`
- **Name:** First Pass Yield
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FPY

## 2. Definition

First Pass Yield (FPY) captures the quality of outputs and outcomes for organizations tracking operations. It is computed as Units Passing All Processes Without Rework / Units Started, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
FPY = Units Passing All Processes Without Rework / Units Started
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 162 (batch 1)
