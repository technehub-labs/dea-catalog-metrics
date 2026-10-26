# dea:metric-longest-delay-in-queue

Candidate Performance Metric record for **Longest Delay in Queue** (LDQ-CC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-longest-delay-in-queue`
- **Name:** Longest Delay in Queue
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LDQ-CC

## 2. Definition

Within Contact Center Standard Measures (Deep Dive), Longest Delay in Queue (LDQ-CC) is used to gauge the quality of outputs and outcomes. Its calculation is Maximum Queue Wait in Period, measured in minutes. It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Maximum Queue Wait in Period
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** contact_center_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4327 (batch 10)
