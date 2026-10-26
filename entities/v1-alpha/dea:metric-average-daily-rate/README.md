# dea:metric-average-daily-rate

Candidate Performance Metric record for **Average Daily Rate** (ADR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-daily-rate`
- **Name:** Average Daily Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ADR

## 2. Definition

A Hospitality & Food Service indicator, Average Daily Rate (ADR) quantifies the economic value created or preserved. It is computed as Room Revenue / Rooms Sold, expressed in currency value. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is concentrated in Hospitality.

## 3. Context

Revenue earned per occupied room-night - the pricing metric of hospitality, and the lever that revenue management exists to pull: with occupancy, it is one of the two variables whose product is rooms revenue, and unlike occupancy it can move without operational change. Its strategic significance is the yield logic: rate and occupancy trade against each other, and the discipline of revenue management is accepting slightly lower occupancy at meaningfully higher rates when the demand curve allows - the practice the airline-yield tradition imported into hotels. The honest comparisons are like-for-like: mix shifts between room classes, seasons, and guest segments move blended ADR without any pricing decision being taken, which is why rate is analyzed within segment and channel, and the honest trend isolates same-property performance.

## Formula

```
ADR = Room Revenue / Rooms Sold
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency value

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** hospitality_food_service
- **Sector:** hospitality

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 505 (batch 1)
