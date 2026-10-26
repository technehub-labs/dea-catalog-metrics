# dea:metric-discount-leakage

Candidate Performance Metric record for **Discount Leakage** (DLK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-discount-leakage`
- **Name:** Discount Leakage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DLK

## 2. Definition

A Pricing & Revenue Management indicator, Discount Leakage (DLK) quantifies the economic value created or preserved. Its calculation is Discount Value Granted outside Policy / Gross Sales Value, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Discount leakage measures price erosion beyond policy-approved discounts - the gap between the intended price architecture and what invoices actually carry - and it is the pure control-failure metric of pricing governance. Leakage differs from discounting: discounts are a legitimate tool, leakage is deviation from the rules that govern them (stacked discounts, expired discounts applied, off-invoice concessions, untracked rebates). The sum is often enormous - pricing consultancies routinely find 1-3 percent of revenue lost to leakage in complex businesses, which flows almost entirely to margin because the cost base does not shrink when price does. Root-cause distribution is the actionable view: system-configuration errors, sales override tolerance, and customer-capture errors are different problems. Read with price-realization rate as the aggregate, exception-approval volume and outcome, and recovery of identified leakage (leakage found but not fixed is a governance failure).

## Formula

```
Discount Value Granted outside Policy / Gross Sales Value
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1065 (batch 4)
