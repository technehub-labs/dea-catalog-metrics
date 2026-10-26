# dea:metric-sortino-ratio-deep-dive

Candidate Performance Metric record for **Sortino Ratio (Deep Dive)** (SORTDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sortino-ratio-deep-dive`
- **Name:** Sortino Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SORTDD

## 2. Definition

Within Investment Performance Measurement, Sortino Ratio (Deep Dive) (SORTDD) is used to gauge exposure to adverse outcomes. It is defined as Return below Target / Downside Deviation; the result is stated in ratio (x:1 or x). In Investment management, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

The Sortino ratio, from Frank A. Sortino's downside-risk framework (1980s), divides return below target by downside deviation only - volatility is penalized only when it hurts. This fixes the Sharpe ratio's most-criticized flaw: punishing upside surprise. For return distributions with positive skew (good funds can look bad on Sharpe), Sortino is the fairer lens. Practical caveats: downside deviation needs enough downside observations to be stable (annual data starves it), and target choice changes the number - state both when reporting. Many practitioners read Sharpe and Sortino together precisely to detect asymmetry the Sharpe ratio hides.

## Formula

```
Return below Target / Downside Deviation
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Frank A. Sortino (downside-risk framework, 1980s)

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3446 (batch 7)
