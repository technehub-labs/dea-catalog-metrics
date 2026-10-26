# dea:metric-product-usage-frequency

Candidate Performance Metric record for **Product Usage Frequency** (PUF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-product-usage-frequency`
- **Name:** Product Usage Frequency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PUF

## 2. Definition

A Customer Success (B2B SaaS) indicator, Product Usage Frequency (PUF) quantifies the engagement or satisfaction of the people involved. It is defined as Active Usage Days / Eligible Days per Account; the result is stated in percent (%). In Software & SaaS, it is a recognized element of the standard performance toolkit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures how often active customers use the product in a period. It matters because frequency is the behavioral backbone of retention and expansion economics. Frequency can be inflated by counting trivial or automated events as usage. Read with Daily/Weekly Active Users depth and Customer Health Score to confirm frequent use is deep, valuable use.

## Formula

```
Active Usage Days / Eligible Days per Account
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 584 (batch 2)
