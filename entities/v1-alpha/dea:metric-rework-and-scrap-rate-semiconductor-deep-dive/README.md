# dea:metric-rework-and-scrap-rate-semiconductor-deep-dive

Candidate Performance Metric record for **Rework and Scrap Rate (Semiconductor Deep Dive)** (RSR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rework-and-scrap-rate-semiconductor-deep-dive`
- **Name:** Rework and Scrap Rate (Semiconductor Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RSR-S

## 2. Definition

Rework and Scrap Rate (Semiconductor Deep Dive) (RSR-S) captures how efficiently resources are converted into outputs for organizations tracking semiconductor manufacturing (deep dive). It is defined as Reworked or Scrapped Wafers / Wafers Processed; the result is stated in percent (%). In Semiconductors, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
RSR-S = Reworked or Scrapped Wafers / Wafers Processed
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2381 (batch 6)
