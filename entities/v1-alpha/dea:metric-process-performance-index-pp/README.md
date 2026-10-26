# dea:metric-process-performance-index-pp

Candidate Performance Metric record for **Process Performance Index (Pp)** (PPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-performance-index-pp`
- **Name:** Process Performance Index (Pp)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PPS

## 2. Definition

Process Performance Index (Pp) (PPS) addresses the quality of outputs and outcomes and is a fixture of process capability & six sigma (deep dive) reporting. It is defined as (Upper Spec - Lower Spec) / (6 x Total Std Dev); the result is stated in ratio (x:1 or x). In Manufacturing, it is a recognized element of the standard performance toolkit. It is a working-level control: thresholds trigger immediate operational response. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
(Upper Spec - Lower Spec) / (6 x Total Std Dev)
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4077 (batch 9)
