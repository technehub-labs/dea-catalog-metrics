# dea:metric-mean-life-mttf-deep-dive

Candidate Performance Metric record for **Mean Life (MTTF Deep Dive)** (MLDD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-life-mttf-deep-dive`
- **Name:** Mean Life (MTTF Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MLDD

## 2. Definition

Mean Life (MTTF Deep Dive) (MLDD) addresses the quality of outputs and outcomes and is a fixture of reliability & maintainability engineering (deep dive) reporting. Its calculation is Total Operating Time to Failure / Failed Units, measured in hours. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the average time to failure for non-repairable assets. MTTF drives sparing, warranty, and replacement economics. Averages hide the failure distribution's spread, which drives spare strategy. Read with mean time between failures (Critical Assets) and remaining useful life prediction accuracy.

## Formula

```
Total Operating Time to Failure / Failed Units
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** capability
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** reliability_maintainability_engineering_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4098 (batch 9)
