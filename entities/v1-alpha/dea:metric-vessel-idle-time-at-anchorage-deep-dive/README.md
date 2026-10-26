# dea:metric-vessel-idle-time-at-anchorage-deep-dive

Candidate Performance Metric record for **Vessel Idle Time at Anchorage (Deep Dive)** (VIT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vessel-idle-time-at-anchorage-deep-dive`
- **Name:** Vessel Idle Time at Anchorage (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VIT-D

## 2. Definition

Within Maritime Shipping (Deep Dive), Vessel Idle Time at Anchorage (Deep Dive) (VIT-D) is used to gauge the utilization or availability of capacity. The formula is Waiting Days / Total Vessel Days - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Maritime sector.

## 3. Context

Measures time ships spend waiting for berth. Anchorage time is the visible symptom of port-system saturation - it burns fuel, strains crews, and delays cargo that planned on schedule, and it is the metric that signals capacity intervention before berth queues become news. Idle time concentrated on specific services indicates terminal allocation problems rather than demand. Read with berth productivity trends and forward-booking visibility.

## Formula

```
Waiting Days / Total Vessel Days
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2432 (batch 6)
