# dea:metric-harvest-loss-rate-deep-dive

Candidate Performance Metric record for **Harvest Loss Rate (Deep Dive)** (HLR-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-harvest-loss-rate-deep-dive`
- **Name:** Harvest Loss Rate (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** HLR-D

## 2. Definition

Harvest Loss Rate (Deep Dive) (HLR-D) addresses how efficiently resources are converted into outputs and is a fixture of agriculture & agronomy (deep dive) reporting. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Field Losses / Potential Yield - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Agriculture sector.

## Formula

```
HLR-D = Field Losses / Potential Yield
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** agriculture_agronomy_deep_dive
- **Sector:** agriculture

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2317 (batch 6)
