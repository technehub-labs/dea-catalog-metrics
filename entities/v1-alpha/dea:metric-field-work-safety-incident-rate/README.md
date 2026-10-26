# dea:metric-field-work-safety-incident-rate

Candidate Performance Metric record for **Field Work Safety Incident Rate** (FWSIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-field-work-safety-incident-rate`
- **Name:** Field Work Safety Incident Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FWSIR

## 2. Definition

A Field Maintenance & Technical Field Service (Deep Dive) indicator, Field Work Safety Incident Rate (FWSIR) quantifies exposure to adverse outcomes. Its calculation is Field Safety Incidents per 200,000 Hours, measured in events per thousand or million (scaled). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures recordable safety incidents per field work hours. Field work (driving, electrical, heights, confined spaces) concentrates the company's physical risk. Underreporting driven by safety-bonus schemes is the classic distortion. Read with workers compensation cost trend and safety audit compliance rate.

## Formula

```
Field Safety Incidents per 200,000 Hours
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2923 (batch 7)
