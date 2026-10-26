# dea:metric-deployment-freeze-exception-rate

Candidate Performance Metric record for **Deployment Freeze Exception Rate** (DFER) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deployment-freeze-exception-rate`
- **Name:** Deployment Freeze Exception Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DFER

## 2. Definition

Within Continuous Delivery & Deployment, Deployment Freeze Exception Rate (DFER) is used to gauge conformance to standards, plans, or obligations. The formula is Freeze-Window Deployments Approved / Freeze Requests - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
Freeze-Window Deployments Approved / Freeze Requests
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2700 (batch 7)
