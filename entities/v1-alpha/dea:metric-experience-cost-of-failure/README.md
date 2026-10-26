# dea:metric-experience-cost-of-failure

Candidate Performance Metric record for **Experience Cost of Failure** (ECF) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-experience-cost-of-failure`
- **Name:** Experience Cost of Failure
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ECF

## 2. Definition

Within Customer Journey & Experience, Experience Cost of Failure (ECF) is used to gauge the economic value created or preserved. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Cost of Rework, Credits, and Recovery per Failed Experience, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the financial cost of experience failures including service, churn, and rework. It matters because costing failure converts experience work into business language. Models can understate by ignoring churn attribution, the largest component. Read with Churn Rate drivers and Service Recovery Effectiveness to confirm cost estimates are defensible.

## Formula

```
Cost of Rework, Credits, and Recovery per Failed Experience
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_journey_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1257 (batch 4)
