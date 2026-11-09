# dea:metric-reliability-centered-maintenance-coverage-grid

Candidate Performance Metric record for **Reliability-Centered Maintenance Coverage (Grid)** (RCMC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-reliability-centered-maintenance-coverage-grid`
- **Name:** Reliability-Centered Maintenance Coverage (Grid)
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RCMC

## 2. Definition

Reliability-Centered Maintenance Coverage (Grid) (RCMC) addresses capability maturity or development and is a fixture of utilities field operations & grid reporting. Its calculation is Critical Assets under RCM Strategy / Critical Assets, measured in percent (%). It originates from and is most used in Utilities practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of critical grid assets under RCM-based (condition and criticality-driven) maintenance programs rather than fixed schedules or reactive work. It converts maintenance from calendar compliance to risk management, which matters when failures cascade into public-safety and wildfire events. Coverage without data instrumentation is nominal, so verify condition-monitoring enablement. Read with asset failure rates and maintenance backlog aging.

## Formula

```
RCMC = Critical Assets under RCM Strategy / Critical Assets
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
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1895 (batch 6)
