# dea:metric-locomotive-availability-deep-dive

Candidate Performance Metric record for **Locomotive Availability (Deep Dive)** (LA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-locomotive-availability-deep-dive`
- **Name:** Locomotive Availability (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LA-D

## 2. Definition

A Rail Freight (Deep Dive) indicator, Locomotive Availability (Deep Dive) (LA-D) quantifies the utilization or availability of capacity. The formula is Locomotives Available / Locomotives in Fleet - reported in percent (%). It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Rail sector.

## 3. Context

Measures the share of locomotives available for assignment. Locomotives are the scarce power asset of rail freight, and availability constrains train starts before any other factor in tight markets. Availability raised by deferring maintenance accumulates failure risk precisely where railroads are most exposed - long, heavy trains in remote territory. Read with maintenance interval adherence and failure rates in-service.

## Formula

```
Locomotives Available / Locomotives in Fleet
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2424 (batch 6)
