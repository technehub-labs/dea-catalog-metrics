# dea:metric-rollback-plan-readiness-rate

Candidate Performance Metric record for **Rollback Plan Readiness Rate** (RPRR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rollback-plan-readiness-rate`
- **Name:** Rollback Plan Readiness Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** RPRR

## 2. Definition

Rollback Plan Readiness Rate (RPRR) captures exposure to adverse outcomes for organizations tracking release management & environments. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Releases with Tested Rollback Plan / Releases, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures the share of releases carrying a tested, current rollback path before deployment. Rollback readiness is the difference between a bad release and a business crisis. Untested rollback plans routinely fail on data migrations, so readiness must mean rehearsed, not documented. Read with deployment downtime per release and MTTR - recover.

## Formula

```
Releases with Tested Rollback Plan / Releases
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** release_management_environments

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2741 (batch 7)
