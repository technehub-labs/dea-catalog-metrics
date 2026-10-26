# dea:metric-design-review-coverage

Candidate Performance Metric record for **Design Review Coverage** (DRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-design-review-coverage`
- **Name:** Design Review Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DRC

## 2. Definition

Within Engineering & Design, Design Review Coverage (DRC) is used to gauge conformance to standards, plans, or obligations. Front-line and delivery teams watch it in real time, as small deviations demand immediate correction. It is computed as Artifacts Passing through Formal Review / Artifacts, expressed in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## Formula

```
DRC = Artifacts Passing through Formal Review / Artifacts
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** engineering_design

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1767 (batch 6)
