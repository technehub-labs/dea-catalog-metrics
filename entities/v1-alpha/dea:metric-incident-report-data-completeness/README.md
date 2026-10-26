# dea:metric-incident-report-data-completeness

Candidate Performance Metric record for **Incident Report Data Completeness** (IRDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-report-data-completeness`
- **Name:** Incident Report Data Completeness
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IRDC

## 2. Definition

Incident Report Data Completeness (IRDC) measures the quality of outputs and outcomes in the IT Incident & Major Problem Management domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Incident Records with Required Fields / Records; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
IRDC = Incident Records with Required Fields / Records
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2903 (batch 7)
