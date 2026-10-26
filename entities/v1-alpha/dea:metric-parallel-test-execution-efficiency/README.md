# dea:metric-parallel-test-execution-efficiency

Candidate Performance Metric record for **Parallel Test Execution Efficiency** (PTEE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-parallel-test-execution-efficiency`
- **Name:** Parallel Test Execution Efficiency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PTEE

## 2. Definition

Parallel Test Execution Efficiency (PTEE) addresses how efficiently resources are converted into outputs and is a fixture of continuous integration reporting. It is computed as Speedup from Parallelization / Theoretical Maximum, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Speedup from Parallelization / Theoretical Maximum
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_integration

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2674 (batch 7)
