# dea:metric-self-service-access-request-rate

Candidate Performance Metric record for **Self-Service Access Request Rate** (SSARR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-self-service-access-request-rate`
- **Name:** Self-Service Access Request Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSARR

## 2. Definition

Self-Service Access Request Rate (SSARR) measures how efficiently resources are converted into outputs in the Identity & Access Management Operations domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Requests via Self-Service Workflow / Requests, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SSARR = Requests via Self-Service Workflow / Requests
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** identity_access_management_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2833 (batch 7)
