# dea:metric-underwriting-exception-rate-mortgage

Candidate Performance Metric record for **Underwriting Exception Rate (Mortgage)** (UERM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-underwriting-exception-rate-mortgage`
- **Name:** Underwriting Exception Rate (Mortgage)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** UERM

## 2. Definition

Underwriting Exception Rate (Mortgage) (UERM) measures exposure to adverse outcomes in the Real Estate & Mortgage Standard Measures domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Loans with Approved Underwriting Exception / Loans; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. In Real estate, it is a recognized element of the standard performance toolkit.

## Formula

```
Loans with Approved Underwriting Exception / Loans
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** real_estate_mortgage_standard_measures
- **Sector:** real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4232 (batch 10)
