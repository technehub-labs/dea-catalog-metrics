# dea:metric-defects-per-unit

Candidate Performance Metric record for **Defects per Unit** (DPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-defects-per-unit`
- **Name:** Defects per Unit
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DPU

## 2. Definition

Defects per Unit (DPU) addresses the quality of outputs and outcomes and is a fixture of quality management reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Total Defects / Total Units, measured in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
DPU = Total Defects / Total Units
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 232 (batch 1)
