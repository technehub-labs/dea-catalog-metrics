# dea:metric-shrink-rate-retail

Candidate Performance Metric record for **Shrink Rate (Retail)** (ShR-R) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shrink-rate-retail`
- **Name:** Shrink Rate (Retail)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ShR-R

## 2. Definition

A Retail & E-commerce indicator, Shrink Rate (Retail) (ShR-R) quantifies exposure to adverse outcomes. The formula is (Recorded Inventory - Counted Inventory) / Sales - reported in percent (%). It is a standard measure in the Retail sector. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures inventory loss from theft, damage, and error as a share of sales. It matters because shrink is a pure margin leak, and rising shrink often signals process and security decay. It can be masked by raising ticket prices to absorb expected shrink invisibly. Read with Shrinkage Rate and cycle count accuracy to confirm losses are falling, not priced in.

## Formula

```
ShR-R = (Recorded Inventory - Counted Inventory) / Sales
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** retail_e_commerce
- **Sector:** retail

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 494 (batch 1)
