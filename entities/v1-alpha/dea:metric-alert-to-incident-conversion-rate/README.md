# dea:metric-alert-to-incident-conversion-rate

Candidate Performance Metric record for **Alert-to-Incident Conversion Rate** (AICR-SOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-alert-to-incident-conversion-rate`
- **Name:** Alert-to-Incident Conversion Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** AICR-SOC

## 2. Definition

Within SecOps & Security Operations Center, Alert-to-Incident Conversion Rate (AICR-SOC) is used to gauge how efficiently resources are converted into outputs. It provides the day-to-day signal that a process is running as designed. Its calculation is Alerts Escalated to Incidents / Alerts, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Alerts Escalated to Incidents / Alerts
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** secops_security_operations_center

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2777 (batch 7)
