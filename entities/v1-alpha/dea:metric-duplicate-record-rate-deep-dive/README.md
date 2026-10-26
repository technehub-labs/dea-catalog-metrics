# dea:metric-duplicate-record-rate-deep-dive

Candidate Performance Metric record for **Duplicate Record Rate (Deep Dive)** (DRR-DQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-duplicate-record-rate-deep-dive`
- **Name:** Duplicate Record Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DRR-DQ

## 2. Definition

A Data Quality Management indicator, Duplicate Record Rate (Deep Dive) (DRR-DQ) quantifies the quality of outputs and outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Duplicate Records / Total Records - reported in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Duplicate Records / Total Records
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3618 (batch 8)
