# dea:metric-sast-findings-per-1-000-lines-of-code

Candidate Performance Metric record for **SAST Findings per 1,000 Lines of Code** (SAST1K) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sast-findings-per-1-000-lines-of-code`
- **Name:** SAST Findings per 1,000 Lines of Code
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SAST1K

## 2. Definition

Within DevSecOps & Application Security Engineering, SAST Findings per 1,000 Lines of Code (SAST1K) is used to gauge exposure to adverse outcomes. It is computed as Static Application Security Findings per KLOC, expressed in events per thousand or million (scaled). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
SAST1K = Static Application Security Findings per KLOC
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** devsecops_application_security_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2749 (batch 7)
