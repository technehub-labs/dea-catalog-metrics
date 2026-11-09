# dea:metric-advisory-model-portfolio-drift

Candidate Performance Metric record for **Advisory Model Portfolio Drift** (AMPD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-advisory-model-portfolio-drift`
- **Name:** Advisory Model Portfolio Drift
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AMPD

## 2. Definition

Advisory Model Portfolio Drift (AMPD) addresses conformance to standards, plans, or obligations and is a fixture of wealth management reporting. The formula is Client Allocations Deviating beyond Tolerance / Client Allocations - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Wealth management sector.

## Formula

```
AMPD = Client Allocations Deviating beyond Tolerance / Client Allocations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** wealth_management
- **Sector:** wealth_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1142 (batch 4)
