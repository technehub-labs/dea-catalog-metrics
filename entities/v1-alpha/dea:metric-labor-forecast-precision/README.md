# dea:metric-labor-forecast-precision

Candidate Performance Metric record for **Labor Forecast Precision** (LFP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-labor-forecast-precision`
- **Name:** Labor Forecast Precision
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LFP

## 2. Definition

Within Workforce Planning & Productivity, Labor Forecast Precision (LFP) is used to gauge the quality of outputs and outcomes. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Forecast vs Actual Labor Hours / Actual, measured in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Forecast vs Actual Labor Hours / Actual
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** organization
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** workforce_planning_productivity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3906 (batch 8)
