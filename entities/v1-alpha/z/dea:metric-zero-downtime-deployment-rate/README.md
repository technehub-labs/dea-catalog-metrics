# dea:metric-zero-downtime-deployment-rate

Candidate Performance Metric record for **Zero-Downtime Deployment Rate** (ZDDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-zero-downtime-deployment-rate`
- **Name:** Zero-Downtime Deployment Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ZDDR

## 2. Definition

Zero-Downtime Deployment Rate (ZDDR) captures the quality of outputs and outcomes for organizations tracking continuous delivery & deployment. The formula is Deployments without Service Interruption / Deployments - reported in percent (%). It is applied across virtually every sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of releases shipped with no perceptible service interruption to users. Continuous availability is a competitive requirement for digital platforms: every minute of deploy downtime erodes trust and revenue. Achieving it depends on architectural readiness (loose coupling, backward-compatible changes), so a low rate may reflect legacy constraints rather than team skill. Read with deployment frequency and change failure rate.

## Formula

```
ZDDR = Deployments without Service Interruption / Deployments
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2689 (batch 7)
