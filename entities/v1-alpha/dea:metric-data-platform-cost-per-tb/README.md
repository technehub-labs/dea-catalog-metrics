# dea:metric-data-platform-cost-per-tb

Candidate Performance Metric record for **Data Platform Cost per TB** (DPC-TB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-platform-cost-per-tb`
- **Name:** Data Platform Cost per TB
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DPC-TB

## 2. Definition

Within Database & Data Platform Operations, Data Platform Cost per TB (DPC-TB) is used to gauge how efficiently resources are converted into outputs. Its calculation is Monthly Platform Spend / Terabytes Managed, measured in currency per unit. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. It originates from and is most used in Software practice.

## Formula

```
Monthly Platform Spend / Terabytes Managed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** database_data_platform_operations
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3238 (batch 7)
