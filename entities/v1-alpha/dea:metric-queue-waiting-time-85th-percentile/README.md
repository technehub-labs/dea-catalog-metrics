# dea:metric-queue-waiting-time-85th-percentile

Candidate Performance Metric record for **Queue Waiting Time - 85th Percentile** (QW85) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-queue-waiting-time-85th-percentile`
- **Name:** Queue Waiting Time - 85th Percentile
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** QW85

## 2. Definition

Within Retail Banking Branch Network (Deep Dive), Queue Waiting Time - 85th Percentile (QW85) is used to gauge the quality of outputs and outcomes. It is defined as Minutes waited by 85th percentile customer; the result is stated in minutes. In Banking, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Minutes waited by 85th percentile customer
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_branch_network_deep_dive
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2116 (batch 6)
