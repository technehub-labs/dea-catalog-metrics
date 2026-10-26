# dea:metric-aircraft-turnaround-compliance-airport

Candidate Performance Metric record for **Aircraft Turnaround Compliance - Airport** (ATCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-aircraft-turnaround-compliance-airport`
- **Name:** Aircraft Turnaround Compliance - Airport
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ATCA

## 2. Definition

A Airport Operations (Deep Dive) indicator, Aircraft Turnaround Compliance - Airport (ATCA) quantifies conformance to standards, plans, or obligations. The formula is Turnarounds within Airline SLA / Turnarounds - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Aviation sector.

## Formula

```
Turnarounds within Airline SLA / Turnarounds
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations_deep_dive
- **Sector:** aviation

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2275 (batch 6)
