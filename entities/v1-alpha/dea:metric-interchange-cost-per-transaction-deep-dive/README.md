# dea:metric-interchange-cost-per-transaction-deep-dive

Candidate Performance Metric record for **Interchange Cost per Transaction (Deep Dive)** (ICPT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-interchange-cost-per-transaction-deep-dive`
- **Name:** Interchange Cost per Transaction (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ICPT-D

## 2. Definition

A Payments & Cards (Deep Dive) indicator, Interchange Cost per Transaction (Deep Dive) (ICPT-D) quantifies how efficiently resources are converted into outputs. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Interchange Fees / Transactions, measured in currency per unit. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Payments practice.

## Formula

```
Interchange Fees / Transactions
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2093 (batch 6)
