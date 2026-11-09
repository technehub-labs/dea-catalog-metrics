# dea:metric-hub-sortation-rate-per-hour

Candidate Performance Metric record for **Hub Sortation Rate per Hour** (HSRH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hub-sortation-rate-per-hour`
- **Name:** Hub Sortation Rate per Hour
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HSRH

## 2. Definition

Within Parcel & Last-Mile Logistics (Deep Dive), Hub Sortation Rate per Hour (HSRH) is used to gauge how efficiently resources are converted into outputs. The formula is Parcels Sorted / Sorter Hour - reported in count (items per period). It is a standard measure in the Logistics & Trade sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
HSRH = Parcels Sorted / Sorter Hour
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** parcel_last_mile_logistics_deep_dive
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2334 (batch 6)
