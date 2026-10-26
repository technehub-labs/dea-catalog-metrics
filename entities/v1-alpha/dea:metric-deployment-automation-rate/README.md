# dea:metric-deployment-automation-rate

Candidate Performance Metric record for **Deployment Automation Rate** (DAR-CD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deployment-automation-rate`
- **Name:** Deployment Automation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DAR-CD

## 2. Definition

Deployment Automation Rate (DAR-CD) measures capability maturity or development in the Continuous Delivery & Deployment domain. It is computed as Deployments Executed Fully Automatically / Deployments, expressed in percent (%). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of deployments executed through automated pipelines versus manual steps. Automation is the consistency foundation of delivery: manual deployments are error-prone, unauditable, and don't scale in frequency, which caps every other CI/CD ambition. Automation must extend through configuration and database changes, since a manual tail negates pipeline reliability. Read with deployment success rate (Deep Dive) and environment-drift findings.

## Formula

```
DAR-CD = Deployments Executed Fully Automatically / Deployments
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2688 (batch 7)
