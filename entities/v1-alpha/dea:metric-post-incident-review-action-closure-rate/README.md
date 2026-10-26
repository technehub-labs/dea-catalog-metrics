# dea:metric-post-incident-review-action-closure-rate

Candidate Performance Metric record for **Post-Incident Review Action Closure Rate** (PIRACR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-post-incident-review-action-closure-rate`
- **Name:** Post-Incident Review Action Closure Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** PIRACR

## 2. Definition

Post-Incident Review Action Closure Rate (PIRACR) measures conformance to standards, plans, or obligations in the Observability & Site Reliability Engineering domain. It is defined as SRE Action Items Closed by Due Date / Items; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of corrective actions from incident reviews completed on time. Incidents only pay off if their lessons are institutionalized. Closure dominated by documentation-type actions while engineering fixes stall is hollow. Read with root cause analysis completion rate and recurring incident ratio.

## Formula

```
SRE Action Items Closed by Due Date / Items
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** compliance
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2877 (batch 7)
