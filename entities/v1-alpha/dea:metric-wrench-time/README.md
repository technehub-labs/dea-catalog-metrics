# dea:metric-wrench-time

Candidate Performance Metric record for **Wrench Time** (WT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wrench-time`
- **Name:** Wrench Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WT

## 2. Definition

Wrench Time (WT) captures how efficiently resources are converted into outputs for organizations tracking maintenance & reliability. It is defined as Direct Tool-Time / Total Technician Time; the result is stated in percent (%). In Manufacturing, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Direct Tool-Time / Total Technician Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 275 (batch 1)
