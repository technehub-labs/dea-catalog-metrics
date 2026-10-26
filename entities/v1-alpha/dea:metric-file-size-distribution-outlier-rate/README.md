# dea:metric-file-size-distribution-outlier-rate

Candidate Performance Metric record for **File Size Distribution Outlier Rate** (FSDOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-file-size-distribution-outlier-rate`
- **Name:** File Size Distribution Outlier Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FSDOR

## 2. Definition

File Size Distribution Outlier Rate (FSDOR) addresses the quality of outputs and outcomes and is a fixture of code quality & static analysis reporting. Its calculation is Files Exceeding Size Guideline / Files, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Software practice.

## Formula

```
Files Exceeding Size Guideline / Files
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4185 (batch 9)
