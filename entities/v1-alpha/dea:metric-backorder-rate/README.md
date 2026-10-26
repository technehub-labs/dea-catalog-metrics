# dea:metric-backorder-rate

Candidate Performance Metric record for **Backorder Rate** (BOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-backorder-rate`
- **Name:** Backorder Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BOR

## 2. Definition

A Operations indicator, Backorder Rate (BOR) quantifies exposure to adverse outcomes. Its calculation is Backordered Lines / Total Order Lines, measured in percent (%). It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of order lines that cannot be fulfilled from stock at order time. It matters because backorders directly drive customer frustration and defection to competitors. Gaming risk includes accepting orders into a system that quietly holds them until stock arrives, hiding true backorders. Read with Fill Rate and Inventory Days of Supply to trace root causes in inventory positioning.

## Formula

```
Backordered Lines / Total Order Lines
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 161 (batch 1)
