# dea:metric-bad-debt-expense-ratio

Candidate Performance Metric record for **Bad Debt Expense Ratio** (BDER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bad-debt-expense-ratio`
- **Name:** Bad Debt Expense Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BDER

## 2. Definition

Bad Debt Expense Ratio (BDER) captures exposure to adverse outcomes for organizations tracking accounts payable & receivable operations (deep dive). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Bad Debt Write-Offs / Credit Sales, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures receivables written off relative to credit sales. Bad debt is the price of credit policy and collection failure in one number. Ratios falling through tighter credit that chokes sales are not pure improvement. Read with expected loss rate (Deep Dive) and collections effectiveness index.

## Formula

```
Bad Debt Write-Offs / Credit Sales
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3808 (batch 8)
