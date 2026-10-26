# dea:metric-solar-performance-ratio

Candidate Performance Metric record for **Solar Performance Ratio** (SPR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-solar-performance-ratio`
- **Name:** Solar Performance Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SPR

## 2. Definition

Solar Performance Ratio (SPR) measures how efficiently resources are converted into outputs in the Energy Transition & Renewables domain. It is defined as Actual Yield / Theoretical Yield at Irradiance; the result is stated in percent (%). Its trend is watched by senior leadership as an early signal of structural performance shifts. Higher values are better; gains are read as improvement and losses as deterioration. In Renewable energy, it is a recognized element of the standard performance toolkit.

## 3. Context

Solar performance ratio measures actual energy output against the theoretical output at reference conditions after accounting for irradiance, and it is the quality metric of PV system operation - a performance ratio around 80-85 percent is typical, with the gap to 100 representing real losses: soiling, temperature, wiring and inverter losses, degradation, shading, and downtime. The metric's value is diagnostic: it isolates system quality from resource variability (poor weather and good system can look like bad weather and bad system in raw production), which is why it is the standard metric in engineering procurement contracts and independent-engineer assessments. Degradation tracking is its long-term use: a declining performance ratio year-over-year reveals module degradation, soiling accumulation, or component degradation, each with different remediation economics. Read with soiling-loss trend (a maintenance-schedule matter), inverter uptime (the dominant downtime source), and availability as the reliability companion.

## Formula

```
Actual Yield / Theoretical Yield at Irradiance
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** sustainability
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** energy_transition_renewables
- **Sector:** renewable_energy

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1103 (batch 4)
