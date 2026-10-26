# dea:metric-indirect-tax-recovery-rate

Candidate Performance Metric record for **Indirect Tax Recovery Rate** (ITRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-indirect-tax-recovery-rate`
- **Name:** Indirect Tax Recovery Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ITRR

## 2. Definition

Within Tax & Fiscal, Indirect Tax Recovery Rate (ITRR) is used to gauge the economic value created or preserved. It is defined as Recoverable Indirect Taxes Claimed / Eligible Amounts; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of recoverable indirect taxes such as VAT actually reclaimed. It matters because unrecovered tax is pure margin leakage and a compliance signal. Gaming risk includes aggressive recovery positions that invite audit assessment later. Read with Tax Audit Adjustment Ratio and compliance filing quality to balance recovery aggressiveness with audit risk.

## Formula

```
ITRR = Recoverable Indirect Taxes Claimed / Eligible Amounts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** tax_fiscal

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 608 (batch 2)
