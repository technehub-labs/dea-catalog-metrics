# dea:metric-cell-site-outage-rate

Candidate Performance Metric record for **Cell Site Outage Rate** (CSOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cell-site-outage-rate`
- **Name:** Cell Site Outage Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CSOR

## 2. Definition

A Telecom Network Operations (Deep Dive) indicator, Cell Site Outage Rate (CSOR) quantifies exposure to adverse outcomes. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Site Outages / Sites; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Telecommunications, it is a recognized element of the standard performance toolkit.

## Formula

```
Site Outages / Sites
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2127 (batch 6)
