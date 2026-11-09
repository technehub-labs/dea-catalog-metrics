# dea:metric-marketing-mix-model-alignment

Candidate Performance Metric record for **Marketing Mix Model Alignment** (MMA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-marketing-mix-model-alignment`
- **Name:** Marketing Mix Model Alignment
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MMA

## 2. Definition

A Marketing Attribution & Analytics indicator, Marketing Mix Model Alignment (MMA) quantifies the economic value created or preserved. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Channel Spend per Model Optimum / Actual Channel Spend, expressed in ratio (x:1 or x). The objective is neither maximization nor minimization but staying within an agreed operating band. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how closely MMM-derived budget guidance and channel effect estimates are followed in planning, and how well MMM results reconcile with experimental ground truth. Models that are ignored, or that disagree with incrementality tests, destroy the analytics investment's value. Watch for one-off recalibrations treated as permanent truth, and channel fragmentation degrading model resolution. Read with incrementality rate and return on ad spend at portfolio level.

## Formula

```
MMA = Channel Spend per Model Optimum / Actual Channel Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** strategic
- **Measurable entity kind:** dea:DataEntity
- **Reputability tier:** industry_standard
- **Domain:** marketing_attribution_analytics

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1492 (batch 5)
