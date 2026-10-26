# dea:metric-payment-run-error-rate

Candidate Performance Metric record for **Payment Run Error Rate** (PER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-payment-run-error-rate`
- **Name:** Payment Run Error Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PER

## 2. Definition

Within Treasury & Cash Management, Payment Run Error Rate (PER) is used to gauge the quality of outputs and outcomes. The formula is Failed or Rejected Payments / Payments Initiated - reported in percent (%). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Failed or Rejected Payments / Payments Initiated
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
- **Domain:** treasury_cash_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 603 (batch 2)
