# dea:metric-vehicles-per-hour

Candidate Performance Metric record for **Vehicles per Hour** (VPH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vehicles-per-hour`
- **Name:** Vehicles per Hour
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VPH

## 2. Definition

Vehicles per Hour (VPH) measures the utilization or availability of capacity in the Automotive domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Vehicles Assembled / Production Hours; the result is stated in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. In Automotive, it is a recognized element of the standard performance toolkit.

## Formula

```
Vehicles Assembled / Production Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 738 (batch 2)
