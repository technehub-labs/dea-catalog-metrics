# dea:metric-average-class-size

Candidate Performance Metric record for **Average Class Size** (ACS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-class-size`
- **Name:** Average Class Size
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ACS

## 2. Definition

A Education indicator, Average Class Size (ACS) quantifies the utilization or availability of capacity. It is defined as Enrolled Students / Classes; the result is stated in ratio (x:1 or x). It is a working-level control: thresholds trigger immediate operational response. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. In Education, it is a recognized element of the standard performance toolkit.

## Formula

```
ACS = Enrolled Students / Classes
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** capability
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** education
- **Sector:** education

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 519 (batch 1)
