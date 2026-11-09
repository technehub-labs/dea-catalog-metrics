# dea:metric-warranty-cost-per-vehicle

Candidate Performance Metric record for **Warranty Cost per Vehicle** (WCPV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-warranty-cost-per-vehicle`
- **Name:** Warranty Cost per Vehicle
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WCPV

## 2. Definition

Within Automotive, Warranty Cost per Vehicle (WCPV) is used to gauge exposure to adverse outcomes. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Total Warranty Cost / Vehicles Sold, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Automotive.

## 3. Context

Warranty cost per vehicle is the manufacturer's accrual for repairs per unit sold, and it is one of the most direct links between engineering design quality and the income statement - each basis point of warranty cost is a direct hit to automotive operating margin, which is why warranty reserves are one of the most scrutinized lines in automaker financials. The metric is a lagging composite of design quality, supplier quality, and assembly quality, making root-cause decomposition essential. Read with claims per vehicle, cost per claim, and per-component claim Pareto analysis to distinguish a widespread design issue from a single supplier problem.

## Formula

```
WCPV = Total Warranty Cost / Vehicles Sold
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 740 (batch 2)
