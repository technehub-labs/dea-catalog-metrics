# dea:metric-tracking-error-deep-dive

Candidate Performance Metric record for **Tracking Error (Deep Dive)** (TE-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tracking-error-deep-dive`
- **Name:** Tracking Error (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TE-D

## 2. Definition

A Investment Management - Portfolio Operations indicator, Tracking Error (Deep Dive) (TE-D) quantifies exposure to adverse outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Standard Deviation of Active Returns; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. In Financial Services, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the standard deviation of portfolio returns relative to the benchmark. It quantifies how actively the mandate is being run: low TE implies closet indexing, high TE implies concentrated bets. TE used without reference to information ratio says nothing about whether the risk paid. Read with excess return over benchmark and beta to benchmark.

## Formula

```
Standard Deviation of Active Returns
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2999 (batch 7)
