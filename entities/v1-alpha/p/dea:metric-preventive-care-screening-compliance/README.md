# dea:metric-preventive-care-screening-compliance

Candidate Performance Metric record for **Preventive Care Screening Compliance** (PCSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-preventive-care-screening-compliance`
- **Name:** Preventive Care Screening Compliance
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCSC

## 2. Definition

A Medical Practice & Clinical Operations indicator, Preventive Care Screening Compliance (PCSC) quantifies the quality of outputs and outcomes. It is defined as Eligible Patients Screened per Guideline / Eligible; the result is stated in percent (%). In Healthcare, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures completion of recommended screenings - cancer, diabetes, cardiovascular - across the eligible patient population. Preventive screening is where clinical quality and economics align most cleanly: late-stage diagnoses cost multiples of early ones in both money and life years. Risk adjustment matters, since populations with access barriers under-screen for structural reasons that blaming providers obscures. Read with population health panels and no-show or outreach completion rates.

## Formula

```
PCSC = Eligible Patients Screened per Guideline / Eligible
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1635 (batch 6)
