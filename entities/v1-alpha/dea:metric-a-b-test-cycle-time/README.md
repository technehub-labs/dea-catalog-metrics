# dea:metric-a-b-test-cycle-time

Candidate Performance Metric record for **A-B Test Cycle Time** (ABTCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-a-b-test-cycle-time`
- **Name:** A-B Test Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ABTCT

## 2. Definition

A-B Test Cycle Time (ABTCT) measures how efficiently resources are converted into outputs in the Data Science & Analytics Operations domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Days from Hypothesis to Decision - reported in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
ABTCT = Days from Hypothesis to Decision
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_science_analytics_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2588 (batch 7)
