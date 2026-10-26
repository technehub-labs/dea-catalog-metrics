# dea:metric-time-weighted-rate-of-return-deep-dive

Candidate Performance Metric record for **Time-Weighted Rate of Return (Deep Dive)** (TWRR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-weighted-rate-of-return-deep-dive`
- **Name:** Time-Weighted Rate of Return (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TWRR-D

## 2. Definition

Within Investment Management - Portfolio Operations, Time-Weighted Rate of Return (Deep Dive) (TWRR-D) is used to gauge how effectively a process or entity achieves its intended outcome. The formula is Compound Sub-Period Returns Adjusted for Flows - reported in percent (%). It is a standard measure in the Financial Services sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the compound growth rate of a portfolio isolating the manager's decisions from cash-flow timing. TWR is the industry-standard basis for comparing managers because it strips out deposit and withdrawal effects. It assumes precise daily valuation, so approximations degrade accuracy for volatile portfolios. Read with money-weighted rate of return and excess return over benchmark.

## Formula

```
Compound Sub-Period Returns Adjusted for Flows
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** effectiveness
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2997 (batch 7)
