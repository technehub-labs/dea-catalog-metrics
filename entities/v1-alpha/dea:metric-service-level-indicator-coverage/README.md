# dea:metric-service-level-indicator-coverage

Candidate Performance Metric record for **Service Level Indicator Coverage** (SLIC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-indicator-coverage`
- **Name:** Service Level Indicator Coverage
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SLIC

## 2. Definition

Within Observability & Site Reliability Engineering, Service Level Indicator Coverage (SLIC) is used to gauge capability maturity or development. It is defined as User-Facing Services with Defined SLIs / Services; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures how completely user-facing services have defined, measured SLIs. SLIs are the vocabulary of reliability: unmeasured user journeys degrade undetected. Coverage limited to technical metrics (CPU, latency) rather than user experience signals misdirects effort. Read with service level objective attainment and error budget consumption rate.

## Formula

```
User-Facing Services with Defined SLIs / Services
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2860 (batch 7)
