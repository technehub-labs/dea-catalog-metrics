# dea:metric-damage-rate-per-1-000-parcels-deep-dive

Candidate Performance Metric record for **Damage Rate per 1,000 Parcels (Deep Dive)** (DR1K-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-damage-rate-per-1-000-parcels-deep-dive`
- **Name:** Damage Rate per 1,000 Parcels (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DR1K-D

## 2. Definition

Damage Rate per 1,000 Parcels (Deep Dive) (DR1K-D) captures the quality of outputs and outcomes for organizations tracking parcel & last-mile logistics (deep dive). It is computed as Damaged Parcels / 1,000 Parcels, expressed in events per thousand or million (scaled). Its use is concentrated in Logistics & Trade. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
DR1K-D = Damaged Parcels / 1,000 Parcels
```

## Unit

- **Unit reference:** `dea:unit-event`
- **Unit:** event
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** parcel_last_mile_logistics_deep_dive
- **Sector:** logistics_trade

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2333 (batch 6)
