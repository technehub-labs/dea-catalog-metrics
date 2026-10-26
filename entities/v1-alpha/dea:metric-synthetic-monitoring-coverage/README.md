# dea:metric-synthetic-monitoring-coverage

Candidate Performance Metric record for **Synthetic Monitoring Coverage** (SYNMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-synthetic-monitoring-coverage`
- **Name:** Synthetic Monitoring Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SYNMC

## 2. Definition

Synthetic Monitoring Coverage (SYNMC) measures the quality of outputs and outcomes in the SRE & Observability Standard Measures domain. Its calculation is Critical User Journeys under Synthetic Test / Critical Journeys, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Software practice.

## Formula

```
Critical User Journeys under Synthetic Test / Critical Journeys
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sre_observability_standard_measures
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4393 (batch 11)
