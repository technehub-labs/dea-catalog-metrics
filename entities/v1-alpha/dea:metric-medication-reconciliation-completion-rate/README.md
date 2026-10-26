# dea:metric-medication-reconciliation-completion-rate

Candidate Performance Metric record for **Medication Reconciliation Completion Rate** (MRCHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-medication-reconciliation-completion-rate`
- **Name:** Medication Reconciliation Completion Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MRCHR

## 2. Definition

Medication Reconciliation Completion Rate (MRCHR) captures exposure to adverse outcomes for organizations tracking healthcare quality & patient safety standard measures. It is a working-level control: thresholds trigger immediate operational response. It is defined as Admissions with Reconciliation Completed / Admissions; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. In Healthcare, it is a recognized element of the standard performance toolkit.

## Formula

```
Admissions with Reconciliation Completed / Admissions
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4247 (batch 10)
