# dea:metric-journey-drop-off-rate-by-stage

Candidate Performance Metric record for **Journey Drop-off Rate by Stage** (JDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-journey-drop-off-rate-by-stage`
- **Name:** Journey Drop-off Rate by Stage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** JDR

## 2. Definition

Journey Drop-off Rate by Stage (JDR) addresses exposure to adverse outcomes and is a fixture of customer journey & experience reporting. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Customers Exiting at Stage / Customers Reaching Stage, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures customer abandonment at each stage of defined journeys. It matters because stage-level drop-off locates the exact friction point instead of aggregate funnels. Stage definitions can be redrawn so drop-offs land outside measurement. Read with Average Journey Cycle Time and Conversion Rate trends to confirm fixes at flagged stages actually stick.

## Formula

```
Customers Exiting at Stage / Customers Reaching Stage
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1249 (batch 4)
