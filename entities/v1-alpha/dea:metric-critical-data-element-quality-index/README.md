# dea:metric-critical-data-element-quality-index

Candidate Performance Metric record for **Critical Data Element Quality Index** (CDEQI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-critical-data-element-quality-index`
- **Name:** Critical Data Element Quality Index
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CDEQI

## 2. Definition

Within Data Quality Management, Critical Data Element Quality Index (CDEQI) is used to gauge the quality of outputs and outcomes. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Weighted Quality Score across CDE Dimensions; the result is stated in index (0-100 or normalized). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures composite quality (accuracy, completeness, timeliness) of the decision-critical elements. The index concentrates effort where quality actually moves decisions. Weighting choices drive the index more than raw quality does. Read with data quality trend index and decision-grade data readiness rate.

## Formula

```
Weighted Quality Score across CDE Dimensions
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3622 (batch 8)
