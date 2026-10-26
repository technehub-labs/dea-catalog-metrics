# dea:metric-network-capacity-forecast-accuracy

Candidate Performance Metric record for **Network Capacity Forecast Accuracy** (NCFA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-network-capacity-forecast-accuracy`
- **Name:** Network Capacity Forecast Accuracy
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** NCFA

## 2. Definition

Network Capacity Forecast Accuracy (NCFA) measures the utilization or availability of capacity in the Network Performance & Capacity domain. It is computed as Forecast vs Actual Utilization Variance, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Forecast vs Actual Utilization Variance
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3346 (batch 7)
