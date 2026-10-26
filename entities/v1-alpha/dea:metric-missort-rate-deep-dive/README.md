# dea:metric-missort-rate-deep-dive

Candidate Performance Metric record for **Missort Rate (Deep Dive)** (MSR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-missort-rate-deep-dive`
- **Name:** Missort Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MSR-D

## 2. Definition

A Parcel & Last-Mile Logistics (Deep Dive) indicator, Missort Rate (Deep Dive) (MSR-D) quantifies the quality of outputs and outcomes. It is defined as Misrouted Parcels / Parcels Sorted; the result is stated in events per thousand or million (scaled). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Logistics & Trade, it is a recognized element of the standard performance toolkit.

## Formula

```
MSR-D = Misrouted Parcels / Parcels Sorted
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** parcel_last_mile_logistics_deep_dive
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2335 (batch 6)
