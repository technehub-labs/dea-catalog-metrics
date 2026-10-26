# dea:metric-hospital-readmission-rate-deep-dive

Candidate Performance Metric record for **Hospital Readmission Rate (Deep Dive)** (HRR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hospital-readmission-rate-deep-dive`
- **Name:** Hospital Readmission Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HRR-D

## 2. Definition

Within Medical Practice & Clinical Operations, Hospital Readmission Rate (Deep Dive) (HRR-D) is used to gauge the quality of outputs and outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Readmissions within 30 Days / Discharges, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Healthcare practice.

## 3. Context

Measures unplanned returns within a window (often 30 days) of discharge. Readmissions are the convergent metric of care quality, discharge planning, and social support, and they are financially penalized in several payment systems. Risk adjustment is essential - severity and socioeconomic mix drive raw rates - and planned readmissions (chemotherapy cycles) must be excluded honestly. Read with discharge follow-up completion and average length of stay for context.

## Formula

```
Readmissions within 30 Days / Discharges
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1639 (batch 6)
