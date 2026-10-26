# dea:metric-door-to-doctor-time

Candidate Performance Metric record for **Door-to-Doctor Time** (D2D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-door-to-doctor-time`
- **Name:** Door-to-Doctor Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** D2D

## 2. Definition

Door-to-Doctor Time (D2D) measures how efficiently resources are converted into outputs in the Healthcare domain. The formula is Minutes from ED Arrival to Clinician Assessment - reported in minutes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Healthcare sector.

## Formula

```
Minutes from ED Arrival to Clinician Assessment
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** healthcare
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 464 (batch 1)
