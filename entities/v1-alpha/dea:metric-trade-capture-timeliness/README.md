# dea:metric-trade-capture-timeliness

Candidate Performance Metric record for **Trade Capture Timeliness** (TCT-TRD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trade-capture-timeliness`
- **Name:** Trade Capture Timeliness
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TCT-TRD

## 2. Definition

Trade Capture Timeliness (TCT-TRD) measures conformance to standards, plans, or obligations in the Investment Research & Trading Operations domain. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Trades Captured within Window / Trades - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Financial Services sector.

## Formula

```
Trades Captured within Window / Trades
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3050 (batch 7)
