# dea:metric-capacity-headroom

Candidate Performance Metric record for **Capacity Headroom** (CH) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-headroom`
- **Name:** Capacity Headroom
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CH

## 2. Definition

Within IT Service Management, Capacity Headroom (CH) is used to gauge the utilization or availability of capacity. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is (Available Capacity - Peak Demand) / Available Capacity, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the unused capacity available above current demand. It matters because headroom is the buffer that absorbs growth and incidents without degradation. Keeping huge headroom to look safe wastes capital; the trick is sizing it to volatility. Read with Bottleneck Utilization and Forecast Accuracy to align headroom with realistic demand uncertainty.

## Formula

```
(Available Capacity - Peak Demand) / Available Capacity
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
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** it_service_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 313 (batch 1)
