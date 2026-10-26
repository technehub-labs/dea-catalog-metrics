# dea:metric-api-mock-availability-rate

Candidate Performance Metric record for **API Mock Availability Rate** (APIMK) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-mock-availability-rate`
- **Name:** API Mock Availability Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APIMK

## 2. Definition

A API Lifecycle Management indicator, API Mock Availability Rate (APIMK) quantifies how efficiently resources are converted into outputs. Its calculation is Endpoints with Runnable Mocks / Endpoints, measured in percent (%). It originates from and is most used in Software practice. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Endpoints with Runnable Mocks / Endpoints
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3225 (batch 7)
