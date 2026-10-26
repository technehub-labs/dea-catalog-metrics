# dea:metric-network-device-cpu-saturation-rate

Candidate Performance Metric record for **Network Device CPU Saturation Rate** (NDCPU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-device-cpu-saturation-rate`
- **Name:** Network Device CPU Saturation Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NDCPU

## 2. Definition

Network Device CPU Saturation Rate (NDCPU) captures the utilization or availability of capacity for organizations tracking network performance & capacity. It is computed as Devices above CPU Threshold / Devices, expressed in percent (%). It is applied across virtually every sector. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
NDCPU = Devices above CPU Threshold / Devices
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3359 (batch 7)
