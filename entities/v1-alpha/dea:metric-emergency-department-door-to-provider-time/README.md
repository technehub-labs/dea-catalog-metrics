# dea:metric-emergency-department-door-to-provider-time

Candidate Performance Metric record for **Emergency Department Door-to-Provider Time** (DTP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-department-door-to-provider-time`
- **Name:** Emergency Department Door-to-Provider Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DTP

## 2. Definition

Emergency Department Door-to-Provider Time (DTP) captures how efficiently resources are converted into outputs for organizations tracking medical practice & clinical operations. It is computed as Minutes from Arrival to First Provider Contact, expressed in minutes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Healthcare.

## Formula

```
Minutes from Arrival to First Provider Contact
```

## Unit

- **Unit reference:** `dea:unit-minutes`
- **Unit:** minutes
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1641 (batch 6)
