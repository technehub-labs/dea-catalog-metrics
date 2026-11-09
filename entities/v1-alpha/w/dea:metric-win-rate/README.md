# dea:metric-win-rate

Candidate Performance Metric record for **Win Rate** (WR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-win-rate`
- **Name:** Win Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WR

## 2. Definition

Within Sales, Win Rate (WR) is used to gauge how effectively a process or entity achieves its intended outcome. It is defined as Closed-Won Deals / Total Closed Deals; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of qualified opportunities that close as wins. It matters as a direct read on competitive strength and qualification discipline. Teams can inflate it by only logging deals they expect to win, silently shrinking the denominator. Read with Pipeline Coverage Ratio and Average Deal Size to detect whether a high win rate hides a thin or under-tracked pipeline.

## Formula

```
WR = Closed-Won Deals / Total Closed Deals
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 88 (batch 1)
