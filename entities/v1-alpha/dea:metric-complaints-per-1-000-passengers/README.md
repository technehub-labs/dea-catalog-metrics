# dea:metric-complaints-per-1-000-passengers

Candidate Performance Metric record for **Complaints per 1,000 Passengers** (CPP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-complaints-per-1-000-passengers`
- **Name:** Complaints per 1,000 Passengers
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CPP

## 2. Definition

A Airlines & Aviation indicator, Complaints per 1,000 Passengers (CPP) quantifies the quality of outputs and outcomes. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Complaints / Passengers x 1,000 - reported in events per thousand or million (scaled). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Airlines & aviation sector.

## 3. Context

Measures complaint frequency normalized by passenger volume. It matters because it is the standard regulator- and media-facing service quality metric. Airlines can reduce it by making complaint channels harder, suppressing the numerator. Read with Customer Satisfaction Score and Baggage Mishandling Rate to check whether fewer complaints mean better service or dimmer signaling.

## Formula

```
Complaints / Passengers x 1,000
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airlines_aviation
- **Sector:** airlines_aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 657 (batch 2)
