# dea:metric-interest-coverage-ratio

Candidate Performance Metric record for **Interest Coverage Ratio** (ICR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-interest-coverage-ratio`
- **Name:** Interest Coverage Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ICR

## 2. Definition

Interest Coverage Ratio (ICR) addresses exposure to adverse outcomes and is a fixture of finance & accounting reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is EBIT / Interest Expense, measured in ratio (x:1 or x). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how many times operating earnings cover interest expense. It matters as an early warning of debt-service stress before covenant breaches occur. EBIT can be inflated with one-off gains or capitalization choices, so a comfortable ratio may mask deteriorating cash coverage. Read with Debt to Equity Ratio and Cash Flow from Operations to confirm the earnings behind the coverage are real.

## Formula

```
ICR = EBIT / Interest Expense
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 20 (batch 1)
