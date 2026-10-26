# dea:metric-hotfix-rate

Candidate Performance Metric record for **Hotfix Rate** (HFR-CD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-hotfix-rate`
- **Name:** Hotfix Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HFR-CD

## 2. Definition

A Continuous Delivery & Deployment indicator, Hotfix Rate (HFR-CD) quantifies exposure to adverse outcomes. It is defined as Hotfixes / Total Deployments; the result is stated in percent (%). It is applied across virtually every sector. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Hotfixes / Total Deployments
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_delivery_deployment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2698 (batch 7)
