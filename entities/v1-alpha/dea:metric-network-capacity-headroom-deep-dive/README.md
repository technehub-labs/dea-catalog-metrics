# dea:metric-network-capacity-headroom-deep-dive

Candidate Performance Metric record for **Network Capacity Headroom (Deep Dive)** (NCH-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-capacity-headroom-deep-dive`
- **Name:** Network Capacity Headroom (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NCH-D

## 2. Definition

Network Capacity Headroom (Deep Dive) (NCH-D) addresses the utilization or availability of capacity and is a fixture of telecom network operations (deep dive) reporting. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is defined as Peak Utilization / Provisioned Capacity; the result is stated in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. In Telecommunications, it is a recognized element of the standard performance toolkit.

## Formula

```
NCH-D = Peak Utilization / Provisioned Capacity
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
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2130 (batch 6)
