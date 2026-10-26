# dea:metric-excess-return-over-benchmark-deep-dive

Candidate Performance Metric record for **Excess Return over Benchmark (Deep Dive)** (EROB-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-excess-return-over-benchmark-deep-dive`
- **Name:** Excess Return over Benchmark (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EROB-D

## 2. Definition

A Investment Management - Portfolio Operations indicator, Excess Return over Benchmark (Deep Dive) (EROB-D) quantifies how effectively a process or entity achieves its intended outcome. The formula is Portfolio Return - Benchmark Return - reported in percent (%). It is a standard measure in the Financial Services sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the portfolio return above its benchmark over the period. Excess return is the headline scoreboard of active management. Without risk adjustment (information ratio), high excess return may just be high risk taken. Read with tracking error and manager selection win rate.

## Formula

```
Portfolio Return - Benchmark Return
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3004 (batch 7)
