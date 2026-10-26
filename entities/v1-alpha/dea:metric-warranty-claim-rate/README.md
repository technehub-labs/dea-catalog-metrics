# dea:metric-warranty-claim-rate

Candidate Performance Metric record for **Warranty Claim Rate** (WCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-warranty-claim-rate`
- **Name:** Warranty Claim Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WCR

## 2. Definition

A Quality Management indicator, Warranty Claim Rate (WCR) quantifies exposure to adverse outcomes. It is defined as Warranty Claims / Units Sold; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Claims made under warranty as a share of units sold or in their service period - the field-failure rate that eventually corroborates or contradicts the factory's internal quality metrics. Its strategic significance is the long shadow it casts: claims arrive with a lag of months to years, which makes the rate both an early warning that survives long after the product has shipped and a backward confirmation of development and manufacturing decisions. Financially it drives the warranty reserve, a liability whose adequacy is a standing audit issue - reserving that lags a rising claim curve builds a earnings cliff into future quarters. The honest read is by cohort and failure mode: a rising rate concentrated in one production period points to a specific manufacturing excursion, while a broad rise points to design or supplier degradation.

## Formula

```
Warranty Claims / Units Sold
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 237 (batch 1)
