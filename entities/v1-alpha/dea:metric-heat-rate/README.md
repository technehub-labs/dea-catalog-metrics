# dea:metric-heat-rate

Candidate Performance Metric record for **Heat Rate** (HR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-heat-rate`
- **Name:** Heat Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** HR

## 2. Definition

Heat Rate (HR) addresses how efficiently resources are converted into outputs and is a fixture of energy & utilities reporting. It is defined as Fuel Energy Input per Unit of Electricity Generated; the result is stated in ratio (x:1 or x). Its trend is watched by senior leadership as an early signal of structural performance shifts. Lower values are better; each reduction is an improvement. In Energy & utilities, it is a recognized element of the standard performance toolkit.

## 3. Context

The fuel-energy input required per unit of electricity generated - the inverse-form expression of thermal efficiency that the power industry prefers, in the same unit-per-unit convention the sector applies everywhere else. Its strategic weight is the direct arithmetic between it and marginal cost: at a given fuel price, heat rate times fuel price is the fuel cost of a megawatt-hour, which is the number that dispatch decisions, bid strategies, and asset valuations all run on - a heat-rate difference between plants is a competitiveness difference in the market's own currency. Regulatory usage gives it a second life: heat-rate benchmarks (implied and reference) appear in capacity-market and dispatch modeling, which means this technical metric also functions as a policy parameter. The measurement honesty requirement is standard conditions: uncorrected heat rates vary with temperature and load by more than genuine changes in plant condition.

## Formula

```
Fuel Energy Input per Unit of Electricity Generated
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_utilities
- **Sector:** energy_utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 441 (batch 1)
