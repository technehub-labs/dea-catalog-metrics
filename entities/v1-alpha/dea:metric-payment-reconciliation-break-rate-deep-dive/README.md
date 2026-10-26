# dea:metric-payment-reconciliation-break-rate-deep-dive

Candidate Performance Metric record for **Payment Reconciliation Break Rate (Deep Dive)** (PRBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payment-reconciliation-break-rate-deep-dive`
- **Name:** Payment Reconciliation Break Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PRBR

## 2. Definition

Within Payments & Cards (Deep Dive), Payment Reconciliation Break Rate (Deep Dive) (PRBR) is used to gauge the quality of outputs and outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Unmatched Items / Reconciled Items, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Payments practice.

## Formula

```
Unmatched Items / Reconciled Items
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** payments_cards_deep_dive
- **Sector:** payments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2101 (batch 6)
