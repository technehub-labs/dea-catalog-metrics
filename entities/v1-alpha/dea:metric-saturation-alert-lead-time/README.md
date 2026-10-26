# dea:metric-saturation-alert-lead-time

Candidate Performance Metric record for **Saturation Alert Lead Time** (SALT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-saturation-alert-lead-time`
- **Name:** Saturation Alert Lead Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SALT

## 2. Definition

Within SRE & Observability Standard Measures, Saturation Alert Lead Time (SALT) is used to gauge the quality of outputs and outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Time between Saturation Alert and Actual Saturation - reported in hours. Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Software sector.

## Formula

```
Time between Saturation Alert and Actual Saturation
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4389 (batch 11)
