# dea:metric-labor-cost-per-order-shipped

Candidate Performance Metric record for **Labor Cost per Order Shipped** (LCPO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-labor-cost-per-order-shipped`
- **Name:** Labor Cost per Order Shipped
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** LCPO

## 2. Definition

A Warehousing indicator, Labor Cost per Order Shipped (LCPO) quantifies how efficiently resources are converted into outputs. The formula is Warehouse Labor Cost / Orders Shipped - reported in currency per unit. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures average warehouse labor cost for each order fulfilled. It matters because it is the dominant controllable cost in fulfillment economics. Gaming risk includes cutting training or quality checks to speed picks, deferring error costs to returns handling. Read with Order Picking Accuracy and Order Fulfillment Cycle Time to confirm cost cuts do not buy error rates.

## Formula

```
Warehouse Labor Cost / Orders Shipped
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** warehousing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 217 (batch 1)
