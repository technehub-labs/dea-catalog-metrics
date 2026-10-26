# dea:metric-return-on-invested-capital

Candidate Performance Metric record for **Return on Invested Capital** (ROIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-return-on-invested-capital`
- **Name:** Return on Invested Capital
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ROIC

## 2. Definition

A Finance & Accounting indicator, Return on Invested Capital (ROIC) quantifies the economic value created or preserved. Its calculation is NOPAT / Invested Capital, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

NOPAT divided by invested capital (debt plus equity minus cash) - the return on all money put to work in the business. Its strategic weight comes from comparison with the weighted average cost of capital: a spread of ROIC over WACC is the arithmetic definition of value creation, and the size of that spread times reinvestment rate predicts long-run growth far better than earnings growth alone. It is harder to game than ROE because debt sits in the denominator, and harder to flatter than ROA because non-operating assets are stripped out. The main disputes are definitional - operating leases, goodwill, excess cash - so check the construction before trusting cross-source comparisons.

## Formula

```
NOPAT / Invested Capital
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
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 13 (batch 1)
