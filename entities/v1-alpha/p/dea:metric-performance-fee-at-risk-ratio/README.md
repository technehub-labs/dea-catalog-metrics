# dea:metric-performance-fee-at-risk-ratio

Candidate Performance Metric record for **Performance Fee at Risk Ratio** (PFARR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-performance-fee-at-risk-ratio`
- **Name:** Performance Fee at Risk Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PFARR

## 2. Definition

Performance Fee at Risk Ratio (PFARR) captures the economic value created or preserved for organizations tracking investment performance measurement. Its calculation is Performance Fee at Target / Fees at Prior Period, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It originates from and is most used in Investment management practice.

## 3. Context

Measures how close the fund is to the high-water mark or hurdle that governs performance fees. Fee-at-risk drives revenue forecasting and manager incentives. Nearness measured on unrealized marks reverses quickly. Read with fund expense ratio trend and net revenue retention.

## Formula

```
PFARR = Performance Fee at Target / Fees at Prior Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_performance_measurement
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3454 (batch 7)
