# dea:metric-data-quality-sla-attainment

Candidate Performance Metric record for **Data Quality SLA Attainment** (DQSLA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-quality-sla-attainment`
- **Name:** Data Quality SLA Attainment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DQSLA

## 2. Definition

Data Quality SLA Attainment (DQSLA) captures the quality of outputs and outcomes for organizations tracking data quality management. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Datasets Meeting Quality SLA / Datasets Monitored, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
DQSLA = Datasets Meeting Quality SLA / Datasets Monitored
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3625 (batch 8)
