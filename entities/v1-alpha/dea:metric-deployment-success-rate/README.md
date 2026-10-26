# dea:metric-deployment-success-rate

Candidate Performance Metric record for **Deployment Success Rate** (DSR-CD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deployment-success-rate`
- **Name:** Deployment Success Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DSR-CD

## 2. Definition

A Continuous Delivery & Deployment indicator, Deployment Success Rate (DSR-CD) quantifies the quality of outputs and outcomes. It is defined as Deployments without Failure / Deployments; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of deployments that complete without rollback, hotfix, or incident. It is the stability counterpart to deployment frequency: the two together separate teams that ship fast-and-reliably from teams that ship fast-and-break-things, and the metric is the cleanest single read on release engineering quality. Failure definition must include degraded-but-not-rolled-back outcomes, or the rate flatters. Read with change failure rate (Deep Dive) and mean time to restore.

## Formula

```
Deployments without Failure / Deployments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_delivery_deployment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2684 (batch 7)
