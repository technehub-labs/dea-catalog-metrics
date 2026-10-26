# dea:metric-error-budget-policy-enforcement-rate

Candidate Performance Metric record for **Error Budget Policy Enforcement Rate** (EBPER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-error-budget-policy-enforcement-rate`
- **Name:** Error Budget Policy Enforcement Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EBPER

## 2. Definition

Error Budget Policy Enforcement Rate (EBPER) addresses conformance to standards, plans, or obligations and is a fixture of observability & site reliability engineering reporting. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Releases Paused when Budget Exhausted / Exhaustion Events - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how consistently the agreed consequence (feature freezes, reliability sprints) triggers when budgets are exhausted. Policies without enforcement teach teams the budget is optional. Enforcement measured as notification rather than action is theater. Read with error budget consumption rate and toil reduction rate.

## Formula

```
Releases Paused when Budget Exhausted / Exhaustion Events
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2862 (batch 7)
