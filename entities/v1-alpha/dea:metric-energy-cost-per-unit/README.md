# dea:metric-energy-cost-per-unit

Candidate Performance Metric record for **Energy Cost per Unit** (ECU) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-energy-cost-per-unit`
- **Name:** Energy Cost per Unit
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** ECU

## 2. Definition

Within Manufacturing, Energy Cost per Unit (ECU) is used to gauge how efficiently resources are converted into outputs. It is reviewed at cadence by planning owners to correct course before issues become strategic. It is computed as Total Energy Cost / Units Produced, expressed in currency per unit. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Manufacturing.

## 3. Context

Measures energy cost per unit produced. It matters because energy is a major controllable cost and a direct emissions driver. Teams can cut it cosmetically by shifting production to off-peak pricing while total consumption rises. Read with Energy Intensity and Total Cost of Ownership for assets to check unit cost gains track real efficiency.

## Formula

```
Total Energy Cost / Units Produced
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
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** manufacturing
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 264 (batch 1)
