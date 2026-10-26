# dea:metric-pricing-win-rate

Candidate Performance Metric record for **Pricing Win Rate** (PWR-P) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pricing-win-rate`
- **Name:** Pricing Win Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PWR-P

## 2. Definition

Pricing Win Rate (PWR-P) captures the economic value created or preserved for organizations tracking pricing & revenue management. It is computed as Deals Won at Target Price / Deals Won, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of deals won at target price without discount erosion. It matters because pricing discipline is the highest-margin revenue lever available. Teams can lift it by winning only easy deals, shrinking the denominator. Read with Price Realization and Discount Leakage trends to confirm wins carry profitable pricing.

## Formula

```
Deals Won at Target Price / Deals Won
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** pricing_revenue_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1067 (batch 4)
