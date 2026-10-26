# dea:metric-benchmark-fit-r-squared

Candidate Performance Metric record for **Benchmark Fit R-Squared** (BFR2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-benchmark-fit-r-squared`
- **Name:** Benchmark Fit R-Squared
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BFR2

## 2. Definition

A Investment Performance Measurement indicator, Benchmark Fit R-Squared (BFR2) quantifies the quality of outputs and outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Explained Variance of Returns vs Benchmark, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Investment management.

## Formula

```
BFR2 = Explained Variance of Returns vs Benchmark
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3452 (batch 7)
