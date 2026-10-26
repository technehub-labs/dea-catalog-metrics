# dea:metric-server-utilization-average

Candidate Performance Metric record for **Server Utilization Average** (SUA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-server-utilization-average`
- **Name:** Server Utilization Average
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SUA

## 2. Definition

Within Data Centers & Cloud Infrastructure, Server Utilization Average (SUA) is used to gauge the utilization or availability of capacity. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Average CPU or Memory Utilization / Capacity, expressed in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Its use is concentrated in Technology.

## Formula

```
Average CPU or Memory Utilization / Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2140 (batch 6)
