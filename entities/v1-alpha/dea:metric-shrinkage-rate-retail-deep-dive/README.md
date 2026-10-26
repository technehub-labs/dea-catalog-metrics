# dea:metric-shrinkage-rate-retail-deep-dive

Candidate Performance Metric record for **Shrinkage Rate (Retail Deep Dive)** (SHR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-shrinkage-rate-retail-deep-dive`
- **Name:** Shrinkage Rate (Retail Deep Dive)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SHR

## 2. Definition

Shrinkage Rate (Retail Deep Dive) (SHR) captures exposure to adverse outcomes for organizations tracking retail standard measures. It is defined as Inventory Loss / Sales; the result is stated in percent (%). In Retail & E-commerce, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Measures inventory lost to theft, damage, and administrative error. Shrink is the silent tax on retail margin. Shrink pushed between period-end counts by deferring known losses smooths reality. Read with inventory record accuracy and cycle count compliance.

## Formula

```
Inventory Loss / Sales
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** customer
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Outcome
- **Reputability tier:** industry_standard
- **Domain:** retail_standard_measures
- **Sector:** retail_e_commerce

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4306 (batch 10)
