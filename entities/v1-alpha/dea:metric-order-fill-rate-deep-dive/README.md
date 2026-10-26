# dea:metric-order-fill-rate-deep-dive

Candidate Performance Metric record for **Order Fill Rate (Deep Dive)** (OFR-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-fill-rate-deep-dive`
- **Name:** Order Fill Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OFR-T

## 2. Definition

Order Fill Rate (Deep Dive) (OFR-T) measures how efficiently resources are converted into outputs in the Investment Research & Trading Operations domain. It is defined as Orders Fully Filled / Orders; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Financial Services, it is a recognized element of the standard performance toolkit.

## Formula

```
Orders Fully Filled / Orders
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
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3036 (batch 7)
