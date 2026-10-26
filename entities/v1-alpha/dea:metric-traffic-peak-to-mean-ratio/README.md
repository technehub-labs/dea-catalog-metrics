# dea:metric-traffic-peak-to-mean-ratio

Candidate Performance Metric record for **Traffic Peak-to-Mean Ratio** (TPMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-traffic-peak-to-mean-ratio`
- **Name:** Traffic Peak-to-Mean Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TPMR

## 2. Definition

Traffic Peak-to-Mean Ratio (TPMR) addresses the utilization or availability of capacity and is a fixture of network performance & capacity reporting. The formula is Peak Traffic / Average Traffic - reported in ratio (x:1 or x). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## Formula

```
Peak Traffic / Average Traffic
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
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3350 (batch 7)
