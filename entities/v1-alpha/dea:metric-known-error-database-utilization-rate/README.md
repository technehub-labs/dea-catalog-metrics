# dea:metric-known-error-database-utilization-rate

Candidate Performance Metric record for **Known Error Database Utilization Rate** (KEDBR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-known-error-database-utilization-rate`
- **Name:** Known Error Database Utilization Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** KEDBR

## 2. Definition

Within IT Incident & Major Problem Management, Known Error Database Utilization Rate (KEDBR) is used to gauge how efficiently resources are converted into outputs. It is computed as Incidents Resolved via Known Error Entries / Applicable Incidents, expressed in percent (%). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Incidents Resolved via Known Error Entries / Applicable Incidents
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2893 (batch 7)
