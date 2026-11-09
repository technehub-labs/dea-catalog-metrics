# dea:metric-occupancy-rate-deep-dive

Candidate Performance Metric record for **Occupancy Rate (Deep Dive)** (OCC-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-occupancy-rate-deep-dive`
- **Name:** Occupancy Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OCC-D

## 2. Definition

Occupancy Rate (Deep Dive) (OCC-D) measures the utilization or availability of capacity in the Contact Center Operations (Deep Dive) domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Handle Time / Scheduled Time; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
OCC-D = Handle Time / Scheduled Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2477 (batch 6)
