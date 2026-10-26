# dea:metric-copper-to-fiber-migration-rate

Candidate Performance Metric record for **Copper to Fiber Migration Rate** (CFMR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-copper-to-fiber-migration-rate`
- **Name:** Copper to Fiber Migration Rate
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CFMR

## 2. Definition

Copper to Fiber Migration Rate (CFMR) captures transformation for organizations tracking telecom field & installation. It is defined as Migrated Lines / Addressable Lines; the result is stated in percent (%). In Telecommunications, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Tracks the share of customers or lines moved from legacy copper to fiber infrastructure over a period. It is the pivot metric for network investment strategy: it sequences capex, releases legacy maintenance cost, and unlocks higher-ARPU products. The trap is conflating physical network readiness with customer migration - copper can be retired in the plan while customers still sit on it, or migration achieved via forced moves that spike churn. Read with churn during migration cohorts and legacy cost run-rate reduction.

## Formula

```
Migrated Lines / Addressable Lines
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** transformation
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** telecom_field_installation
- **Sector:** telecommunications

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1285 (batch 5)
