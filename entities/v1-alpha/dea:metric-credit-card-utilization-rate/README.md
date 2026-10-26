# dea:metric-credit-card-utilization-rate

Candidate Performance Metric record for **Credit Card Utilization Rate** (CCUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-credit-card-utilization-rate`
- **Name:** Credit Card Utilization Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CCUR

## 2. Definition

Credit Card Utilization Rate (CCUR) measures exposure to adverse outcomes in the Retail Banking & Lending domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Outstanding Card Balances / Approved Credit Limits - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Banking sector.

## 3. Context

Measures outstanding balances relative to credit limits across the portfolio. It matters because utilization predicts both revenue and default risk, so it is a dual-edged metric. Limit increases lower utilization and risk-weighted exposure cosmetically while customer behavior is unchanged. Read with Delinquency Rate and revenue per account to interpret utilization moves correctly.

## Formula

```
Outstanding Card Balances / Approved Credit Limits
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_banking_lending
- **Sector:** banking

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 838 (batch 3)
