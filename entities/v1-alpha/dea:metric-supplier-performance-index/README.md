# dea:metric-supplier-performance-index

Candidate Performance Metric record for **Supplier Performance Index** (SPI) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-supplier-performance-index`
- **Name:** Supplier Performance Index
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPI

## 2. Definition

Supplier Performance Index (SPI) captures the quality of outputs and outcomes for organizations tracking procurement. It is computed as Weighted Index of Quality, Delivery, Cost, Service, expressed in index (0-100 or normalized). It is reviewed at cadence by planning owners to correct course before issues become strategic. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures a composite score of supplier quality, delivery, cost, and responsiveness. It matters because it concentrates scattered signals into one comparable supplier scorecard. Composite weightings can be tuned so favored suppliers rank well despite weak fundamentals. Read with Supplier On-Time Delivery and Supplier Defect Rate to audit the components behind the headline index.

## Formula

```
SPI = Weighted Index of Quality, Delivery, Cost, Service
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessService
- **Reputability tier:** industry_standard
- **Domain:** procurement

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 225 (batch 1)
