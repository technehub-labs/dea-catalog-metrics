# dea:metric-fibre-loss-rate

Candidate Performance Metric record for **Fibre Loss Rate** (FLR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fibre-loss-rate`
- **Name:** Fibre Loss Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FLR

## 2. Definition

Fibre Loss Rate (FLR) addresses how efficiently resources are converted into outputs and is a fixture of pulp, paper & forest products reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Fibre Lost to Effluent / Fibre Input - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Manufacturing sector.

## Formula

```
FLR = Fibre Lost to Effluent / Fibre Input
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pulp_paper_forest_products
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1856 (batch 6)
