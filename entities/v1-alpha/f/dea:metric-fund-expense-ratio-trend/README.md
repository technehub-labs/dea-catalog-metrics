# dea:metric-fund-expense-ratio-trend

Candidate Performance Metric record for **Fund Expense Ratio Trend** (FERT-IM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fund-expense-ratio-trend`
- **Name:** Fund Expense Ratio Trend
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FERT-IM

## 2. Definition

Within Investment Management - Portfolio Operations, Fund Expense Ratio Trend (FERT-IM) is used to gauge how efficiently resources are converted into outputs. Its calculation is Total Expense Ratio Change per Year, measured in percent (%). It originates from and is most used in Financial Services practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the direction of total annual fund operating costs as a share of assets. Fees compound against returns relentlessly; a 1% gap reshapes long-horizon outcomes. Falling industry-wide index pricing makes stagnant fees a competitive warning. Read with active share and net revenue retention.

## Formula

```
FERT-IM = Total Expense Ratio Change per Year
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** investment_management_portfolio_operations
- **Sector:** financial_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3007 (batch 7)
