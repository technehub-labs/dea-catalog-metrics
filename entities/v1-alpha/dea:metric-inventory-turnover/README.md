# dea:metric-inventory-turnover

Candidate Performance Metric record for **Inventory Turnover** (ITR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-inventory-turnover`
- **Name:** Inventory Turnover
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ITR

## 2. Definition

Within Supply Chain, Inventory Turnover (ITR) is used to gauge how efficiently resources are converted into outputs. Its calculation is Cost of Goods Sold / Average Inventory, measured in times per period. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Cost of goods sold divided by average inventory - how many times per year the stock is sold and replaced, the classic gauge of supply chain velocity. Higher turns mean less capital tied up, less obsolescence, and lower storage cost per unit sold, but past a point they mean stockouts and expediting, and finding that point is the strategic task. The metric disciplines every inventory philosophy from lean to resilience: companies that hold strategic buffers after supply shocks should expect turns to fall and should say so, rather than let the metric silently punish a deliberate policy. Read the composition - raw materials, work in process, finished goods move for different reasons - and use gross margin to convert turns into days, which is the cross-industry comparable form.

## Formula

```
Cost of Goods Sold / Average Inventory
```

## Unit

- **Unit reference:** `dea:unit-times`
- **Unit:** times
- **Unit label (as published):** times per period

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 177 (batch 1)
