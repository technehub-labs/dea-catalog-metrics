# dea:metric-supplier-on-time-delivery

Candidate Performance Metric record for **Supplier On-Time Delivery** (SOTD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-on-time-delivery`
- **Name:** Supplier On-Time Delivery
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SOTD

## 2. Definition

Within Supply Chain, Supplier On-Time Delivery (SOTD) is used to gauge the quality of outputs and outcomes. Its calculation is Supplier Deliveries On Time / Total Supplier Deliveries, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of supplier order lines delivered by the agreed date. It matters because supplier reliability directly controls downstream production and service commitments. It can be gamed by agreeing inflated lead times so on-time becomes trivially easy, or counting partial shipments as on-time. Read with Supplier Lead Time Variability and Fill Rate to distinguish punctual but unstable suppliers from reliable ones.

## Formula

```
Supplier Deliveries On Time / Total Supplier Deliveries
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 175 (batch 1)
