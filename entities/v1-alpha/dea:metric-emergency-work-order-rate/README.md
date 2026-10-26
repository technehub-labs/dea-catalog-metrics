# dea:metric-emergency-work-order-rate

Candidate Performance Metric record for **Emergency Work Order Rate** (EWR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-emergency-work-order-rate`
- **Name:** Emergency Work Order Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** EWR

## 2. Definition

Emergency Work Order Rate (EWR) captures exposure to adverse outcomes for organizations tracking maintenance & reliability. It is computed as Emergency Work Orders / Total Work Orders, expressed in percent (%). It is reviewed at cadence by planning owners to correct course before issues become strategic. Lower values are better; each reduction is an improvement. Its use is concentrated in Manufacturing.

## 3. Context

Measures the share of maintenance work orders that are emergency or breakdown-driven. It matters because reactive maintenance costs multiples of planned work and signals reliability failure. Teams can reclassify urgent jobs as planned to green the metric. Read with Preventive Maintenance Compliance and Asset Failure Recurrence Rate to confirm the reactive share is truly falling.

## Formula

```
Emergency Work Orders / Total Work Orders
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
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 272 (batch 1)
