# dea:metric-staff-to-patient-ratio

Candidate Performance Metric record for **Staff-to-Patient Ratio** (SPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-staff-to-patient-ratio`
- **Name:** Staff-to-Patient Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SPR

## 2. Definition

A Healthcare indicator, Staff-to-Patient Ratio (SPR) quantifies the utilization or availability of capacity. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Clinical Staff on Duty / Patients in Care - reported in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. It is a standard measure in the Healthcare sector.

## Formula

```
Clinical Staff on Duty / Patients in Care
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 470 (batch 1)
