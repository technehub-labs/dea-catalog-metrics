# dea:metric-recipe-yield-variance

Candidate Performance Metric record for **Recipe Yield Variance** (RYV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-recipe-yield-variance`
- **Name:** Recipe Yield Variance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RYV

## 2. Definition

Recipe Yield Variance (RYV) addresses how efficiently resources are converted into outputs and is a fixture of food & beverage manufacturing reporting. It is computed as Actual Yield - Standard Yield / Standard Yield, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Food & Beverage.

## Formula

```
RYV = Actual Yield - Standard Yield / Standard Yield
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** food_beverage_manufacturing
- **Sector:** food_beverage

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1797 (batch 6)
