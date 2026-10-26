# dea:metric-payment-exception-rate

Candidate Performance Metric record for **Payment Exception Rate** (PER-AP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payment-exception-rate`
- **Name:** Payment Exception Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PER-AP

## 2. Definition

Payment Exception Rate (PER-AP) addresses the quality of outputs and outcomes and is a fixture of accounts payable & receivable operations (deep dive) reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Payments Requiring Manual Exception Handling / Payments - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Payments Requiring Manual Exception Handling / Payments
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** accounts_payable_receivable_operations_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3812 (batch 8)
