# dea:metric-shrinkage-rate

Candidate Performance Metric record for **Shrinkage Rate** (ShR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shrinkage-rate`
- **Name:** Shrinkage Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** ShR

## 2. Definition

Within Warehousing, Shrinkage Rate (ShR) is used to gauge exposure to adverse outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Unexplained Inventory Loss Value / Inventory Value, expressed in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures inventory loss from theft, damage, and administrative error as a share of inventory value. It matters because shrink is a pure profit leak and a signal of process and security weakness. It can be masked by adjusting cycle-count baselines or writing losses into obsolescence accounting. Read with Inventory Record Accuracy and cycle count findings to see whether shrink is falling or just relabeled.

## Formula

```
Unexplained Inventory Loss Value / Inventory Value
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 218 (batch 1)
