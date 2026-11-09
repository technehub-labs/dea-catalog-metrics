# dea:metric-graduation-rate-deep-dive

Candidate Performance Metric record for **Graduation Rate (Deep Dive)** (GRDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-graduation-rate-deep-dive`
- **Name:** Graduation Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** GRDD

## 2. Definition

Graduation Rate (Deep Dive) (GRDD) captures the quality of outputs and outcomes for organizations tracking education & training outcome standard measures. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Cohort Completing within 150% of Program Time / Cohort - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Education sector.

## 3. Context

Measures the share of entrants completing their program within a defined window. It is the headline outcome measure of educational effectiveness. Rates computed on retained students rather than entrants overstate. Read with first-year retention rate (Cohort) and time-to-degree (Median).

## Formula

```
GRDD = Cohort Completing within 150% of Program Time / Cohort
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** education_training_outcome_standard_measures
- **Sector:** education

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4395 (batch 11)
