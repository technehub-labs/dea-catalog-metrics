# dea:metric-capacity-factor-renewables

Candidate Performance Metric record for **Capacity Factor (Renewables)** (CFR-E) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-capacity-factor-renewables`
- **Name:** Capacity Factor (Renewables)
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CFR-E

## 2. Definition

Capacity Factor (Renewables) (CFR-E) measures the utilization or availability of capacity in the Energy Transition & Renewables domain. It is defined as Actual Generation / Nameplate Generation Potential; the result is stated in percent (%). In Renewable energy, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Capacity factor measures actual energy production against theoretical maximum at full rated output, and it is the utilization metric that determines renewable-project economics - wind typically runs 25-45 percent, solar 15-25 percent, while conventional thermal plants historically ran above 50, which is why renewables must be compared on levelized cost rather than nameplate capacity alone. The capacity factor is where resource quality, technology reliability, and curtailment all intersect: the same turbine design produces different capacity factors in different wind regimes, and grid curtailment (producing below capability because the grid cannot absorb it) suppresses the factor without any equipment problem. That curtailment split is the honest measurement: availability-adjusted capacity factor versus revenue-adjusted factor diverge when curtailment grows. Read with turbine availability (its reliability companion), resource assessment accuracy (forecast versus actualized wind speed), and curtailment minutes which quantify grid-constraint exposure.

## Formula

```
Actual Generation / Nameplate Generation Potential
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1100 (batch 4)
