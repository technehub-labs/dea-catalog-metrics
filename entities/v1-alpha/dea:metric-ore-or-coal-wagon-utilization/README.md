# dea:metric-ore-or-coal-wagon-utilization

Candidate Performance Metric record for **Ore or Coal Wagon Utilization** (OWU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ore-or-coal-wagon-utilization`
- **Name:** Ore or Coal Wagon Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OWU

## 2. Definition

Within Rail Freight (Deep Dive), Ore or Coal Wagon Utilization (OWU) is used to gauge the utilization or availability of capacity. It is defined as Loaded Wagon Days / Total Wagon Days; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Rail, it is a recognized element of the standard performance toolkit.

## Formula

```
Loaded Wagon Days / Total Wagon Days
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
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2426 (batch 6)
