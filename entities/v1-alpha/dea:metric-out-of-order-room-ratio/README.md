# dea:metric-out-of-order-room-ratio

Candidate Performance Metric record for **Out-of-Order Room Ratio** (OORR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-out-of-order-room-ratio`
- **Name:** Out-of-Order Room Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OORR

## 2. Definition

Out-of-Order Room Ratio (OORR) addresses the utilization or availability of capacity and is a fixture of hotel & resort operations (deep dive) reporting. The formula is Rooms out of Order / Total Rooms - reported in percent (%). It is a standard measure in the Hospitality sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Rooms out of Order / Total Rooms
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** hotel_resort_operations_deep_dive
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1916 (batch 6)
