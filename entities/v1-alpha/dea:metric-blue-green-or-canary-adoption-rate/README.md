# dea:metric-blue-green-or-canary-adoption-rate

Candidate Performance Metric record for **Blue-Green or Canary Adoption Rate** (BGCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-blue-green-or-canary-adoption-rate`
- **Name:** Blue-Green or Canary Adoption Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BGCA

## 2. Definition

Blue-Green or Canary Adoption Rate (BGCA) captures capability maturity or development for organizations tracking continuous delivery & deployment. Its calculation is Services Using Progressive Delivery / Services, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of deployments using progressive or zero-downtime release patterns. Adoption is the capability metric for release risk engineering: canary releases convert deployment failures from outages into data points, and blue-green eliminates the downtime window entirely. Adoption must include automated rollback, since canary without rollback is a slower way to fail. Read with deployment success rate (Deep Dive) and incident duration trends.

## Formula

```
Services Using Progressive Delivery / Services
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2686 (batch 7)
