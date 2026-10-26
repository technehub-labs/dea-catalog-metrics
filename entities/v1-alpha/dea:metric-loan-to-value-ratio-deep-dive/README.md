# dea:metric-loan-to-value-ratio-deep-dive

Candidate Performance Metric record for **Loan-to-Value Ratio (Deep Dive)** (LTVDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-loan-to-value-ratio-deep-dive`
- **Name:** Loan-to-Value Ratio (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LTVDD

## 2. Definition

Within Real Estate & Mortgage Standard Measures, Loan-to-Value Ratio (Deep Dive) (LTVDD) is used to gauge exposure to adverse outcomes. It is defined as Loan Amount / Appraised Property Value; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Real estate, it is a recognized element of the standard performance toolkit.

## 3. Context

Measures the loan as a share of collateral value. LTV is the primary security cushion in secured lending. Valuations from peak-cycle appraisals make LTV comfort false. Read with combined loan-to-value ratio and collateral coverage ratio.

## Formula

```
LTVDD = Loan Amount / Appraised Property Value
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4215 (batch 10)
