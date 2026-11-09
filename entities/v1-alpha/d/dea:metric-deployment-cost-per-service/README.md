# dea:metric-deployment-cost-per-service

Candidate Performance Metric record for **Deployment Cost per Service** (DCPS-CD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deployment-cost-per-service`
- **Name:** Deployment Cost per Service
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCPS-CD

## 2. Definition

Within Continuous Delivery & Deployment, Deployment Cost per Service (DCPS-CD) is used to gauge how efficiently resources are converted into outputs. It is computed as Pipeline Cost per Deployable Service per Month, expressed in currency value. It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
DCPS-CD = Pipeline Cost per Deployable Service per Month
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2701 (batch 7)
