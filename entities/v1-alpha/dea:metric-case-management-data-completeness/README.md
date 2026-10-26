# dea:metric-case-management-data-completeness

Candidate Performance Metric record for **Case Management Data Completeness** (CMDC-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-case-management-data-completeness`
- **Name:** Case Management Data Completeness
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CMDC-SOC

## 2. Definition

Case Management Data Completeness (CMDC-SOC) captures the quality of outputs and outcomes for organizations tracking secops & security operations center. Its calculation is Incident Records with Required Fields / Records, measured in percent (%). It provides the day-to-day signal that a process is running as designed. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Incident Records with Required Fields / Records
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2795 (batch 7)
