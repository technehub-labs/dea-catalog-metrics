# dea:metric-die-yield-deep-dive

Candidate Performance Metric record for **Die Yield (Deep Dive)** (DYL-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-die-yield-deep-dive`
- **Name:** Die Yield (Deep Dive)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DYL-D

## 2. Definition

Within Semiconductor Manufacturing (Deep Dive), Die Yield (Deep Dive) (DYL-D) is used to gauge the quality of outputs and outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Good Die / Gross Die per Wafer, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Semiconductors.

## 3. Context

Measures functional dies against total dies per wafer. It is the economics core of semiconductors: yield is the multiplication factor on enormous fixed costs, and a few points of die yield can swing between profit and loss on the same volume. Yield breakdown by defect mechanism directs the improvement roadmap. Read with defect density (Deep Dive) and test first pass yield (Deep Dive).

## Formula

```
DYL-D = Good Die / Gross Die per Wafer
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2373 (batch 6)
