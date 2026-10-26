# dea:metric-bind-rate-within-deadline

Candidate Performance Metric record for **Bind Rate within Deadline** (BRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bind-rate-within-deadline`
- **Name:** Bind Rate within Deadline
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BRD

## 2. Definition

Bind Rate within Deadline (BRD) measures the quality of outputs and outcomes in the Insurance Distribution & Brokerage domain. It is defined as Applications Bound before Underwriting Deadline / Applications; the result is stated in percent (%). In Insurance distribution, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Applications Bound before Underwriting Deadline / Applications
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** insurance_distribution_brokerage
- **Sector:** insurance_distribution

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1159 (batch 4)
