# dea:metric-mean-time-between-failures-service-view

Candidate Performance Metric record for **Mean Time between Failures - Service View** (MTBF-SV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-between-failures-service-view`
- **Name:** Mean Time between Failures - Service View
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MTBF-SV

## 2. Definition

Mean Time between Failures - Service View (MTBF-SV) addresses the quality of outputs and outcomes and is a fixture of it incident & major problem management reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Operating Hours between Service Failures, expressed in hours. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures average operating time between service-impacting failures. MTBF at the service view reflects what users experience, unlike component-level metrics. Defining what counts as a failure (degraded vs. unavailable) determines comparability. Read with service level objective attainment and recurring incident ratio.

## Formula

```
Operating Hours between Service Failures
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2901 (batch 7)
