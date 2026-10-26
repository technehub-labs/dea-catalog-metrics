# dea:metric-slippage-versus-arrival-price-deep-dive

Candidate Performance Metric record for **Slippage versus Arrival Price (Deep Dive)** (SAP-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-slippage-versus-arrival-price-deep-dive`
- **Name:** Slippage versus Arrival Price (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SAP-D

## 2. Definition

Slippage versus Arrival Price (Deep Dive) (SAP-D) measures the quality of outputs and outcomes in the Investment Research & Trading Operations domain. It is computed as Execution Price vs Arrival Price Difference, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Financial Services.

## Formula

```
Execution Price vs Arrival Price Difference
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3039 (batch 7)
