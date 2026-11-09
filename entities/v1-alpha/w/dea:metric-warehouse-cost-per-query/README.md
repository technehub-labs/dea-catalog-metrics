# dea:metric-warehouse-cost-per-query

Candidate Performance Metric record for **Warehouse Cost per Query** (WCQ-DS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-warehouse-cost-per-query`
- **Name:** Warehouse Cost per Query
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WCQ-DS

## 2. Definition

Within Data Science & Analytics Operations, Warehouse Cost per Query (WCQ-DS) is used to gauge how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Warehouse Spend / Queries Executed - reported in currency per unit. It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## Formula

```
WCQ-DS = Warehouse Spend / Queries Executed
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** data_science_analytics_operations

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2601 (batch 7)
