# dea:metric-downside-capture-ratio-deep-dive

Candidate Performance Metric record for **Downside Capture Ratio (Deep Dive)** (DCR-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-downside-capture-ratio-deep-dive`
- **Name:** Downside Capture Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCR-IM

## 2. Definition

Downside Capture Ratio (Deep Dive) (DCR-IM) measures exposure to adverse outcomes in the Investment Management - Portfolio Operations domain. The formula is Fund Downside Return / Benchmark Downside Return - reported in ratio (x:1 or x). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Lower values are better; each reduction is an improvement. It is a standard measure in the Financial Services sector.

## 3. Context

Measures the percentage of benchmark losses the portfolio realizes in down markets. Downside capture below 100% is the signature of genuine defensive value for clients. Capture computed on monthly data can miss intra-month drawdown dynamics. Read with maximum drawdown and upside capture ratio.

## Formula

```
DCR-IM = Fund Downside Return / Benchmark Downside Return
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3001 (batch 7)
