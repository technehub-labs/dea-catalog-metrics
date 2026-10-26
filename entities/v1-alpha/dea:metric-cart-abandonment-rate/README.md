# dea:metric-cart-abandonment-rate

Candidate Performance Metric record for **Cart Abandonment Rate** (CAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cart-abandonment-rate`
- **Name:** Cart Abandonment Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CAR

## 2. Definition

Within Retail & E-commerce, Cart Abandonment Rate (CAR) is used to gauge exposure to adverse outcomes. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Abandoned Carts / Carts Created, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Retail practice.

## 3. Context

Measures the share of initiated e-commerce checkouts that do not complete. It matters because abandoned carts represent warm demand lost to friction at the highest-intent moment. Teams can understate it by only counting logged-in users or hiding the metric behind simplified checkout steps that merely move friction earlier. Read with Conversion Rate (Retail) and Payment Failure Rate to locate whether price, shipping, or payment friction drives abandonment.

## Formula

```
Abandoned Carts / Carts Created
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 495 (batch 1)
