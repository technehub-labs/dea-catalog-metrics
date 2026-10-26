# dea:metric-equipment-availability-mining

Candidate Performance Metric record for **Equipment Availability (Mining)** (EA-M) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-equipment-availability-mining`
- **Name:** Equipment Availability (Mining)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EA-M

## 2. Definition

Within Mining & Metals, Equipment Availability (Mining) (EA-M) is used to gauge the utilization or availability of capacity. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Available Equipment Hours / Scheduled Hours; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Mining & metals, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of scheduled time mining equipment is operable. It matters because haul trucks and excavators cap throughput, so availability drives every downstream tonne metric. Teams can log equipment as available while it operates derated, overstating true capacity. Read with Effective Utilization (time at work face) and Preventive Maintenance Compliance to confirm availability is productive.

## Formula

```
EA-M = Available Equipment Hours / Scheduled Hours
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** mining_metals
- **Sector:** mining_metals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 719 (batch 2)
