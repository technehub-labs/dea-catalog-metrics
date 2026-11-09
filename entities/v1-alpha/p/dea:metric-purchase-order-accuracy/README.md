# dea:metric-purchase-order-accuracy

Candidate Performance Metric record for **Purchase Order Accuracy** (POA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-purchase-order-accuracy`
- **Name:** Purchase Order Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** POA

## 2. Definition

Purchase Order Accuracy (POA) measures the quality of outputs and outcomes in the Procurement domain. It is computed as Error-Free Purchase Orders / Purchase Orders Issued, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
POA = Error-Free Purchase Orders / Purchase Orders Issued
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 223 (batch 1)
