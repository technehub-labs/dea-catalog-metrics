# dea:metric-sre-reliability-review-coverage

Candidate Performance Metric record for **SRE Reliability Review Coverage** (SRRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sre-reliability-review-coverage`
- **Name:** SRE Reliability Review Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** SRRC

## 2. Definition

Within Observability & Site Reliability Engineering, SRE Reliability Review Coverage (SRRC) is used to gauge capability maturity or development. Its trend is watched by senior leadership as an early signal of structural performance shifts. It is defined as Critical Services Reviewed per Quarter / Critical Services; the result is stated in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of critical services receiving structured design-for-reliability reviews. Reviews catch single points of failure and missing runbooks before launch. Coverage without change-action follow-through re-finds the same issues each cycle. Read with service level objective attainment and post-incident review action closure rate.

## Formula

```
SRRC = Critical Services Reviewed per Quarter / Critical Services
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capability
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** observability_site_reliability_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2882 (batch 7)
