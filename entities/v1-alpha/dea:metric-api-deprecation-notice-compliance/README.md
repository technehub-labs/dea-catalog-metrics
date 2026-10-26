# dea:metric-api-deprecation-notice-compliance

Candidate Performance Metric record for **API Deprecation Notice Compliance** (APIDNC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-api-deprecation-notice-compliance`
- **Name:** API Deprecation Notice Compliance
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** APIDNC

## 2. Definition

API Deprecation Notice Compliance (APIDNC) measures conformance to standards, plans, or obligations in the API Lifecycle Management domain. Its calculation is Deprecations Announced within Policy Lead Time / Deprecations, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Software practice.

## Formula

```
Deprecations Announced within Policy Lead Time / Deprecations
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3209 (batch 7)
