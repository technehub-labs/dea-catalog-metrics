# dea:metric-service-delivery-trips-operated-deep-dive

Candidate Performance Metric record for **Service Delivery - Trips Operated (Deep Dive)** (SDTO-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-delivery-trips-operated-deep-dive`
- **Name:** Service Delivery - Trips Operated (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SDTO-D

## 2. Definition

Service Delivery - Trips Operated (Deep Dive) (SDTO-D) measures conformance to standards, plans, or obligations in the Public Transit (Deep Dive) domain. The formula is Trips Operated / Trips Scheduled - reported in percent (%). It is a standard measure in the Public Transit sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of scheduled transit trips actually operated. It is the reliability contract with riders: every canceled trip strands passengers who then lose the transit habit, and reliability is the primary determinant of ridership retention. Trips operated with severe delays or short-turns are cancelations wearing a different name, so read completion quality alongside volume. Read with on-time performance and driver vacancy rates for causes.

## Formula

```
SDTO-D = Trips Operated / Trips Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2409 (batch 6)
