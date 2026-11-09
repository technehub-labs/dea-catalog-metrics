# dea:metric-deployment-downtime-per-release

Candidate Performance Metric record for **Deployment Downtime per Release** (DDPR-CD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deployment-downtime-per-release`
- **Name:** Deployment Downtime per Release
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DDPR-CD

## 2. Definition

A Continuous Delivery & Deployment indicator, Deployment Downtime per Release (DDPR-CD) quantifies the quality of outputs and outcomes. It is computed as Customer-Visible Minutes Lost per Release, expressed in minutes. It is applied across virtually every sector. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the average user-visible service interruption attributable to each deployment. It quantifies the true operational cost of shipping, exposing teams whose release process taxes customers. Teams can game it by batching large, rare releases that shift downtime into bigger outages. Read with deployment frequency and zero-downtime deployment rate.

## Formula

```
DDPR-CD = Customer-Visible Minutes Lost per Release
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_delivery_deployment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2696 (batch 7)
