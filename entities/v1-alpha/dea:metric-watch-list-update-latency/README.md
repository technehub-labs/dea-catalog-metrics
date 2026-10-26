# dea:metric-watch-list-update-latency

Candidate Performance Metric record for **Watch List Update Latency** (WLUL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-watch-list-update-latency`
- **Name:** Watch List Update Latency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WLUL

## 2. Definition

Watch List Update Latency (WLUL) measures conformance to standards, plans, or obligations in the Insurance Fraud & Financial Crime domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Hours to Deploy New Sanctions List; the result is stated in hours. It should be driven down, since lower readings signal healthier performance. In Financial Services, it is a recognized element of the standard performance toolkit.

## Formula

```
Hours to Deploy New Sanctions List
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** risk
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_fraud_financial_crime
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2473 (batch 6)
