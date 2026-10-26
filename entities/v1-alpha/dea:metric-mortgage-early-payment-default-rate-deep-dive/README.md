# dea:metric-mortgage-early-payment-default-rate-deep-dive

Candidate Performance Metric record for **Mortgage Early Payment Default Rate (Deep Dive)** (MEPDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mortgage-early-payment-default-rate-deep-dive`
- **Name:** Mortgage Early Payment Default Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MEPDR

## 2. Definition

Mortgage Early Payment Default Rate (Deep Dive) (MEPDR) measures exposure to adverse outcomes in the Real Estate & Mortgage Standard Measures domain. The formula is Defaults within 24 Months of Origination / Loans Originated - reported in percent (%). It is a standard measure in the Real estate sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures defaults occurring within months of loan origination. Early payment default is the classic marker of bad underwriting or fraud. EPD measured from funding rather than first payment start understates. Read with vintage default emergence curve and probability of default (Deep Dive).

## Formula

```
Defaults within 24 Months of Origination / Loans Originated
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** real_estate_mortgage_standard_measures
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4231 (batch 10)
