# dea:metric-food-cost-percentage-deep-dive

Candidate Performance Metric record for **Food Cost Percentage (Deep Dive)** (FCP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-food-cost-percentage-deep-dive`
- **Name:** Food Cost Percentage (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FCP-D

## 2. Definition

Within Restaurant Operations (Deep Dive), Food Cost Percentage (Deep Dive) (FCP-D) is used to gauge how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Food Cost / Food Sales; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. In Restaurants, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures food and beverage cost against food revenue. It is the largest controllable margin lever in restaurants, and its integrity depends on consistent recipe costing, yield testing, and inventory discipline - a drifting food cost percentage is usually waste, theft, or portion drift, not price movement. Percentage alone misleads, since menu price rises can mask waste growth. Read with variance between theoretical and actual food cost and waste tracking.

## Formula

```
Food Cost / Food Sales
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurant_operations_deep_dive
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2347 (batch 6)
