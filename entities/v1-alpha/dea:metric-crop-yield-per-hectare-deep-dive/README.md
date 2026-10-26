# dea:metric-crop-yield-per-hectare-deep-dive

Candidate Performance Metric record for **Crop Yield per Hectare (Deep Dive)** (CYH-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-crop-yield-per-hectare-deep-dive`
- **Name:** Crop Yield per Hectare (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CYH-D

## 2. Definition

Crop Yield per Hectare (Deep Dive) (CYH-D) measures how effectively a process or entity achieves its intended outcome in the Agriculture & Agronomy (Deep Dive) domain. Its calculation is Harvested Tonnes / Hectares, measured in tonnes. It originates from and is most used in Agriculture practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures harvested output per land unit, the foundational productivity metric of agriculture. Yield is where genetics, agronomy, inputs, and weather converge into economics, and it is the denominator of food security and farm margin alike. Comparability requires multi-year averages to smooth weather, and yield without input cost is an incomplete story. Read with input-use efficiency and yield-gap analysis against attainable potential.

## Formula

```
Harvested Tonnes / Hectares
```

## Unit

- **Unit reference:** `dea:unit-tonnes`
- **Unit:** tonnes
- **Unit label (as published):** tonnes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_agronomy_deep_dive
- **Sector:** agriculture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2312 (batch 6)
