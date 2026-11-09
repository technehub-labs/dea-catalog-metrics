# dea:metric-data-completeness-rate

Candidate Performance Metric record for **Data Completeness Rate** (DCR-DQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-completeness-rate`
- **Name:** Data Completeness Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCR-DQ

## 2. Definition

Data Completeness Rate (DCR-DQ) captures the quality of outputs and outcomes for organizations tracking data quality management. It is computed as Mandatory Fields Populated / Mandatory Fields, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
DCR-DQ = Mandatory Fields Populated / Mandatory Fields
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3615 (batch 8)
