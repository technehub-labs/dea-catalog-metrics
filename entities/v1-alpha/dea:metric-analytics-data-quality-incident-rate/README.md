# dea:metric-analytics-data-quality-incident-rate

Candidate Performance Metric record for **Analytics Data Quality Incident Rate** (ADQIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-analytics-data-quality-incident-rate`
- **Name:** Analytics Data Quality Incident Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ADQIR

## 2. Definition

Analytics Data Quality Incident Rate (ADQIR) measures the quality of outputs and outcomes in the Data Science & Analytics Operations domain. Its calculation is Data Quality Incidents per 1,000 Dashboard Uses, measured in events per thousand or million (scaled). It is applied across virtually every sector. It provides the day-to-day signal that a process is running as designed. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
ADQIR = Data Quality Incidents per 1,000 Dashboard Uses
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_science_analytics_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2595 (batch 7)
