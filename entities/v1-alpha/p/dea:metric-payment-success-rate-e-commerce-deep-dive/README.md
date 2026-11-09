# dea:metric-payment-success-rate-e-commerce-deep-dive

Candidate Performance Metric record for **Payment Success Rate (E-commerce Deep Dive)** (PSR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payment-success-rate-e-commerce-deep-dive`
- **Name:** Payment Success Rate (E-commerce Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PSR-D

## 2. Definition

Payment Success Rate (E-commerce Deep Dive) (PSR-D) measures the quality of outputs and outcomes in the Payments & Cards (Deep Dive) domain. The formula is Settled Payments / Initiated Payments - reported in percent (%). It is a standard measure in the Payments sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of checkout attempts that complete as paid orders. It is the conversion plumbing of e-commerce: failed payments are abandoned revenue invisible to marketing analytics, and failure rates vary sharply by geography, method, and acquirer routing. Retry logic and smart routing move the number materially. Read with authorization approval rate (Deep Dive) and method-mix effects by market.

## Formula

```
PSR-D = Settled Payments / Initiated Payments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2091 (batch 6)
