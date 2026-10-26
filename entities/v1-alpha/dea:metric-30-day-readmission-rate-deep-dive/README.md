# dea:metric-30-day-readmission-rate-deep-dive

Candidate Performance Metric record for **30-Day Readmission Rate (Deep Dive)** (R30DD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-30-day-readmission-rate-deep-dive`
- **Name:** 30-Day Readmission Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** R30DD

## 2. Definition

A Healthcare Quality & Patient Safety Standard Measures indicator, 30-Day Readmission Rate (Deep Dive) (R30DD) quantifies the quality of outputs and outcomes. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Readmissions within 30 Days / Discharges - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Healthcare sector.

## 3. Context

Measures the share of discharged patients readmitted within 30 days. Readmissions are the signature measure of discharge quality and care coordination, with payment penalties attached. Readmissions originating elsewhere can be excluded by attribution rules, honestly or otherwise. Read with average length of stay (Inpatient) and care transition compliance rate.

## Formula

```
Readmissions within 30 Days / Discharges
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** healthcare_quality_patient_safety_standard_measures
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4235 (batch 10)
