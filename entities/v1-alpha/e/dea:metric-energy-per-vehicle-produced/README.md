# dea:metric-energy-per-vehicle-produced

Candidate Performance Metric record for **Energy per Vehicle Produced** (EPV) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-energy-per-vehicle-produced`
- **Name:** Energy per Vehicle Produced
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** EPV

## 2. Definition

Within Automotive, Energy per Vehicle Produced (EPV) is used to gauge environmental and social sustainability performance. The formula is Energy Consumed / Vehicles Produced - reported in ratio (x:1 or x). It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. It is a standard measure in the Automotive sector.

## 3. Context

Measures energy consumed per vehicle built. It matters because it is the plant-level efficiency and emissions lever in automotive manufacturing. Purchased-vehicle energy accounting can blur the boundary when assembly is outsourced. Read with Energy Cost per Unit and plant-level emissions data to confirm reductions are genuine.

## Formula

```
EPV = Energy Consumed / Vehicles Produced
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** sustainability
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** automotive
- **Sector:** automotive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 750 (batch 2)
