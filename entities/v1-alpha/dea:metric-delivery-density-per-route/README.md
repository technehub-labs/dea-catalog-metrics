# dea:metric-delivery-density-per-route

Candidate Performance Metric record for **Delivery Density per Route** (DDPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-delivery-density-per-route`
- **Name:** Delivery Density per Route
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DDPR

## 2. Definition

Within Parcel & Last-Mile Logistics (Deep Dive), Delivery Density per Route (DDPR) is used to gauge the utilization or availability of capacity. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Stops / Route, expressed in count (items per period). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Logistics & Trade.

## Formula

```
Stops / Route
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** parcel_last_mile_logistics_deep_dive
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2337 (batch 6)
