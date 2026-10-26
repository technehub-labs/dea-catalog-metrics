# dea:metric-order-cycle-time-in-warehouse

Candidate Performance Metric record for **Order Cycle Time in Warehouse** (OCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-order-cycle-time-in-warehouse`
- **Name:** Order Cycle Time in Warehouse
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OCT

## 2. Definition

Order Cycle Time in Warehouse (OCT) addresses how efficiently resources are converted into outputs and is a fixture of warehousing reporting. The formula is Hours from Order Release to Shipment - reported in hours. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Hours from Order Release to Shipment
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** warehousing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 213 (batch 1)
