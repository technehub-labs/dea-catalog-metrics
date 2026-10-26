# dea:metric-reinsurance-recovery-timeliness

Candidate Performance Metric record for **Reinsurance Recovery Timeliness** (RRT-I) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reinsurance-recovery-timeliness`
- **Name:** Reinsurance Recovery Timeliness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RRT-I

## 2. Definition

A Claims Operations (Insurance) indicator, Reinsurance Recovery Timeliness (RRT-I) quantifies how efficiently resources are converted into outputs. The formula is Reinsurance Recoveries Received by Due Date / Recoveries Due - reported in percent (%). It is a standard measure in the Insurance sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how quickly ceded reinsurance recoveries are collected. It matters because slow recovery strands capital and distorts liquidity. Timeliness can be improved by settling recoveries at discounts, buying the metric with value. Read with Recoverable Aging and Dispute Rate with reinsurers to confirm speed is not costly.

## Formula

```
Reinsurance Recoveries Received by Due Date / Recoveries Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** claims_operations_insurance
- **Sector:** insurance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 857 (batch 3)
