# dea:metric-forecast-bias

Candidate Performance Metric record for **Forecast Bias** (FB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-forecast-bias`
- **Name:** Forecast Bias
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FB

## 2. Definition

Forecast Bias (FB) addresses the quality of outputs and outcomes and is a fixture of supply chain reporting. It is computed as Sum of Forecast Errors / Sum of Actual Demand, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the systematic tendency of forecasts to run high or low versus actuals. It matters because persistent bias silently distorts inventory, capacity, and cash decisions. Teams can game it by manually overriding models toward whatever target looks good this quarter. Read with Plan Accuracy and Inventory Days of Supply to see whether bias is being corrected or absorbed as buffer stock.

## Formula

```
Sum of Forecast Errors / Sum of Actual Demand
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 184 (batch 1)
