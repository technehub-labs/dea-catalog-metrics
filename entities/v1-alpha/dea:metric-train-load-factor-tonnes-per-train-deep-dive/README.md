# dea:metric-train-load-factor-tonnes-per-train-deep-dive

Candidate Performance Metric record for **Train Load Factor - Tonnes per Train (Deep Dive)** (TLF-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-train-load-factor-tonnes-per-train-deep-dive`
- **Name:** Train Load Factor - Tonnes per Train (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** TLF-D

## 2. Definition

Within Rail Freight (Deep Dive), Train Load Factor - Tonnes per Train (Deep Dive) (TLF-D) is used to gauge how efficiently resources are converted into outputs. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Net Tonnes / Trains, measured in tonnes. Improvement means raising this figure toward best-in-class levels. It originates from and is most used in Rail practice.

## 3. Context

Measures average train payload against capacity. It is the core productivity metric of rail freight economics: fixed crew and path costs spread over payload, and under-loaded trains are the quiet margin leak. Load factors must be read against service-type (unit trains versus manifest) and network congestion effects, since interlining splits loads. Read with network velocity (Deep Dive) and path utilization.

## Formula

```
Net Tonnes / Trains
```

## Unit

- **Unit reference:** `dea:unit-tonne`
- **Unit:** tonne
- **Unit label (as published):** tonnes

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** rail_freight_deep_dive
- **Sector:** rail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2421 (batch 6)
