# dea:metric-process-performance-index-ppk

Candidate Performance Metric record for **Process Performance Index (Ppk)** (PPKS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-process-performance-index-ppk`
- **Name:** Process Performance Index (Ppk)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PPKS

## 2. Definition

Process Performance Index (Ppk) (PPKS) measures the quality of outputs and outcomes in the Process Capability & Six Sigma (Deep Dive) domain. The formula is Min Distance of Mean to Spec Limit / (3 x Total Std Dev) - reported in ratio (x:1 or x). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Manufacturing sector.

## Formula

```
Min Distance of Mean to Spec Limit / (3 x Total Std Dev)
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4078 (batch 9)
