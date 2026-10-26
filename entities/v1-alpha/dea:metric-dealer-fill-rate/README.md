# dea:metric-dealer-fill-rate

Candidate Performance Metric record for **Dealer Fill Rate** (DFR-A) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dealer-fill-rate`
- **Name:** Dealer Fill Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** DFR-A

## 2. Definition

Within Automotive, Dealer Fill Rate (DFR-A) is used to gauge the quality of outputs and outcomes. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Vehicle Orders Filled from Stock / Vehicle Orders, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Automotive.

## 3. Context

Measures the share of dealer vehicle or parts orders fulfilled promptly from manufacturer stock. It matters because dealer inventory health drives customer wait times and channel loyalty. Fill can be improved by pushing excess stock onto dealers rather than true availability. Read with Days Supply at Dealer and Dealer Inventory Turnover to confirm manufacturer performance is not being displaced downstream.

## Formula

```
Vehicle Orders Filled from Stock / Vehicle Orders
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 746 (batch 2)
