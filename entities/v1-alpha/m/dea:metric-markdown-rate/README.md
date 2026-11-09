# dea:metric-markdown-rate

Candidate Performance Metric record for **Markdown Rate** (MDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-markdown-rate`
- **Name:** Markdown Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MDR

## 2. Definition

Markdown Rate (MDR) captures the economic value created or preserved for organizations tracking retail & e-commerce. Its calculation is Markdown Value / Gross Sales Value, measured in percent (%). It originates from and is most used in Retail practice. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of sales or inventory sold below original ticket price. It matters because markdowns flow directly to gross margin and signal buying or pricing mistakes. Gaming risk includes re-pricing items before launch so the first ticket already embeds markdown cushion. Read with Sell-Through Rate and Gross Margin Return on Inventory to confirm margin is protected honestly.

## Formula

```
MDR = Markdown Value / Gross Sales Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** value_delivery
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 493 (batch 1)
