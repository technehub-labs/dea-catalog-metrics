# dea:metric-proof-of-delivery-capture-rate

Candidate Performance Metric record for **Proof of Delivery Capture Rate** (PODR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-proof-of-delivery-capture-rate`
- **Name:** Proof of Delivery Capture Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PODR

## 2. Definition

Within Parcel & Last-Mile Logistics (Deep Dive), Proof of Delivery Capture Rate (PODR) is used to gauge conformance to standards, plans, or obligations. Its calculation is Deliveries with Electronic POD / Deliveries, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Logistics & Trade practice.

## Formula

```
PODR = Deliveries with Electronic POD / Deliveries
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** parcel_last_mile_logistics_deep_dive
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2332 (batch 6)
