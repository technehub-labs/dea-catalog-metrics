# dea:metric-api-sunset-cycle-compliance

Candidate Performance Metric record for **API Sunset Cycle Compliance** (APISCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-sunset-cycle-compliance`
- **Name:** API Sunset Cycle Compliance
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** APISCC

## 2. Definition

API Sunset Cycle Compliance (APISCC) measures conformance to standards, plans, or obligations in the API Lifecycle Management domain. Its calculation is Versions Retired per Published Sunset Plan / Planned, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Software practice.

## Formula

```
Versions Retired per Published Sunset Plan / Planned
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** api_lifecycle_management
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3222 (batch 7)
