# dea:metric-post-deployment-verification-coverage

Candidate Performance Metric record for **Post-Deployment Verification Coverage** (PDVC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-post-deployment-verification-coverage`
- **Name:** Post-Deployment Verification Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PDVC

## 2. Definition

A Continuous Delivery & Deployment indicator, Post-Deployment Verification Coverage (PDVC) quantifies the quality of outputs and outcomes. The formula is Deployments with Automated Smoke Verification / Deployments - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Deployments with Automated Smoke Verification / Deployments
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** continuous_delivery_deployment

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2699 (batch 7)
