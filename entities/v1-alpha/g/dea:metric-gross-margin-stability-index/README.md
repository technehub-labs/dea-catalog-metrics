# dea:metric-gross-margin-stability-index

Candidate Performance Metric record for **Gross Margin Stability Index** (GMSI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-gross-margin-stability-index`
- **Name:** Gross Margin Stability Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GMSI

## 2. Definition

Gross Margin Stability Index (GMSI) captures exposure to adverse outcomes for organizations tracking balanced scorecard - financial perspective. Its calculation is Variance of Gross Margin around Trend, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the variance of gross margins over time. Stability signals pricing power and disciplined discounting; volatile margins reveal commodity exposure or weak price control. Stability achieved through cost deferrals eventually breaks. Read with pricing power index and operating margin trend.

## Formula

```
GMSI = Variance of Gross Margin around Trend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_financial_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3057 (batch 7)
