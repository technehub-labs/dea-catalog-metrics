# dea:metric-demand-plan-bias

Candidate Performance Metric record for **Demand Plan Bias** (DPB-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-demand-plan-bias`
- **Name:** Demand Plan Bias
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DPB-S

## 2. Definition

A Sales & Operations Planning indicator, Demand Plan Bias (DPB-S) quantifies the quality of outputs and outcomes. The formula is Sum of Plan Errors / Sum of Actuals - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures systematic over- or under-forecasting in the S&OP demand plan. It matters because bias corrupts every downstream supply and financial plan. Commercial teams can bias plans low to protect their targets, sandbagging supply. Read with Demand Plan Accuracy and Inventory Plan Accuracy to confirm bias is being corrected, not absorbed.

## Formula

```
Sum of Plan Errors / Sum of Actuals
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1290 (batch 5)
