# dea:metric-liquidity-coverage-ratio-fund-ops

Candidate Performance Metric record for **Liquidity Coverage Ratio (Fund Ops)** (LCRFO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-liquidity-coverage-ratio-fund-ops`
- **Name:** Liquidity Coverage Ratio (Fund Ops)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LCRFO

## 2. Definition

Liquidity Coverage Ratio (Fund Ops) (LCRFO) captures exposure to adverse outcomes for organizations tracking investment risk & middle office operations. Its calculation is Liquid Assets within Days / Projected Redemptions, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Investment management practice.

## 3. Context

Measures the fund's buffer of liquid assets against stressed redemption demands. Liquidity mismatch is the classic fund failure mode: assets that cannot be sold funding liabilities that must be paid. HQLA classifications that are generous under stress assumptions invite false comfort. Read with redemption rate and stress test scenario coverage.

## Formula

```
Liquid Assets within Days / Projected Redemptions
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_risk_middle_office_operations
- **Sector:** investment_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3459 (batch 7)
