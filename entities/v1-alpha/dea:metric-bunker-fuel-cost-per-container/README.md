# dea:metric-bunker-fuel-cost-per-container

Candidate Performance Metric record for **Bunker Fuel Cost per Container** (BFCC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bunker-fuel-cost-per-container`
- **Name:** Bunker Fuel Cost per Container
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BFCC

## 2. Definition

Bunker Fuel Cost per Container (BFCC) addresses how efficiently resources are converted into outputs and is a fixture of maritime & shipping reporting. It is computed as Fuel Cost / Containers Carried, expressed in currency per unit. Its use is concentrated in Maritime & shipping. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Bunker fuel cost per container measures the fuel expense allocated to each box moved, and it is the metric where shipping economics meet emissions regulation - fuel is a large share of vessel operating cost, so per-container fuel economics determine route viability, vessel speed (slow steaming), and the financial calculus of IMO 2020 low-sulfur rules and CII efficiency requirements. The allocation subtlety is real: fuel per container depends on utilization (a full ship spreads fuel across more boxes), vessel size (larger ships are more fuel-efficient per box), and speed (fuel burn rises with the cube of speed roughly, so slow steaming is a powerful lever). Read with fuel efficiency by vessel class, slow-steaming prevalence, utilization-adjusted fuel cost trends, and scrubber or alternative-fuel cost differentials.

## Formula

```
Fuel Cost / Containers Carried
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
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maritime_shipping
- **Sector:** maritime_shipping

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 982 (batch 3)
