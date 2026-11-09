# dea:metric-fill-rate

Candidate Performance Metric record for **Fill Rate** (FR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-fill-rate`
- **Name:** Fill Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FR

## 2. Definition

A Supply Chain indicator, Fill Rate (FR) quantifies the quality of outputs and outcomes. Its calculation is Items Shipped from Stock / Items Ordered, measured in percent (%). Its value drives prioritization and resource reallocation among competing initiatives. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of customer demand satisfied immediately from stock. It matters because it is the customer-felt availability metric that competes with rivals' shelves. Gaming risk includes counting a line as filled when only partial quantity ships, or defining fill at warehouse rather than order level. Read with Stockout Rate and Inventory Days of Supply to confirm availability is achieved efficiently rather than by overstocking.

## Formula

```
FR = Items Shipped from Stock / Items Ordered
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 176 (batch 1)
