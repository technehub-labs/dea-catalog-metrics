# dea:metric-release-note-completeness

Candidate Performance Metric record for **Release Note Completeness** (RNC-RM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-release-note-completeness`
- **Name:** Release Note Completeness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RNC-RM

## 2. Definition

Release Note Completeness (RNC-RM) measures the quality of outputs and outcomes in the Release Management & Environments domain. Its calculation is Changes Documented in Release Notes / Changes Shipped, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Changes Documented in Release Notes / Changes Shipped
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
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2734 (batch 7)
