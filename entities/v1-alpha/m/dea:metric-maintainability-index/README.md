# dea:metric-maintainability-index

Candidate Performance Metric record for **Maintainability Index** (MAINIDX) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintainability-index`
- **Name:** Maintainability Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MAINIDX

## 2. Definition

Maintainability Index (MAINIDX) captures the quality of outputs and outcomes for organizations tracking code quality & static analysis. It provides the day-to-day signal that a process is running as designed. Its calculation is Composite of Cyclomatic Complexity, Halstead, LOC, measured in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Software practice.

## Formula

```
MAINIDX = Composite of Cyclomatic Complexity, Halstead, LOC
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4177 (batch 9)
