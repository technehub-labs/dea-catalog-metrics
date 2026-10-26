# dea:metric-steam-or-compressed-air-loss-rate

Candidate Performance Metric record for **Steam or Compressed Air Loss Rate** (SCAL) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-steam-or-compressed-air-loss-rate`
- **Name:** Steam or Compressed Air Loss Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SCAL

## 2. Definition

Steam or Compressed Air Loss Rate (SCAL) addresses how efficiently resources are converted into outputs and is a fixture of operations energy management reporting. Its calculation is Leakage Losses / Generated Utility Volume, measured in percent (%). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Leakage Losses / Generated Utility Volume
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** operations_energy_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1436 (batch 5)
