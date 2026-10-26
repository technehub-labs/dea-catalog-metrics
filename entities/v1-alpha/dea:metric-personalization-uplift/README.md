# dea:metric-personalization-uplift

Candidate Performance Metric record for **Personalization Uplift** (PU-CX) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-personalization-uplift`
- **Name:** Personalization Uplift
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PU-CX

## 2. Definition

A Customer Journey & Experience indicator, Personalization Uplift (PU-CX) quantifies the economic value created or preserved. It is computed as (Personalized Conversion - Baseline Conversion) / Baseline Conversion, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures performance improvement from personalized versus generic experiences. It matters because personalization is expensive and must prove incremental value. Holdout-group manipulation or post-hoc segmenting can manufacture uplift. Read with Experiment Win Rate for personalization and Incremental Revenue per personalized session to confirm uplift is real.

## Formula

```
(Personalized Conversion - Baseline Conversion) / Baseline Conversion
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** customer_journey_experience

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1252 (batch 4)
