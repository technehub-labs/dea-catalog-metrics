# dea:metric-medevac-or-illness-disembarkation-rate

Candidate Performance Metric record for **Medevac or Illness Disembarkation Rate** (MIDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-medevac-or-illness-disembarkation-rate`
- **Name:** Medevac or Illness Disembarkation Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MIDR

## 2. Definition

Within Cruise & Passenger Shipping, Medevac or Illness Disembarkation Rate (MIDR) is used to gauge exposure to adverse outcomes. Its calculation is Medical Disembarkations / Passengers, measured in events per thousand or million (scaled). It provides the day-to-day signal that a process is running as designed. Lower values are better; each reduction is an improvement. It originates from and is most used in Hospitality practice.

## Formula

```
Medical Disembarkations / Passengers
```

## Unit

- **Unit reference:** `dea:unit-events`
- **Unit:** events
- **Unit label (as published):** events per thousand or million (scaled)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1925 (batch 6)
