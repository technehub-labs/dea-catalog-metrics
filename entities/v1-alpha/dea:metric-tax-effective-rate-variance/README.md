# dea:metric-tax-effective-rate-variance

Candidate Performance Metric record for **Tax Effective Rate Variance** (TERV-BSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-tax-effective-rate-variance`
- **Name:** Tax Effective Rate Variance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TERV-BSC

## 2. Definition

A Balanced Scorecard - Financial Perspective indicator, Tax Effective Rate Variance (TERV-BSC) quantifies conformance to standards, plans, or obligations. The formula is Effective Tax Rate - Plan / Plan - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
TERV-BSC = Effective Tax Rate - Plan / Plan
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** strategy
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** balanced_scorecard_financial_perspective

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3064 (batch 7)
