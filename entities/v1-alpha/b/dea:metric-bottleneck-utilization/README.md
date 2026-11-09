# dea:metric-bottleneck-utilization

Candidate Performance Metric record for **Bottleneck Utilization** (BU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bottleneck-utilization`
- **Name:** Bottleneck Utilization
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** BU

## 2. Definition

A Operations indicator, Bottleneck Utilization (BU) quantifies the utilization or availability of capacity. The formula is Load on Constraint Resource / Constraint Capacity - reported in percent (%). It is applied across virtually every sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures how intensely the constrained resource in a process is loaded. It matters because bottleneck throughput caps the whole system, so every idle minute there is lost system output. Running bottlenecks near 100 percent removes protective slack and makes the line fragile to any disruption. Read with Capacity Headroom and Process Cycle Efficiency to balance exploitation of the constraint against resilience.

## Formula

```
BU = Load on Constraint Resource / Constraint Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 158 (batch 1)
