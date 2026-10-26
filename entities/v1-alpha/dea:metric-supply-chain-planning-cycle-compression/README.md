# dea:metric-supply-chain-planning-cycle-compression

Candidate Performance Metric record for **Supply Chain Planning Cycle Compression** (SCPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supply-chain-planning-cycle-compression`
- **Name:** Supply Chain Planning Cycle Compression
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SCPC

## 2. Definition

A Supply Chain Standard Measures (Deep Dive) indicator, Supply Chain Planning Cycle Compression (SCPC) quantifies how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Reduction in S&OP Cycle Days vs Baseline, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures shortening of the plan-and-replan cycle. Faster planning cycles let supply chase volatile demand. Compression bought by reducing scenario depth is fragility, not speed. Read with demand forecast accuracy and S&OP cycle time.

## Formula

```
SCPC = Reduction in S&OP Cycle Days vs Baseline
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4267 (batch 10)
