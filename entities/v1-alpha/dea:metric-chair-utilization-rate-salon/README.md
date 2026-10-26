# dea:metric-chair-utilization-rate-salon

Candidate Performance Metric record for **Chair Utilization Rate (Salon)** (CUR-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-chair-utilization-rate-salon`
- **Name:** Chair Utilization Rate (Salon)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CUR-S

## 2. Definition

Chair Utilization Rate (Salon) (CUR-S) measures the utilization or availability of capacity in the Beauty & Personal Care Services domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Booked Stylist Hours / Available Chair Hours, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Personal Services practice.

## Formula

```
CUR-S = Booked Stylist Hours / Available Chair Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** beauty_personal_care_services
- **Sector:** personal_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2019 (batch 6)
