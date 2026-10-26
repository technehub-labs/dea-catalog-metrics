# dea:metric-incident-detection-via-monitoring-ratio

Candidate Performance Metric record for **Incident Detection via Monitoring Ratio** (IDVMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-incident-detection-via-monitoring-ratio`
- **Name:** Incident Detection via Monitoring Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IDVMR

## 2. Definition

Incident Detection via Monitoring Ratio (IDVMR) addresses capability maturity or development and is a fixture of it incident & major problem management reporting. It is computed as Incidents Detected before User Report / Incidents, expressed in percent (%). It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of incidents detected by monitoring before users report them. Detection lead time is the difference between proactive operations and a call-center-driven fire brigade. Ratios fall when monitoring coverage lags new services. Read with service level indicator coverage and unmonitored critical device count.

## Formula

```
Incidents Detected before User Report / Incidents
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** it_incident_major_problem_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2900 (batch 7)
