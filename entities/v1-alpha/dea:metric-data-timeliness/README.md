# dea:metric-data-timeliness

Candidate Performance Metric record for **Data Timeliness** (DT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-timeliness`
- **Name:** Data Timeliness
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DT

## 2. Definition

Data Timeliness (DT) addresses the quality of outputs and outcomes and is a fixture of data management & analytics reporting. The formula is Data Available within Target Latency / Total Data Deliveries - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Data Available within Target Latency / Total Data Deliveries
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
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** data_management_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 337 (batch 1)
