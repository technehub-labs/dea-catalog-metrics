# dea:metric-grid-balancing-cost

Candidate Performance Metric record for **Grid Balancing Cost** (GBC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-grid-balancing-cost`
- **Name:** Grid Balancing Cost
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** GBC

## 2. Definition

A Energy & Utilities indicator, Grid Balancing Cost (GBC) quantifies how efficiently resources are converted into outputs. It is computed as Cost of Balancing Operations / Energy Delivered, expressed in currency per unit. Its use is concentrated in Energy & utilities. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the cost of matching electricity supply and demand in real time. It matters because balancing costs explode as intermittent renewables grow, so managing them is central to transition economics. Costs can be shifted into curtailment payments or capacity contracts that hide the true figure. Read with Unplanned Outage Rate and Renewable Penetration metrics to judge whether balancing costs are being managed or deferred.

## Formula

```
Cost of Balancing Operations / Energy Delivered
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 447 (batch 1)
