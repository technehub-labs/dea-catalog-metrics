# dea:metric-falls-with-injury-rate

Candidate Performance Metric record for **Falls with Injury Rate** (FWIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-falls-with-injury-rate`
- **Name:** Falls with Injury Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FWIR

## 2. Definition

Falls with Injury Rate (FWIR) addresses exposure to adverse outcomes and is a fixture of healthcare quality & patient safety standard measures reporting. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Falls Causing Injury / 1,000 Patient Days - reported in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Healthcare sector.

## Formula

```
Falls Causing Injury / 1,000 Patient Days
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4249 (batch 10)
