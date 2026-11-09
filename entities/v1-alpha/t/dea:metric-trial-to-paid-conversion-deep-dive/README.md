# dea:metric-trial-to-paid-conversion-deep-dive

Candidate Performance Metric record for **Trial-to-Paid Conversion (Deep Dive)** (TTPC-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-trial-to-paid-conversion-deep-dive`
- **Name:** Trial-to-Paid Conversion (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TTPC-D

## 2. Definition

Trial-to-Paid Conversion (Deep Dive) (TTPC-D) addresses growth over time and is a fixture of software product operations (deep dive) reporting. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Paid Conversions / Trials; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Technology, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the share of product trials becoming paid subscriptions. It is the demand-side quality metric of product-led growth, and its integrity depends on trial design - long, feature-limited trials produce different conversion than short full-featured ones, so read with trial-type mix. Conversion without activation discipline buys low-intent customers who churn early. Read with activation rate (SaaS Deep Dive) and first-renewal retention of converted trials.

## Formula

```
TTPC-D = Paid Conversions / Trials
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2165 (batch 6)
