# dea:metric-money-weighted-return-gap

Candidate Performance Metric record for **Money-Weighted Return Gap** (MWRG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-money-weighted-return-gap`
- **Name:** Money-Weighted Return Gap
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MWRG

## 2. Definition

Money-Weighted Return Gap (MWRG) captures the economic value created or preserved for organizations tracking investment performance measurement. It is computed as Money-Weighted minus Time-Weighted Return, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is concentrated in Investment management.

## Formula

```
Money-Weighted minus Time-Weighted Return
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3442 (batch 7)
