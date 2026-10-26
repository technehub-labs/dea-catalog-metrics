# dea:metric-warranty-cost-per-vehicle-deep-dive

Candidate Performance Metric record for **Warranty Cost per Vehicle (Deep Dive)** (WCPV-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-warranty-cost-per-vehicle-deep-dive`
- **Name:** Warranty Cost per Vehicle (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** WCPV-D

## 2. Definition

Warranty Cost per Vehicle (Deep Dive) (WCPV-D) measures exposure to adverse outcomes in the Automotive Manufacturing (Deep Dive) domain. The formula is Warranty Spend / Vehicles Sold - reported in currency per unit. It is a standard measure in the Automotive sector. It carries weight in boardroom and executive reviews, where it anchors cross-organization trade-offs. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures warranty spend normalized by vehicles sold. It is the long-delay truth serum of automotive quality: design and manufacturing decisions surface here years later, and per-vehicle warranty cost trends predict both profitability and brand equity trajectories. Aging claims analysis (maturation curves) matters, since early-life rates extrapolate poorly. Read with recall history and supplier quality warranty recovery.

## Formula

```
Warranty Spend / Vehicles Sold
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive_manufacturing_deep_dive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2363 (batch 6)
