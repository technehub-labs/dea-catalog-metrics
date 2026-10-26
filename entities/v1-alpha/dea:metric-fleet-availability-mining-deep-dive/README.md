# dea:metric-fleet-availability-mining-deep-dive

Candidate Performance Metric record for **Fleet Availability (Mining Deep Dive)** (FAM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fleet-availability-mining-deep-dive`
- **Name:** Fleet Availability (Mining Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FAM

## 2. Definition

Fleet Availability (Mining Deep Dive) (FAM) addresses the utilization or availability of capacity and is a fixture of metals & mining operations (deep dive) reporting. It is defined as Available Equipment Hours / Scheduled Hours; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Metals & Mining, it is a recognized element of the standard performance toolkit.

## Formula

```
Available Equipment Hours / Scheduled Hours
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** metals_mining_operations_deep_dive
- **Sector:** metals_mining

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1844 (batch 6)
