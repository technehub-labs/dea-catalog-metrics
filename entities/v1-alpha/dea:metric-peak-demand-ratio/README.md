# dea:metric-peak-demand-ratio

Candidate Performance Metric record for **Peak Demand Ratio** (PDR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-peak-demand-ratio`
- **Name:** Peak Demand Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PDR-E

## 2. Definition

Within Operations Energy Management, Peak Demand Ratio (PDR-E) is used to gauge the utilization or availability of capacity. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Peak Power Demand / Contracted Demand Capacity - reported in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures peak demand relative to average demand in operations energy management. It matters because peak spikes drive capacity charges and infrastructure sizing. Peaks can be shifted, not reduced, through load timing games that move cost elsewhere. Read with Load Factor (Energy) and demand charge trends to confirm peak management is genuine.

## Formula

```
Peak Power Demand / Contracted Demand Capacity
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** operations_energy_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1431 (batch 5)
