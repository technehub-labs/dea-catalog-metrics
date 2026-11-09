# dea:metric-spare-parts-stockout-rate

Candidate Performance Metric record for **Spare Parts Stockout Rate** (SPS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-spare-parts-stockout-rate`
- **Name:** Spare Parts Stockout Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SPS

## 2. Definition

Spare Parts Stockout Rate (SPS) captures exposure to adverse outcomes for organizations tracking maintenance & reliability. The formula is Critical Spare Stockouts / Spare Parts Demand Events - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Lower values are better; each reduction is an improvement. It is a standard measure in the Manufacturing sector.

## Formula

```
SPS = Critical Spare Stockouts / Spare Parts Demand Events
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** maintenance_reliability
- **Sector:** manufacturing

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 274 (batch 1)
