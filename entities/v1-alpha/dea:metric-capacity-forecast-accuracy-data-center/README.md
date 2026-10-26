# dea:metric-capacity-forecast-accuracy-data-center

Candidate Performance Metric record for **Capacity Forecast Accuracy (Data Center)** (CFA-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-forecast-accuracy-data-center`
- **Name:** Capacity Forecast Accuracy (Data Center)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CFA-D

## 2. Definition

A Data Centers & Cloud Infrastructure indicator, Capacity Forecast Accuracy (Data Center) (CFA-D) quantifies the quality of outputs and outcomes. It is computed as 1 - Forecast Error / Actual, expressed in percent (%). Its use is concentrated in Technology. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures deviation between forecast and actual demand for power, space, and cooling. Data center capacity has brutal lead times - power procurement and construction run years - so forecast error converts directly into either stranded capital or sold-out growth windows. Accuracy by constraint type matters, since power is usually binding before space. Read with contracted-versus-utilized capacity and sales pipeline conversion assumptions.

## Formula

```
1 - Forecast Error / Actual
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_centers_cloud_infrastructure
- **Sector:** technology

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2143 (batch 6)
