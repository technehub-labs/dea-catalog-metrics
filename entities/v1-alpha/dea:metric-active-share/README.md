# dea:metric-active-share

Candidate Performance Metric record for **Active Share** (ACTSH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-active-share`
- **Name:** Active Share
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACTSH

## 2. Definition

Within Investment Management - Portfolio Operations, Active Share (ACTSH) is used to gauge exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Non-Overlapping Portfolio Weight / Total, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. It originates from and is most used in Financial Services practice.

## 3. Context

Measures the percentage of a portfolio that differs from its benchmark holdings. Active share identifies closet indexers charging active fees, a core due diligence screen. High active share alone is not skill: it means different, not better. Read with tracking error and fund expense ratio trend.

## Formula

```
ACTSH = Non-Overlapping Portfolio Weight / Total
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3005 (batch 7)
