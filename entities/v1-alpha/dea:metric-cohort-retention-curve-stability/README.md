# dea:metric-cohort-retention-curve-stability

Candidate Performance Metric record for **Cohort Retention Curve Stability** (CRCS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cohort-retention-curve-stability`
- **Name:** Cohort Retention Curve Stability
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CRCS

## 2. Definition

A Unit Economics & Growth (Deep Dive) indicator, Cohort Retention Curve Stability (CRCS) quantifies the quality of outputs and outcomes. The formula is Variance of Retention Curves across Cohorts - reported in index (0-100 or normalized). It is a standard measure in the Software sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures how consistently retention curves flatten at a predictable plateau. Stable plateaus make LTV modelable and expansion plannable. Curves compared across periods with different acquisition mixes mislead. Read with customer lifetime value (Deep Dive) and logo churn rate (Unit Economics).

## Formula

```
Variance of Retention Curves across Cohorts
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** unit_economics_growth_deep_dive
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4164 (batch 9)
