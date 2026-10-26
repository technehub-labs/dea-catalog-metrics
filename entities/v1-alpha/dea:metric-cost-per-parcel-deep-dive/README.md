# dea:metric-cost-per-parcel-deep-dive

Candidate Performance Metric record for **Cost per Parcel (Deep Dive)** (CPP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-parcel-deep-dive`
- **Name:** Cost per Parcel (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPP-D

## 2. Definition

Cost per Parcel (Deep Dive) (CPP-D) captures how efficiently resources are converted into outputs for organizations tracking parcel & last-mile logistics (deep dive). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Delivery Cost / Parcels Delivered; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. In Logistics & Trade, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures fully loaded delivery cost per parcel. It is the unit-economics metric of parcel networks, and density is destiny in this business: cost per parcel falls with drop density and rises with route length, so network design and volume mix can move the number more than any operational program. Compare only within comparable service tiers and geographies. Read with driver retention rate (Deep Dive) and first attempt delivery rate (Deep Dive).

## Formula

```
Delivery Cost / Parcels Delivered
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** parcel_last_mile_logistics_deep_dive
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2336 (batch 6)
