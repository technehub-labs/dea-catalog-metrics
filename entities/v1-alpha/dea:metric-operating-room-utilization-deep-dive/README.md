# dea:metric-operating-room-utilization-deep-dive

Candidate Performance Metric record for **Operating Room Utilization (Deep Dive)** (ORU-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-operating-room-utilization-deep-dive`
- **Name:** Operating Room Utilization (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ORU-D

## 2. Definition

Operating Room Utilization (Deep Dive) (ORU-D) addresses the utilization or availability of capacity and is a fixture of medical practice & clinical operations reporting. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is In-Use OR Minutes / Available OR Minutes, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Healthcare practice.

## Formula

```
ORU-D = In-Use OR Minutes / Available OR Minutes
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1643 (batch 6)
