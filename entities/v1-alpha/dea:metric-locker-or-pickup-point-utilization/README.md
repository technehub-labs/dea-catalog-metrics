# dea:metric-locker-or-pickup-point-utilization

Candidate Performance Metric record for **Locker or Pickup Point Utilization** (LPPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-locker-or-pickup-point-utilization`
- **Name:** Locker or Pickup Point Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LPPU

## 2. Definition

Locker or Pickup Point Utilization (LPPU) measures the utilization or availability of capacity in the Parcel & Last-Mile Logistics (Deep Dive) domain. The formula is Locker Transactions / Locker Capacity - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Logistics & Trade sector.

## Formula

```
Locker Transactions / Locker Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2344 (batch 6)
