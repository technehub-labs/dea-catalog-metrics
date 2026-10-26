# dea:metric-headway-adherence-coefficient-deep-dive

Candidate Performance Metric record for **Headway Adherence Coefficient (Deep Dive)** (HAC-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-headway-adherence-coefficient-deep-dive`
- **Name:** Headway Adherence Coefficient (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** HAC-D

## 2. Definition

Headway Adherence Coefficient (Deep Dive) (HAC-D) captures the quality of outputs and outcomes for organizations tracking public transit (deep dive). It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Actual Headway Variance / Scheduled Headway, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Public Transit.

## Formula

```
Actual Headway Variance / Scheduled Headway
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit_deep_dive
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2410 (batch 6)
