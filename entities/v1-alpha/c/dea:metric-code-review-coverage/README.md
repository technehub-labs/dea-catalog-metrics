# dea:metric-code-review-coverage

Candidate Performance Metric record for **Code Review Coverage** (CRC-SD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-code-review-coverage`
- **Name:** Code Review Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CRC-SD

## 2. Definition

Within Software Development - Coding & Engineering Practices, Code Review Coverage (CRC-SD) is used to gauge the quality of outputs and outcomes. It provides the day-to-day signal that a process is running as designed. Its calculation is Changes Reviewed before Merge / Changes Merged, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
CRC-SD = Changes Reviewed before Merge / Changes Merged
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** software_development_coding_engineering_practices

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2640 (batch 7)
