# dea:metric-configuration-drift-incidents

Candidate Performance Metric record for **Configuration Drift Incidents** (CDI-CD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-configuration-drift-incidents`
- **Name:** Configuration Drift Incidents
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDI-CD

## 2. Definition

Within Continuous Delivery & Deployment, Configuration Drift Incidents (CDI-CD) is used to gauge exposure to adverse outcomes. It is defined as Drift Incidents Detected per Month; the result is stated in count (items per period). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
CDI-CD = Drift Incidents Detected per Month
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2694 (batch 7)
