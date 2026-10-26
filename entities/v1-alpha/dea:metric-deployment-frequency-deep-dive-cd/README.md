# dea:metric-deployment-frequency-deep-dive-cd

Candidate Performance Metric record for **Deployment Frequency (Deep Dive - CD)** (DFCD-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deployment-frequency-deep-dive-cd`
- **Name:** Deployment Frequency (Deep Dive - CD)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DFCD-D

## 2. Definition

Deployment Frequency (Deep Dive - CD) (DFCD-D) measures how efficiently resources are converted into outputs in the Continuous Delivery & Deployment domain. It is defined as Production Deployments per Week per Team; the result is stated in times per period. Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how often code deploys to production. It is the first of the DORA metrics for good reason: frequency is the metabolic indicator of delivery capability, and high-performing teams deploy on demand while low performers batch releases into risk events. Frequency without stability is churn, so it must be read with change failure rate together. Read with deployment lead time - commit to production (Deep Dive) and deployment success rate (Deep Dive).

## Formula

```
Production Deployments per Week per Team
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2682 (batch 7)
