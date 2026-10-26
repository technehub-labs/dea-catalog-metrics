# dea:metric-expansion-revenue-rate-saas-deep-dive

Candidate Performance Metric record for **Expansion Revenue Rate (SaaS Deep Dive)** (ERR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-expansion-revenue-rate-saas-deep-dive`
- **Name:** Expansion Revenue Rate (SaaS Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ERR-D

## 2. Definition

Expansion Revenue Rate (SaaS Deep Dive) (ERR-D) addresses growth over time and is a fixture of software product operations (deep dive) reporting. It is defined as Expansion MRR / Starting MRR; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Technology, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures revenue growth from existing customers via upsell, cross-sell, seat growth, and price. It is the efficiency crown of SaaS economics: expansion revenue carries near-zero acquisition cost, and its share of growth separates efficient compounders from churn-limited treadmill businesses. Price-led expansion must be read with churn and contraction, since increases that drive exits can be net-negative. Read with net revenue retention and logo churn rate (Deep Dive).

## Formula

```
ERR-D = Expansion MRR / Starting MRR
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** growth
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** software_product_operations_deep_dive
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2157 (batch 6)
