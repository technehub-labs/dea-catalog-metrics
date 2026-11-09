# dea:metric-landfill-rate

Candidate Performance Metric record for **Landfill Rate** (LFR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-landfill-rate`
- **Name:** Landfill Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LFR

## 2. Definition

Landfill Rate (LFR) measures environmental and social sustainability performance in the Sustainability & ESG domain. It is computed as Landfilled Waste / Total Waste, expressed in percent (%). It is applied across virtually every sector. It is reviewed at cadence by planning owners to correct course before issues become strategic. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures the share of total waste sent to landfill. It matters because landfill is the worst outcome environmentally and increasingly the most expensive route. Teams can shrink it cosmetically by shipping waste to incineration and calling it recovery. Read with Waste Diversion Rate and Waste Intensity to verify the reduction reflects source reduction, not disposal reclassification.

## Formula

```
LFR = Landfilled Waste / Total Waste
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 422 (batch 1)
