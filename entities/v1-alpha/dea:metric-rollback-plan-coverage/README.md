# dea:metric-rollback-plan-coverage

Candidate Performance Metric record for **Rollback Plan Coverage** (RBPC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-rollback-plan-coverage`
- **Name:** Rollback Plan Coverage
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** RBPC

## 2. Definition

Within Network Change & Configuration Management, Rollback Plan Coverage (RBPC) is used to gauge exposure to adverse outcomes. The formula is Changes with Tested Rollback Plan / High-Risk Changes - reported in percent (%). It is applied across virtually every sector. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. It should be maximized within the limits of cost and quality trade-offs.

## Formula

```
Changes with Tested Rollback Plan / High-Risk Changes
```

## Unit

- **Unit reference:** `dea:unit-percent`
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
- **Domain:** network_change_configuration_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3372 (batch 7)
