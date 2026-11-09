# dea:metric-workplace-availability-rate

Candidate Performance Metric record for **Workplace Availability Rate** (WAR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-workplace-availability-rate`
- **Name:** Workplace Availability Rate
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** WAR

## 2. Definition

A Facilities & Real Estate indicator, Workplace Availability Rate (WAR) quantifies the utilization or availability of capacity. The formula is Functional Workstations / Total Workstations - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
WAR = Functional Workstations / Total Workstations
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** facilities_real_estate

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 451 (batch 1)
