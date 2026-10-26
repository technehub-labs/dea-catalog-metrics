# dea:metric-repeat-purchase-rate

Candidate Performance Metric record for **Repeat Purchase Rate** (RPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-repeat-purchase-rate`
- **Name:** Repeat Purchase Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RPR

## 2. Definition

Repeat Purchase Rate (RPR) measures the retention of customers, users, or assets over time in the Customer domain. It is computed as Customers with >1 Purchase / Total Customers, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of customers who make more than one purchase in a period. It matters because repeat behavior is the practical evidence of product-market fit and cheaper growth than acquisition. It can be gamed by counting trivial add-on purchases or re-engagement discounts that buy the second order but not loyalty. Read with Customer Retention Rate and Average Order Value to check that repeats are profitable, not just frequent.

## Formula

```
Customers with >1 Purchase / Total Customers
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 79 (batch 1)
