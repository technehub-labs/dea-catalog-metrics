# dea:metric-patient-falls-per-1-000-patient-days

Candidate Performance Metric record for **Patient Falls per 1,000 Patient Days** (PF1K) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-patient-falls-per-1-000-patient-days`
- **Name:** Patient Falls per 1,000 Patient Days
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PF1K

## 2. Definition

Within Medical Practice & Clinical Operations, Patient Falls per 1,000 Patient Days (PF1K) is used to gauge exposure to adverse outcomes. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Reported Falls / Patient Days x 1,000 - reported in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Healthcare sector.

## Formula

```
Reported Falls / Patient Days x 1,000
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1646 (batch 6)
