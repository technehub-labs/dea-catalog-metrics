# dea:metric-interest-expense-ratio

Candidate Performance Metric record for **Interest Expense Ratio** (IER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-interest-expense-ratio`
- **Name:** Interest Expense Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IER

## 2. Definition

Interest Expense Ratio (IER) captures how efficiently resources are converted into outputs for organizations tracking treasury & cash management. Its calculation is Interest Expense / Total Debt, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures interest expense as a share of revenue or operating income. It matters because it reveals how much of operating performance is consumed by financing cost. Capitalizing interest during build periods can suppress the ratio temporarily. Read with Interest Coverage Ratio and Weighted Average Cost of Capital to see whether the financing structure is the real issue.

## Formula

```
Interest Expense / Total Debt
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 601 (batch 2)
