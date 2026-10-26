# dea:metric-cloud-misconfiguration-density

Candidate Performance Metric record for **Cloud Misconfiguration Density** (CMDEN) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cloud-misconfiguration-density`
- **Name:** Cloud Misconfiguration Density
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CMDEN

## 2. Definition

A Cloud Security Posture Management indicator, Cloud Misconfiguration Density (CMDEN) quantifies exposure to adverse outcomes. It is computed as Open Misconfigurations per 100 Cloud Resources, expressed in events per thousand or million (scaled). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Open Misconfigurations per 100 Cloud Resources
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** risk
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cloud_security_posture_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3302 (batch 7)
