# dea:metric-vehicle-defects-per-unit

Candidate Performance Metric record for **Vehicle Defects per Unit** (VDPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vehicle-defects-per-unit`
- **Name:** Vehicle Defects per Unit
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** VDPU

## 2. Definition

Vehicle Defects per Unit (VDPU) measures the quality of outputs and outcomes in the Automotive domain. Its calculation is Assembly Defects / Vehicles Produced, measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Automotive practice.

## Formula

```
Assembly Defects / Vehicles Produced
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 741 (batch 2)
