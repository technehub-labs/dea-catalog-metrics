# dea:metric-cspm-finding-recurrence-rate

Candidate Performance Metric record for **CSPM Finding Recurrence Rate** (CFRR-CS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cspm-finding-recurrence-rate`
- **Name:** CSPM Finding Recurrence Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CFRR-CS

## 2. Definition

A Cloud Security Posture Management indicator, CSPM Finding Recurrence Rate (CFRR-CS) quantifies the quality of outputs and outcomes. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Findings Reopened after Remediation / Findings, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Findings Reopened after Remediation / Findings
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** risk
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3320 (batch 7)
