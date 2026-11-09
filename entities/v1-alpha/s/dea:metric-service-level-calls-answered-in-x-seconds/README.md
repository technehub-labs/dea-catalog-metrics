# dea:metric-service-level-calls-answered-in-x-seconds

Candidate Performance Metric record for **Service Level (Calls Answered in X seconds)** (SL-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-calls-answered-in-x-seconds`
- **Name:** Service Level (Calls Answered in X seconds)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SL-CC

## 2. Definition

A Contact Center indicator, Service Level (Calls Answered in X seconds) (SL-CC) quantifies conformance to standards, plans, or obligations. It is computed as Calls Answered within Threshold / Calls Offered, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
SL-CC = Calls Answered within Threshold / Calls Offered
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 565 (batch 2)
