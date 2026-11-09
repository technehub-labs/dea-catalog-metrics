# dea:metric-container-dwell-time-deep-dive

Candidate Performance Metric record for **Container Dwell Time (Deep Dive)** (CDT-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-container-dwell-time-deep-dive`
- **Name:** Container Dwell Time (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** CDT-D

## 2. Definition

Container Dwell Time (Deep Dive) (CDT-D) captures how efficiently resources are converted into outputs for organizations tracking maritime shipping (deep dive). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Days Container in Yard before Pickup - reported in days. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Maritime sector.

## Formula

```
CDT-D = Days Container in Yard before Pickup
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
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping_deep_dive
- **Sector:** maritime

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2434 (batch 6)
