# dea:metric-manufacturing-cost-per-unit

Candidate Performance Metric record for **Manufacturing Cost per Unit** (MCU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-manufacturing-cost-per-unit`
- **Name:** Manufacturing Cost per Unit
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** MCU

## 2. Definition

Within Manufacturing, Manufacturing Cost per Unit (MCU) is used to gauge how efficiently resources are converted into outputs. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Total Manufacturing Cost / Units Produced; the result is stated in currency per unit. It should be driven down, since lower readings signal healthier performance. In Manufacturing, it is a recognized element of the standard performance toolkit.

## 3. Context

Total manufacturing cost - materials, labor, and manufacturing overhead - divided by good units produced, the standard costing metric that sits at the heart of every product profitability discussion. Its strategic content is decomposition: material cost moves with procurement and design choices, direct labor with productivity and wage rates, and overhead absorption with volume, and only the split tells you which lever a change actually pulled. That volume-sensitivity is the trap: cost per unit falls when volume rises purely through overhead spreading - a benefit that reverses exactly when volumes drop - so standard-cost variances matter more than the level. It is also the number that decides make-versus-buy, transfer pricing, and eventually price floors, which is why finance and operations argue over its allocation conventions.

## Formula

```
MCU = Total Manufacturing Cost / Units Produced
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 258 (batch 1)
