# dea:metric-function-parameter-count-compliance

Candidate Performance Metric record for **Function Parameter Count Compliance** (FPCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-function-parameter-count-compliance`
- **Name:** Function Parameter Count Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FPCC

## 2. Definition

A Code Quality & Static Analysis indicator, Function Parameter Count Compliance (FPCC) quantifies the quality of outputs and outcomes. The formula is Functions within Parameter Limit / Functions - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Software sector.

## Formula

```
Functions within Parameter Limit / Functions
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4186 (batch 9)
