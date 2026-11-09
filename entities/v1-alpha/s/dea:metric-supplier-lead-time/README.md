# dea:metric-supplier-lead-time

Candidate Performance Metric record for **Supplier Lead Time** (SLT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-lead-time`
- **Name:** Supplier Lead Time
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SLT

## 2. Definition

Supplier Lead Time (SLT) measures how efficiently resources are converted into outputs in the Procurement domain. Its calculation is Average Days from PO to Delivery, measured in days. Its value drives prioritization and resource reallocation among competing initiatives. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the average time from purchase order to receipt of goods. It matters because it sets reorder points, safety stock, and responsiveness to demand changes. Suppliers can quote short lead times then ship incomplete or partial to reset the clock. Read with Supplier Lead Time Variability and Supplier On-Time Delivery to judge whether speed coexists with dependability.

## Formula

```
SLT = Average Days from PO to Delivery
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 227 (batch 1)
