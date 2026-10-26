# dea:metric-excess-return-consistency-rate

Candidate Performance Metric record for **Excess Return Consistency Rate** (ERCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-excess-return-consistency-rate`
- **Name:** Excess Return Consistency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERCR

## 2. Definition

Excess Return Consistency Rate (ERCR) addresses the economic value created or preserved and is a fixture of investment performance measurement reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Periods Beating Benchmark / Periods in Window, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Investment management practice.

## 3. Context

Measures how frequently the portfolio beats its benchmark across periods. Consistency is stronger evidence of skill than cumulative outperformance. Consistency measured on short windows rewards luck. Read with rolling three-year percentile rank and information ratio.

## Formula

```
ERCR = Periods Beating Benchmark / Periods in Window
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3443 (batch 7)
