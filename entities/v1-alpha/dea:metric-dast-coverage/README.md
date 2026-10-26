# dea:metric-dast-coverage

Candidate Performance Metric record for **DAST Coverage** (DASTC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dast-coverage`
- **Name:** DAST Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DASTC

## 2. Definition

DAST Coverage (DASTC) measures exposure to adverse outcomes in the Application Security (AppSec) domain. It is computed as Applications Under Dynamic Testing / Internet-Facing Applications, expressed in percent (%). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Applications Under Dynamic Testing / Internet-Facing Applications
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3323 (batch 7)
