# dea:metric-excess-and-obsolete-inventory-ratio

Candidate Performance Metric record for **Excess and Obsolete Inventory Ratio** (EOIR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-excess-and-obsolete-inventory-ratio`
- **Name:** Excess and Obsolete Inventory Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EOIR

## 2. Definition

Excess and Obsolete Inventory Ratio (EOIR) addresses exposure to adverse outcomes and is a fixture of sales & operations planning reporting. It is defined as Excess and Obsolete Inventory Value / Total Inventory Value; the result is stated in percent (%). It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of inventory value that is excess to foreseeable demand, obsolete, or aged beyond policy. It is the scar tissue of forecast error, product transitions, and buying discipline, and it quietly ties up warehouse space and cash that growth needs. Definitional traps include coverage thresholds set generously and reclassification games where excess stock is re-labeled after minor modification. Read with consensus forecast accuracy (S&OP) and inventory write-off trends.

## Formula

```
EOIR = Excess and Obsolete Inventory Value / Total Inventory Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1296 (batch 5)
