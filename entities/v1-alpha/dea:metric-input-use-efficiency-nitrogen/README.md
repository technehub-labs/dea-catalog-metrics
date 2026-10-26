# dea:metric-input-use-efficiency-nitrogen

Candidate Performance Metric record for **Input Use Efficiency - Nitrogen** (NUE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-input-use-efficiency-nitrogen`
- **Name:** Input Use Efficiency - Nitrogen
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** NUE

## 2. Definition

Within Agriculture & Agronomy (Deep Dive), Input Use Efficiency - Nitrogen (NUE) is used to gauge environmental and social sustainability performance. Its calculation is Crop Nitrogen Uptake / Applied Nitrogen, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. It originates from and is most used in Agriculture practice.

## 3. Context

Measures crop output per unit of nitrogen applied. It is the sustainability-and-margin convergence metric of modern agriculture: nitrogen is the largest input cost and the largest waterway and emissions liability, so efficiency gains pay twice. Efficiency comparisons need soil-context adjustment, since the same application rate is profligate on fertile ground and necessary on depleted fields. Read with soil organic matter trend and yield trends to confirm efficiency is not yield erosion in disguise.

## Formula

```
Crop Nitrogen Uptake / Applied Nitrogen
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** sustainability
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2314 (batch 6)
