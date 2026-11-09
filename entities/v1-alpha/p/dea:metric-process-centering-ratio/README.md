# dea:metric-process-centering-ratio

Candidate Performance Metric record for **Process Centering Ratio** (PCR-SS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-centering-ratio`
- **Name:** Process Centering Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PCR-SS

## 2. Definition

A Process Capability & Six Sigma (Deep Dive) indicator, Process Centering Ratio (PCR-SS) quantifies the quality of outputs and outcomes. The formula is Distance of Process Mean from Spec Midpoint / Half-Tolerance - reported in ratio (x:1 or x). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Manufacturing sector.

## Formula

```
PCR-SS = Distance of Process Mean from Spec Midpoint / Half-Tolerance
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
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4084 (batch 9)
