# dea:metric-consensus-forecast-accuracy-s-op

Candidate Performance Metric record for **Consensus Forecast Accuracy (S&OP)** (CFA-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-consensus-forecast-accuracy-s-op`
- **Name:** Consensus Forecast Accuracy (S&OP)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CFA-S

## 2. Definition

Within Sales & Operations Planning, Consensus Forecast Accuracy (S&OP) (CFA-S) is used to gauge the quality of outputs and outcomes. It is defined as 1 - ABS(Consensus Forecast - Actual) / Actual; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how closely the jointly agreed demand plan matches actual demand, the signal that determines whether the whole S&OP chain is worth trusting. Inaccuracy here propagates into inventory, capacity, and service failures with a lag. Two honest-read rules: measure at the right aggregation level (a plan can be accurate in total and useless by SKU-region), and watch for sandbagging, where functions deliberately bias the consensus to hit their own targets. Read with bias measures and excess and obsolete inventory ratio.

## Formula

```
1 - ABS(Consensus Forecast - Actual) / Actual
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1289 (batch 5)
