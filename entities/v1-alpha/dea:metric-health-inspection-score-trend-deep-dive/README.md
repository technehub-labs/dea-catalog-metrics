# dea:metric-health-inspection-score-trend-deep-dive

Candidate Performance Metric record for **Health Inspection Score Trend (Deep Dive)** (HIST-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-health-inspection-score-trend-deep-dive`
- **Name:** Health Inspection Score Trend (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HIST-D

## 2. Definition

Health Inspection Score Trend (Deep Dive) (HIST-D) addresses conformance to standards, plans, or obligations and is a fixture of restaurant operations (deep dive) reporting. It is defined as Change in Inspection Score over Time; the result is stated in score (points). In Restaurants, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the trajectory of regulatory hygiene inspection results. Trend matters more than any single score: inspections are snapshots, and deteriorating trajectories predict the critical violations that close restaurants and end brands. Internal audit scores should track regulator scores - divergence indicates either theater or an unlucky inspector, and neither is safe. Read with internal audit findings and staff food-safety training currency.

## Formula

```
HIST-D = Change in Inspection Score over Time
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurant_operations_deep_dive
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2352 (batch 6)
