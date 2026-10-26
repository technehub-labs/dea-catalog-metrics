# dea:metric-service-level-objective-attainment

Candidate Performance Metric record for **Service Level Objective Attainment** (SLOA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-service-level-objective-attainment`
- **Name:** Service Level Objective Attainment
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SLOA

## 2. Definition

Service Level Objective Attainment (SLOA) measures the quality of outputs and outcomes in the Observability & Site Reliability Engineering domain. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is SLO Windows Achieved / Total Windows, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of services meeting defined SLOs over the period. SLOs align engineering on user-perceived reliability rather than infrastructure uptime vanity metrics. Missed SLOs concentrated in one or two services indicate architectural debt, not effort gaps. Read with error budget consumption rate and SRE reliability review coverage.

## Formula

```
SLO Windows Achieved / Total Windows
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2863 (batch 7)
