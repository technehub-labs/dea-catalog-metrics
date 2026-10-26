# dea:metric-dependency-freshness-ratio

Candidate Performance Metric record for **Dependency Freshness Ratio** (DFR-CQ) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-dependency-freshness-ratio`
- **Name:** Dependency Freshness Ratio
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DFR-CQ

## 2. Definition

Dependency Freshness Ratio (DFR-CQ) captures exposure to adverse outcomes for organizations tracking code quality & static analysis. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Dependencies within One Major of Latest / Dependencies - reported in percent (%). Improvement means raising this figure toward best-in-class levels. It is a standard measure in the Software sector.

## Formula

```
DFR-CQ = Dependencies within One Major of Latest / Dependencies
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** code_quality_static_analysis
- **Sector:** software

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 4193 (batch 9)
