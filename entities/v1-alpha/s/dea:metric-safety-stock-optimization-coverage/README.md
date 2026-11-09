# dea:metric-safety-stock-optimization-coverage

Candidate Performance Metric record for **Safety Stock Optimization Coverage** (SSOC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-safety-stock-optimization-coverage`
- **Name:** Safety Stock Optimization Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SSOC

## 2. Definition

Safety Stock Optimization Coverage (SSOC) measures how efficiently resources are converted into outputs in the Supply Chain Standard Measures (Deep Dive) domain. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is SKUs with Statistically Sized Safety Stock / SKUs - reported in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
SSOC = SKUs with Statistically Sized Safety Stock / SKUs
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain_standard_measures_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4270 (batch 10)
