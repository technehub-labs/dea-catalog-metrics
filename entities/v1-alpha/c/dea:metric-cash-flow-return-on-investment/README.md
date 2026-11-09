# dea:metric-cash-flow-return-on-investment

Candidate Performance Metric record for **Cash Flow Return on Investment** (CFROI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-flow-return-on-investment`
- **Name:** Cash Flow Return on Investment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CFROI

## 2. Definition

Cash Flow Return on Investment (CFROI) captures the economic value created or preserved for organizations tracking balanced scorecard - financial perspective. Its calculation is Cash Flow / Invested Capital, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures cash operating returns relative to invested capital. CFROI is harder to manipulate than earnings-based measures because it follows cash rather than accounting judgments. It requires estimation-heavy asset life and inflation adjustments. Read with free cash flow margin and return on capital employed.

## Formula

```
CFROI = Cash Flow / Invested Capital
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_financial_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3056 (batch 7)
