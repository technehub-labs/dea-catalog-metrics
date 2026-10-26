# dea:metric-payment-reconciliation-break-rate

Candidate Performance Metric record for **Payment Reconciliation Break Rate** (PRBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payment-reconciliation-break-rate`
- **Name:** Payment Reconciliation Break Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PRBR

## 2. Definition

Payment Reconciliation Break Rate (PRBR) measures the quality of outputs and outcomes in the Payments & Fintech domain. It is defined as Unreconciled Items / Transactions Processed; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Lower values are better; each reduction is an improvement. In Payments & fintech, it is a recognized element of the standard performance toolkit.

## Formula

```
Unreconciled Items / Transactions Processed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** payments_fintech
- **Sector:** payments_fintech

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 780 (batch 2)
