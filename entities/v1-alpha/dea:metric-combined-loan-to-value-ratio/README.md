# dea:metric-combined-loan-to-value-ratio

Candidate Performance Metric record for **Combined Loan-to-Value Ratio** (CLTV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-combined-loan-to-value-ratio`
- **Name:** Combined Loan-to-Value Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CLTV

## 2. Definition

A Real Estate & Mortgage Standard Measures indicator, Combined Loan-to-Value Ratio (CLTV) quantifies exposure to adverse outcomes. It is defined as All Secured Debt / Property Value; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Real estate, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures all liens against the property relative to its value. CLTV exposes the equity cushion when second liens exist. Silent junior liens not on the lender's books distort CLTV. Read with loan-to-value ratio (Deep Dive) and debt service coverage ratio (Property Investment).

## Formula

```
All Secured Debt / Property Value
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4216 (batch 10)
