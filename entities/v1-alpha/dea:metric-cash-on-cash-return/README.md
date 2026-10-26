# dea:metric-cash-on-cash-return

Candidate Performance Metric record for **Cash-on-Cash Return** (COCR-RE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cash-on-cash-return`
- **Name:** Cash-on-Cash Return
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** COCR-RE

## 2. Definition

Cash-on-Cash Return (COCR-RE) measures the economic value created or preserved in the Real Estate & Mortgage Standard Measures domain. Its calculation is Pre-Tax Cash Flow / Cash Invested, measured in percent (%). It originates from and is most used in Real estate practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures annual pre-tax cash flow relative to equity invested. It is the investor's realized yield on actual cash in the deal. Returns computed with refinance proceeds in the denominator are creative. Read with capitalization rate and equity multiple (investment).

## Formula

```
COCR-RE = Pre-Tax Cash Flow / Cash Invested
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** real_estate_mortgage_standard_measures
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4219 (batch 10)
