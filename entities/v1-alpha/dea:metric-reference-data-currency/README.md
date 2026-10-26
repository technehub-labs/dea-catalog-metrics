# dea:metric-reference-data-currency

Candidate Performance Metric record for **Reference Data Currency** (REFDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reference-data-currency`
- **Name:** Reference Data Currency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** REFDC

## 2. Definition

A Data Quality Management indicator, Reference Data Currency (REFDC) quantifies the quality of outputs and outcomes. It is computed as Reference Sets within Refresh Cycle / Reference Sets, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Reference Sets within Refresh Cycle / Reference Sets
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_quality_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3632 (batch 8)
