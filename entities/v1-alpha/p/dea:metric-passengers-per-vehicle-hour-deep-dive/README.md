# dea:metric-passengers-per-vehicle-hour-deep-dive

Candidate Performance Metric record for **Passengers per Vehicle Hour (Deep Dive)** (PPVH-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-passengers-per-vehicle-hour-deep-dive`
- **Name:** Passengers per Vehicle Hour (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** PPVH-D

## 2. Definition

A Public Transit (Deep Dive) indicator, Passengers per Vehicle Hour (Deep Dive) (PPVH-D) quantifies how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Passengers / Vehicle Revenue Hour - reported in count (items per period). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Public Transit sector.

## 3. Context

Measures ridership carried per vehicle service hour. It is the productive-efficiency metric of transit operations: service hours are the cost currency, and passengers per hour determines how efficiently those hours serve mobility. High ratios achieved by cutting low-ridership coverage routes are efficiency that abandons the transit-equity mission. Read with route-level distribution and coverage-versus-productivity policy balance.

## Formula

```
PPVH-D = Passengers / Vehicle Revenue Hour
```

## Unit

- **Unit reference:** `dea:unit-count`
- **Unit:** count
- **Unit label (as published):** count (items per period)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** public_transit_deep_dive
- **Sector:** public_transit

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2412 (batch 6)
