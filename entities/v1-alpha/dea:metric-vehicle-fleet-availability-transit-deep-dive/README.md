# dea:metric-vehicle-fleet-availability-transit-deep-dive

Candidate Performance Metric record for **Vehicle Fleet Availability (Transit Deep Dive)** (VFA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-vehicle-fleet-availability-transit-deep-dive`
- **Name:** Vehicle Fleet Availability (Transit Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** VFA-D

## 2. Definition

Vehicle Fleet Availability (Transit Deep Dive) (VFA-D) measures the utilization or availability of capacity in the Public Transit (Deep Dive) domain. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Vehicles Available for Service / Peak Vehicles Required - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Public Transit sector.

## 3. Context

Measures the share of fleet available for service versus maintenance hold. Availability is the operational ceiling on trips operated, and aging fleets with parts scarcity have quietly become the binding constraint on service delivery in many agencies. Availability must be weighted by peak-requirement, since a vehicle unavailable at the morning peak is the outage that matters. Read with maintenance backlog aging and mean-distance-between-failures trends.

## Formula

```
Vehicles Available for Service / Peak Vehicles Required
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2415 (batch 6)
