# dea:metric-api-gateway-availability

Candidate Performance Metric record for **API Gateway Availability** (APGA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-gateway-availability`
- **Name:** API Gateway Availability
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APGA

## 2. Definition

API Gateway Availability (APGA) measures the quality of outputs and outcomes in the API Lifecycle Management domain. Its calculation is Uptime of API Gateway Tier, measured in percent (%). It originates from and is most used in Software practice. It provides the day-to-day signal that a process is running as designed. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Uptime of API Gateway Tier
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
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3216 (batch 7)
