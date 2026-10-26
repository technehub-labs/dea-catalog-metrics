# dea:metric-rollback-rate

Candidate Performance Metric record for **Rollback Rate** (RBR-CD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rollback-rate`
- **Name:** Rollback Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RBR-CD

## 2. Definition

Rollback Rate (RBR-CD) captures exposure to adverse outcomes for organizations tracking continuous delivery & deployment. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Deployments Rolled Back / Deployments; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Deployments Rolled Back / Deployments
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2685 (batch 7)
