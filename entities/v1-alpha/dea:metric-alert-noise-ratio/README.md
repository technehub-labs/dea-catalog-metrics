# dea:metric-alert-noise-ratio

Candidate Performance Metric record for **Alert Noise Ratio** (ALNR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alert-noise-ratio`
- **Name:** Alert Noise Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ALNR

## 2. Definition

A SRE & Observability Standard Measures indicator, Alert Noise Ratio (ALNR) quantifies the quality of outputs and outcomes. Its calculation is Non-Actionable Alerts / Total Alerts, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Software practice.

## Formula

```
Non-Actionable Alerts / Total Alerts
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
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4380 (batch 11)
