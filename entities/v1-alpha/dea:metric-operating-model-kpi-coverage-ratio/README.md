# dea:metric-operating-model-kpi-coverage-ratio

Candidate Performance Metric record for **Operating Model KPI Coverage Ratio** (OMKPCR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-operating-model-kpi-coverage-ratio`
- **Name:** Operating Model KPI Coverage Ratio
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** OMKPCR

## 2. Definition

Within Operating Model Monitoring & Design Effectiveness, Operating Model KPI Coverage Ratio (OMKPCR) is used to gauge capability maturity or development. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Value Streams with Defined KPIs / Value Streams, measured in percent (%). Improvement means raising this figure toward best-in-class levels. Practitioners in nearly any industry can adopt it directly.

## 3. Context

Measures how completely the operating model's elements have defined, owned KPIs. Unmeasured operating-model elements are unmanaged ones. Coverage without quality (vanity or stale KPIs) is inventory, not monitoring. Read with target operating model realization rate and operating model review cadence compliance.

## Formula

```
Value Streams with Defined KPIs / Value Streams
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capability
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** operating_model_monitoring_design_effectiveness

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3112 (batch 7)
