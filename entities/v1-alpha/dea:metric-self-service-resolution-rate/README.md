# dea:metric-self-service-resolution-rate

Candidate Performance Metric record for **Self-Service Resolution Rate** (SSRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-self-service-resolution-rate`
- **Name:** Self-Service Resolution Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SSRR

## 2. Definition

A IT Service Management indicator, Self-Service Resolution Rate (SSRR) quantifies how efficiently resources are converted into outputs. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Self-Service Resolutions / Total Service Requests; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of support issues resolved entirely through self-service channels without human intervention. It matters because every deflected contact saves cost while giving customers instant answers. Teams can inflate it by counting abandoned self-service sessions as resolutions, hiding frustration behind a green metric. Read with Containment Rate and Customer Effort Score to confirm self-service is resolving issues rather than trapping users.

## Formula

```
Self-Service Resolutions / Total Service Requests
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 307 (batch 1)
