# dea:metric-return-per-unit-of-risk-realized

Candidate Performance Metric record for **Return per Unit of Risk Realized** (RPRUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-per-unit-of-risk-realized`
- **Name:** Return per Unit of Risk Realized
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RPRUR

## 2. Definition

A Investment Performance Measurement indicator, Return per Unit of Risk Realized (RPRUR) quantifies the economic value created or preserved. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Realized Return / Realized Volatility - reported in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Investment management sector.

## 3. Context

Measures realized excess return per unit of realized risk (the realized information ratio). It answers whether the risk budget was spent on returns or on fees and noise. Realized ratios over short periods are unstable. Read with information ratio and excess return over benchmark.

## Formula

```
Realized Return / Realized Volatility
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3451 (batch 7)
