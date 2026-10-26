# dea:metric-sca-dependency-coverage

Candidate Performance Metric record for **SCA Dependency Coverage** (SCADC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sca-dependency-coverage`
- **Name:** SCA Dependency Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SCADC

## 2. Definition

SCA Dependency Coverage (SCADC) measures exposure to adverse outcomes in the Application Security (AppSec) domain. It is computed as Projects with Dependency Scanning / Projects, expressed in percent (%). Its use is concentrated in Software. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Projects with Dependency Scanning / Projects
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3324 (batch 7)
