# dea:metric-maximum-drawdown-deep-dive

Candidate Performance Metric record for **Maximum Drawdown (Deep Dive)** (MDD-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maximum-drawdown-deep-dive`
- **Name:** Maximum Drawdown (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MDD-D

## 2. Definition

Maximum Drawdown (Deep Dive) (MDD-D) measures exposure to adverse outcomes in the Investment Management - Portfolio Operations domain. The formula is Largest Peak-to-Trough Decline - reported in percent (%). It is a standard measure in the Financial Services sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the largest peak-to-trough decline in portfolio value over the period. Drawdown is the risk number clients actually feel and the one that triggers redemptions. It is path-dependent: the same average return can hide very different drawdown experiences. Read with downside capture ratio and recovery time from peak drawdown.

## Formula

```
Largest Peak-to-Trough Decline
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3000 (batch 7)
