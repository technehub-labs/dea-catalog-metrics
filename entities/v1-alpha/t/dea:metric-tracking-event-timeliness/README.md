# dea:metric-tracking-event-timeliness

Candidate Performance Metric record for **Tracking Event Timeliness** (TET) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tracking-event-timeliness`
- **Name:** Tracking Event Timeliness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TET

## 2. Definition

A Postal & Courier indicator, Tracking Event Timeliness (TET) quantifies the quality of outputs and outcomes. It is defined as Scan Events Posted within Threshold / Events Generated; the result is stated in percent (%). In Postal & courier, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
TET = Scan Events Posted within Threshold / Events Generated
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** postal_courier
- **Sector:** postal_courier

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 831 (batch 2)
