# dea:metric-portfolio-turnover-ratio-deep-dive

Candidate Performance Metric record for **Portfolio Turnover Ratio (Deep Dive)** (PTR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-turnover-ratio-deep-dive`
- **Name:** Portfolio Turnover Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PTR-D

## 2. Definition

Within Asset & Wealth Management (Deep Dive), Portfolio Turnover Ratio (Deep Dive) (PTR-D) is used to gauge how efficiently resources are converted into outputs. Its calculation is Min(Purchases, Sales) / Average AUM, measured in percent (%). It originates from and is most used in Financial Services practice. Its value drives prioritization and resource reallocation among competing initiatives. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Min(Purchases, Sales) / Average AUM
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** asset_wealth_management_deep_dive
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2106 (batch 6)
