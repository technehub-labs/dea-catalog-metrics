# dea:metric-balance-of-system-downtime

Candidate Performance Metric record for **Balance of System Downtime** (BOSD) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-balance-of-system-downtime`
- **Name:** Balance of System Downtime
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** BOSD

## 2. Definition

A Energy Transition & Renewables indicator, Balance of System Downtime (BOSD) quantifies exposure to adverse outcomes. It is monitored close to the work: teams act on it within a shift, sprint, or daily review. The formula is Grid or Inverter Downtime Hours / Total Hours - reported in percent (%). It should be driven down, since lower readings signal healthier performance. It is a standard measure in the Renewable energy sector.

## Formula

```
Grid or Inverter Downtime Hours / Total Hours
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** risk
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1104 (batch 4)
