# dea:metric-kitchen-ticket-time-deep-dive

Candidate Performance Metric record for **Kitchen Ticket Time (Deep Dive)** (KTT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-kitchen-ticket-time-deep-dive`
- **Name:** Kitchen Ticket Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** KTT-D

## 2. Definition

Kitchen Ticket Time (Deep Dive) (KTT-D) captures how efficiently resources are converted into outputs for organizations tracking restaurant operations (deep dive). Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Minutes from Order Fire to Plate, expressed in minutes. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Restaurants.

## Formula

```
KTT-D = Minutes from Order Fire to Plate
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** restaurant_operations_deep_dive
- **Sector:** restaurants

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2351 (batch 6)
