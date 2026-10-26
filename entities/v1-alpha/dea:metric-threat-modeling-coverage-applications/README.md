# dea:metric-threat-modeling-coverage-applications

Candidate Performance Metric record for **Threat Modeling Coverage (Applications)** (TMCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threat-modeling-coverage-applications`
- **Name:** Threat Modeling Coverage (Applications)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TMCA

## 2. Definition

Within Application Security (AppSec), Threat Modeling Coverage (Applications) (TMCA) is used to gauge exposure to adverse outcomes. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is High-Risk Apps with Threat Model / High-Risk Apps, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Software practice.

## 3. Context

Measures the share of applications with current threat models. Threat modeling is the cheapest moment to remove vulnerability classes. Coverage with stale models (from before major changes) is nominal. Read with threat modeling coverage for new services and security architect review coverage.

## Formula

```
High-Risk Apps with Threat Model / High-Risk Apps
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** application_security_appsec
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3329 (batch 7)
