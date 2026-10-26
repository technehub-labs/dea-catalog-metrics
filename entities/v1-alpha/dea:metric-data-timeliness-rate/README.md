# dea:metric-data-timeliness-rate

Candidate Performance Metric record for **Data Timeliness Rate** (DTR-DQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-timeliness-rate`
- **Name:** Data Timeliness Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DTR-DQ

## 2. Definition

Data Timeliness Rate (DTR-DQ) captures the quality of outputs and outcomes for organizations tracking data quality management. It provides the day-to-day signal that a process is running as designed. Its calculation is Records Available within Freshness SLA / Records, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Records Available within Freshness SLA / Records
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3619 (batch 8)
