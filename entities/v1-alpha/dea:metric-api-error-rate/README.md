# dea:metric-api-error-rate

Candidate Performance Metric record for **API Error Rate** (APIER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-error-rate`
- **Name:** API Error Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APIER

## 2. Definition

Within Software Engineering, API Error Rate (APIER) is used to gauge the quality of outputs and outcomes. It is computed as Failed API Requests / Total API Requests, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Failed API Requests / Total API Requests
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** software_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 288 (batch 1)
