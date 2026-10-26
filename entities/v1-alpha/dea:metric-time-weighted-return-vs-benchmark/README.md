# dea:metric-time-weighted-return-vs-benchmark

Candidate Performance Metric record for **Time-Weighted Return vs Benchmark** (TWRB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-time-weighted-return-vs-benchmark`
- **Name:** Time-Weighted Return vs Benchmark
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TWRB

## 2. Definition

Time-Weighted Return vs Benchmark (TWRB) captures the economic value created or preserved for organizations tracking investment performance measurement. Its calculation is TWR minus Benchmark Return in Period, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Investment management practice.

## 3. Context

Measures the manager's time-weighted return against its declared benchmark. This is the cleanest manager-skill comparison available. Small differences are noise without long horizons. Read with excess return over benchmark and tracking error.

## Formula

```
TWRB = TWR minus Benchmark Return in Period
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3441 (batch 7)
