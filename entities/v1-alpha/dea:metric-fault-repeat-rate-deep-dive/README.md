# dea:metric-fault-repeat-rate-deep-dive

Candidate Performance Metric record for **Fault Repeat Rate (Deep Dive)** (FRR-N) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fault-repeat-rate-deep-dive`
- **Name:** Fault Repeat Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FRR-N

## 2. Definition

Fault Repeat Rate (Deep Dive) (FRR-N) measures the quality of outputs and outcomes in the Telecom Network Operations (Deep Dive) domain. It is defined as Recurring Faults within 30 Days / Faults; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. In Telecommunications, it is a recognized element of the standard performance toolkit.

## Formula

```
Recurring Faults within 30 Days / Faults
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2138 (batch 6)
