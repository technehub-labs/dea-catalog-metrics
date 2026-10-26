# dea:metric-bandwidth-utilization

Candidate Performance Metric record for **Bandwidth Utilization** (BU-T) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bandwidth-utilization`
- **Name:** Bandwidth Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BU-T

## 2. Definition

Bandwidth Utilization (BU-T) captures the utilization or availability of capacity for organizations tracking telecommunications. The formula is Used Capacity / Provisioned Capacity - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It is a standard measure in the Telecommunications sector.

## Formula

```
Used Capacity / Provisioned Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** telecommunications
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 533 (batch 1)
