# dea:metric-medication-adherence-proportion-of-days-covered

Candidate Performance Metric record for **Medication Adherence - Proportion of Days Covered** (PDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-medication-adherence-proportion-of-days-covered`
- **Name:** Medication Adherence - Proportion of Days Covered
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PDC

## 2. Definition

Medication Adherence - Proportion of Days Covered (PDC) measures the quality of outputs and outcomes in the Medical Practice & Clinical Operations domain. The formula is Days Covered by Dispensed Medication / Observation Days - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Healthcare sector.

## 3. Context

Measures the share of days a patient has medication on hand over the measurement period. Adherence is the hinge between prescribing and outcomes: efficacy proven in trials evaporates in unmedicated patients, and PDC below 80 percent is the conventional non-adherence line. Pharmacy claims measure possession, not ingestion, and polypharmacy patients distort simple readings. Read with condition-specific outcome rates and refill synchronization programs.

## Formula

```
Days Covered by Dispensed Medication / Observation Days
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_practice_clinical_operations
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1640 (batch 6)
