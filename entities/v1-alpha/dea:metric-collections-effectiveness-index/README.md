# dea:metric-collections-effectiveness-index

Candidate Performance Metric record for **Collections Effectiveness Index** (CEI-AR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-collections-effectiveness-index`
- **Name:** Collections Effectiveness Index
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CEI-AR

## 2. Definition

A Accounts Payable & Receivable Operations (Deep Dive) indicator, Collections Effectiveness Index (CEI-AR) quantifies the quality of outputs and outcomes. Its calculation is Collected Amount / Amount Receivable in Period, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how completely collectible receivables are collected within the period. CEI is the standard honest measure of collections performance. Indexes computed on gross receivables including uncollectible ones penalize by design. Read with best possible DSO gap and recovery rate on charged-off (Deep Dive).

## Formula

```
Collected Amount / Amount Receivable in Period
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3804 (batch 8)
