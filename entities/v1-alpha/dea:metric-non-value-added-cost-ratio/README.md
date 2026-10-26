# dea:metric-non-value-added-cost-ratio

Candidate Performance Metric record for **Non-Value-Added Cost Ratio** (NVAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-non-value-added-cost-ratio`
- **Name:** Non-Value-Added Cost Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NVAC

## 2. Definition

Non-Value-Added Cost Ratio (NVAC) captures how efficiently resources are converted into outputs for organizations tracking process excellence (lean six sigma). It is defined as Non-Value-Added Cost / Total Process Cost; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Non-value-added cost ratio measures the share of cost consumed by activities the customer would not pay for - inspection, rework, movement, waiting, over-processing, the classic Lean waste categories - and it is the diagnostic metric of Lean improvement: it tells the improvement program where the money is. The measurement is inherently estimate-based (value-add classification is a judgment exercise, done through process observation and value-stream mapping), which makes the ratio a direction-and-magnitude tool rather than a precise accounting figure. Its strategic use is prioritization: improvement programs that chase visible waste in low-cost processes while value-stream mapping shows the big NVA costs in support functions miss the opportunity. Read with value-stream-map refresh cadence (the classification ages), NVA-reduction project pipeline (is the ratio producing action?), and first-pass quality metrics for the underlying driver.

## Formula

```
Non-Value-Added Cost / Total Process Cost
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_excellence_lean_six_sigma

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1119 (batch 4)
