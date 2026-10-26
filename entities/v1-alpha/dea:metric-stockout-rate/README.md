# dea:metric-stockout-rate

Candidate Performance Metric record for **Stockout Rate** (SOR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-stockout-rate`
- **Name:** Stockout Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SOR

## 2. Definition

A Supply Chain indicator, Stockout Rate (SOR) quantifies exposure to adverse outcomes. It is defined as Stockout Events / Total Demand Events; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of demand events or SKUs that hit zero stock. It matters because stockouts are lost sales today and customer defection tomorrow. It can be gamed by reclassifying stockouts as demand smoothing, or only measuring top SKUs where buffers are generous. Read with Fill Rate and Backorder Rate to see the full availability picture including unmet demand handling.

## Formula

```
Stockout Events / Total Demand Events
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** supply_chain

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 180 (batch 1)
