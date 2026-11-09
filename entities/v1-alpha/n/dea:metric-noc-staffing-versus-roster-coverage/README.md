# dea:metric-noc-staffing-versus-roster-coverage

Candidate Performance Metric record for **NOC Staffing versus Roster Coverage** (NSVRC) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-noc-staffing-versus-roster-coverage`
- **Name:** NOC Staffing versus Roster Coverage
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** NSVRC

## 2. Definition

NOC Staffing versus Roster Coverage (NSVRC) measures the utilization or availability of capacity in the Network Operations Center (Deep Dive) domain. The formula is Shifts Fully Covered / Shifts Scheduled - reported in percent (%). It is monitored close to the work: teams act on it within a shift, sprint, or daily review. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
NSVRC = Shifts Fully Covered / Shifts Scheduled
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** capacity
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** network_operations_center_deep_dive

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 2846 (batch 7)
