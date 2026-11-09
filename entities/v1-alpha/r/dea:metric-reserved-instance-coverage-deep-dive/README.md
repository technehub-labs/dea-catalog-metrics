# dea:metric-reserved-instance-coverage-deep-dive

Candidate Performance Metric record for **Reserved Instance Coverage (Deep Dive)** (RIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reserved-instance-coverage-deep-dive`
- **Name:** Reserved Instance Coverage (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RIC

## 2. Definition

A Data Centers & Cloud Infrastructure indicator, Reserved Instance Coverage (Deep Dive) (RIC) quantifies how efficiently resources are converted into outputs. It is defined as Spend on Reserved Capacity / Eligible Spend; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Technology, it is a recognized element of the standard performance toolkit.

## Formula

```
RIC = Spend on Reserved Capacity / Eligible Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2146 (batch 6)
