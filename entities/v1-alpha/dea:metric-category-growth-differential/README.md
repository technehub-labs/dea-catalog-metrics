# dea:metric-category-growth-differential

Candidate Performance Metric record for **Category Growth Differential** (CGD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-category-growth-differential`
- **Name:** Category Growth Differential
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CGD

## 2. Definition

Category Growth Differential (CGD) addresses growth over time and is a fixture of market structure & economics standard measures reporting. It is computed as Entity Category Growth minus Market Growth, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures whether the company grows faster or slower than its category. The differential is growth stripped of market beta: it isolates company performance. Category data quality determines whether the differential is real. Read with market growth capture ratio and compound annual growth rate (Deep Dive).

## Formula

```
CGD = Entity Category Growth minus Market Growth
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4145 (batch 9)
