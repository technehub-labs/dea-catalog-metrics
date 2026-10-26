# dea:metric-feature-flag-configuration-error-rate

Candidate Performance Metric record for **Feature Flag Configuration Error Rate** (FFCER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-feature-flag-configuration-error-rate`
- **Name:** Feature Flag Configuration Error Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** FFCER

## 2. Definition

Within Continuous Delivery & Deployment, Feature Flag Configuration Error Rate (FFCER) is used to gauge exposure to adverse outcomes. It is defined as Incidents Caused by Flag Misconfiguration / Incidents; the result is stated in percent (%). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Incidents Caused by Flag Misconfiguration / Incidents
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_delivery_deployment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2691 (batch 7)
