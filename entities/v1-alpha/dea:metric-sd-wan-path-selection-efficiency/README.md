# dea:metric-sd-wan-path-selection-efficiency

Candidate Performance Metric record for **SD-WAN Path Selection Efficiency** (SPSE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-sd-wan-path-selection-efficiency`
- **Name:** SD-WAN Path Selection Efficiency
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SPSE

## 2. Definition

SD-WAN Path Selection Efficiency (SPSE) addresses how efficiently resources are converted into outputs and is a fixture of network performance & capacity reporting. It is defined as Optimal Path Selections / Steering Decisions; the result is stated in percent (%). It is a working-level control: thresholds trigger immediate operational response. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
Optimal Path Selections / Steering Decisions
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_performance_capacity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3358 (batch 7)
