# dea:metric-line-yield-deep-dive

Candidate Performance Metric record for **Line Yield (Deep Dive)** (LYL-D) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-line-yield-deep-dive`
- **Name:** Line Yield (Deep Dive)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** LYL-D

## 2. Definition

A Semiconductor Manufacturing (Deep Dive) indicator, Line Yield (Deep Dive) (LYL-D) quantifies the quality of outputs and outcomes. It is computed as Wafers Completed / Wafers Started, expressed in percent (%). Its use is concentrated in Semiconductors. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures wafers surviving the full process flow without scrapping. It captures cumulative process loss - particles, misprocessing, breakage - across hundreds of steps, and it is the fab-level complement to die yield: line yield protects the material investment before device functionality is even tested. Pareto analysis by step identifies the loss concentration. Read with die yield (Deep Dive) and fab constraint-step capability.

## Formula

```
Wafers Completed / Wafers Started
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** product_or_service
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** semiconductor_manufacturing_deep_dive
- **Sector:** semiconductors

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2374 (batch 6)
