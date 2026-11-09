# dea:metric-beta-to-benchmark-deep-dive

Candidate Performance Metric record for **Beta to Benchmark (Deep Dive)** (BETA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-beta-to-benchmark-deep-dive`
- **Name:** Beta to Benchmark (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BETA-D

## 2. Definition

A Investment Management - Portfolio Operations indicator, Beta to Benchmark (Deep Dive) (BETA-D) quantifies exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Covariance with Benchmark / Benchmark Variance, measured in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. It originates from and is most used in Financial Services practice.

## 3. Context

Measures the sensitivity of portfolio returns to benchmark movements. Beta is the exposure dial: it separates market risk from the risk the manager actually controls. Estimated from historical windows, beta drifts as portfolio composition changes. Read with tracking error and downside capture ratio.

## Formula

```
BETA-D = Covariance with Benchmark / Benchmark Variance
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3003 (batch 7)
