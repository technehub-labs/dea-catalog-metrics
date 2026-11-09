# dea:metric-asset-utilization-rate

Candidate Performance Metric record for **Asset Utilization Rate** (AUR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-asset-utilization-rate`
- **Name:** Asset Utilization Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** AUR

## 2. Definition

A Maintenance & Reliability indicator, Asset Utilization Rate (AUR) quantifies the utilization or availability of capacity. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Productive Asset Hours / Available Asset Hours, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Its use is concentrated in Manufacturing.

## 3. Context

Actual productive use of an asset against its available or design capacity - the measure of how much of the installed asset base is earning. Its strategic significance is capital efficiency: every asset carries financing, depreciation, and space cost whether used or not, and low utilization is literally paying for capacity that no one is buying. The pattern matters more than the level - utilization that is low and stable reflects a structurally oversized asset base (a capital allocation question), while utilization that swings with demand reflects a sizing strategy (a resilience question, and deliberate spare capacity is a strategic choice the metric alone cannot judge). Read with availability: high utilization achieved by deferring maintenance borrows the number from future availability, which is the classic way this metric is manufactured.

## Formula

```
AUR = Productive Asset Hours / Available Asset Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
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
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 273 (batch 1)
