# dea:metric-inventory-days-of-supply-automotive

Candidate Performance Metric record for **Inventory Days of Supply (Automotive)** (IDS-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-inventory-days-of-supply-automotive`
- **Name:** Inventory Days of Supply (Automotive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** IDS-A

## 2. Definition

Within Automotive, Inventory Days of Supply (Automotive) (IDS-A) is used to gauge the utilization or availability of capacity. Its calculation is Vehicle and Parts Inventory / Average Daily Usage, measured in days. It originates from and is most used in Automotive practice. Its value drives prioritization and resource reallocation among competing initiatives. Values outside the intended band, on either side, warrant investigation.

## 3. Context

Measures days of vehicle or parts demand covered by current stock. It matters because working capital in automotive is enormous and lean supply is a competitive weapon. Under-stocking to flatter the metric risks line stoppages that cost multiples of the inventory saved. Read with Line Stop Rate and Fill Rate to confirm leanness coexists with production continuity.

## Formula

```
Vehicle and Parts Inventory / Average Daily Usage
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 745 (batch 2)
