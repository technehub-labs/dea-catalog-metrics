# dea:metric-over-privileged-role-ratio

Candidate Performance Metric record for **Over-Privileged Role Ratio** (OPRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-over-privileged-role-ratio`
- **Name:** Over-Privileged Role Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OPRR

## 2. Definition

Within Cloud Security Posture Management, Over-Privileged Role Ratio (OPRR) is used to gauge exposure to adverse outcomes. Its calculation is Roles Exceeding Required Permissions / Roles, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
OPRR = Roles Exceeding Required Permissions / Roles
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3309 (batch 7)
