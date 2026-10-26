# dea:metric-fleet-maintenance-cost-per-mile

Candidate Performance Metric record for **Fleet Maintenance Cost per Mile** (FMCM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fleet-maintenance-cost-per-mile`
- **Name:** Fleet Maintenance Cost per Mile
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FMCM

## 2. Definition

Fleet Maintenance Cost per Mile (FMCM) measures how efficiently resources are converted into outputs in the Logistics & Transportation domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Total Maintenance Cost / Total Miles; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. In Logistics, it is a recognized element of the standard performance toolkit.

## Formula

```
Total Maintenance Cost / Total Miles
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 208 (batch 1)
