# dea:metric-units-per-hour

Candidate Performance Metric record for **Units per Hour** (UPH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-units-per-hour`
- **Name:** Units per Hour
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UPH

## 2. Definition

Within Manufacturing, Units per Hour (UPH) is used to gauge the utilization or availability of capacity. It is a working-level control: thresholds trigger immediate operational response. It is defined as Units Produced / Production Hours; the result is stated in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. In Manufacturing, it is a recognized element of the standard performance toolkit.

## Formula

```
UPH = Units Produced / Production Hours
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
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 247 (batch 1)
