# dea:metric-student-to-faculty-ratio-standard

Candidate Performance Metric record for **Student-to-Faculty Ratio (Standard)** (STFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-student-to-faculty-ratio-standard`
- **Name:** Student-to-Faculty Ratio (Standard)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** STFR

## 2. Definition

A Education & Training Outcome Standard Measures indicator, Student-to-Faculty Ratio (Standard) (STFR) quantifies the utilization or availability of capacity. Its calculation is Enrolled Students / Full-Time Faculty, measured in ratio (x:1 or x). It originates from and is most used in Education practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures students per faculty member. It is the crudest resource-intensity proxy in education. Ratios including non-teaching research faculty misrepresent classroom reality. Read with class size distribution and instructional cost per student.

## Formula

```
STFR = Enrolled Students / Full-Time Faculty
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** organization
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** education_training_outcome_standard_measures
- **Sector:** education

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4401 (batch 11)
