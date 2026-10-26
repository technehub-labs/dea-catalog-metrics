# dea:metric-failed-record-remediation-cycle-time

Candidate Performance Metric record for **Failed Record Remediation Cycle Time** (FRRCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-failed-record-remediation-cycle-time`
- **Name:** Failed Record Remediation Cycle Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FRRCT

## 2. Definition

A Data Quality Management indicator, Failed Record Remediation Cycle Time (FRRCT) quantifies how efficiently resources are converted into outputs. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Days to Remediate Failed Records, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
FRRCT = Days to Remediate Failed Records
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3626 (batch 8)
