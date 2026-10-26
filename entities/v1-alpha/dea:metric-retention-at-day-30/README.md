# dea:metric-retention-at-day-30

Candidate Performance Metric record for **Retention at Day 30** (R30) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-retention-at-day-30`
- **Name:** Retention at Day 30
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** R30

## 2. Definition

Within Product Management, Retention at Day 30 (R30) is used to gauge the retention of customers, users, or assets over time. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Users Active on Day 30 / Users in Cohort; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

The share of a new-user cohort still active thirty days after signup - the early-retention checkpoint that became the industry's standard onboarding verdict, and strategically the cheapest quality signal available: acquiring users is a marketing cost, but users acquired who leave within a month were paid for and never delivered. Its significance is diagnostic placement: day-30 sits past the novelty window but before habit maturity, so failure here points at activation and initial-value delivery rather than at long-term satisfaction. The benchmark reality is category-bound: 30-day retention varies several-fold across utility, content, and social categories, and the honest read is the retention curve, not the single checkpoint - a curve that flattens early at a low level is a different product problem from one that decays smoothly, and the remedies differ completely.

## Formula

```
R30 = Users Active on Day 30 / Users in Cohort
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** retention
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 558 (batch 1)
