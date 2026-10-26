# dea:metric-fuel-per-nautical-mile-deep-dive

Candidate Performance Metric record for **Fuel per Nautical Mile (Deep Dive)** (FPM-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fuel-per-nautical-mile-deep-dive`
- **Name:** Fuel per Nautical Mile (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FPM-D

## 2. Definition

Fuel per Nautical Mile (Deep Dive) (FPM-D) addresses how efficiently resources are converted into outputs and is a fixture of cruise & passenger shipping reporting. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Fuel Consumed / Nautical Miles Sailed, expressed in ratio (x:1 or x). It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Hospitality.

## 3. Context

Measures fuel consumption normalized by distance, adjusted for speed and itinerary profile. Fuel is the largest controllable operating cost in cruising, and per-mile intensity is the efficiency lever that speed optimization and hull maintenance move. Weather and routing effects are large, so normalize against planned profiles. Read with hull cleaning cadence and itinerary fuel budget variance.

## Formula

```
Fuel Consumed / Nautical Miles Sailed
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cruise_passenger_shipping
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1923 (batch 6)
