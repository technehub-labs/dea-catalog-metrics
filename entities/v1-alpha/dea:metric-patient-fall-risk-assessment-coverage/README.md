# dea:metric-patient-fall-risk-assessment-coverage

Candidate Performance Metric record for **Patient Fall Risk Assessment Coverage** (PFRAC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patient-fall-risk-assessment-coverage`
- **Name:** Patient Fall Risk Assessment Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PFRAC

## 2. Definition

Patient Fall Risk Assessment Coverage (PFRAC) captures exposure to adverse outcomes for organizations tracking healthcare quality & patient safety standard measures. The formula is Admissions Screened for Fall Risk within Policy Window / Admissions - reported in percent (%). It is a standard measure in the Healthcare sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Admissions Screened for Fall Risk within Policy Window / Admissions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4253 (batch 10)
