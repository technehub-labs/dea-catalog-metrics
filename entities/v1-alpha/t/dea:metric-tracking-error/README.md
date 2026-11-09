# dea:metric-tracking-error

Candidate Performance Metric record for **Tracking Error** (TE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tracking-error`
- **Name:** Tracking Error
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TE

## 2. Definition

Within Investment Management, Tracking Error (TE) is used to gauge exposure to adverse outcomes. The formula is Standard Deviation of Portfolio Return minus Benchmark Return - reported in percent (%). It is a standard measure in the Asset management sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Tracking error is the annualized standard deviation of a portfolio's return relative to its benchmark - the magnitude of its active bets expressed as volatility. It is the constraint clients negotiate into mandates and the budget managers allocate across positions. But it says nothing about direction: two portfolios with identical tracking error can sit on opposite sides of the benchmark, and it can be gamed by tilting toward high-beta names rather than forming true active views. Ex-ante (modeled) and ex-post (realized) tracking error frequently diverge, and that gap itself is a risk-management signal. Read with active share and factor exposure deltas to judge whether risk is concentrated or spread.

## Formula

```
TE = Standard Deviation of Portfolio Return minus Benchmark Return
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
- **Domain:** investment_management
- **Sector:** asset_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 765 (batch 2)
