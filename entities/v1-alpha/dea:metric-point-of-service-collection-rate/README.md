# dea:metric-point-of-service-collection-rate

Candidate Performance Metric record for **Point-of-Service Collection Rate** (POSC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-point-of-service-collection-rate`
- **Name:** Point-of-Service Collection Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** POSC

## 2. Definition

Within Healthcare Revenue Cycle, Point-of-Service Collection Rate (POSC) is used to gauge the economic value created or preserved. It is computed as Patient Payments Collected at Service / Patient Payments Due, expressed in percent (%). Its use is concentrated in Healthcare. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of patient financial responsibility collected at or before service. It matters because collection probability decays sharply once patients leave. Pushing hard upfront collection can degrade patient experience and access. Read with Patient Satisfaction and Bad Debt Rate to confirm collection discipline is humane.

## Formula

```
Patient Payments Collected at Service / Patient Payments Due
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** healthcare_revenue_cycle
- **Sector:** healthcare

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 878 (batch 3)
