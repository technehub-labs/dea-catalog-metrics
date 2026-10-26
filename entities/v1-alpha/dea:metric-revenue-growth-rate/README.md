# dea:metric-revenue-growth-rate

Candidate Performance Metric record for **Revenue Growth Rate** (RGR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-revenue-growth-rate`
- **Name:** Revenue Growth Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RGR

## 2. Definition

Within Finance & Accounting, Revenue Growth Rate (RGR) is used to gauge growth over time. Its calculation is (Revenue_current - Revenue_prior) / Revenue_prior, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Period-over-period change in the top line - the first question in every equity story and the denominator of every compounding argument. Strategically it matters less as a number than as a decomposition: price versus volume, organic versus acquired, existing customers versus new, and which of those is durable. Ten percent growth built on price rises in a flat market is a different risk than ten percent built on new-customer acquisition, and acquired growth stops the moment the checkbook closes. The rate also self-decodes through the law of large numbers - sustaining it gets structurally harder as the base grows - so judge growth against the addressable market remaining, not just the trailing rate.

## Formula

```
(Revenue_current - Revenue_prior) / Revenue_prior
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 27 (batch 1)
