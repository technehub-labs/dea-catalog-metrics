# dea:metric-runtime-application-self-protection-coverage

Candidate Performance Metric record for **Runtime Application Self-Protection Coverage** (RASPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-runtime-application-self-protection-coverage`
- **Name:** Runtime Application Self-Protection Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RASPC

## 2. Definition

A DevSecOps & Application Security Engineering indicator, Runtime Application Self-Protection Coverage (RASPC) quantifies exposure to adverse outcomes. It is computed as Critical Services with RASP or Runtime Protection / Critical Services, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Critical Services with RASP or Runtime Protection / Critical Services
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2761 (batch 7)
