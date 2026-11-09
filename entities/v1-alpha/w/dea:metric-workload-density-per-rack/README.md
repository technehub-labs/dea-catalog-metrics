# dea:metric-workload-density-per-rack

Candidate Performance Metric record for **Workload Density per Rack** (WDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workload-density-per-rack`
- **Name:** Workload Density per Rack
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WDR

## 2. Definition

A Data Center & Cloud Operations indicator, Workload Density per Rack (WDR) quantifies the utilization or availability of capacity. The formula is Compute Power or Workloads / Rack - reported in ratio (x:1 or x). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Higher values are better; gains are read as improvement and losses as deterioration. It is a standard measure in the Technology & data centers sector.

## 3. Context

Measures compute workload packed per rack. It matters because higher density improves facility economics but stresses power and cooling limits. Density can be pushed past thermal design margins, storing reliability risk. Read with Data Center Cooling Efficiency and Incident Rate in the facility to confirm density is stable.

## Formula

```
WDR = Compute Power or Workloads / Rack
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1097 (batch 4)
