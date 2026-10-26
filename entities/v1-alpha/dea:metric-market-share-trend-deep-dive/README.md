# dea:metric-market-share-trend-deep-dive

Candidate Performance Metric record for **Market Share Trend (Deep Dive)** (MST-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-market-share-trend-deep-dive`
- **Name:** Market Share Trend (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MST-D

## 2. Definition

Market Share Trend (Deep Dive) (MST-D) captures growth over time for organizations tracking balanced scorecard - customer perspective. Its calculation is Change in Market Share between Periods, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the direction of the company's share of the addressable market. Trend matters more than level: a shrinking share in a growing market is strategic erosion. Market definitions that redefine the denominator upward flatter the number. Read with revenue growth rate and brand preference score.

## Formula

```
MST-D = Change in Market Share between Periods
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** growth
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_customer_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3080 (batch 7)
