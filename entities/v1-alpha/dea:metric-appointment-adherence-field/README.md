# dea:metric-appointment-adherence-field

Candidate Performance Metric record for **Appointment Adherence (Field)** (AAFT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-appointment-adherence-field`
- **Name:** Appointment Adherence (Field)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** AAFT

## 2. Definition

Within Telecom Field & Installation, Appointment Adherence (Field) (AAFT) is used to gauge conformance to standards, plans, or obligations. The formula is Appointments within Committed Window / Appointments - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Telecommunications sector.

## Formula

```
Appointments within Committed Window / Appointments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** telecom_field_installation
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1282 (batch 5)
