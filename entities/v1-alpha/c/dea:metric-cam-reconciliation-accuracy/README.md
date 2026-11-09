# dea:metric-cam-reconciliation-accuracy

Candidate Performance Metric record for **CAM Reconciliation Accuracy** (CAMRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cam-reconciliation-accuracy`
- **Name:** CAM Reconciliation Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CAMRA

## 2. Definition

CAM Reconciliation Accuracy (CAMRA) captures the quality of outputs and outcomes for organizations tracking real estate portfolio & property management. Its calculation is Reconciliations without Adjustment / Reconciliations, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Real Estate practice.

## Formula

```
CAMRA = Reconciliations without Adjustment / Reconciliations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** real_estate_portfolio_property_management
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1755 (batch 6)
