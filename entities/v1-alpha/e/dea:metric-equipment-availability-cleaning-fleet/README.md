# dea:metric-equipment-availability-cleaning-fleet

Candidate Performance Metric record for **Equipment Availability (Cleaning Fleet)** (EAF-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-equipment-availability-cleaning-fleet`
- **Name:** Equipment Availability (Cleaning Fleet)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EAF-C

## 2. Definition

Equipment Availability (Cleaning Fleet) (EAF-C) addresses the utilization or availability of capacity and is a fixture of cleaning & environmental services reporting. Its calculation is Available Equipment Hours / Scheduled Hours, measured in percent (%). It originates from and is most used in Facility Services practice. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
EAF-C = Available Equipment Hours / Scheduled Hours
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
- **Domain:** cleaning_environmental_services
- **Sector:** facility_services

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2047 (batch 6)
