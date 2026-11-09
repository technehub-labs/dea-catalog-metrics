# dea:metric-opportunity-slippage-rate

Candidate Performance Metric record for **Opportunity Slippage Rate** (OSR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-opportunity-slippage-rate`
- **Name:** Opportunity Slippage Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OSR

## 2. Definition

A Sales indicator, Opportunity Slippage Rate (OSR) quantifies exposure to adverse outcomes. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Deals Slipping from Forecast Period / Forecast Deals; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of deals forecast to close in a period that slip into later ones. It matters because slippage is the leading indicator of forecast misses and disguised pipeline weakness. Reps can hide slippage by pushing close dates before the forecast is locked, then extending after. Read with Forecast Accuracy and Sales Cycle Length to see whether slippage is honest friction or systematic date-shuffling.

## Formula

```
OSR = Deals Slipping from Forecast Period / Forecast Deals
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 96 (batch 1)
