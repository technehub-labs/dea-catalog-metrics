# dea:metric-legacy-code-coverage

Candidate Performance Metric record for **Legacy Code Coverage** (LCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legacy-code-coverage`
- **Name:** Legacy Code Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LCC

## 2. Definition

A Code Quality & Static Analysis indicator, Legacy Code Coverage (LCC) quantifies exposure to adverse outcomes. It is defined as Legacy Modules under Test / Legacy Modules; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Higher values are better; gains are read as improvement and losses as deterioration. In Software, it is a recognized element of the standard performance toolkit.

## Formula

```
Legacy Modules under Test / Legacy Modules
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4190 (batch 9)
