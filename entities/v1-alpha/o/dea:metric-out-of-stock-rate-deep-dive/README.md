# dea:metric-out-of-stock-rate-deep-dive

Candidate Performance Metric record for **Out-of-Stock Rate (Deep Dive)** (OOSDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-out-of-stock-rate-deep-dive`
- **Name:** Out-of-Stock Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OOSDD

## 2. Definition

Out-of-Stock Rate (Deep Dive) (OOSDD) captures the quality of outputs and outcomes for organizations tracking retail standard measures. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as SKU-Location Days Out of Stock / SKU-Location Days, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Retail & E-commerce.

## Formula

```
OOSDD = SKU-Location Days Out of Stock / SKU-Location Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** retail_standard_measures
- **Sector:** retail_e_commerce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4304 (batch 10)
