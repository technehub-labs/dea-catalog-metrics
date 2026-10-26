# dea:metric-field-service-cost-per-work-order

Candidate Performance Metric record for **Field Service Cost per Work Order** (FSCWO) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-field-service-cost-per-work-order`
- **Name:** Field Service Cost per Work Order
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** FSCWO

## 2. Definition

Field Service Cost per Work Order (FSCWO) measures how efficiently resources are converted into outputs in the Field Service & Asset Performance domain. It is defined as Field Cost / Completed Work Orders; the result is stated in currency per unit. It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
FSCWO = Field Cost / Completed Work Orders
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** operations
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** field_service_asset_performance

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3389 (batch 7)
