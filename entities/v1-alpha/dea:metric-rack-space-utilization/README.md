# dea:metric-rack-space-utilization

Candidate Performance Metric record for **Rack Space Utilization** (RSU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rack-space-utilization`
- **Name:** Rack Space Utilization
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RSU

## 2. Definition

Rack Space Utilization (RSU) addresses the utilization or availability of capacity and is a fixture of data center & cloud operations reporting. The formula is Occupied Rack Units / Total Rack Units - reported in percent (%). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. It is a standard measure in the Technology & data centers sector.

## 3. Context

Measures the share of rack positions filled in data center facilities. It matters because data center economics depend on density per square foot. High utilization without power and cooling headroom strands capacity that cannot be energized. Read with Workload Density per Rack and Data Center Cooling Efficiency to confirm space is usable, not just occupied.

## Formula

```
Occupied Rack Units / Total Rack Units
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1091 (batch 4)
