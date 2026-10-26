# dea:metric-e-government-service-uptime

Candidate Performance Metric record for **E-Government Service Uptime** (EGSU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-e-government-service-uptime`
- **Name:** E-Government Service Uptime
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EGSU

## 2. Definition

E-Government Service Uptime (EGSU) measures the utilization or availability of capacity in the Government & Public Administration domain. It is computed as Available Hours of Digital Services / Total Hours, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Public Sector.

## Formula

```
Available Hours of Digital Services / Total Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** governance
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** government_public_administration
- **Sector:** public_sector

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1576 (batch 6)
