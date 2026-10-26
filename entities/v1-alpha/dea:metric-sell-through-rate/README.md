# dea:metric-sell-through-rate

Candidate Performance Metric record for **Sell-Through Rate** (STR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sell-through-rate`
- **Name:** Sell-Through Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** STR

## 2. Definition

Within Retail & E-commerce, Sell-Through Rate (STR) is used to gauge how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Units Sold / Units Available for Sale, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Retail.

## 3. Context

Measures the share of received inventory sold at full or planned price within the season. It matters because it is the cleanest read on buying accuracy and markdown risk. Teams can improve it by under-buying, protecting the metric while losing sales to stockouts. Read with Markdown Rate and Inventory Days of Supply to balance sell-through against availability and margin.

## Formula

```
Units Sold / Units Available for Sale
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 492 (batch 1)
