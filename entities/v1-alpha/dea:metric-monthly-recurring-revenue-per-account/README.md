# dea:metric-monthly-recurring-revenue-per-account

Candidate Performance Metric record for **Monthly Recurring Revenue per Account** (MRRA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-monthly-recurring-revenue-per-account`
- **Name:** Monthly Recurring Revenue per Account
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MRRA

## 2. Definition

Monthly Recurring Revenue per Account (MRRA) addresses the economic value created or preserved and is a fixture of customer success (b2b saas) reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as MRR / Active Accounts; the result is stated in currency per unit. Improvement means raising this figure toward best-in-class levels. In Software & SaaS, it is a recognized element of the standard performance toolkit.

## 3. Context

Recurring revenue divided by account count - the average-account-value metric of the subscription base, and the number that describes what kind of customer the business actually serves, whatever the positioning says. Its strategic significance is segment honesty: the average reveals whether the product is a enterprise tool with a few large accounts or a mass self-serve product with many small ones, and the trend tracks the deliberate movement between those models - mid-market focus, upmarket migration, or downmarket expansion all show here first. The distribution matters more than the mean: subscription revenue concentrates heavily, so a rising average can be one whale landing rather than a broad segment shift, and the median alongside the mean is the honesty check. Read with segment-margin data: a customer tier whose MRR per account grows while its service cost grows faster is scaling the wrong way.

## Formula

```
MRR / Active Accounts
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_success_b2b_saas
- **Sector:** software_saas

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 589 (batch 2)
