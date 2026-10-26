# dea:metric-days-inventory-outstanding

Candidate Performance Metric record for **Days Inventory Outstanding** (DIO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-days-inventory-outstanding`
- **Name:** Days Inventory Outstanding
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DIO

## 2. Definition

A Finance & Accounting indicator, Days Inventory Outstanding (DIO) quantifies how efficiently resources are converted into outputs. Its calculation is (Inventory / Cost of Goods Sold) x 365, measured in days. It is applied across virtually every sector. Its value drives prioritization and resource reallocation among competing initiatives. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the average number of days inventory sits before being sold. It matters because inventory ties up cash and risks obsolescence, especially in fast-moving goods. Teams can cut it by under-stocking, which spikes stockouts and backorders later. Read with Inventory Turnover Ratio and Stockout Rate to ensure leaner inventory is not simply deferring lost sales.

## Formula

```
(Inventory / Cost of Goods Sold) x 365
```

## Unit

- **Unit reference:** `dea:unit-days`
- **Unit:** days
- **Unit label (as published):** days

## Classification

- **Subject classification:** financial
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** finance_accounting

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 25 (batch 1)
