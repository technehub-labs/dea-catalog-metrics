# dea:metric-internal-rate-of-return-fund-level-deep-dive

Candidate Performance Metric record for **Internal Rate of Return - Fund Level (Deep Dive)** (FIRR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-internal-rate-of-return-fund-level-deep-dive`
- **Name:** Internal Rate of Return - Fund Level (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FIRR-D

## 2. Definition

Internal Rate of Return - Fund Level (Deep Dive) (FIRR-D) captures the economic value created or preserved for organizations tracking investment management - portfolio operations. Its calculation is Fund Cash Flow IRR, measured in percent (%). It originates from and is most used in Financial Services practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the annualized return of the fund including timing of cash flows. IRR is the private-markets headline, but it rewards early exits and can be flattered by small quick wins on a large denominator. It should never be read without DPI and the J-curve context. Read with distribution-to-paid-in ratio and time-weighted rate of return.

## Formula

```
Fund Cash Flow IRR
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3021 (batch 7)
