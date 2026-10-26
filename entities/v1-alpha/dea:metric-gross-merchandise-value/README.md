# dea:metric-gross-merchandise-value

Candidate Performance Metric record for **Gross Merchandise Value** (GMV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-merchandise-value`
- **Name:** Gross Merchandise Value
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GMV

## 2. Definition

Gross Merchandise Value (GMV) captures growth over time for organizations tracking retail & e-commerce. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Total Value of Goods Transacted via Platform; the result is stated in currency value. Improvement means raising this figure toward best-in-class levels. In Retail, it is a recognized element of the standard performance toolkit.

## 3. Context

The total value of goods transacted on a platform before any take-rate deductions - the volume metric of marketplaces, where the platform's revenue is a fraction of the commerce that flows through it, making GMV the raw flow and revenue the skim. Its strategic significance is the ecosystem-size argument: network effects price to GMV, not revenue, since more goods attracts more buyers which attracts more sellers - which is why marketplace strategies have historically subsidized GMV growth well past the point of revenue sense. The honest analysis separates first-party from third-party GMV (the economics differ fundamentally), watches return rates netted or not, and treats GMV inflated by low-quality or subsidized transactions as growth in the metric without growth in the business. Read with take-rate trend, since GMV times take rate is the revenue identity the whole model rests on.

## Formula

```
Total Value of Goods Transacted via Platform
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 497 (batch 1)
