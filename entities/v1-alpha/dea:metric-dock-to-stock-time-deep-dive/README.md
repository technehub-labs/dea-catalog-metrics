# dea:metric-dock-to-stock-time-deep-dive

Candidate Performance Metric record for **Dock-to-Stock Time (Deep Dive)** (D2ST) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dock-to-stock-time-deep-dive`
- **Name:** Dock-to-Stock Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** D2ST

## 2. Definition

Dock-to-Stock Time (Deep Dive) (D2ST) measures how efficiently resources are converted into outputs in the Supply Chain Standard Measures (Deep Dive) domain. It is a working-level control: thresholds trigger immediate operational response. It is defined as Hours from Receipt to Saleable Inventory; the result is stated in hours. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
Hours from Receipt to Saleable Inventory
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4263 (batch 10)
