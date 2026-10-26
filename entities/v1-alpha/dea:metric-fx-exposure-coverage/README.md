# dea:metric-fx-exposure-coverage

Candidate Performance Metric record for **FX Exposure Coverage** (FXC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fx-exposure-coverage`
- **Name:** FX Exposure Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FXC

## 2. Definition

FX Exposure Coverage (FXC) measures exposure to adverse outcomes in the Treasury & Cash Management domain. The formula is Hedged Foreign Exposure / Total Foreign Exposure - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures the share of foreign exchange exposure that is hedged. It matters because unhedged exposure turns currency noise into earnings noise. Over-hedging to look prudent locks in costs and can become its own speculative position. Read with Hedge Effectiveness Ratio and FX gain/loss volatility to confirm coverage is sized to actual exposure, not optics.

## Formula

```
Hedged Foreign Exposure / Total Foreign Exposure
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 600 (batch 2)
