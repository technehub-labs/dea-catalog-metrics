# dea:metric-api-spec-compliance-rate

Candidate Performance Metric record for **API Spec Compliance Rate** (APISC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-spec-compliance-rate`
- **Name:** API Spec Compliance Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APISC

## 2. Definition

API Spec Compliance Rate (APISC) captures conformance to standards, plans, or obligations for organizations tracking api lifecycle management. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Implementations Matching Published Spec / Endpoints Tested, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Software.

## Formula

```
Implementations Matching Published Spec / Endpoints Tested
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3220 (batch 7)
