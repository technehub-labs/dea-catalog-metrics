# dea:metric-prescription-fill-rate-deep-dive

Candidate Performance Metric record for **Prescription Fill Rate (Deep Dive)** (PFR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-prescription-fill-rate-deep-dive`
- **Name:** Prescription Fill Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PFR-D

## 2. Definition

Prescription Fill Rate (Deep Dive) (PFR-D) addresses how effectively a process or entity achieves its intended outcome and is a fixture of pharmacy retail reporting. It is defined as Prescriptions Filled / Prescriptions Received; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. In Healthcare, it is a recognized element of the standard performance toolkit.

## Formula

```
Prescriptions Filled / Prescriptions Received
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** pharmacy_retail
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2283 (batch 6)
