# dea:metric-inventory-turns-bulk-materials

Candidate Performance Metric record for **Inventory Turns (Bulk Materials)** (ITBM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-inventory-turns-bulk-materials`
- **Name:** Inventory Turns (Bulk Materials)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ITBM

## 2. Definition

Within Cement & Building Materials, Inventory Turns (Bulk Materials) (ITBM) is used to gauge the utilization or availability of capacity. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Annual Volume / Average Silo Stock, measured in times per period. Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Manufacturing practice.

## Formula

```
Annual Volume / Average Silo Stock
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** cement_building_materials
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1871 (batch 6)
