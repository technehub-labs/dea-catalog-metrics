# dea:metric-data-consistency-rate

Candidate Performance Metric record for **Data Consistency Rate** (DCONR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-consistency-rate`
- **Name:** Data Consistency Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCONR

## 2. Definition

Data Consistency Rate (DCONR) addresses the quality of outputs and outcomes and is a fixture of data quality management reporting. It is computed as Values Consistent across Systems / Cross-System Pairs Sampled, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
DCONR = Values Consistent across Systems / Cross-System Pairs Sampled
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3617 (batch 8)
