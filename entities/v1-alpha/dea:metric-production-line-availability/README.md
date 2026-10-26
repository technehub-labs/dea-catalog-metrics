# dea:metric-production-line-availability

Candidate Performance Metric record for **Production Line Availability** (PLA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-production-line-availability`
- **Name:** Production Line Availability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PLA

## 2. Definition

Production Line Availability (PLA) addresses the utilization or availability of capacity and is a fixture of automotive reporting. It is defined as Line Uptime / Scheduled Line Time; the result is stated in percent (%). In Automotive, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Line Uptime / Scheduled Line Time
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 744 (batch 2)
