# dea:metric-yield-to-capacity-ratio

Candidate Performance Metric record for **Yield-to-Capacity Ratio** (YCR-SS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-yield-to-capacity-ratio`
- **Name:** Yield-to-Capacity Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** YCR-SS

## 2. Definition

Within Process Capability & Six Sigma (Deep Dive), Yield-to-Capacity Ratio (YCR-SS) is used to gauge how efficiently resources are converted into outputs. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. The formula is Good Units Produced / Theoretical Maximum Capacity - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Manufacturing sector.

## 3. Context

Measures the share of installed capacity actually converting to good output. It separates capability losses (yield) from utilization losses (demand). Ratio improved by slowing the line is capacity bought with throughput. Read with first pass yield and capacity utilization vs. demand.

## Formula

```
YCR-SS = Good Units Produced / Theoretical Maximum Capacity
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** capability
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** process_capability_six_sigma_deep_dive
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4091 (batch 9)
