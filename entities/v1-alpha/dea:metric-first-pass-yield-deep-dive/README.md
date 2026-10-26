# dea:metric-first-pass-yield-deep-dive

Candidate Performance Metric record for **First Pass Yield (Deep Dive)** (FPYDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-first-pass-yield-deep-dive`
- **Name:** First Pass Yield (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FPYDD

## 2. Definition

First Pass Yield (Deep Dive) (FPYDD) addresses the quality of outputs and outcomes and is a fixture of process capability & six sigma (deep dive) reporting. The formula is Units Passing All Steps without Rework / Units Started - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Manufacturing sector.

## Formula

```
Units Passing All Steps without Rework / Units Started
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4081 (batch 9)
