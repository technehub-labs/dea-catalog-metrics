# dea:metric-portfolio-turnover-investment-deep-dive

Candidate Performance Metric record for **Portfolio Turnover (Investment Deep Dive)** (PTID) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-portfolio-turnover-investment-deep-dive`
- **Name:** Portfolio Turnover (Investment Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PTID

## 2. Definition

Portfolio Turnover (Investment Deep Dive) (PTID) measures how efficiently resources are converted into outputs in the Investment Management - Portfolio Operations domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Lesser of Purchases or Sales / Average NAV, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. It originates from and is most used in Financial Services practice.

## Formula

```
PTID = Lesser of Purchases or Sales / Average NAV
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3006 (batch 7)
