# dea:metric-manufacturing-yield-devices

Candidate Performance Metric record for **Manufacturing Yield (Devices)** (MYD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-manufacturing-yield-devices`
- **Name:** Manufacturing Yield (Devices)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MYD

## 2. Definition

Manufacturing Yield (Devices) (MYD) addresses the quality of outputs and outcomes and is a fixture of medical devices reporting. The formula is Conforming Devices / Devices Started - reported in percent (%). It is a standard measure in the Medical devices sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
MYD = Conforming Devices / Devices Started
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** medical_devices
- **Sector:** medical_devices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 760 (batch 2)
