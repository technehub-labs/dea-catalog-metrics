# dea:metric-target-costing-gap

Candidate Performance Metric record for **Target Costing Gap** (TCG) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-target-costing-gap`
- **Name:** Target Costing Gap
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** TCG

## 2. Definition

Target Costing Gap (TCG) captures the economic value created or preserved for organizations tracking product costing & margin management. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as (Target Cost - Current Cost) / Target Cost; the result is stated in percent (%). It should be driven down, since lower readings signal healthier performance. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Compares the allowable cost of a product, given its target price and required margin, against the currently achievable cost, quantifying how much engineering and sourcing work must close the gap before launch. It matters because it forces cost discipline at design stage, where the large majority of lifecycle cost is committed. Be honest about optimistic should-cost estimates and gaps closed by spec-cutting that erodes value perception. Read with cost reduction program realization and gross margin per product line.

## Formula

```
(Target Cost - Current Cost) / Target Cost
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** financial
- **Purpose classification:** value_delivery
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:Service
- **Reputability tier:** industry_standard
- **Domain:** product_costing_margin_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1243 (batch 4)
