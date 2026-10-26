# dea:metric-forecast-bias-ratio

Candidate Performance Metric record for **Forecast Bias Ratio** (FBR-SC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-forecast-bias-ratio`
- **Name:** Forecast Bias Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** FBR-SC

## 2. Definition

Forecast Bias Ratio (FBR-SC) captures the quality of outputs and outcomes for organizations tracking supply chain standard measures (deep dive). Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Cumulative Forecast Error / Cumulative Actual Demand, measured in percent (%). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Cumulative Forecast Error / Cumulative Actual Demand
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4260 (batch 10)
