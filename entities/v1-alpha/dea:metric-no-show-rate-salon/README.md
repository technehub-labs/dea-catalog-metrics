# dea:metric-no-show-rate-salon

Candidate Performance Metric record for **No-Show Rate (Salon)** (NSR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-no-show-rate-salon`
- **Name:** No-Show Rate (Salon)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NSR-S

## 2. Definition

No-Show Rate (Salon) (NSR-S) captures how efficiently resources are converted into outputs for organizations tracking beauty & personal care services. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Missed Appointments / Appointments - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Personal Services sector.

## Formula

```
NSR-S = Missed Appointments / Appointments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** beauty_personal_care_services
- **Sector:** personal_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2024 (batch 6)
