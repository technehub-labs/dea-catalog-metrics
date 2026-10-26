# dea:metric-inventory-days-of-supply

Candidate Performance Metric record for **Inventory Days of Supply** (IDS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-inventory-days-of-supply`
- **Name:** Inventory Days of Supply
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** IDS

## 2. Definition

Inventory Days of Supply (IDS) measures the utilization or availability of capacity in the Supply Chain domain. The formula is Average Inventory Value / Average Daily Usage - reported in days. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures days of forward demand covered by current inventory. It matters because it translates stock into runway and exposes over- and under-positioning. Gaming risk includes understating forward demand to make coverage look lean, or using optimistic seasonality assumptions. Read with Fill Rate and Inventory Turnover Ratio to check positioning against actual availability outcomes.

## Formula

```
Average Inventory Value / Average Daily Usage
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 178 (batch 1)
