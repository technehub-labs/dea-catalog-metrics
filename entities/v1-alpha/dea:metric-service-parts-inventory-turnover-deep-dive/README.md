# dea:metric-service-parts-inventory-turnover-deep-dive

Candidate Performance Metric record for **Service Parts Inventory Turnover (Deep Dive)** (SPIT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-parts-inventory-turnover-deep-dive`
- **Name:** Service Parts Inventory Turnover (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPIT-D

## 2. Definition

Service Parts Inventory Turnover (Deep Dive) (SPIT-D) measures the utilization or availability of capacity in the Field Maintenance & Technical Field Service (Deep Dive) domain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Annual Parts Issued / Average Parts Stock, measured in times per period. Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SPIT-D = Annual Parts Issued / Average Parts Stock
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_maintenance_technical_field_service_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2925 (batch 7)
