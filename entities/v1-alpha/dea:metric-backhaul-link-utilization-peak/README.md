# dea:metric-backhaul-link-utilization-peak

Candidate Performance Metric record for **Backhaul Link Utilization Peak** (BLUP) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backhaul-link-utilization-peak`
- **Name:** Backhaul Link Utilization Peak
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BLUP

## 2. Definition

Backhaul Link Utilization Peak (BLUP) captures the utilization or availability of capacity for organizations tracking telecom network operations (deep dive). It is computed as Peak Backhaul Throughput / Link Capacity, expressed in percent (%). Its use is concentrated in Telecommunications. It is reviewed at cadence by planning owners to correct course before issues become strategic. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Peak Backhaul Throughput / Link Capacity
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
- **Domain:** telecom_network_operations_deep_dive
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2136 (batch 6)
