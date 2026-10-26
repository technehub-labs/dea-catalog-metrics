# dea:metric-capacity-headroom-ratio

Candidate Performance Metric record for **Capacity Headroom Ratio** (CHR-NW) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-headroom-ratio`
- **Name:** Capacity Headroom Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CHR-NW

## 2. Definition

Capacity Headroom Ratio (CHR-NW) addresses the utilization or availability of capacity and is a fixture of network performance & capacity reporting. It is defined as Available Capacity / Peak Demand; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures available capacity above current peak demand. Headroom is the buffer that converts demand spikes into non-events. Excess headroom is idle capital; the right ratio is demand-volatility-specific. Read with capacity forecast accuracy - services and utilization vs. capacity.

## Formula

```
Available Capacity / Peak Demand
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3347 (batch 7)
