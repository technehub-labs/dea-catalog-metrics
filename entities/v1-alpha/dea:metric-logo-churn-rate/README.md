# dea:metric-logo-churn-rate

Candidate Performance Metric record for **Logo Churn Rate** (LogoChurn) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-logo-churn-rate`
- **Name:** Logo Churn Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LogoChurn

## 2. Definition

A Customer Success (B2B SaaS) indicator, Logo Churn Rate (LogoChurn) quantifies exposure to adverse outcomes. Its calculation is Customers Lost / Customers at Start of Period, measured in percent (%). It originates from and is most used in Software & SaaS practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

The share of customer accounts lost in a period - the people-counting companion to revenue churn, and the metric that keeps the human story visible inside the financial one. Its strategic significance is the small-customer honesty it enforces: MRR-based churn is dominated by big accounts, so a revenue metric can improve while the customer base quietly disintegrates - a pattern that looks fine until the mid-market pipeline thins and the concentration risk in the remaining giants is revealed. Read logo churn by segment: small-logo churn is usually a product-deliverability and onboarding problem (self-service did not activate them), while enterprise logo churn is a renewal-cycle and relationship problem. The metric also anchors the lifetime-value arithmetic that growth spending is justified against, since logo survival is what turns CAC into LTV.

## Formula

```
Customers Lost / Customers at Start of Period
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 579 (batch 2)
