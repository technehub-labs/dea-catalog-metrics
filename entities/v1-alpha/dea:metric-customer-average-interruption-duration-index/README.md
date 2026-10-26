# dea:metric-customer-average-interruption-duration-index

Candidate Performance Metric record for **Customer Average Interruption Duration Index** (CAIDI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-average-interruption-duration-index`
- **Name:** Customer Average Interruption Duration Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CAIDI

## 2. Definition

Customer Average Interruption Duration Index (CAIDI) addresses the quality of outputs and outcomes and is a fixture of energy & utilities reporting. It is defined as Total Interruption Minutes / Total Interruptions; the result is stated in minutes. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. In Energy & utilities, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the average outage duration each customer experiences over a period. It matters because regulators and customers care about customer-felt reliability, not equipment uptime. It can be gamed by excluding major-event days from the calculation window. Read with System Average Interruption Frequency Index and Unplanned Outage Rate to see both duration and frequency sides of reliability.

## Formula

```
Total Interruption Minutes / Total Interruptions
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 438 (batch 1)
