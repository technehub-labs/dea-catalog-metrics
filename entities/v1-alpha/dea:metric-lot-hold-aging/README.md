# dea:metric-lot-hold-aging

Candidate Performance Metric record for **Lot Hold Aging** (LHA-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-lot-hold-aging`
- **Name:** Lot Hold Aging
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LHA-S

## 2. Definition

Within Semiconductor Manufacturing (Deep Dive), Lot Hold Aging (LHA-S) is used to gauge the quality of outputs and outcomes. It is computed as Wafers on Hold over Threshold / Wafers on Hold, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Semiconductors.

## Formula

```
Wafers on Hold over Threshold / Wafers on Hold
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2382 (batch 6)
