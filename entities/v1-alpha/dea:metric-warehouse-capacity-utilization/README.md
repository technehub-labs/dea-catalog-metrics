# dea:metric-warehouse-capacity-utilization

Candidate Performance Metric record for **Warehouse Capacity Utilization** (WCU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-warehouse-capacity-utilization`
- **Name:** Warehouse Capacity Utilization
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WCU

## 2. Definition

A Warehousing indicator, Warehouse Capacity Utilization (WCU) quantifies the utilization or availability of capacity. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Occupied Storage Space / Total Storage Space, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of available storage space or throughput capacity in use. It matters because warehouses are fixed-cost assets and utilization drives unit economics. Sustained peaks above the mid-90s percent leave no slack for surges and drive labor inefficiency through congestion. Read with Inventory Days of Supply and Order Fulfillment Cycle Time to balance utilization against responsiveness.

## Formula

```
WCU = Occupied Storage Space / Total Storage Space
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** warehousing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 211 (batch 1)
