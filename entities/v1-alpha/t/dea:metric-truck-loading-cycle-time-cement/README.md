# dea:metric-truck-loading-cycle-time-cement

Candidate Performance Metric record for **Truck Loading Cycle Time (Cement)** (TLCT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-truck-loading-cycle-time-cement`
- **Name:** Truck Loading Cycle Time (Cement)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** TLCT

## 2. Definition

Truck Loading Cycle Time (Cement) (TLCT) measures how efficiently resources are converted into outputs in the Cement & Building Materials domain. It provides the day-to-day signal that a process is running as designed. Its calculation is Minutes to Load and Dispatch Truck, measured in minutes. It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Manufacturing practice.

## Formula

```
TLCT = Minutes to Load and Dispatch Truck
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cement_building_materials
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1872 (batch 6)
