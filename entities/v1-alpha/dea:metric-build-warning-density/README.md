# dea:metric-build-warning-density

Candidate Performance Metric record for **Build Warning Density** (BWD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-build-warning-density`
- **Name:** Build Warning Density
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BWD

## 2. Definition

A Code Quality & Static Analysis indicator, Build Warning Density (BWD) quantifies the quality of outputs and outcomes. It is computed as Compiler and Linter Warnings per Build, expressed in count (items per period). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is concentrated in Software.

## Formula

```
Compiler and Linter Warnings per Build
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4194 (batch 9)
