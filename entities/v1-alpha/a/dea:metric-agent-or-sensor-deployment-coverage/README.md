# dea:metric-agent-or-sensor-deployment-coverage

Candidate Performance Metric record for **Agent or Sensor Deployment Coverage** (ASDC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-agent-or-sensor-deployment-coverage`
- **Name:** Agent or Sensor Deployment Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ASDC

## 2. Definition

A Vulnerability & Exposure Management indicator, Agent or Sensor Deployment Coverage (ASDC) quantifies capability maturity or development. The formula is Endpoints with Vulnerability Agent / Endpoints - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
ASDC = Endpoints with Vulnerability Agent / Endpoints
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** vulnerability_exposure_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2802 (batch 7)
