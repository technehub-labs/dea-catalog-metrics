# dea:metric-guideline-pre-trade-compliance-coverage

Candidate Performance Metric record for **Guideline Pre-Trade Compliance Coverage** (GPTCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-guideline-pre-trade-compliance-coverage`
- **Name:** Guideline Pre-Trade Compliance Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GPTCC

## 2. Definition

Within Investment Management - Portfolio Operations, Guideline Pre-Trade Compliance Coverage (GPTCC) is used to gauge exposure to adverse outcomes. The formula is Orders Screened Pre-Trade / Orders - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Financial Services sector.

## 3. Context

Measures the share of orders checked against mandate rules before execution. Pre-trade checks are the difference between preventing breaches and reporting them. Coverage that exempts hard-to-model derivatives leaves the complex exposures unchecked. Read with mandate compliance breach count and best execution compliance rate.

## Formula

```
Orders Screened Pre-Trade / Orders
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3027 (batch 7)
