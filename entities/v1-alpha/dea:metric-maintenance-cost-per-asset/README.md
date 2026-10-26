# dea:metric-maintenance-cost-per-asset

Candidate Performance Metric record for **Maintenance Cost per Asset** (MCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-maintenance-cost-per-asset`
- **Name:** Maintenance Cost per Asset
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** MCA

## 2. Definition

Within Maintenance & Reliability, Maintenance Cost per Asset (MCA) is used to gauge how efficiently resources are converted into outputs. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. The formula is Total Maintenance Cost / Assets in Service - reported in currency per unit. It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Manufacturing sector.

## 3. Context

Measures average maintenance spend per asset or per unit of replacement value. It matters because it benchmarks whether maintenance is preventive or reactive in character. Low values can reflect deferred maintenance that will surface as future emergency cost and downtime. Read with Emergency Work Order Rate and Availability to judge whether low spend is efficiency or dangerous deferral.

## Formula

```
Total Maintenance Cost / Assets in Service
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
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 270 (batch 1)
