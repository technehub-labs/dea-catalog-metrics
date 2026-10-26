# dea:metric-assembly-line-availability-deep-dive

Candidate Performance Metric record for **Assembly Line Availability (Deep Dive)** (ALA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-assembly-line-availability-deep-dive`
- **Name:** Assembly Line Availability (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ALA-D

## 2. Definition

Assembly Line Availability (Deep Dive) (ALA-D) measures the utilization or availability of capacity in the Automotive Manufacturing (Deep Dive) domain. It is computed as Uptime / Scheduled Production Time, expressed in percent (%). Its use is concentrated in Automotive. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Uptime / Scheduled Production Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2362 (batch 6)
