# dea:metric-occupancy-rate

Candidate Performance Metric record for **Occupancy Rate** (OCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-occupancy-rate`
- **Name:** Occupancy Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OCC

## 2. Definition

Occupancy Rate (OCC) measures the utilization or availability of capacity in the Hospitality & Food Service domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Rooms Occupied / Rooms Available - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Hospitality sector.

## 3. Context

The share of available units or capacity sold - the revenue-side twin of vacancy, and the first number in every hospitality and multi-let real estate conversation because it sets the denominator for everything else. Its strategic significance is the yield-management context: occupancy is never maximized in isolation, since a full house achieved at distressed rates can carry less revenue than a leaner house at healthy ones - which is why the metric is always read with average daily rate, and their product is the number that actually matters. Read the demand mix: occupancy built on one dominant segment (a single corporate account, one tour operator) is concentration risk in hospitality clothes, and the segment-split occupancy is the honest view. Structural occupancy also prices flexibility: the extra points from 85 to 95 percent cost more in rate erosion than they earn in room revenue.

## Formula

```
Rooms Occupied / Rooms Available
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** hospitality_food_service
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 504 (batch 1)
