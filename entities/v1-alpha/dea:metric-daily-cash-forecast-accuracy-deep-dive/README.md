# dea:metric-daily-cash-forecast-accuracy-deep-dive

Candidate Performance Metric record for **Daily Cash Forecast Accuracy (Deep Dive)** (DCFA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-daily-cash-forecast-accuracy-deep-dive`
- **Name:** Daily Cash Forecast Accuracy (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DCFA-D

## 2. Definition

Daily Cash Forecast Accuracy (Deep Dive) (DCFA-D) addresses the quality of outputs and outcomes and is a fixture of corporate treasury (deep dive) reporting. Its calculation is 1 - Absolute Forecast Error / Actual Cash, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures deviation between forecast and actual cash positions. Forecast accuracy is the operational currency of treasury: it sets how much buffer must be parked in low-yield accounts, and error compounds into funding gaps or idle liquidity. Variance by entity and account identifies where the process fails, and payment-timing assumptions are usually the culprit. Read with liquidity buffer compliance and working capital ratio (Deep Dive).

## Formula

```
1 - Absolute Forecast Error / Actual Cash
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_treasury_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2180 (batch 6)
