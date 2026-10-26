# dea:metric-market-growth-capture-ratio

Candidate Performance Metric record for **Market Growth Capture Ratio** (MGCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-market-growth-capture-ratio`
- **Name:** Market Growth Capture Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MGCR

## 2. Definition

Market Growth Capture Ratio (MGCR) measures growth over time in the Market Structure & Economics Standard Measures domain. It is defined as Entity Growth Rate / Market Growth Rate; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how much of the market's growth the company captured. Capture below 100% in a growing market means competitors are taking the future. Capture computed against a redefined market is unfalsifiable. Read with market share trend (Deep Dive) and relative market share.

## Formula

```
MGCR = Entity Growth Rate / Market Growth Rate
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** growth
- **Scope classification:** business_domain
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** market_structure_economics_standard_measures

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4139 (batch 9)
