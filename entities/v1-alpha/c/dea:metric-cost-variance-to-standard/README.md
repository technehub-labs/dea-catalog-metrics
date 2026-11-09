# dea:metric-cost-variance-to-standard

Candidate Performance Metric record for **Cost Variance to Standard** (CVS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-variance-to-standard`
- **Name:** Cost Variance to Standard
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CVS

## 2. Definition

Cost Variance to Standard (CVS) measures conformance to standards, plans, or obligations in the Product Costing & Margin Management domain. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as (Actual Cost - Standard Cost) / Standard Cost, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures deviation of actual product cost from established standard cost. It matters because standards are the control baseline for margin visibility. Repeated standard re-setting absorbs variances instead of fixing them. Read with Purchase Price Variance and Scrap Cost trends to confirm variance control reflects process improvement.

## Formula

```
CVS = (Actual Cost - Standard Cost) / Standard Cost
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_costing_margin_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1240 (batch 4)
