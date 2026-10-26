# dea:metric-dock-to-stock-time

Candidate Performance Metric record for **Dock-to-Stock Time** (D2S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dock-to-stock-time`
- **Name:** Dock-to-Stock Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** D2S

## 2. Definition

Dock-to-Stock Time (D2S) measures how efficiently resources are converted into outputs in the Logistics & Transportation domain. The formula is Hours from Receiving Dock to Stock Availability - reported in hours. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Logistics sector.

## Formula

```
D2S = Hours from Receiving Dock to Stock Availability
```

## Unit

- **Unit reference:** `dea:unit-hour`
- **Unit:** hour
- **Unit label (as published):** hours

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** logistics_transportation
- **Sector:** logistics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 200 (batch 1)
