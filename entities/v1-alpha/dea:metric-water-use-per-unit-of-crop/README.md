# dea:metric-water-use-per-unit-of-crop

Candidate Performance Metric record for **Water Use per Unit of Crop** (WUC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-water-use-per-unit-of-crop`
- **Name:** Water Use per Unit of Crop
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WUC

## 2. Definition

Water Use per Unit of Crop (WUC) addresses environmental and social sustainability performance and is a fixture of agriculture & food processing reporting. It is computed as Irrigation Water / Crop Mass Produced, expressed in ratio (x:1 or x). Its use is concentrated in Agriculture & food. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures irrigation water consumed per unit of crop output. It matters because agriculture dominates freshwater use and water productivity defines sustainability in stressed basins. Denominator choice (yield vs biomass vs revenue) can swing the metric to taste. Read with Water Intensity and local basin stress context to judge whether usage is defensible where it matters.

## Formula

```
WUC = Irrigation Water / Crop Mass Produced
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
- **Domain:** agriculture_food_processing
- **Sector:** agriculture_food

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 732 (batch 2)
