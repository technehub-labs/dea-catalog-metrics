# dea:metric-demand-volatility-index

Candidate Performance Metric record for **Demand Volatility Index** (DVI-MKT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-demand-volatility-index`
- **Name:** Demand Volatility Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DVI-MKT

## 2. Definition

Demand Volatility Index (DVI-MKT) addresses exposure to adverse outcomes and is a fixture of market structure & economics standard measures reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Coefficient of Variation of Market Demand; the result is stated in index (0-100 or normalized). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the variability of demand over time. Volatility drives everything downstream: safety stock, capacity buffers, workforce flexibility. Index smoothing over long windows hides the spikes that break operations. Read with demand forecast accuracy and capacity-to-demand match index.

## Formula

```
DVI-MKT = Coefficient of Variation of Market Demand
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** risk
- **Scope classification:** business_domain
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** market_structure_economics_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4151 (batch 9)
