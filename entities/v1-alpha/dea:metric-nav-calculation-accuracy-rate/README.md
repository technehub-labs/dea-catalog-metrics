# dea:metric-nav-calculation-accuracy-rate

Candidate Performance Metric record for **NAV Calculation Accuracy Rate** (NAVCAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-nav-calculation-accuracy-rate`
- **Name:** NAV Calculation Accuracy Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NAVCAR

## 2. Definition

NAV Calculation Accuracy Rate (NAVCAR) measures the quality of outputs and outcomes in the Investment Management - Portfolio Operations domain. The formula is NAV Calculations without Error / Calculations - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Financial Services sector.

## 3. Context

Measures the share of net asset value calculations completed without material error. NAV is the price every transaction rests on: errors misprice every investor simultaneously. Accuracy at the aggregate level can hide systematic errors concentrated in illiquid instruments. Read with NAV publication timeliness and valuation policy adherence rate.

## Formula

```
NAV Calculations without Error / Calculations
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3012 (batch 7)
