# dea:metric-on-time-delivery-semiconductor

Candidate Performance Metric record for **On-Time Delivery (Semiconductor)** (OTD-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-on-time-delivery-semiconductor`
- **Name:** On-Time Delivery (Semiconductor)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** OTD-S

## 2. Definition

A Semiconductor & Electronics indicator, On-Time Delivery (Semiconductor) (OTD-S) quantifies the quality of outputs and outcomes. Its value drives prioritization and resource reallocation among competing initiatives. Its calculation is Order Lines Delivered on Commit Date / Order Lines, measured in percent (%). Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Electronics & semiconductors practice.

## 3. Context

Measures the share of wafer or chip orders delivered on committed dates. It matters because fab capacity cycles make delivery reliability the differentiator for long-term supply agreements. Easy date commitments inflate the rate while hiding real responsiveness. Read with Cycle Time Line Yield and Customer Commit Attainment to confirm delivery promises are competitive.

## Formula

```
OTD-S = Order Lines Delivered on Commit Date / Order Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** semiconductor_electronics
- **Sector:** electronics_semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 908 (batch 3)
