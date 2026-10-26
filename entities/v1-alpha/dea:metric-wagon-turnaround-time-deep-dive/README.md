# dea:metric-wagon-turnaround-time-deep-dive

Candidate Performance Metric record for **Wagon Turnaround Time (Deep Dive)** (WTT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wagon-turnaround-time-deep-dive`
- **Name:** Wagon Turnaround Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WTT-D

## 2. Definition

Within Rail Freight (Deep Dive), Wagon Turnaround Time (Deep Dive) (WTT-D) is used to gauge how efficiently resources are converted into outputs. It is defined as Days from Load to Reload; the result is stated in days. In Rail, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures elapsed time from wagon dispatch to return for reloading. Wagon fleet is constrained capital in rail freight, and turnaround is the asset-velocity metric: slow turnarounds require more wagons for the same throughput, and dwell at customer sidings and yards is where the time hides. Turnaround improved by expedite favors for select customers degrades the baseline flow. Read with yard dwell decomposition and wagon fleet utilization.

## Formula

```
Days from Load to Reload
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2420 (batch 6)
