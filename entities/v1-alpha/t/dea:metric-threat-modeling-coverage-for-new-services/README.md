# dea:metric-threat-modeling-coverage-for-new-services

Candidate Performance Metric record for **Threat Modeling Coverage for New Services** (TMCFNS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-threat-modeling-coverage-for-new-services`
- **Name:** Threat Modeling Coverage for New Services
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TMCFNS

## 2. Definition

Threat Modeling Coverage for New Services (TMCFNS) captures exposure to adverse outcomes for organizations tracking devsecops & application security engineering. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as New Services with Threat Model before Design Sign-off / New Services; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of new services or major changes that complete structured threat modeling before build. It is the cheapest point to remove entire vulnerability classes from an architecture. Coverage without quality control produces checkbox diagrams that name no threats. Read with attack surface reduction rate and security champion coverage per team.

## Formula

```
TMCFNS = New Services with Threat Model before Design Sign-off / New Services
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2757 (batch 7)
