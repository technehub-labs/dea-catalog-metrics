# dea:metric-clinical-trial-enrollment-rate

Candidate Performance Metric record for **Clinical Trial Enrollment Rate** (CTER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-clinical-trial-enrollment-rate`
- **Name:** Clinical Trial Enrollment Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CTER

## 2. Definition

A Pharmaceuticals & Life Sciences indicator, Clinical Trial Enrollment Rate (CTER) quantifies how efficiently resources are converted into outputs. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Enrolled Subjects / Planned Subjects, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Pharmaceuticals practice.

## 3. Context

Measures enrolled subjects against the planned enrollment curve. It matters because enrollment is the pacing item of trial timelines, and slow trials burn patent life. Teams can inflate it by enrolling poorly matched subjects to hit numbers, risking data quality and protocol deviations. Read with Screen Failure Rate and Protocol Deviation counts to confirm enrollment speed is not bought with subject quality.

## Formula

```
Enrolled Subjects / Planned Subjects
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmaceuticals_life_sciences
- **Sector:** pharmaceuticals

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 484 (batch 1)
