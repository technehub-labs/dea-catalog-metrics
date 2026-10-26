# dea:metric-table-turnover-rate-deep-dive

Candidate Performance Metric record for **Table Turnover Rate (Deep Dive)** (TTR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-table-turnover-rate-deep-dive`
- **Name:** Table Turnover Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TTR-D

## 2. Definition

Within Restaurant Operations (Deep Dive), Table Turnover Rate (Deep Dive) (TTR-D) is used to gauge the utilization or availability of capacity. It is computed as Party Turns per Table per Service, expressed in times per period. Its use is concentrated in Restaurants. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Party Turns per Table per Service
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurant_operations_deep_dive
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2345 (batch 6)
