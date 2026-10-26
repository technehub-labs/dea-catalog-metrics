# dea:metric-space-utilization

Candidate Performance Metric record for **Space Utilization** (SUT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-space-utilization`
- **Name:** Space Utilization
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SUT

## 2. Definition

Space Utilization (SUT) captures the utilization or availability of capacity for organizations tracking facilities & real estate. It is defined as Occupied Workspaces / Total Workspaces; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

The share of workplace capacity actually occupied in use - the metric through which the hybrid-work era converted real estate from a fixed assumption into a live portfolio question, since occupancy that runs at a fraction of capacity while the leases run full-term is visible, quantifiable waste. Its strategic significance is portfolio compression: organizations that measure utilization by zone and time find dense pockets and dead zones in the same building, and consolidation decisions that would have taken an anecdote now take an audit. The measurement honesty requirements are method-matching: badge data measures presence, seat-sensing measures occupancy, and booking data measures intent - each overstates or understates differently, and mixed-method trends are noise. Read with the collaboration-quality dimension: utilization-maximizing layouts that degrade the reasons people come in trade a real-estate win for a productivity cost, which the metric cannot see.

## Formula

```
Occupied Workspaces / Total Workspaces
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 448 (batch 1)
