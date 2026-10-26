# dea:metric-time-between-price-reviews

Candidate Performance Metric record for **Time between Price Reviews** (TBPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-between-price-reviews`
- **Name:** Time between Price Reviews
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TBPR

## 2. Definition

Time between Price Reviews (TBPR) measures conformance to standards, plans, or obligations in the Pricing & Revenue Management domain. Its calculation is Days since Last Documented Price Review per Segment, measured in days. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the elapsed time between formal price reviews. It matters because stale pricing silently erodes margin against moving cost and market conditions. Teams can shrink measured gaps with trivial administrative reviews. Read with Price Realization trends and Gross Margin per Unit to confirm review cadence translates into updated, effective prices.

## Formula

```
TBPR = Days since Last Documented Price Review per Segment
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1075 (batch 4)
