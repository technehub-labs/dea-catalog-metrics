# dea:metric-water-intensity

Candidate Performance Metric record for **Water Intensity** (WI2) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-water-intensity`
- **Name:** Water Intensity
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WI2

## 2. Definition

Within Sustainability & ESG, Water Intensity (WI2) is used to gauge environmental and social sustainability performance. It is computed as Water Withdrawn / Unit of Output, expressed in ratio (x:1 or x). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures water consumed per unit of output. It matters because water stress is a material operating and reputational risk in many regions. Gaming risk includes excluding abstraction from own wells or counting once-through water as recycled. Read with Water Recycling Rate and local water stress context to judge whether intensity is low enough for the basin.

## Formula

```
WI2 = Water Withdrawn / Unit of Output
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** sustainability
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** sustainability_esg

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 418 (batch 1)
