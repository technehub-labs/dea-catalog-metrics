# dea:metric-budget-variance

Candidate Performance Metric record for **Budget Variance** (BV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-budget-variance`
- **Name:** Budget Variance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BV

## 2. Definition

Budget Variance (BV) addresses conformance to standards, plans, or obligations and is a fixture of finance & accounting reporting. It is defined as (Actual Spend - Budgeted Spend) / Budgeted Spend; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the gap between budgeted and actual spending or revenue for a period. It matters as the primary control signal for cost discipline and forecasting quality. Managers can game it through conservative budget padding or by shifting expenses across cost centers or periods. Read with Plan Accuracy and Budget Attainment to tell honest misses from sandbagged baselines.

## Formula

```
(Actual Spend - Budgeted Spend) / Budgeted Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 29 (batch 1)
