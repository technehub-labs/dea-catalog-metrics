# dea:metric-pipeline-coverage-ratio

Candidate Performance Metric record for **Pipeline Coverage Ratio** (PCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-pipeline-coverage-ratio`
- **Name:** Pipeline Coverage Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** PCR

## 2. Definition

A Sales indicator, Pipeline Coverage Ratio (PCR) quantifies the utilization or availability of capacity. Its calculation is Pipeline Value / Quota for Period, measured in ratio (x:1 or x). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures open pipeline value relative to the remaining quota for the period. It matters because it forecasts whether enough qualified demand exists to hit target. Reps can stuff the pipeline with unqualified or duplicate deals to look safe, inflating coverage without real demand. Read with Opportunity Slippage Rate and Win Rate to judge how much of the coverage is genuinely closable.

## Formula

```
Pipeline Value / Quota for Period
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 90 (batch 1)
