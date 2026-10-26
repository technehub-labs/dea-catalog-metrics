# dea:metric-price-protection-payout-ratio

Candidate Performance Metric record for **Price Protection Payout Ratio** (PPPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-price-protection-payout-ratio`
- **Name:** Price Protection Payout Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PPPR

## 2. Definition

A Channel & Distribution Management indicator, Price Protection Payout Ratio (PPPR) quantifies the economic value created or preserved. It provides the day-to-day signal that a process is running as designed. Its calculation is Price Protection Claims Paid / Claims Assessed, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Price Protection Claims Paid / Claims Assessed
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** channel_distribution_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3981 (batch 8)
