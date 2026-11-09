# dea:metric-ed-length-of-stay-median

Candidate Performance Metric record for **ED Length of Stay (Median)** (EDLOS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ed-length-of-stay-median`
- **Name:** ED Length of Stay (Median)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EDLOS

## 2. Definition

A Healthcare Quality & Patient Safety Standard Measures indicator, ED Length of Stay (Median) (EDLOS) quantifies how efficiently resources are converted into outputs. It is computed as Median Time from ED Arrival to Discharge or Admission, expressed in hours. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Healthcare.

## Formula

```
EDLOS = Median Time from ED Arrival to Discharge or Admission
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4243 (batch 10)
