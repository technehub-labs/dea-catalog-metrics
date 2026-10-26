# dea:metric-api-security-standard-coverage

Candidate Performance Metric record for **API Security Standard Coverage** (APISSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-security-standard-coverage`
- **Name:** API Security Standard Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APISSC

## 2. Definition

API Security Standard Coverage (APISSC) addresses exposure to adverse outcomes and is a fixture of api lifecycle management reporting. It provides the day-to-day signal that a process is running as designed. Its calculation is Endpoints Enforcing Auth and Rate Policy / Endpoints, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Software practice.

## Formula

```
Endpoints Enforcing Auth and Rate Policy / Endpoints
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3223 (batch 7)
