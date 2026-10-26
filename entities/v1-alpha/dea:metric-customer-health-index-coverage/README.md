# dea:metric-customer-health-index-coverage

Candidate Performance Metric record for **Customer Health Index Coverage** (CHIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-customer-health-index-coverage`
- **Name:** Customer Health Index Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CHIC

## 2. Definition

Within Customer Success (B2B SaaS), Customer Health Index Coverage (CHIC) is used to gauge conformance to standards, plans, or obligations. It is defined as Accounts with Current Health Score / Total Accounts; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Software & SaaS, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of accounts with a current health score. It matters because unscored accounts escape risk management and renewal preparation. Stale scores updated on a schedule can keep coverage green while signals age. Read with Churn Prediction Coverage and renewal outcomes to confirm scored accounts actually receive intervention.

## Formula

```
Accounts with Current Health Score / Total Accounts
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 587 (batch 2)
