# dea:metric-jitter-rate

Candidate Performance Metric record for **Jitter Rate** (JTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-jitter-rate`
- **Name:** Jitter Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** JTR

## 2. Definition

Jitter Rate (JTR) measures the quality of outputs and outcomes in the Network Performance & Capacity domain. It is defined as Packet Delay Variation Exceeding Threshold / Samples; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
JTR = Packet Delay Variation Exceeding Threshold / Samples
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3343 (batch 7)
