# dea:metric-instant-payment-adoption-rate

Candidate Performance Metric record for **Instant Payment Adoption Rate** (IPAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-instant-payment-adoption-rate`
- **Name:** Instant Payment Adoption Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IPAR

## 2. Definition

A Payments & Cards (Deep Dive) indicator, Instant Payment Adoption Rate (IPAR) quantifies growth over time. The formula is Instant Payment Volume / Total Payment Volume - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Payments sector.

## 3. Context

Measures the share of transaction volume on instant payment rails. Instant rails compress settlement, improve cash flow for recipients, and displace card and transfer fees in many corridors, so adoption is both an efficiency and a competitiveness metric. Adoption without fraud controls for irrevocable payments is a risk transfer, not progress. Read with payment fraud rates on instant rails and treasury settlement-cycle improvements.

## Formula

```
Instant Payment Volume / Total Payment Volume
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** growth
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2092 (batch 6)
