# dea:metric-sell-side-broker-scorecard-coverage

Candidate Performance Metric record for **Sell-Side Broker Scorecard Coverage** (SBSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sell-side-broker-scorecard-coverage`
- **Name:** Sell-Side Broker Scorecard Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SBSC

## 2. Definition

Sell-Side Broker Scorecard Coverage (SBSC) measures conformance to standards, plans, or obligations in the Investment Research & Trading Operations domain. The formula is Brokers Evaluated on Scorecard / Active Brokers - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Financial Services sector.

## Formula

```
SBSC = Brokers Evaluated on Scorecard / Active Brokers
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_research_trading_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3046 (batch 7)
