# dea:metric-deployment-lead-time-commit-to-production

Candidate Performance Metric record for **Deployment Lead Time - Commit to Production** (DLTCP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-deployment-lead-time-commit-to-production`
- **Name:** Deployment Lead Time - Commit to Production
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DLTCP

## 2. Definition

Deployment Lead Time - Commit to Production (DLTCP) measures how efficiently resources are converted into outputs in the Continuous Delivery & Deployment domain. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Median Days from Commit to Running in Production, expressed in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures elapsed time from code commit to production deployment. Lead time is the responsiveness metric of the delivery pipeline, and it is the second DORA metric: short lead times mean feedback loops are tight, options are open, and batch sizes are small. Lead time distribution matters more than the mean, since the long tail (the quarter-old branch) is the process dysfunction. Read with deployment frequency (Deep Dive - CD) and work-in-process aging.

## Formula

```
DLTCP = Median Days from Commit to Running in Production
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2683 (batch 7)
