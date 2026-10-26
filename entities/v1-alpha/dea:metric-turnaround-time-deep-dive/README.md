# dea:metric-turnaround-time-deep-dive

Candidate Performance Metric record for **Turnaround Time (Deep Dive)** (TAT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-turnaround-time-deep-dive`
- **Name:** Turnaround Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TAT-D

## 2. Definition

Turnaround Time (Deep Dive) (TAT-D) addresses how efficiently resources are converted into outputs and is a fixture of airline operations (deep dive) reporting. It is defined as Minutes from On-Blocks to Off-Blocks; the result is stated in minutes. In Airlines, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Minutes from On-Blocks to Off-Blocks
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airline_operations_deep_dive
- **Sector:** airlines

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2257 (batch 6)
