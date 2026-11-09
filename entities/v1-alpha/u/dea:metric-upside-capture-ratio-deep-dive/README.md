# dea:metric-upside-capture-ratio-deep-dive

Candidate Performance Metric record for **Upside Capture Ratio (Deep Dive)** (UCR-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-upside-capture-ratio-deep-dive`
- **Name:** Upside Capture Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** UCR-IM

## 2. Definition

Upside Capture Ratio (Deep Dive) (UCR-IM) captures how effectively a process or entity achieves its intended outcome for organizations tracking investment management - portfolio operations. It is defined as Fund Upside Return / Benchmark Upside Return; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Financial Services, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the percentage of benchmark gains the portfolio realizes in up markets. Upside capture shows whether defensive positioning costs too much participation. Ratios measured over short windows are noise-dominated. Read with downside capture ratio and excess return over benchmark.

## Formula

```
UCR-IM = Fund Upside Return / Benchmark Upside Return
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3002 (batch 7)
