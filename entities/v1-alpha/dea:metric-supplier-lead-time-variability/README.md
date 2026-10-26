# dea:metric-supplier-lead-time-variability

Candidate Performance Metric record for **Supplier Lead Time Variability** (SLTV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-lead-time-variability`
- **Name:** Supplier Lead Time Variability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SLTV

## 2. Definition

Supplier Lead Time Variability (SLTV) captures exposure to adverse outcomes for organizations tracking supply chain. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Standard Deviation of Supplier Lead Time, measured in days. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the standard deviation of supplier delivery lead times. It matters because variability, not average lead time, drives the safety stock that eats working capital. Suppliers can look stable by sandbagging quoted lead times wide enough to never miss. Read with Supplier On-Time Delivery and Inventory Days of Supply to see whether variability or length is driving your buffers.

## Formula

```
SLTV = Standard Deviation of Supplier Lead Time
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 192 (batch 1)
