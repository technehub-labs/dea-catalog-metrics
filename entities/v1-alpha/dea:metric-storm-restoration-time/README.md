# dea:metric-storm-restoration-time

Candidate Performance Metric record for **Storm Restoration Time** (SRT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-storm-restoration-time`
- **Name:** Storm Restoration Time
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** SRT

## 2. Definition

A Utilities Field Operations & Grid indicator, Storm Restoration Time (SRT) quantifies how effectively a process or entity achieves its intended outcome. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. It is computed as Hours from Storm End to Full Restoration, expressed in hours. It should be driven down, since lower readings signal healthier performance. Its use is concentrated in Utilities.

## 3. Context

Measures elapsed time to restore customers after major weather events. It is the resilience metric customers and regulators remember, and performance sets both reputational and regulatory context (and penalties in many jurisdictions). Restoration speed must be read with crew safety and with restoration prioritization honesty, since restoring dense feeders first flatters customer-hours metrics. Read with SAIDI storm-normalized and mutual aid activation time.

## Formula

```
Hours from Storm End to Full Restoration
```

## Unit

- **Unit reference:** `dea:unit-hours`
- **Unit:** hours
- **Unit label (as published):** hours

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** effectiveness
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** utilities_field_operations_grid
- **Sector:** utilities

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1888 (batch 6)
