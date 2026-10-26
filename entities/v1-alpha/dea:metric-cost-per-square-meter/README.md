# dea:metric-cost-per-square-meter

Candidate Performance Metric record for **Cost per Square Meter** (CPSM) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-square-meter`
- **Name:** Cost per Square Meter
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** CPSM

## 2. Definition

A Facilities & Real Estate indicator, Cost per Square Meter (CPSM) quantifies how efficiently resources are converted into outputs. It is defined as Total Facilities Cost / Total Floor Area; the result is stated in currency per unit. It is applied across virtually every sector. Its trend is watched by senior leadership as an early signal of structural performance shifts. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Total occupancy cost - rent, service charges, utilities, maintenance, and fit-out amortization - divided by floor area, the standard unit-cost metric of the corporate real estate function. Its strategic significance is benchmark currency: portfolio decisions, consolidation cases, and lease-versus-own analyses are all argued in this metric's terms, and a gap to market benchmarks for comparable space is either a negotiation opportunity or a consolidation signal. The definitional discipline is what the cost base includes: buildings quoted with full-service rent differ from net-quoted by multiples of the metric's own movement, so comparisons require reconciling the cost stack before the number means anything. Read with utilization: a low cost per square meter at low occupancy is expensive per actually-used workstation, which is the metric that carries the hybrid-era truth.

## Formula

```
Total Facilities Cost / Total Floor Area
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
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 449 (batch 1)
