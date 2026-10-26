# dea:metric-duplicate-payment-rate

Candidate Performance Metric record for **Duplicate Payment Rate** (DUPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-duplicate-payment-rate`
- **Name:** Duplicate Payment Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DUPR

## 2. Definition

Within Accounts Payable & Receivable Operations (Deep Dive), Duplicate Payment Rate (DUPR) is used to gauge exposure to adverse outcomes. The formula is Duplicate Payments Detected / Payments Sampled - reported in events per thousand or million (scaled). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
DUPR = Duplicate Payments Detected / Payments Sampled
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3800 (batch 8)
