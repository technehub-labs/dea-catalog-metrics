# dea:metric-total-value-to-paid-in-ratio-private

Candidate Performance Metric record for **Total Value to Paid-In Ratio (Private)** (TVPI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-total-value-to-paid-in-ratio-private`
- **Name:** Total Value to Paid-In Ratio (Private)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TVPI

## 2. Definition

Total Value to Paid-In Ratio (Private) (TVPI) addresses the economic value created or preserved and is a fixture of investment management - portfolio operations reporting. Its calculation is (Distributions + Residual Value) / Paid-In Capital, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Financial Services practice.

## 3. Context

Measures total fund value (distributions plus residual unrealized value) against paid-in capital. TVPI blends realized and promised value, so early in fund life it is mostly markups. The gap between TVPI and DPI measures how much performance is still just opinion. Read with distribution-to-paid-in ratio and valuation policy adherence rate.

## Formula

```
(Distributions + Residual Value) / Paid-In Capital
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3020 (batch 7)
