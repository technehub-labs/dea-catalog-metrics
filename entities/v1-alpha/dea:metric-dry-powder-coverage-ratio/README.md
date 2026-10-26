# dea:metric-dry-powder-coverage-ratio

Candidate Performance Metric record for **Dry Powder Coverage Ratio** (DPCR-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dry-powder-coverage-ratio`
- **Name:** Dry Powder Coverage Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DPCR-IM

## 2. Definition

Dry Powder Coverage Ratio (DPCR-IM) measures the utilization or availability of capacity in the Investment Management - Portfolio Operations domain. Its calculation is Available Uncalled Capital / Planned Investments, measured in ratio (x:1 or x). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It originates from and is most used in Financial Services practice.

## 3. Context

Measures available committed capital relative to expected near-term deployment needs. It answers whether the fund can act on the deals it wants without emergency measures. Excess dry powder pushes managers toward marginal deals to deploy. Read with uninvested commitment ratio and investment pacing variance.

## Formula

```
DPCR-IM = Available Uncalled Capital / Planned Investments
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3022 (batch 7)
