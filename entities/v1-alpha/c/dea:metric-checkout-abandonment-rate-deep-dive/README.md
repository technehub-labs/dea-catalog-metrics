# dea:metric-checkout-abandonment-rate-deep-dive

Candidate Performance Metric record for **Checkout Abandonment Rate (Deep Dive)** (CARD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-checkout-abandonment-rate-deep-dive`
- **Name:** Checkout Abandonment Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CARD

## 2. Definition

Checkout Abandonment Rate (Deep Dive) (CARD) measures the retention of customers, users, or assets over time in the Web & Digital Analytics Standard Measures domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Carts Abandoned before Purchase / Carts Created; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Digital product, it is a recognized element of the standard performance toolkit.

## Formula

```
CARD = Carts Abandoned before Purchase / Carts Created
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** retention
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** web_digital_analytics_standard_measures
- **Sector:** digital_product

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4361 (batch 11)
