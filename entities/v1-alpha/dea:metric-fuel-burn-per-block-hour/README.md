# dea:metric-fuel-burn-per-block-hour

Candidate Performance Metric record for **Fuel Burn per Block Hour** (FBH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fuel-burn-per-block-hour`
- **Name:** Fuel Burn per Block Hour
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FBH

## 2. Definition

Fuel Burn per Block Hour (FBH) captures how efficiently resources are converted into outputs for organizations tracking airlines & aviation. Its calculation is Fuel Consumed / Block Hours, measured in ratio (x:1 or x). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Airlines & aviation practice.

## Formula

```
Fuel Consumed / Block Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 659 (batch 2)
