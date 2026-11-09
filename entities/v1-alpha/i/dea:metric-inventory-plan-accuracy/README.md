# dea:metric-inventory-plan-accuracy

Candidate Performance Metric record for **Inventory Plan Accuracy** (IPA-S) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-inventory-plan-accuracy`
- **Name:** Inventory Plan Accuracy
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** IPA-S

## 2. Definition

Inventory Plan Accuracy (IPA-S) addresses the quality of outputs and outcomes and is a fixture of sales & operations planning reporting. It is defined as Inventory per Plan / Actual Inventory; the result is stated in percent (%). It bridges daily operations and executive reporting, giving managers a lever to pull within a quarter. It is managed toward a defined target band rather than an extreme - both overshoot and undershoot can signal problems. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how closely actual inventory lands against the S&OP inventory plan. It matters because inventory drift signals broken planning or execution. Accuracy can be improved by planning wide ranges that include any outcome. Read with Inventory Days of Supply and Demand Plan Bias to confirm accuracy reflects planning discipline.

## Formula

```
IPA-S = Inventory per Plan / Actual Inventory
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** organizational_unit
- **Directionality:** target_band
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** sales_operations_planning

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1292 (batch 5)
